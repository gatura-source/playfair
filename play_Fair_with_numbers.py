
def create_diagraph(inp):
    dia=[]
    group = 0
    for i  in range(2, len(inp), 2):
        dia.append(inp[group:i])

        group = i
    dia.append(inp[group:])
    return dia


def checkduplicate(string):
    length = len(string.upper())
    if length % 2 != 0:
        for i in range(0, length-1, 2):
            if string[i] == string[i+1]:
                new_word = string[0:i+1] + str('x') + string[i+1:]
                new_word = checkduplicate(new_word)
                break
        else:
            new_word = string
    else:
        for i in range(0, length, 2):
            if string[i] == string[i + 1]:
                new_word = string[0:i+1] + str('x') + string[i+1:]
                new_word = checkduplicate(new_word)
                break
            else:
                new_word = string
    return new_word
class Playfair(object):
    """docstring fos Playfair"""
    def __init__(self, keyword, plaintext):
        self.keyword = str(keyword)
        self.plaintext = plaintext
    def rm_spaces(self):
        new = ""
        for i in self.plaintext:
            if i == " ":
                pass
            else:
               new = new + i
        return new

    def create_table(self):
        alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ0123456789'
        key = []
        for i in self.keyword.upper():
            if i not in key:
                key.append(i)
        complements = []
        for i in key:
            if i not in complements:
                complements.append(i)
        for i in alphabet:
            if i not in complements:
                complements.append(i)
        matrix = []
        while complements != []:
            matrix.append(complements[:5])
            complements = complements[5:]
        return matrix

    


    def search_matrix(self, matrix, element):
        for i in range(7):
            for j in range(5):
                if (matrix[i][j] == element):
                    return i, j


    def row_Rule(self, matrix, x1, y1, x2, y2):
        character = ''
        if y1 == 4:
            character = matrix[x1][0]
        else:
            character = matrix[x1][y1 + 1]
        character_2 = ''
        if y2 == 4:
            character_2 = matrix[x2][0]
        else:
            character_2 = matrix[x2][y2 + 1]
        return character, character_2
    

    def col_Rule(self, matrix, x1, y1, x2, y2):
        character = ''
        if x1 == 4:
            character = matrix[0][y1]
        else:
            character = matrix[x1 + 1][y1]
        character_2 = ''
        if x2 == 4:
            character_2 = matrix[0][y2]
        else:
            character_2 = matrix[x2 + 1][y2]
        return character, character_2

    def other_Rule(self, matrix, x1, y1, x2, y2):
        character = ''
        character_2 = ''
        character = matrix[x1][y2]
        character_2 = matrix[x2][y1]
        return character, character_2

    def encrypt(self):
        Ciphered = []
        new_plaintext = self.rm_spaces()
        print(new_plaintext)
        non_duplicate = checkduplicate(new_plaintext)
        print(non_duplicate)
        non_duplicate = non_duplicate.upper()
        pure_input = create_diagraph(non_duplicate)
        if len(pure_input[-1] )!= 2:
            pure_input[-1] = pure_input[-1]+'Z'
        matrix = self.create_table()
        for i in range(0, len(pure_input)):
            c1 = 0
            c2 = 0
            ele_1x, ele_1y = self.search_matrix(matrix, pure_input[i][0])
            print(f'{ele_1x}{ele_1y}')
            ele_2x, ele_2y = self.search_matrix(matrix, pure_input[i][1])
            print(f'##{ele_2x}{ele_2y}')
            if ele_1x == ele_2x:
                c1, c2 = self.row_Rule(matrix, ele_1x, ele_1y, ele_2x, ele_2y)
            elif ele_1y == ele_2y:
                c1, c2 = self.col_Rule(matrix, ele_1x, ele_1y, ele_2x, ele_2y)
            else:
                c1, c2 = self.other_Rule(matrix, ele_1x, ele_1y, ele_2x, ele_2y)
            cipher = c1 + c2
            Ciphered.append(cipher)
        return Ciphered
if __name__ == '__main__':
    play = Playfair('Monarch67', 'instruments')
    c= play.encrypt()
    Encrypted = ""
    for char in c:
        Encrypted = Encrypted + char
    print(f'+++++++++++++++++++++\n The Encrypted text is {Encrypted} \n++++++++++++++++++++')