import unittest
import guessgame


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = guessgame.run_guess(answer, guess)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = guessgame.run_guess(5, 0)
        self.assertFalse(result)

    def test_input_wrong_number(self):
        result = guessgame.run_guess(5, 11)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = guessgame.run_guess(5, '11')
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()
