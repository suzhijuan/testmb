import unittest
from testcases.testsharepage import TestSharePage
from testcases.testhomepage import TestHomePage


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestSharePage)
    unittest.TextTestRunner(verbosity=2).run(suite)


    