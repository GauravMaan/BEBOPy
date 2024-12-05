from Task11.string_util import reverse_string, is_palindrome
from Task11.number_util import is_even, is_prime


test_string = "madam"
print(f"Reverse of '{test_string}': {reverse_string(test_string)}")
print(f"Is '{test_string}' a palindrome? {is_palindrome(test_string)}")

test_number = 17
print(f"Is {test_number} even? {is_even(test_number)}")
print(f"Is {test_number} prime? {is_prime(test_number)}")