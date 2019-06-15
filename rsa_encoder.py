import string

from rsa_cryptosystem import RSA


class RSAEncoder(RSA):
    """
    Class for encoding using RSA method.
    """
    def __init__(self):
        """
        Initial function for RSAEncoder object.
        """
        super().__init__()

        self.__encoded_msg = ''

    @property
    def encoded_msg(self):
        """
        :return: value of __encoded_msg field
        """
        return self.__encoded_msg

    @encoded_msg.setter
    def encoded_msg(self, value):
        raise Exception('you cannot set a value to encoded_msg field')

    def __repr__(self):
        """
        Function for developer's usage.
        :return: string consisting of RSA decoder's open and secret keys
        """
        return '''
        open key ({}, {})
        secret key {}
        '''.format(self.n, self.e, self.__d)

    @staticmethod
    def is_valid_msg(msg):
        """
        Method for checking whether user's input is valid.
        :param msg: user's input message
        :return: True if the message is valid, and False otherwise
        """
        for char in msg:
            if char not in string.ascii_letters and char not in string.punctuation and char != ' ':
                return False
        return True

    def preprocess_msg(self):
        """
        Overloaded method for message preprocessing for encoding.
        :return:
        """
        self.tmp_msg = self.tmp_msg.lower()
        cleared = ''
        for ch in self.tmp_msg:
            if ch in string.ascii_lowercase:
                cleared += ch

        c = ''
        for ch in cleared:
            c += '{:02d}'.format(ord(ch) - 97)
        if len(c) % 4 != 0:
            c += '99'
        self.tmp_msg = c

        super().preprocess_msg()

    def encode(self):
        """
        Method for encoding massage.
        :return:
        """
        self.preprocess_msg()
        self._find_e()

        self.__encoded_msg = self._calculate(self.e)

    def read(self):
        """
        Method for reading user's input, validating user's input
        and assigning the values to certain fields.
        :return:
        """
        print('enter message to encode in latin alphabet')
        self.msg = input('> ')
        while not self.is_valid_msg(self.msg):
            print('! wrong input')
            self.msg = input('> ')
        self.tmp_msg = self.msg

        print('enter (p, q) for open and secret keys generation')
        p_q = list(map(int, input('> ').strip().split()))
        while True:
            if len(p_q) != 2:
                print('! wrong input')
            elif p_q[0] not in self.PRIME_NUMBERS and p_q[1] not in self.PRIME_NUMBERS:
                print('! p and q must be prime numbers')
            else:
                break
            p_q = list(map(int, input('> ').strip().split()))

        self.p = p_q[0]
        self.q = p_q[1]
        self.n = self.p * self.q

        self.modify_primes()

    def get_result(self):
        """
        Function for users to get encoding result.
        :return:
        """
        print('''message: {}
open key: ({}, {})
encoded message: {}'''.format(self.msg, self.n, self.e, self.__encoded_msg))
