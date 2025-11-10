class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        result = 0
        for i in range(b):
            result = self.add(result, a)
        return result

    def divide(self, a, b):
        negative = (a < 0) ^ (b < 0) 
        a, b = abs(a), abs(b)
        
        result = 0
        while a >= b:
            a = self.subtract(a, b)
            result += 1

        if negative:
            result = -result
        
        return result

    
    def modulo(self, a, b):
        sign_a = 1 if a >= 0 else -1
        sign_b = 1 if b >= 0 else -1

        a, b = abs(a), abs(b)

        while a >= b:
            a -= b

        if sign_a != sign_b and a != 0:
            a = b - a

        if sign_b == -1:
            a = -a

        return a


# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))