import unittest

from phrasehunter.phrase import Phrase

class TestPhrase(unittest.TestCase):

    def test_it_exists_with_attributes(self):
        my_phrase = Phrase('Hello World')

        self.assertIsInstance(my_phrase, Phrase)
        self.assertEqual(my_phrase.phrase, 'Hello World')
