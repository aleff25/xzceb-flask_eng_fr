import unittest

from teste import english_to_french, french_to_english


class TestTranslateEnglish(unittest.TestCase):
    def testFrench(self):
        self.assertEqual(french_to_english("Bonjour"), "Hello")


class TestTranslateFrench(unittest.TestCase):
    def testEnglish(self):
        self.assertEqual(english_to_french("Hello"), "Bonjour")


if _name_ == '_main_':
    unittest.main()