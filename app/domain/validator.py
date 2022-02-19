class Validator:
    @staticmethod
    def validate(sentence):
        if len(sentence) < 3:
            raise Exception('Sentence not valid')
        sent_split = sentence.split(' ')
        for sent in sent_split:
            if len(sent) < 3:
                raise Exception('Sentence not valid')
