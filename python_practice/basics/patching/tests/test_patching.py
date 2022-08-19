from unittest import mock, TestCase
from files import patching

class TestExamples(TestCase):
    @mock.patch('files.patching.check_output', return_value=b'foo\nbar\n')
    def test_print_contents(self, mock_check_output):
        actual = patching.print_context()

        expected = b'foo'
        self.assertIn(expected,actual)