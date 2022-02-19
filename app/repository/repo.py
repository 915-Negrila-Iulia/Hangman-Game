class Repository:
    def __init__(self, sentences_list=None):
        self._sentences_list = []
        if sentences_list is not None:
            self._sentences_list = sentences_list

    @property
    def sentences(self):
        return self._sentences_list

    def add_sentence(self, sentence):
        """
        Adds sentence to the list of sentences
        :param sentence: sentence to be added
        :return: -
        """
        for sent in self._sentences_list:
            if sent == sentence:
                raise Exception('Duplication')
        self._sentences_list.append(sentence)
