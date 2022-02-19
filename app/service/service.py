import random
from app.domain.sentence import Sentence


class Service:
    def __init__(self, sentences_repo, validator):
        self._sentences_repo = sentences_repo
        self._validator = validator

    @property
    def sentences(self):
        return self._sentences_repo.sentences

    def add_sentence(self, sentence):
        """
        Checks if the sentence is valid, if so add it to the list of sentences
        :param sentence: sentence to be added
        :return: -
        """
        self._validator.validate(sentence)
        self._sentences_repo.add_sentence(Sentence(sentence))

    def init_sentences(self):
        """
        Initialize list of sentences
        :return: -
        """
        self.add_sentence('anna has apples')
        self.add_sentence('patricia has pears')
        self.add_sentence('cars are fast')
        self.add_sentence('plans are quick')
        self.add_sentence('the quick brown fox jumps over the lazy dog')

    def get_random(self):
        """
        Use random to choose a sentence
        :return: random sentence from the list of sentences
        """
        return random.choice(self.sentences)