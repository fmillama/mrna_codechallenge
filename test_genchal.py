import unittest
import io
import os
import genchal

class TestGenChal(unittest.TestCase):

    def test_genex(self):
        mock1='ACg ACG\nUAAACG uAA\nUAA'
        mock2='ACG ACG UAA ACG'
        mock3='ACG ACG UAA AC'
        mock4='ACG UAA ECG'
        result1=[['ACG','ACG','UAA'],['ACG','UAA'],['UAA']]
        self.assertRaises(genchal.InvalidArgument,genchal.genex,25)
        self.assertEqual(genchal.genex(mock1), result1)
        self.assertRaises(genchal.InvalidEndingError,genchal.genex,mock2)
        self.assertRaises(genchal.InvalidLengthError,genchal.genex,mock3)
        self.assertRaises(genchal.InvalidLetterError,genchal.genex,mock4)

if __name__=='__main__':
    unittest.main()


