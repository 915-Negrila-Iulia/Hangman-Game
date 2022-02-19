class Game:
    def __init__(self, sentence=None):
        self._sentence = sentence

    @property
    def sentence(self):
        return self._sentence

    @sentence.setter
    def sentence(self, value):
        self._sentence = value

    def player_guess(self, given_letter):
        self._sentence.check_letter(given_letter)

    def check_win(self):
        return self._sentence.check_win()

    def check_lose(self):
        return self._sentence.check_lose()
