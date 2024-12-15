class EvenNumbers:
    def generate_numbers(self, n):
        return [2 * i for i in range(n)]

class OddNumbers:
    def generate_numbers(self, n):
        return [2 * i + 1 for i in range(n)]

def print_numbers(generator, n):
    numbers = generator.generate_numbers(n)
    print(f"Generated numbers: {numbers}")
even = EvenNumbers()
odd = OddNumbers()
print_numbers(even, 5)
print_numbers(odd, 5)
