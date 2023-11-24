class Letter:
    def __init__(self, char, positions=None):
        self.char = char
        self.positions = positions if positions else []

    def add_position(self, pos):
        self.positions.append(pos)


class WordConstructor:
    def __init__(self, length=None, letters=None, spaces=0):
        self.length = length
        self.letters = letters
        self.positions = None
        self.spaces = spaces

        if not self.length:
            self.ui_get_length()

        if not self.letters:
            self.ui_get_letters()

        print('There are words without repeats:')
        self.generate_wo_repeats()

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
                letter = input(f'Input letter {i + 1}: ').upper()
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

            print(
                f'\nLet\'s check possible positions of {self.letters[i].char}.  Type "0" if it\'s no more known positions.')
            for j in range(self.length):
                while True:
                    if self.letters[i].positions:
                        print(f'Possible positions for {self.letters[i].char}: {str(self.letters[i].positions)[1:-1]}.')
                    pos = input(
                        f'Input{" next " if self.letters[i].positions else " "}possible position for {self.letters[i].char}: ')
                    if pos == '0':
                        break
                    try:
                        pos = int(pos)
                        if not 0 < pos <= self.length:
                            raise ValueError
                        print()
                        break
                    except ValueError:
                        print('Input number bigger than 0 and not bigger than length of word!\n')
                        continue

                if pos == '0':
                    print()
                    break
                self.letters[i].add_position(pos)

        if len(self.letters) < self.length:
            self.spaces = self.length - len(self.letters)
            self.letters.append(Letter(char='_', positions=[1, 2, 3, 4, 5]))

    def generate_wo_repeats(self):
        positions = {}
        for let in self.letters:
            for pos in let.positions:
                if positions.get(pos):
                    positions[pos].append(let.char)
                else:
                    positions[pos] = [let.char]

        self.positions = positions
        self.recursion_generation_wo_repeats(word=[], pos=1)

    def recursion_generation_wo_repeats(self, word, pos):
        if pos > self.length:
            string_word = ''
            for letter in word:
                string_word = ''.join((string_word, letter))
            print(string_word)
            return

        else:
            for char in self.positions[pos]:
                if char == '_' and word.count(char) < self.spaces:
                    new_word = word.copy()
                    new_word.append(char)
                    self.recursion_generation_wo_repeats(new_word, pos + 1)
                elif char not in word:
                    new_word = word.copy()
                    new_word.append(char)
                    self.recursion_generation_wo_repeats(new_word, pos + 1)
            return


if __name__ == '__main__':
    print('{:#^65}'.format('  Word Constructor  '))
    WordConstructor()
