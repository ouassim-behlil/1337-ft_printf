# ft_printf

A custom implementation of the C standard library `printf` function.

## Building

```bash
make
```

This creates `libftprintf.a` library.

## Testing

### Using Docker

Build and run tests in a containerized environment:

```bash
docker build -t ft_printf_tester .
docker run --rm -it ft_printf_tester
```

### Using Makefile

Run tests locally (requires build tools, git, valgrind, python3):

```bash
cd Tester
make test
```

## Cleaning

```bash
make clean   # Remove object files
make fclean  # Remove object files and library
make re      # Rebuild everything
```

## Supported Conversions

- `%c` - Character
- `%s` - String
- `%p` - Pointer address
- `%d` - Decimal integer
- `%i` - Integer
- `%u` - Unsigned decimal
- `%x` - Hexadecimal (lowercase)
- `%X` - Hexadecimal (uppercase)
- `%%` - Percent sign
