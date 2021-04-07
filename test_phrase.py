import unittest

from phrasehunter.phrase import Phrase

class SmokeTest(unittest.TestCase):

    def test_it_exists_with_attributes(self):
        my_phrase = Phrase('Hello World')

        self.assertIsInstance(my_phrase, Phrase)
        self.assertEqual(my_phrase.phrase, 'hello world')

    def test_it_exists_with_different_attributes(self):
        my_phrase = Phrase('Hello Friends')

        self.assertIsInstance(my_phrase, Phrase)
        self.assertEqual(my_phrase.phrase, 'hello friends')


class LetterCheckingTest(unittest.TestCase):

    def test_it_displays_underscores_when_letters_unchecked(self):
        my_phrase = Phrase('Hello World')

        self.assertEqual(my_phrase.display(), '_ _ _ _ _   _ _ _ _ _')

    def test_it_displays_letters_when_letters_checked(self):
        my_phrase = Phrase('Hello World')
        my_phrase.check_letter('o')

        self.assertEqual(my_phrase.display(), '_ _ _ _ o   _ o _ _ _')

    def test_it_displays_more_letters_when_letters_checked(self):
        my_phrase = Phrase('Hello World')
        my_phrase.check_letter('o')
        my_phrase.check_letter('l')

        self.assertEqual(my_phrase.display(), '_ _ l l o   _ o _ l _')

    def test_it_displays_more_letters_when_letters_checked(self):
        my_phrase = Phrase('Hello World')
        for letter in 'heworld':
            my_phrase.check_letter(letter)

        self.assertEqual(my_phrase.display(), 'h e l l o   w o r l d')

    def test_it_checks_complete_when_all_letters_checked(self):
        my_phrase = Phrase('Hello World')
        self.assertFalse(my_phrase.check_complete())
        for letter in 'heworld':
            my_phrase.check_letter(letter)

        self.assertTrue(my_phrase.check_complete())
