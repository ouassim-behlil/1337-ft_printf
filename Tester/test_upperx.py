"""Hexadecimal uppercase (%X) tests for ft_printf"""

def test_upperx(tester):
    """Test %X format specifier"""
    tester.run_test("zero", " %X ", 0)
    tester.run_test("one", " %X ", 1)
    tester.run_test("nine", " %X ", 9)
    tester.run_test("ten", " %X ", 10)
    tester.run_test("eleven", " %X ", 11)
    tester.run_test("fifteen", " %X ", 15)
    tester.run_test("sixteen", " %X ", 16)
    tester.run_test("seventeen", " %X ", 17)
    tester.run_test("ninety-nine", " %X ", 99)
    tester.run_test("one hundred", " %X ", 100)
    tester.run_test("one hundred one", " %X ", 101)
    tester.run_test("UINT_MAX", " %X ", 4294967295)
    tester.run_test("INT_MAX", " %X ", 2147483647)
    tester.run_test("hex values", " %X %X %X %X ", 255, 256, 4096, 65535)
    tester.run_test("multiple hex", " %X %X %X %X %X", 4294967295, 0, 1, 100, 42)
