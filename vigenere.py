keyed_alphabet = "KRYPTOSABCDEFGHIJLMNQUVWXZ0123456789"
DEBUG = 1
table = [list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////'), list('////////////////////////////////////')]
plaintext = list('////////////////////////////////////////////////////////////////////////////////////////////////////')
key = list('////////////////////////////////////////////////////////////////////////////////////////////////////')
ciphertext = list('////////////////////////////////////////////////////////////////////////////////////////////////////')

def generate_alphabet(alphabet):
    offset = 0
    # i is top
    # j is side

    for i in range(0, 36):
        k = 0
        for j in range(0, 36):
            tmp = k + offset
            while tmp > 35:
                if tmp > 35:
                    tmp = tmp - 36
            table[i][j] = alphabet[tmp]
            k = k + 1
        offset = offset + 1

if DEBUG:
    def dbg_print_alphabet():
        # TODO: figure out why we get an extra newline every single line
        print("DEBUG: PRINT VIGENERE TABLE")
        for i in range(0, 36):
            for j in range(0, 36):
                print(table[i][j], end='')
            print('\n')

def extend_key(keyu):
    tmp = int(len(plaintext) / len(keyu))
    tmp2 = int(len(plaintext) % len(keyu))
    global key
    key = keyu * tmp + keyu[:tmp2]

def encrypt():
    for count in range(0, len(plaintext), 1):
        if plaintext[count] == '/':
            return
        j = keyed_alphabet.index(plaintext[count])
        i = keyed_alphabet.index(key[count])
        global ciphertext
        ciphertext[count] = table[i][j]

def decrypt():
    for count in range(0, len(ciphertext), 1):
        if ciphertext[count] == '/':
            return
        j = keyed_alphabet.index(key[count])
        current_row = table[j]
        i = current_row.index(ciphertext[count])
        global plaintext
        plaintext[count] = keyed_alphabet[i]

def set_key(keyl):
    print('DEPRECATED FUNCTION - MOVE ASAP TO EXTEND_KEY()')
    tmp = len(keyl)
    tmp = 100 - tmp
    tmp = '/' * tmp
    global key
    key = list(keyl + tmp)

def set_plaintext(plaintextl):
    tmp = len(plaintextl)
    tmp = 100 - tmp
    tmp = '/' * tmp
    global plaintext
    plaintext = list(plaintextl + tmp)

def get_plaintext():
    return ''.join(plaintext[:plaintext.index('/')])

def set_ciphertext(ciphertextl):
    tmp = len(ciphertextl)
    tmp = 100 - tmp
    tmp = '/' * tmp
    global ciphertext
    ciphertext = list(ciphertextl + tmp)

def get_ciphertext():
    return ''.join(ciphertext[:ciphertext.index('/')])

def set_alphabet():
    print('This function is not implemented by design. If you want to set the alphabet please a. figure out how the Vigenere cipher works and b1. either write this function yourself or b2. change the keyed_alphabet variable in the code.')
    raise NotImplementedError

def get_alphabet():
    return keyed_alphabet
