class Phrase():

    def __init__(self, phrase):
        self.phrase = self.validate_phrase(phrase)
        self.character_map = self.set_character_map(self.phrase)
        self.underscored_phrase = self.set_underscores(self.phrase, init=True)

    def display(self):
        return self.underscored_phrase

    def check_letter(self, letter):
        try:
            self.replace_underscores(letter)
            return True
        except KeyError:
            return False

    def replace_underscores(self, character):
        indices = self.character_map[character]
        characters = self.parse_characters(self.underscored_phrase)
        for index in indices:
            characters[index] = character
        characters = ''.join(characters)
        self.underscored_phrase = self.set_underscores(characters)

    def check_complete(self):
        return '_' not in self.underscored_phrase

    def parse_characters(self, underscored_phrase):
        words = []
        for word in underscored_phrase.split('   '):
            word = ''.join(word.split(' '))
            words.append(word)
        return [character for character in ' '.join(words)]

    def set_character_map(self, phrase):
        map = {}
        for index, character in enumerate(phrase):
            try:
                map[character].append(index)
            except KeyError:
                map[character] = list()
                map[character].append(index)
        return map

    def set_underscores(self, phrase, init=False):
        underscores = []
        for word in phrase.split(' '):
            if init is True:
                characters = ['_' for character in word]
            else:
                characters = [character for character in word]
            underscores.append(' '.join(characters))
        return '   '.join(underscores)

    def validate_phrase(self, phrase):
        if ' ' not in phrase or phrase == ' ':
            raise ValueError('Phrase must be more than one word')
        characters = phrase.lower()
        for character in characters:
            if character not in 'abcdefghijklmnopqrstuvwxyz ':
                raise ValueError(f'{character} is not a letter or space')
        return characters
