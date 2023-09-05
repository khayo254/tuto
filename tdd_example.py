import unittest
import banking_app


class Tdd_Python(unittest.TestCase):
    def test_banking_credit_method_returns_correct_result(self):
      bank = banking_app.Banking()
      final_bal = bank.credit(1000)
      self.assertEqual(1000, final_bal)

if __name__ == '__main__':
   unittest.main()