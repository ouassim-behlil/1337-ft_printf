"""String (%s) tests for ft_printf"""

def test_s(tester):
    """Test %s format specifier"""
    tester.run_test("empty string", "%s", "")
    tester.run_test("empty string with leading space", " %s", "")
    tester.run_test("empty string with trailing space", "%s ", "")
    tester.run_test("empty string with spaces", " %s ", "")
    tester.run_test("dash with spaces", " %s ", "-")
    tester.run_test("empty and dash", " %s %s ", "", "-")
    tester.run_test("dash and empty", " %s %s ", " - ", "")
    tester.run_test("simple string", "%s", "Hello, World!")
    tester.run_test("multiple strings", "%s %s %s", "Hello", "World", "!")
    tester.run_test("string with special chars", "%s", "Test\nNew\tLine")
