#!/usr/bin/python
from argparse import ArgumentParser
from bcrypt import gensalt, hashpw
from Crypto.Cipher import AES
from hashlib import sha256

import os, struct

def main():
    parser = ArgumentParser(description = "Encrypts or decrypts a file using " +
                            "bcrypt for the password and triple AES for file encryption.")
    parser.add_argument('-p', '--passphrase', required = True, 
                        help = "The passphrase to use for encryption.")
    parser.add_argument('-i', '--input', required = True,
                        help = "The input file for encryption / decryption.")
    parser.add_argument('-o', '--output', required = True,
                        help = "The output file for encryption / decryption.")
    parser.add_argument('-r', '--rounds', default = 10, 
                        help = "The number of bcrypt rounds to use.")
    parser.add_argument('-s', '--salt', default = None,
                        help = "The salt to use with bcrypt in decryption.")
    parser.add_argument('operation', choices = ('encrypt', 'decrypt'),
                        help = "The operation to apply, whether to encrypt or decrypt data.")

    parameters = parser.parse_args()

    print "Got salt from parameters: {}".format(parameters.salt)

    print "Salt: "
    salt = raw_input()
    
    if parameters.operation == 'encrypt':
        encrypt(parameters.input, parameters.output, parameters.passphrase,
                parameters.rounds)
    elif parameters.operation == 'decrypt':
        decrypt(parameters.input, parameters.output, parameters.passphrase,
                salt)

def encrypt(input_file, output_file, passphrase, rounds):
    bcrypt_salt = gensalt(rounds)
    bcrypt_passphrase = hashpw(passphrase, bcrypt_salt)
    passphrase_hash = sha256(bcrypt_passphrase).digest()

    print "Salt: %s" % (bcrypt_salt, )

    iv = os.urandom(16)

    cipher = AES.new(passphrase_hash, AES.MODE_CBC, iv)

    with open(input_file, 'rb') as infile:
        infile.seek(0, 2)
        input_size = infile.tell()

        infile.seek(0)  

        with open(output_file, 'wb') as outfile:
            outfile.write(struct.pack('<Q', input_size))
            outfile.write(iv)

            while True:
                chunk = infile.read(64 * 1024)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' ' * (16 - len(chunk) % 16)

                outfile.write(cipher.encrypt(chunk))

    return bcrypt_salt

def decrypt(input_file, output_file, passphrase, salt):
    print "Salt: %s" % (salt,)

    bcrypt_passphrase = hashpw(passphrase, salt)
    passphrase_hash = sha256(bcrypt_passphrase).digest()

    with open(input_file, 'rb') as infile:
        input_size = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)

        cipher = AES.new(passphrase_hash, AES.MODE_CBC, iv)

        with open(output_file, 'wb') as outfile:
            while True:
                chunk = infile.read(64 * 1024)
                if len(chunk) == 0:
                    break

                outfile.write(cipher.decrypt(chunk))

            outfile.truncate(input_size)

if __name__ == "__main__":
    main()
