import unittest
from testcases.testsharepage import TestSharePage
from testcases.testhomepage import TestHomePage
from testcases.testlivepage import TestLivePage


if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(TestLivePage)
    unittest.TextTestRunner(verbosity=2).run(suite)
