class Calculator:
    def add(self, a, b):
        return a + b
    @staticmethod
    def info():
        print("This is a calculator class.")
cal = Calculator()
result = cal.add(10, 20)
print(f"The sum of 10 and 20 is: {result}")
Calculator.info()