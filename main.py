class Letter:
    def __init__(self, char, positions=None):
        self.char = char
        self.positions = positions if positions else []

    def add_position(self, pos):
        self.positions.append(pos)


class WordConstructor:
    def __init__(self, length=None, letters=None):
        self.length = length
        self.letters = letters
        self.positions = None

        if not self.length:
            self.ui_get_length()

        if not self.letters:
            self.ui_get_letters()

        self.generate()

    def ui_get_length(self):
        while True:
            length = input('How many letters in your word? ')
            try:
                length = int(length)
                if length < 2:
                    raise ValueError
                break
            except ValueError:
                print('Input number bigger than  2!\n')
                continue
        self.length = length

    def ui_get_letters(self):
        self.letters = []

        print('\nLet\'s check your letters.  Type "0" if it\'s no more known letters.')
        for i in range(self.length):
            while True:
                letter = input(f'Input letter {i+1}: ').upper()
                if letter == '0':
                    break
                try:
                    if len(letter) != 1:
                        raise ValueError
                    if not letter.isalpha():
                        raise ValueError
                    break
                except ValueError:
                    print('Input one letter!\n')
                    continue

            if letter == '0':
                break
            self.letters.append(Letter(letter))

            print(f'\nLet\'s check possible positions of {self.letters[i].char}.  Type "0" if it\'s no more known positions.')
            for j in range(self.length):
                while True:
                    print()
                    if self.letters[i].positions:
                        print(f'Possible positions for {self.letters[i].char}: {str(self.letters[i].positions)[1:-1]}.')
                    pos = input(f'Input{" next " if self.letters[i].positions else " "}possible position for {self.letters[i].char}: ')
                    if pos == '0':
                        break
                    try:
                        pos = int(pos)
                        if not 0 < pos <= self.length:
                            raise ValueError
                        break
                    except ValueError:
                        print('Input number bigger than 0 and not bigger than length of word!\n')
                        continue

                if pos == '0':
                    print()
                    break
                self.letters[i].add_position(pos)

        if len(self.letters) < self.length:
            delta = self.length - len(self.letters)
            for i in range(delta):
                self.letters.append(Letter(char='_', positions=[1, 2, 3, 4, 5]))

    def generate(self):
        positions = {}
        for let in self.letters:
            for pos in let.positions:
                if positions.get(pos):
                    positions[pos].append(let.char)
                else:
                    positions[pos] = [let.char]
        print(positions)
        self.positions = positions
        self.recursion_generation(word=[], pos=1)

    def recursion_generation(self, word, pos):
        if pos > self.length:
            print(word)
            return

        else:
            for char in self.positions[pos]:
                if char not in word:
                    new_word = word.copy()
                    new_word.append(char)
                    self.recursion_generation(new_word, pos+1)
            return


if __name__ == '__main__':
    print('{:#^65}'.format('  Word Constructor  '))
    WordConstructor()
