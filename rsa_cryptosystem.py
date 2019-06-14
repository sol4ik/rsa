from help_math import generate_primes, gcd


class RSA:
    """
    Basic class for RSA encoder and decoder that consists of common fields and methods.
    """
    PRIME_NUMBERS = generate_primes(100)

    def __init__(self):
        """
        Initial function for RSA object (encoder and decoder as well).
        """
        self.n = 0
        self.e = 0

        self.p = 0
        self.q = 0

        self._d = 0

        self.msg = None
        self.tmp_msg = None

    def __str__(self):
        """
        Function for string representation of RSA object.
        :return: string with open key od RSA cypher.
        """
        return 'open key ({}, {})'.format(self.n, self.e)

    def _find_p_q(self):
        """
        Function for finding prime p and q for decoder with open key.
        :return: False, if prime p and q weren't found
        """
        for num in self.PRIME_NUMBERS:
            if self.n % num == 0 and self.n / num in self.PRIME_NUMBERS:
                self.p, self.q = num, self.n / num
        return False

    def _find_e(self):
        """
        Function for calculating e for RSA open key.
        :return: False, if odd e wasn't found
        """
        for num in range(3, max(self.p, self.q), 2):
            if gcd((self.p - 1) * (self.q - 1), num)[0] == 1:
                self.e = num
                return True
        return False

    def _find_d(self):
        """
        Function for calculating RSA secret key.
        :return:
        """
        self._d = gcd(self.e, (self.p - 1) * (self.q - 1))[1]
        if self._d < 0:
            self._d += (self.p - 1) * (self.q - 1)

    @staticmethod
    def is_valid_msg():
        """
        Abstract staticmethod for checking whether user's input message was correct.
        :return:
        """
        raise NotImplementedError('this method must be implemented for RSA encoder/decoder')

    def preprocess_msg(self):
        """
        Function for preprocessing the encoded message.
        :return:
        """
        tmp_msg = ''
        counter = 0
        for ch in self.tmp_msg:
            tmp_msg += ch
            counter += 1
            if counter % 4 == 0:
                tmp_msg += '.'
        self.tmp_msg = tmp_msg

    def _calculate(self, power):
        """
        Function for RSA calculations.
        :param power: e for RSAEncoder and d for RSA decoder
        :return: calculated message
        """
        tmp = self.tmp_msg
        to_return = ''
        while '.' in tmp:
            pos = tmp.index('.')
            m = int(tmp[:pos])
            m = (m ** power) % self.n
            to_return += '{:04d}'.format(m)
            tmp = tmp[pos + 1:]

        return to_return

    def modify_primes(self):
        """
        Function for modifying instance's PRIME_NUMBERS value.
        :return:
        """
        if self.n > 100:
            self.PRIME_NUMBERS = generate_primes(self.n)

    def read(self):
        """
        Abstract method for reading user's input.
        :return:
        """
        raise NotImplementedError('this method must be implemented for RSA encoder/decoder')

    def get_result(self):
        """
        Abstract method for results output.
        :return:
        """
        raise NotImplementedError('this method must be implemented for RSA encoder/decoder')
