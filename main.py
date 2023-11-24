class Letter:
    def __init__(self, char, positions=None):
        self.char = char
        self.positions = positions if positions else []

    def add_position(self, pos):
        self.positions.append(pos)


class WordConstructor:
    def __init__(self):
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
        self.letters = []

        print('\nLet\'s check your letters.  Type "0" if it\'s no more known letters.')
        for i in range(length):
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
            for j in range(length):
                while True:
                    print()
                    if self.letters[i].positions:
                        print(f'Possible positions for {self.letters[i].char}: {str(self.letters[i].positions)[1:-1]}.')
                    pos = input(f'Input{" next " if self.letters[i].positions else " "}possible position for {self.letters[i].char}: ')
                    if pos == '0':
                        break
                    try:
                        pos = int(pos)
                        if not 0 < pos <= length:
                            raise ValueError
                        break
                    except ValueError:
                        print('Input number bigger than 0 and not bigger than length of word!\n')
                        continue

                if pos == '0':
                    print()
                    break
                self.letters[i].add_position(pos)
        if len(self.letters) < length:
            delta = length - len(self.letters)
            for i in range(delta):
                self.letters.append(Letter(char='_', positions=[1, 2, 3, 4, 5]))

        self.generate()

    def generate(self):
        for let in self.letters:
            print(let.char, let.positions)


if __name__ == '__main__':
    print('{:#^65}'.format('  Word Constructor  '))
    WordConstructor()




