#!/usr/bin/env python3
"""
ft_printf Python Tester
This tester validates the ft_printf implementation against the standard printf.
Uses C wrapper programs to properly test variadic functions.
"""

import sys
import os
import subprocess
import tempfile

# ANSI Color codes
class Colors:
    RESET = '\033[0m'
    RED = '\033[91m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    MAGENTA = '\033[95m'
    CYAN = '\033[96m'
    GRAY = '\033[90m'
    BOLD = '\033[1m'

class PrintfTester:
    def __init__(self, lib_path='../libftprintf.a'):
        """Initialize the tester with the ft_printf library."""
        self.lib_path = os.path.abspath(lib_path)
        self.header_path = os.path.abspath('../ft_printf.h')
        self.passed = 0
        self.failed = 0
        self.total = 0
        self.failed_tests = []
        
    def load_library(self):
        """Compile the ft_printf library if needed."""
        if not os.path.exists(self.lib_path):
            print(f"{Colors.YELLOW}Library not found. Compiling...{Colors.RESET}")
            result = subprocess.run(['make', '-C', '..'], capture_output=True, text=True)
            if result.returncode != 0:
                print(f"{Colors.RED}Failed to compile library{Colors.RESET}")
                print(result.stderr)
                sys.exit(1)
        
        if not os.path.exists(self.header_path):
            print(f"{Colors.RED}Header file ft_printf.h not found!{Colors.RESET}")
            sys.exit(1)
            
        print(f"{Colors.GREEN}Library ready!{Colors.RESET}\n")
    
    def run_test(self, test_name, format_str, *args):
        """Run a single test comparing printf and ft_printf."""
        self.total += 1
        
        try:
            # Generate C code for both printf and ft_printf
            c_code = self.generate_test_c_code(format_str, *args)
            
            # Compile and run the test
            with tempfile.NamedTemporaryFile(mode='w', suffix='.c', delete=False) as f:
                f.write(c_code)
                c_file = f.name
            
            exe_file = c_file.replace('.c', '')
            
            # Compile
            compile_cmd = [
                'gcc', '-o', exe_file, c_file,
                '-I..', self.lib_path,
                '-Wno-format'
            ]
            compile_result = subprocess.run(compile_cmd, capture_output=True, text=True)
            
            if compile_result.returncode != 0:
                raise Exception(f"Compilation failed: {compile_result.stderr}")
            
            # Run
            run_result = subprocess.run([exe_file], capture_output=True, text=True, timeout=2)
            
            # Clean up
            os.unlink(c_file)
            os.unlink(exe_file)
            
            # Parse output using delimiter
            delimiter = "<<<DELIMITER>>>"
            parts = run_result.stdout.split(delimiter)
            
            if len(parts) < 5:
                raise Exception(f"Unexpected output format: {run_result.stdout}")
            
            # Parts: ['', '\nOUTPUT1\n', '\nRET1\n', '\nOUTPUT2\n', '\nRET2\n']
            expected_output = parts[1].strip('\n')
            expected_ret = int(parts[2].strip())
            actual_output = parts[3].strip('\n')
            actual_ret = int(parts[4].strip())
            
            # Compare results
            if expected_output == actual_output and expected_ret == actual_ret:
                print(f"{Colors.GREEN}✓{Colors.RESET} Test {self.total}: {test_name}")
                self.passed += 1
                return True
            else:
                print(f"{Colors.RED}✗{Colors.RESET} Test {self.total}: {test_name}")
                print(f"  {Colors.CYAN}Format:{Colors.RESET} {repr(format_str)}")
                if args:
                    print(f"  {Colors.CYAN}Args:{Colors.RESET} {args}")
                print(f"  {Colors.YELLOW}Expected:{Colors.RESET} [{repr(expected_output)}] = {expected_ret}")
                print(f"  {Colors.MAGENTA}Got:{Colors.RESET}      [{repr(actual_output)}] = {actual_ret}")
                self.failed += 1
                self.failed_tests.append((self.total, test_name))
                return False
                
        except subprocess.TimeoutExpired:
            print(f"{Colors.RED}✗{Colors.RESET} Test {self.total}: {test_name} - {Colors.RED}TIMEOUT{Colors.RESET}")
            self.failed += 1
            self.failed_tests.append((self.total, test_name))
            return False
        except Exception as e:
            print(f"{Colors.RED}✗{Colors.RESET} Test {self.total}: {test_name} - {Colors.RED}ERROR: {e}{Colors.RESET}")
            self.failed += 1
            self.failed_tests.append((self.total, test_name))
            return False
    
    def generate_test_c_code(self, format_str, *args):
        """Generate C code to test both printf and ft_printf."""
        # Escape the format string for C
        escaped_fmt = format_str.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')
        
        # Parse format string to determine expected types
        import re
        format_specs = re.findall(r'%[csdipuxX%]', format_str)
        
        # Build argument list based on format specifiers
        arg_list = []
        arg_index = 0
        for spec in format_specs:
            if spec == '%%':
                continue  # %% doesn't consume an argument
            
            if arg_index >= len(args):
                break
                
            arg = args[arg_index]
            arg_index += 1
            
            if spec == '%c':
                # Character argument
                if isinstance(arg, str):
                    if arg == '\0' or ord(arg) == 0:
                        arg_list.append('0')
                    elif arg == "'":
                        arg_list.append("'\\''")
                    elif arg == '\\':
                        arg_list.append("'\\\\'")
                    else:
                        arg_list.append(f"'{arg}'")
                elif isinstance(arg, int):
                    arg_list.append(str(arg))
                else:
                    arg_list.append(str(arg))
            elif spec == '%s':
                # String argument
                if isinstance(arg, str):
                    escaped_arg = arg.replace('\\', '\\\\').replace('"', '\\"').replace('\n', '\\n').replace('\t', '\\t')
                    arg_list.append(f'"{escaped_arg}"')
                elif arg is None:
                    arg_list.append('NULL')
                else:
                    arg_list.append(f'"{str(arg)}"')
            else:
                # Numeric argument (%d, %i, %u, %x, %X, %p)
                if isinstance(arg, int):
                    arg_list.append(str(arg))
                else:
                    arg_list.append(str(arg))
        
        args_str = ', '.join(arg_list) if arg_list else ''
        comma = ', ' if args_str else ''
        
        return f"""
#include <stdio.h>
#include <limits.h>
#include <stdint.h>
#include <unistd.h>
#include <string.h>
#include "ft_printf.h"

#define BUFFER_SIZE 4096
#define DELIMITER "<<<DELIMITER>>>"

int main(void) {{
    int ret1, ret2;
    char buffer1[BUFFER_SIZE];
    char buffer2[BUFFER_SIZE];
    int saved_stdout;
    int pipe_fd[2];
    
    /* Test with standard printf */
    saved_stdout = dup(STDOUT_FILENO);
    pipe(pipe_fd);
    dup2(pipe_fd[1], STDOUT_FILENO);
    
    ret1 = printf("{escaped_fmt}"{comma}{args_str});
    fflush(stdout);
    
    dup2(saved_stdout, STDOUT_FILENO);
    close(pipe_fd[1]);
    
    int len1 = read(pipe_fd[0], buffer1, BUFFER_SIZE - 1);
    buffer1[len1] = '\\0';
    close(pipe_fd[0]);
    
    /* Test with ft_printf */
    pipe(pipe_fd);
    dup2(pipe_fd[1], STDOUT_FILENO);
    
    ret2 = ft_printf("{escaped_fmt}"{comma}{args_str});
    fflush(stdout);
    
    dup2(saved_stdout, STDOUT_FILENO);
    close(pipe_fd[1]);
    
    int len2 = read(pipe_fd[0], buffer2, BUFFER_SIZE - 1);
    buffer2[len2] = '\\0';
    close(pipe_fd[0]);
    close(saved_stdout);
    
    /* Output results with delimiters */
    printf("%s\\n", DELIMITER);
    fwrite(buffer1, 1, len1, stdout);
    printf("\\n%s\\n", DELIMITER);
    printf("%d\\n", ret1);
    printf("%s\\n", DELIMITER);
    fwrite(buffer2, 1, len2, stdout);
    printf("\\n%s\\n", DELIMITER);
    printf("%d\\n", ret2);
    
    return 0;
}}
"""
    
    def print_summary(self):
        """Print test summary."""
        print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
        print(f"{Colors.BOLD}Test Summary{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}")
        print(f"Total tests: {self.total}")
        print(f"{Colors.GREEN}Passed: {self.passed}{Colors.RESET}")
        print(f"{Colors.RED}Failed: {self.failed}{Colors.RESET}")
        
        if self.failed > 0:
            print(f"\n{Colors.RED}Failed tests:{Colors.RESET}")
            for num, name in self.failed_tests:
                print(f"  {num}. {name}")
        
        percentage = (self.passed / self.total * 100) if self.total > 0 else 0
        print(f"\n{Colors.BOLD}Success rate: {percentage:.1f}%{Colors.RESET}")
        print(f"{Colors.BOLD}{'='*60}{Colors.RESET}\n")

def main():
    """Main test runner."""
    tester = PrintfTester()
    
    print(f"{Colors.BOLD}{Colors.CYAN}")
    print("=" * 60)
    print("  ft_printf Python Tester")
    print("=" * 60)
    print(f"{Colors.RESET}\n")
    
    # Load the library
    tester.load_library()
    
    # Import test modules
    from test_c import test_c
    from test_s import test_s
    from test_d import test_d
    from test_i import test_i
    from test_u import test_u
    from test_x import test_x
    from test_upperx import test_upperx
    from test_p import test_p
    from test_percent import test_percent
    from test_mix import test_mix
    
    # Run all tests
    print(f"{Colors.YELLOW}{Colors.BOLD}Running Character Tests (%c){Colors.RESET}")
    test_c(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running String Tests (%s){Colors.RESET}")
    test_s(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Integer Tests (%d){Colors.RESET}")
    test_d(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Integer Tests (%i){Colors.RESET}")
    test_i(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Unsigned Tests (%u){Colors.RESET}")
    test_u(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Hex Lowercase Tests (%x){Colors.RESET}")
    test_x(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Hex Uppercase Tests (%X){Colors.RESET}")
    test_upperx(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Pointer Tests (%p){Colors.RESET}")
    test_p(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Percent Tests (%%){Colors.RESET}")
    test_percent(tester)
    
    print(f"\n{Colors.YELLOW}{Colors.BOLD}Running Mixed Tests{Colors.RESET}")
    test_mix(tester)
    
    # Print summary
    tester.print_summary()
    
    # Exit with appropriate code
    sys.exit(0 if tester.failed == 0 else 1)

if __name__ == '__main__':
    main()
