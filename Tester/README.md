# ft_printf Python Tester

A comprehensive Python-based tester for the 42 School ft_printf project using ctypes.

## Features

- ✅ Tests all mandatory format specifiers: `%c`, `%s`, `%d`, `%i`, `%u`, `%x`, `%X`, `%p`, `%%`
- ✅ Compares output and return values against standard `printf`
- ✅ Colorized output for easy reading
- ✅ Detailed test reports with pass/fail statistics
- ✅ Automated testing via Makefile
- ✅ Individual test category execution
- ✅ Based on tests from printfTester

## Requirements

- Python 3.6 or higher
- GCC compiler
- Make

## Installation

The tester is already set up in the `Tester` directory. No additional installation required.

## Usage

### Run All Tests

```bash
make test
# or simply
make
```

### Run Specific Test Categories

```bash
make test_c        # Character tests (%c)
make test_s        # String tests (%s)
make test_d        # Decimal tests (%d)
make test_i        # Integer tests (%i)
make test_u        # Unsigned tests (%u)
make test_x        # Hex lowercase tests (%x)
make test_X        # Hex uppercase tests (%X)
make test_p        # Pointer tests (%p)
make test_percent  # Percent tests (%%)
make test_mix      # Mixed format tests
```

### Other Commands

```bash
make build    # Build the ft_printf library only
make clean    # Remove temporary files
make fclean   # Remove all generated files
make re       # Rebuild and test everything
make help     # Show help message
```

## Test Categories

### Character Tests (`%c`)
- Single characters
- Multiple characters
- Null characters
- Special characters

### String Tests (`%s`)
- Empty strings
- Regular strings
- Multiple strings
- Strings with special characters

### Integer Tests (`%d`, `%i`)
- Zero
- Positive numbers
- Negative numbers
- INT_MAX and INT_MIN
- Multiple integers

### Unsigned Tests (`%u`)
- Zero
- Positive numbers
- UINT_MAX
- Multiple unsigned integers

### Hexadecimal Tests (`%x`, `%X`)
- Zero
- Small numbers
- Large numbers
- UINT_MAX
- Both lowercase and uppercase

### Pointer Tests (`%p`)
- NULL pointers
- Various pointer values
- Large addresses
- Multiple pointers

### Percent Tests (`%%`)
- Single percent
- Multiple percents
- Percents in text

### Mixed Tests
- Combinations of different format specifiers
- Complex format strings

## Output

The tester provides:
- ✅ Green checkmark for passed tests
- ❌ Red X for failed tests
- Detailed comparison showing expected vs actual output
- Summary statistics at the end
- Success rate percentage

## Example Output

```
============================================================
  ft_printf Python Tester
============================================================

Library loaded successfully!

Running Character Tests (%c)
✓ Test 1: single char '0'
✓ Test 2: char with spaces
✓ Test 3: char with leading space
...

============================================================
Test Summary
============================================================
Total tests: 100
Passed: 98
Failed: 2

Success rate: 98.0%
============================================================
```

## How It Works

1. **Library Loading**: The tester compiles your `libftprintf.a` into a shared library and loads it using Python's ctypes
2. **Test Execution**: Each test calls both `printf` and `ft_printf` with the same arguments
3. **Output Capture**: Output is captured using file descriptors and pipes
4. **Comparison**: Both the output string and return value are compared
5. **Reporting**: Results are displayed with color-coded output

## Troubleshooting

### Library Not Found
If you get a "Library not found" error, make sure:
- You're running the tester from the `Tester` directory
- Your `ft_printf` implementation is in the parent directory
- The Makefile in the parent directory works correctly

### Compilation Errors
If compilation fails:
- Check that all required source files are present
- Ensure your code compiles with the flags: `-Wall -Wextra -Werror`
- Fix any compilation errors in your ft_printf implementation

### Test Failures
If tests fail:
- Check the detailed output showing expected vs actual results
- Verify your implementation handles edge cases
- Compare with the standard printf behavior

## Credits

Based on the test cases from [printfTester](https://github.com/Tripouille/printfTester) by Tripouille.

## License

This tester is provided as-is for educational purposes.
