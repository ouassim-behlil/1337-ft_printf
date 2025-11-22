# Makefile for ft_printf Python Tester
# This automates the testing process

.PHONY: all test clean fclean re help

# Colors
GREEN = \033[0;32m
YELLOW = \033[0;33m
RED = \033[0;31m
CYAN = \033[0;36m
RESET = \033[0m

# Paths
PRINTF_DIR = ..
LIB_NAME = libftprintf.a
LIB_PATH = $(PRINTF_DIR)/$(LIB_NAME)
TESTER = tester.py

all: test

# Build the ft_printf library
build:
	@echo "$(CYAN)Building ft_printf library...$(RESET)"
	@$(MAKE) -C $(PRINTF_DIR)
	@echo "$(GREEN)Library built successfully!$(RESET)"

# Run the Python tester
test: build
	@echo "$(CYAN)Running Python tester...$(RESET)"
	@python3 $(TESTER)

# Run specific test category
test_c: build
	@echo "$(CYAN)Running character tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_c import test_c; t = PrintfTester(); t.load_library(); test_c(t); t.print_summary()"

test_s: build
	@echo "$(CYAN)Running string tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_s import test_s; t = PrintfTester(); t.load_library(); test_s(t); t.print_summary()"

test_d: build
	@echo "$(CYAN)Running decimal tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_d import test_d; t = PrintfTester(); t.load_library(); test_d(t); t.print_summary()"

test_i: build
	@echo "$(CYAN)Running integer tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_i import test_i; t = PrintfTester(); t.load_library(); test_i(t); t.print_summary()"

test_u: build
	@echo "$(CYAN)Running unsigned tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_u import test_u; t = PrintfTester(); t.load_library(); test_u(t); t.print_summary()"

test_x: build
	@echo "$(CYAN)Running hex lowercase tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_x import test_x; t = PrintfTester(); t.load_library(); test_x(t); t.print_summary()"

test_X: build
	@echo "$(CYAN)Running hex uppercase tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_upperx import test_upperx; t = PrintfTester(); t.load_library(); test_upperx(t); t.print_summary()"

test_p: build
	@echo "$(CYAN)Running pointer tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_p import test_p; t = PrintfTester(); t.load_library(); test_p(t); t.print_summary()"

test_percent: build
	@echo "$(CYAN)Running percent tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_percent import test_percent; t = PrintfTester(); t.load_library(); test_percent(t); t.print_summary()"

test_mix: build
	@echo "$(CYAN)Running mixed tests...$(RESET)"
	@python3 -c "from tester import PrintfTester; from test_mix import test_mix; t = PrintfTester(); t.load_library(); test_mix(t); t.print_summary()"

# Clean temporary files
clean:
	@echo "$(YELLOW)Cleaning temporary files...$(RESET)"
	@rm -f /tmp/libftprintf.so
	@rm -f /tmp/printf_test /tmp/printf_test.c
	@find . -type d -name "__pycache__" -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@$(MAKE) -C $(PRINTF_DIR) clean
	@echo "$(GREEN)Cleaned!$(RESET)"

# Full clean including library
fclean: clean
	@$(MAKE) -C $(PRINTF_DIR) fclean
	@echo "$(GREEN)Full clean complete!$(RESET)"

# Rebuild everything
re: fclean all

# Help message
help:
	@echo "$(CYAN)========================================$(RESET)"
	@echo "$(CYAN)  ft_printf Python Tester - Makefile  $(RESET)"
	@echo "$(CYAN)========================================$(RESET)"
	@echo ""
	@echo "$(YELLOW)Available targets:$(RESET)"
	@echo "  $(GREEN)make$(RESET) or $(GREEN)make test$(RESET)     - Run all tests"
	@echo "  $(GREEN)make build$(RESET)            - Build the ft_printf library"
	@echo "  $(GREEN)make test_c$(RESET)           - Run character tests only"
	@echo "  $(GREEN)make test_s$(RESET)           - Run string tests only"
	@echo "  $(GREEN)make test_d$(RESET)           - Run decimal tests only"
	@echo "  $(GREEN)make test_i$(RESET)           - Run integer tests only"
	@echo "  $(GREEN)make test_u$(RESET)           - Run unsigned tests only"
	@echo "  $(GREEN)make test_x$(RESET)           - Run hex lowercase tests only"
	@echo "  $(GREEN)make test_X$(RESET)           - Run hex uppercase tests only"
	@echo "  $(GREEN)make test_p$(RESET)           - Run pointer tests only"
	@echo "  $(GREEN)make test_percent$(RESET)     - Run percent tests only"
	@echo "  $(GREEN)make test_mix$(RESET)         - Run mixed format tests only"
	@echo "  $(GREEN)make clean$(RESET)            - Remove temporary files"
	@echo "  $(GREEN)make fclean$(RESET)           - Remove all generated files"
	@echo "  $(GREEN)make re$(RESET)               - Rebuild and test everything"
	@echo "  $(GREEN)make help$(RESET)             - Show this help message"
	@echo ""
	@echo "$(CYAN)========================================$(RESET)"

.DEFAULT_GOAL := help
