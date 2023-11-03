import unittest
from test_scripts.LoginLogoutTest import LoginLogoutTest


test_suite = unittest.TestSuite()

test_suite.addTest(unittest.TestLoader().loadTestsFromTestCase(LoginLogoutTest))

if __name__ == '__main__':
    unittest.TextTestRunner(verbosity=2).run(test_suite)

