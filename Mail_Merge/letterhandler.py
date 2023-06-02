class LetterHandler:
    def __init__(self):
        self.content = ''
        self.names = []
        self.read_letter()
        self.read_names()

    def read_letter(self):
        with open('./Input/Letters/starting_letter.txt') as file:
            self.content = file.read()

    def write_to_letter(self, name):
        temp_content = self.content
        temp_content.replace('[name]', name)
        with open(f'./Output/ReadyToSend/letter_for_{name}.txt', mode='w') as file:
            file.write(self.content)

    def read_names(self):
        with open('./Input/Names/invited_names.txt') as file:
            for name in file:
                self.names.append(name.strip())
