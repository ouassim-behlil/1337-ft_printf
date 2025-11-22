"""Mixed format tests for ft_printf"""

def test_mix(tester):
    """Test mixed format specifiers"""
    tester.run_test("char and string", "%c %s", 'A', "test")
    tester.run_test("int and hex", "%d %x", 42, 42)
    tester.run_test("all types", "%c %s %d %i %u %x %X %p %%", 'A', "test", -42, 42, 42, 255, 255, 0xdeadbeef)
    tester.run_test("complex mix", "Char: %c, String: %s, Int: %d, Hex: %x", 'Z', "Hello", 123, 456)
    tester.run_test("numbers mix", "%d + %d = %d", 5, 3, 8)
    tester.run_test("hex comparison", "Lower: %x, Upper: %X", 255, 255)
    tester.run_test("pointer and int", "Ptr: %p, Val: %d", 0x1234, 4660)
