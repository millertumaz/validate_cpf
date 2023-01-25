import re

class ValidateCPF:

    def __init__(self, cpf):
        self.cpf = cpf

    @property
    def cpf(self):
        return self._cpf
    
    @cpf.setter
    def cpf(self, cpf):
        self._cpf = self.numberonly(cpf)

    @staticmethod
    def numberonly(cpf):
        return re.sub('[^0-9]', '', cpf)
    
    def validates(self):
        if not self.cpf:
            return False       
        
        new_cpf = self.calculate_digits(self.cpf[:9])
        new_cpf = self.calculate_digits(new_cpf)

        if new_cpf == self.cpf:
            return True
        return False

    @staticmethod
    def calculate_digits(nine_digits):
        if not nine_digits:
            return False

        sequence = nine_digits[0] * len(nine_digits)
        
        if sequence == nine_digits:
            return False

        sum=0
        for key, multiplier in enumerate(range(len(nine_digits)+1, 1, -1)):
            sum += int(nine_digits[key]) * multiplier

        leftover = 11 - (sum%11)
        leftover = leftover if leftover <= 9 else 0

        return f'{nine_digits}{leftover}'
