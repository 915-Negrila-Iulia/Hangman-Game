from app.domain.sentence import Sentence
from app.repository.repo import Repository


class FileRepository(Repository):

    def __init__(self, file_name='sentence.txt'):

        super().__init__()
        self._file_name = file_name
        self._load()

    def add_sentence(self, sentence):

        super().add_sentence(sentence)
        self._save()

    def _load(self):
        """
        Reads line by line from the file text and adds students to the list of students
        :return: -
        """
        file = open(self._file_name, 'rt')
        lines = file.readlines()
        file.close()

        for line in lines:
            super().add_sentence(Sentence(line))

    def _save(self):
        """
        Writes the students to the file
        :return: -
        """
        file = open(self._file_name, 'wt')
        for sentence in self.sentences:
            line = str(sentence)
            file.write(line)
            file.write('\n')
        file.close()
