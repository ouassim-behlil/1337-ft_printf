"""Hexadecimal lowercase (%x) tests for ft_printf"""

def test_x(tester):
    """Test %x format specifier"""
    tester.run_test("zero", " %x ", 0)
    tester.run_test("one", " %x ", 1)
    tester.run_test("nine", " %x ", 9)
    tester.run_test("ten", " %x ", 10)
    tester.run_test("eleven", " %x ", 11)
    tester.run_test("fifteen", " %x ", 15)
    tester.run_test("sixteen", " %x ", 16)
    tester.run_test("seventeen", " %x ", 17)
    tester.run_test("ninety-nine", " %x ", 99)
    tester.run_test("one hundred", " %x ", 100)
    tester.run_test("one hundred one", " %x ", 101)
    tester.run_test("UINT_MAX", " %x ", 4294967295)
    tester.run_test("INT_MAX", " %x ", 2147483647)
    tester.run_test("hex values", " %x %x %x %x ", 255, 256, 4096, 65535)
    tester.run_test("multiple hex", " %x %x %x %x %x", 4294967295, 0, 1, 100, 42)
