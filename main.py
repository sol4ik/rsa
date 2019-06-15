"""
The main module of the system.
User input reading.
"""

from rsa_encoder import RSAEncoder
from rsa_decoder import RSADecoder

while True:
    print('''enter \'e\' if you want to encode message with the RSA cypher
\'d\' if you want to decode it
\'q\' if you want to quit the program''')
    mode = input('> ')
    while mode not in ['e', 'd', 'q']:
        print('! wrong input')
        mode = input('> ')

    if mode == 'e':  # encoding mode
        encoder = RSAEncoder()
        encoder.read()
        encoder.encode()
        encoder.get_result()
        print('\n\n')
    elif mode == 'd':  # decoding mode
        decoder = RSADecoder()
        decoder.read()
        decoder.decode()
        decoder.get_result()
        print('\n\n')
    else:  # quit
        break
