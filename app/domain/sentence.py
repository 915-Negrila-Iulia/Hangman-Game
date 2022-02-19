class Sentence:
    def __init__(self, word_list, letters=None, hangman=0):
        """
        constructor for a sentence
        :param word_list: sentence
        :param letters: list of letters that are in the sentence and were guessed by the user
        :param hangman: number of chances to guess
        """
        self._word_list = word_list
        self._letters = []
        if letters is not None:
            self._letters = letters
        self._hangman = 0
        if hangman is not None:
            self._hangman = hangman

    @property
    def letters(self):
        return self._letters

    @letters.setter
    def letters(self, value):
        self._letters = value

    @property
    def word_list(self):
        return self._word_list

    @property
    def get_first(self):
        """
        finds the first letter from each word
        :return: list of these letters
        """
        firsts = [self._word_list[0]]
        for i in range(1, len(self._word_list)):
            if self._word_list[i - 1] == ' ':
                firsts.append(self._word_list[i])
        return firsts

    @property
    def get_last(self):
        """
        finds the last letter from each word
        :return: list of these letters
        """
        lasts = [self._word_list[-1]]
        for i in range(0, len(self._word_list) - 1):
            if self._word_list[i + 1] == ' ':
                lasts.append(self._word_list[i])
        return lasts

    def check_letter(self, given_letter):
        """
        checks if the sentence contains the letter given by the player
        increases the 'hangman' which means they have -1 chances to win if they guessed wrong
        appends the letter to the list of guessed letters if the player guessed
        :param given_letter: sentence
        :return: True if letter is in the sentence, False otherwise
        """
        if given_letter in self._word_list:
            self._letters.append(given_letter)
            return True
        else:
            self._hangman += 1
            return False

    def check_win(self):
        """
        Checks if all the letters from the sentence are guessed
        :return: False if there is at least one letter not guessed, True otherwise
        """
        for letter in self._word_list:
            if letter not in self._letters and letter != ' ':
                return False
        return True

    def check_lose(self):
        """
        Check if there are any mor chances to guess
        :return: True if all chances were used, false otherwise
        """
        if self._hangman == 7:
            return True
        else:
            return False

    def __str__(self):
        """
        Prints the sentence
        :return: sentence
        """
        print_sentence = ''
        self._letters.extend(self.get_first)
        self._letters.extend(self.get_last)
        for letter in self._word_list:
            if letter in self._letters:
                print_sentence += letter
            elif letter == ' ':
                print_sentence += letter
            else:
                print_sentence += '_'
        hangman_string = 'hangman'
        hangman_print = ''
        for i in range(self._hangman):
            hangman_print += hangman_string[i]
        return str(print_sentence) + ' ' + str(hangman_print)
