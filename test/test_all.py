import unittest

from test import test_block, test_math, test_self_eval, test_variables, test_while, test_if_condition, test_parser, \
    test_functions, test_lambda, test_syntactic_sugar, test_switch, test_class, test_module, test_import

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(test_block.EvaTest))
    suite.addTest(unittest.makeSuite(test_math.EvaTest))
    suite.addTest(unittest.makeSuite(test_self_eval.EvaTest))
    suite.addTest(unittest.makeSuite(test_variables.EvaTest))
    suite.addTest(unittest.makeSuite(test_while.EvaTest))
    suite.addTest(unittest.makeSuite(test_if_condition.EvaTest))
    suite.addTest(unittest.makeSuite(test_parser.EvaTest))
    suite.addTest(unittest.makeSuite(test_functions.EvaTest))
    suite.addTest(unittest.makeSuite(test_lambda.EvaTest))
    suite.addTest(unittest.makeSuite(test_syntactic_sugar.EvaTest))
    suite.addTest(unittest.makeSuite(test_switch.EvaTest))
    suite.addTest(unittest.makeSuite(test_class.EvaTest))
    suite.addTest(unittest.makeSuite(test_module.EvaTest))
    suite.addTest(unittest.makeSuite(test_import.EvaTest))
    runner = unittest.TextTestRunner()
    runner.run(suite)
