class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase.lower()
        self.phrase_map = self.set_phrase_map(self.phrase)
        self.underscores = self.set_underscores(self.phrase, init=True)
        self.guessed_letters = list()

    def display(self):
        return self.underscores

    def check_letter(self, letter):
        try:
            indices = self.phrase_map[letter]
            characters = self.parse_characters(self.underscores)
            for index in indices:
                characters[index] = letter
            characters = ''.join(characters)
            self.underscores = self.set_underscores(characters)
            self.guessed_letters.append(letter)
        except KeyError:
            pass

    def check_complete(self):
        return '_' not in self.underscores

    def parse_characters(self, underscores):
        words = []
        for word in underscores.split('   '):
            word = ''.join(word.split(' '))
            words.append(word)
        return [character for character in ' '.join(words)]

    def set_phrase_map(self, letters):
        map = {}
        for index, letter in enumerate(letters):
            try:
                map[letter].append(index)
            except KeyError:
                map[letter] = list()
                map[letter].append(index)
        return map

    def set_underscores(self, words, init=False):
        underscores = []
        for word in words.split(' '):
            if init is True:
                characters = ['_' for character in word]
            else:
                characters = [character for character in word]
            underscores.append(' '.join(characters))
        return '   '.join(underscores)
