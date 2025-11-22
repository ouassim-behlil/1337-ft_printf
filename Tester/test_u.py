"""Unsigned integer (%u) tests for ft_printf"""

def test_u(tester):
    """Test %u format specifier"""
    tester.run_test("zero", " %u ", 0)
    tester.run_test("one", " %u ", 1)
    tester.run_test("nine", " %u ", 9)
    tester.run_test("ten", " %u ", 10)
    tester.run_test("eleven", " %u ", 11)
    tester.run_test("fifteen", " %u ", 15)
    tester.run_test("sixteen", " %u ", 16)
    tester.run_test("seventeen", " %u ", 17)
    tester.run_test("ninety-nine", " %u ", 99)
    tester.run_test("one hundred", " %u ", 100)
    tester.run_test("one hundred one", " %u ", 101)
    tester.run_test("UINT_MAX", " %u ", 4294967295)
    tester.run_test("multiple unsigned", " %u %u %u %u %u", 4294967295, 0, 1, 100, 42)
