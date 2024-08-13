# keyed-vigenere-cipher-with-numbers
Encryption &amp; decryption library for a keyed Vigenere cipher fork with support for encrypting numbers.

## How to use

### Normal functions

#### generate_alphabet(alphabet)

Generates a Vigenere table (also known as a tabula recta) from a given 36-letter string, where every character is unique. There's no error handling so be careful.

Default alphabet is "KRYPTOSABCDEFGHIJLMNQUVWXZ0123456789" (the kryptos thing is left in there from initial sanity testing)

#### extend_key(keyu)

Extends (see how a Vigenere cipher works to figure out what this means) and sets the key.

WARNING: You MUST initialize the "plaintext" variable using set_plaintext before using this, or stuff WILL break.

WARNING 2: Maximum key length is 100 characters (see jank code warning at the bottom for reasons)

#### encrypt()

Encrypts the string in plaintext using key and keyed_alphabet and puts the result in ciphertext.

WARNING: Maximum plaintext length is 100 characters (see jank code warning at the bottom for reasons)

#### decrypt()

Decrypts the string in ciphertext using key and keyed_alphabet and puts the result in plaintext.

WARNING: Maximum ciphertext length is 100 characters (see jank code warning at the bottom for reasons)

#### set_key(keyl)

Leftover from original C code API which I have no idea why I added. DO NOT USE.

#### set_plaintext(plaintextl)

Sets plaintext to plaintextl, with the necessary padding.

#### get_plaintext()

Returns a str containing the plaintext (without the internal padding).

#### set_ciphertext(ciphertextl)

Sets ciphertext to ciphertextl, with the necessary padding.

#### get_ciphertext()

Returns a str containing the ciphertext (without the internal padding).

#### set_alphabet()

Unimplemented by design. I don't want any of you debugging for 3 hours because you don't know how this cipher works.

#### get_alphabet()

Returns an str containing the keyed alphabet.

### Debug-only functions (accessible with DEBUG = 1)

#### dbg_print_alphabet()

Prints the tabula recta (also known as the Vigenere table)

## Usage example

```py
generate_alphabet(keyed_alphabet)
dbg_print_alphabet()
set_plaintext('NUMBERTEST1245780369')
extend_key('HIDDEN')
encrypt()
print(get_ciphertext())
decrypt()
print(get_plaintext())
print(get_alphabet())
```

## JANK CODE WARNING

This code has been originally written in C for a personal project, no outside consumers were ever intended. Because of this the code makes several assumptions about string lengths (refer to the code). After the code was translated into Python for a different project no issues were ever resolved. PRs are still welcome though.
