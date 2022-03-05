"""
CMPS 2200  Recitation 3.
See recitation-03.pdf for details.
"""
import time


class BinaryNumber:
    """ done """

    def __init__(self, n):
        self.decimal_val = n
        self.binary_vec = list('{0:b}'.format(n))

    def __repr__(self):
        return ('decimal=%d binary=%s' % (self.decimal_val, ''.join(self.binary_vec)))


## Implement multiplication functions here. Note that you will have to
## ensure that x, y are appropriately sized binary vectors for a
## divide and conquer approach.
def _quadratic_multiply(x, y):  # returns binary number object
    # x is a BinaryNumber
    # y is a BinaryNumber

    if str(type(x)) == "<class 'int'>":
        xbin = BinaryNumber(x)
    else:
        xbin = BinaryNumber(x.decimal_val)

    if str(type(y)) == "<class 'int'>":
        ybin = BinaryNumber(y)
    else:
        ybin = BinaryNumber(y.decimal_val)

    x_vec = xbin.binary_vec  # type list
    y_vec = ybin.binary_vec  # type list

    x_vec, y_vec = pad(x_vec, y_vec)
    n = len(x_vec)

    if xbin.decimal_val <= 1 and ybin.decimal_val <= 1:
        return BinaryNumber(xbin.decimal_val * ybin.decimal_val)

    else:
        x_left, x_right = split_number(x_vec)  # object type BinaryNumber
        y_left, y_right = split_number(y_vec)  # object type BinaryNumber

        left = (_quadratic_multiply(x_left.decimal_val, y_left.decimal_val))
        left_middle = (_quadratic_multiply(x_left.decimal_val, y_right.decimal_val))
        right_middle = (_quadratic_multiply(x_right.decimal_val, y_left.decimal_val))
        right = (_quadratic_multiply(x_right.decimal_val, y_right.decimal_val))
        middle = BinaryNumber(left_middle.decimal_val + right_middle.decimal_val)

        left = (bit_shift(left, n))
        middle = (bit_shift(middle, (n // 2)))
        result = BinaryNumber(left.decimal_val + middle.decimal_val + right.decimal_val)

        return BinaryNumber(result.decimal_val)


def quadratic_multiply(x, y):  # returns integer
    return (_quadratic_multiply(x, y)).decimal_val


def binary2int(binary_vec):
    if len(binary_vec) == 0:
        return BinaryNumber(0)
    return BinaryNumber(int(''.join(binary_vec), 2))


def split_number(vec):
    return (binary2int(vec[:len(vec) // 2]),
            binary2int(vec[len(vec) // 2:]))


def bit_shift(number, n):
    # append n 0s to this number's binary string
    return binary2int(number.binary_vec + ['0'] * n)


def pad(x, y):
    # pad with leading 0 if x/y have different number of bits
    # e.g., [1,0] vs [1]
    # ensures that both vectors are equal lengths
    if len(x) < len(y):
        x = ['0'] * (len(y) - len(x)) + x
    elif len(y) < len(x):
        y = ['0'] * (len(x) - len(y)) + y
    # pad with leading 0 if not even number of bits
    # adds a 0 if the len is odd
    if len(x) % 2 != 0:
        x = ['0'] + x
        y = ['0'] + y
    return x, y


## Feel free to add your own tests here.
def test_multiply():
    assert quadratic_multiply(BinaryNumber(2), BinaryNumber(2)) == 2 * 2


def time_multiply(x, y, f):
    start = time.time()
    # multiply two numbers x, y using function f
    return (time.time() - start) * 1000
