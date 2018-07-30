import unittest
import authr as a


class authr_tests(unittest.TestCase):
    def test_shodan_connection(self):
        self.assertEqual(a.authr.set_shodan_api_environment('test'), 'API_KEY_SET')


if __name__ == '__main__':
    unittest.main()
