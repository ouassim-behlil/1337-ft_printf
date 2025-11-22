# Quick Reference Card

## Getting Started
```bash
cd Tester
make help          # Show all available commands
./quickstart.sh    # Interactive quick start
```

## Common Commands

### Run Tests
```bash
make test          # Run all tests
make               # Same as 'make test'
python3 tester.py  # Run directly with Python
```

### Run Specific Tests
```bash
make test_c        # Character tests (%c)
make test_s        # String tests (%s)
make test_d        # Decimal tests (%d)
make test_i        # Integer tests (%i)
make test_u        # Unsigned tests (%u)
make test_x        # Hex lowercase (%x)
make test_X        # Hex uppercase (%X)
make test_p        # Pointer tests (%p)
make test_percent  # Percent tests (%%)
make test_mix      # Mixed format tests
```

### Build & Clean
```bash
make build         # Build ft_printf library
make clean         # Remove temporary files
make fclean        # Remove all generated files
make re            # Rebuild and test everything
```

## Understanding Output

### Success
```
✓ Test 1: single char '0'
```

### Failure
```
✗ Test 2: char with spaces
  Format: ' %c '
  Args: ('0',)
  Expected: [' 0 '] = 3
  Got:      [' 0'] = 2
```

### Summary
```
============================================================
Test Summary
============================================================
Total tests: 100
Passed: 98
Failed: 2

Success rate: 98.0%
============================================================
```

## Test Categories

| Category | Format | Description |
|----------|--------|-------------|
| test_c | %c | Character output |
| test_s | %s | String output |
| test_d | %d | Signed decimal integer |
| test_i | %i | Signed integer |
| test_u | %u | Unsigned decimal integer |
| test_x | %x | Hexadecimal (lowercase) |
| test_X | %X | Hexadecimal (uppercase) |
| test_p | %p | Pointer address |
| test_percent | %% | Percent sign |
| test_mix | mixed | Multiple formats |

## Troubleshooting

### Library not found
```bash
cd ..
make
cd Tester
```

### Python not found
```bash
# Install Python 3
sudo apt-get install python3  # Ubuntu/Debian
```

### GCC not found
```bash
# Install GCC
sudo apt-get install gcc  # Ubuntu/Debian
```

### Permission denied
```bash
chmod +x tester.py
chmod +x quickstart.sh
```

## Files

- `tester.py` - Main test runner
- `test_*.py` - Individual test modules
- `Makefile` - Build automation
- `README.md` - Full documentation
- `OVERVIEW.md` - Directory structure
- `quickstart.sh` - Quick start script

## Tips

1. Run `make help` to see all available commands
2. Start with `make test_c` to test a small category first
3. Check the detailed output for failed tests
4. Use `make clean` regularly to remove temporary files
5. Read README.md for comprehensive documentation

## Support

For issues or questions:
1. Check README.md for detailed documentation
2. Review OVERVIEW.md for structure information
3. Ensure your ft_printf implementation compiles without errors
4. Verify all required files are in the parent directory
