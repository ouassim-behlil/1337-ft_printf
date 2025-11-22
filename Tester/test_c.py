"""Character (%c) tests for ft_printf"""

def test_c(tester):
    """Test %c format specifier"""
    tester.run_test("single char '0'", "%c", '0')
    tester.run_test("char with spaces", " %c ", '0')
    tester.run_test("char with leading space", " %c", '0')
    tester.run_test("char with trailing space", "%c ", '0')
    tester.run_test("multiple chars with null", " %c %c %c ", '0', '\0', '1')
    tester.run_test("multiple spaces", " %c %c %c ", ' ', ' ', ' ')
    tester.run_test("multiple digits", " %c %c %c ", '1', '2', '3')
    tester.run_test("chars with null at end", " %c %c %c ", '2', '1', '\0')
    tester.run_test("null at beginning", " %c %c %c ", '\0', '1', '2')
