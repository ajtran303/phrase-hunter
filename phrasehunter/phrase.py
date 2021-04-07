class Phrase():

    def __init__(self, phrase):
        self.phrase = phrase

    def display(self):
        words = self.phrase.split(' ')
        underscores = []

        for word in words:
            word = ' '.join(['_' for x in word.lower()])
            underscores.append(word)

        return '   '.join(underscores)

    def check_letter(self, letter):
        pass
