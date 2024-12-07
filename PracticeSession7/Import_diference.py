# The difference between import module_name and from module_name import specific_function lies in
# how you access the functionality of a module:
# 	1.	import module_name:
# 	•	Imports the entire module.
# 	•	To use a function or attribute, you must prefix it with the module’s name.
# 	2.	from module_name import specific_function:
# 	•	Imports only the specified functions or attributes.
# 	•	You can use the imported function directly without the module’s prefix.
import math

print("Using `import math`:")
print(f"Square root of 16: {math.sqrt(16)}") 
print(f"Value of pi: {math.pi}")

# Using `from module_name import specific_function`
from math import sqrt, pi

print("\nUsing `from math import sqrt, pi`:")
print(f"Square root of 16: {sqrt(16)}")  # Access directly
print(f"Value of pi: {pi}")