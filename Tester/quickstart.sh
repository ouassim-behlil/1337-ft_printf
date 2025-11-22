#!/bin/bash
# Quick start script for ft_printf Python Tester

echo "=========================================="
echo "  ft_printf Python Tester Quick Start"
echo "=========================================="
echo ""
echo "This script will guide you through using the tester."
echo ""

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✓ Python 3 found: $(python3 --version)"

# Check if GCC is installed
if ! command -v gcc &> /dev/null; then
    echo "❌ GCC is not installed. Please install GCC first."
    exit 1
fi

echo "✓ GCC found: $(gcc --version | head -n1)"
echo ""

echo "Available commands:"
echo "  make test       - Run all tests"
echo "  make test_c     - Run character tests"
echo "  make test_s     - Run string tests"
echo "  make test_d     - Run decimal tests"
echo "  make help       - Show all available commands"
echo ""

read -p "Would you like to run all tests now? (y/n) " -n 1 -r
echo ""

if [[ $REPLY =~ ^[Yy]$ ]]; then
    echo ""
    echo "Running tests..."
    echo ""
    make test
fi
