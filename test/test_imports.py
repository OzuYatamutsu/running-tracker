from unittest import TestCase


class TestImports(TestCase):
    def test_imports_are_working_correctly(self):
        from runningtracker import api  # noqa
        from runningtracker import frontend  # noqa
        assert True
