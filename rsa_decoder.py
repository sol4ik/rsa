import string

from rsa_cryptosystem import RSA


class RSADecoder(RSA):
    def __init__(self):
        super().__init__()

        self.__decoded_msg = ''

    @property
    def decoded_msg(self):
        return self.__decoded_msg

    @decoded_msg.setter
    def decoded_msg(self, value):
        raise Exception('you cannot set a value to decoded_msg field')

    def __str__(self):
        return '''
        open key ({}, {})
        secret key {}
        '''.format(self.n, self.e, self.__d)

    @staticmethod
    def is_valid_msg(msg):
        for ch in msg:
            if ch not in string.digits:
                return False
        return True

    @staticmethod
    def is_valid_n(n):
        for number in RSA.PRIME_NUMBERS:
            if n % number == 0 and n // number in RSA.PRIME_NUMBERS:
                return number, n // number
        return False

    @staticmethod
    def is_valid_e(e):
        if e % 2 == 1 and e > 3:
            return True
        else:
            return False

    def postprocess_msg(self):
        tmp_msg = ''
        counter = 0
        for ch in self.__decoded_msg:
            tmp_msg += ch
            counter += 1
            if counter % 4 == 0:
                tmp_msg += '.'
        self.__decoded_msg = tmp_msg

        tmp = self.__decoded_msg
        msg = ''
        while '.' in tmp:
            pos = tmp.index('.')
            s = tmp[:pos]
            ch1 = s[:2]
            if int(ch1) != 99:
                ch1 = chr(int(ch1) + 97)
                msg += ch1
            ch2 = s[2:]
            if int(ch2) != 99:
                ch2 = chr(int(ch2) + 97)
                msg += ch2
            tmp = tmp[pos + 1:]

        self.__decoded_msg = msg

    def decode(self):
        self.preprocess_msg()
        self._find_d()

        self.__decoded_msg = self._calculate(self._d)

        self.postprocess_msg()

    def read(self):
        print('enter encoded message consisting only of digits')
        self.msg = input('> ')
        while not self.is_valid_msg(self.msg):
            print('! wrong input')
            self.msg = input('> ')
        self.tmp_msg = self.msg

        print('enter open key (n, e) for secret key generation')
        n_e = list(map(int, input('> ').strip().split()))
        while True:
            if len(n_e) != 2:
                print('! wrong input')
            elif not self.is_valid_n(n_e[0]) or not self.is_valid_e(n_e[1]):
                print('! n must be the product of two prime numbers and e must be odd')
            else:
                break
            n_e = list(map(int, input('> ').strip().split()))

        self.n = n_e[0]
        self.e = n_e[1]
        self.p = self.is_valid_n(self.n)[0]
        self.q = self.is_valid_n(self.n)[1]

    def get_result(self):
        """
        Function for users to get decoding result.
        :return:
        """
        print('''encoded message: {}
        open key: ({}, {})
        secret key: {}
        decoded message: {}'''.format(self.msg, self.n, self.e, self._d, self.__decoded_msg))

