from rsa_encoder import RSAEncoder
from rsa_decoder import RSADecoder


print('enter \'e\' if you want to encode message with the RSA cypher or \'d\' if you want to decode it')
mode = input('> ')
while mode not in ['e', 'd']:
    print('! wrong input')
    mode = input('> ')

if mode == 'e':
    encoder = RSAEncoder()
    encoder.read()
    encoder.encode()
    encoder.get_result()
else:
    decoder = RSADecoder()
    decoder.read()
    decoder.decode()
    decoder.get_result()
