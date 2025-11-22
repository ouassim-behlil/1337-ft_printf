"""Pointer (%p) tests for ft_printf"""

def test_p(tester):
    """Test %p format specifier"""
    tester.run_test("NULL pointer", " %p ", 0)
    tester.run_test("pointer value 1", " %p ", 1)
    tester.run_test("pointer value 15", " %p ", 15)
    tester.run_test("pointer value 16", " %p ", 16)
    tester.run_test("pointer value 17", " %p ", 17)
    tester.run_test("large pointer", " %p ", 0xdeadbeef)
    tester.run_test("max pointer 32bit", " %p ", 0xffffffff)
    tester.run_test("multiple pointers", " %p %p ", 0, 0xdeadbeef)
    tester.run_test("pointer range", " %p %p %p %p ", 0, 1, 15, 0xffffffff)
