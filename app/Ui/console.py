from app.domain.validator import Validator
from app.repository.repo_file import FileRepository
from app.service.game import Game
from app.service.service import Service


class Console:
    def __init__(self, service_sentences, game):
        self._service_sentences = service_sentences
        self._game = game

    def split_command(self, command):
        splited = command.split(' ',1)
        name = splited[0]
        sentence = splited[1]
        return name, sentence

    def display_sentences(self):
        for sent in self._service_sentences.sentences:
            print(sent)

    def menu(self):
        print('add -> add sentence')
        print('display -> show all the sentences')
        print('start -> start a game')
        print('exit -> exit program')
        print()

    def start(self):
        #self._service_sentences.init_sentences()
        done = False
        while not done:
            try:
                print()
                self.menu()
                command = input('command: ')
                if command == 'display':
                    self.display_sentences()
                elif command == 'exit':
                    done=True
                elif command != 'start':
                    name, sentence = self.split_command(command)
                    if name == 'add':
                        self._service_sentences.add_sentence(sentence)
                    else:
                        print('wrong command')
                elif command == 'start':
                    finish = False
                    print('game starts!')
                    self._game.sentence=self._service_sentences.get_random()
                    print(self._game.sentence)
                    while not finish:
                        letter=input('give letter: ')
                        self._game.player_guess(letter)
                        print(self._game.sentence)
                        if self._game.check_win() is True:
                            print('player win')
                            finish = True
                        elif self._game.check_lose() is True:
                            print('player lose')
                            finish = True
            except Exception as exception:
                print(str(exception))

game = Game()
repo = FileRepository()
validator = Validator()
service = Service(repo,validator)
console = Console(service, game)
console.start()