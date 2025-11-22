# Tester Directory Structure

## Overview
This directory contains a comprehensive Python-based tester for the ft_printf project using ctypes.

## Files

### Main Files
- **tester.py** - Main test runner script
- **Makefile** - Automation for building and running tests
- **README.md** - Comprehensive documentation
- **quickstart.sh** - Quick start guide script

### Test Modules
- **test_c.py** - Character format (%c) tests
- **test_s.py** - String format (%s) tests
- **test_d.py** - Decimal integer format (%d) tests
- **test_i.py** - Integer format (%i) tests
- **test_u.py** - Unsigned integer format (%u) tests
- **test_x.py** - Hexadecimal lowercase format (%x) tests
- **test_upperx.py** - Hexadecimal uppercase format (%X) tests
- **test_p.py** - Pointer format (%p) tests
- **test_percent.py** - Percent format (%%) tests
- **test_mix.py** - Mixed format tests

## Test Coverage

The tester includes tests from the printfTester repository covering:

1. **Basic Format Specifiers**
   - %c (character)
   - %s (string)
   - %d and %i (signed integers)
   - %u (unsigned integers)
   - %x and %X (hexadecimal)
   - %p (pointers)
   - %% (percent sign)

2. **Edge Cases**
   - NULL pointers
   - Empty strings
   - Null characters
   - INT_MAX and INT_MIN
   - UINT_MAX
   - Zero values
   - Negative numbers

3. **Complex Scenarios**
   - Multiple format specifiers
   - Mixed types
   - Special characters
   - Boundary values

## How It Works

1. **Compilation**: The tester compiles your libftprintf.a library
2. **Test Generation**: For each test, it generates a C program that calls both printf and ft_printf
3. **Execution**: The C program is compiled and executed
4. **Comparison**: Output and return values are compared
5. **Reporting**: Results are displayed with color-coded output

## Usage Examples

### Run all tests
```bash
make test
# or
make
```

### Run specific category
```bash
make test_c    # Character tests
make test_s    # String tests
make test_d    # Decimal tests
```

### Run directly with Python
```bash
python3 tester.py
```

### Clean up
```bash
make clean     # Remove temporary files
make fclean    # Remove all generated files
```

## Test Statistics

The tester provides:
- Total number of tests run
- Number of passed tests
- Number of failed tests
- Success rate percentage
- Detailed failure information

## Requirements

- Python 3.6+
- GCC compiler
- Make
- Your ft_printf implementation in the parent directory

## Advantages

✅ **Comprehensive**: Tests all mandatory format specifiers
✅ **Automated**: One command to run all tests
✅ **Clear Output**: Color-coded results
✅ **Detailed**: Shows expected vs actual output
✅ **Flexible**: Run all tests or specific categories
✅ **Based on printfTester**: Uses proven test cases

## Notes

- Tests are based on the printfTester repository by Tripouille
- The tester compares both output and return values
- All tests use the same approach as the standard printf
- Temporary files are automatically cleaned up
