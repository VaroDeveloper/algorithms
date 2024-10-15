def next_number(digits, base):
    """
    :param digits: list containing all the digits of a number 
                   in the given base
    :param base: numeric base of the number
    :return: list representing the next value of the number

     Example: digits = [0, 1, 0, 1]   number 5
                base = 2

              returns [0, 1, 1, 0]    number 6
    """

    next_digits = digits.copy()
    carry = 1

    # Añade tu código aqui
    for i in range(len(next_digits) - 1, -1, -1):
        next_digits[i] += carry
        if next_digits[i] >= base:
            next_digits[i] = 0
            carry = 1
        else:
            carry = 0

    return next_digits

# ----------------------------------------------------------

class My_Iterator:

    def __init__(self, num_digits, base):
        # 2.1 Añade código aqui
        self.num_digits = num_digits
        self.base = base
        self.current = [0] * num_digits
        self.finished = False

    def next(self):
        
        while not self.finished:
            yield self.current.copy()

            next_value = next_number(self.current, self.base)

            if next_value == [0] * self.num_digits:
                self.finished = True

            self.current = next_value
