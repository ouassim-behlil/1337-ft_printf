"""Percent (%%) tests for ft_printf"""

def test_percent(tester):
    """Test %% format specifier"""
    tester.run_test("single percent", "%%")
    tester.run_test("percent with spaces", " %% ")
    tester.run_test("double percent", "%%%%")
    tester.run_test("percent with text", "Hello %% World")
    tester.run_test("multiple percents", " %% %% %% ")
    tester.run_test("percent in sentence", "This is 100%% correct!")
