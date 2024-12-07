students = [{"name": "Alice", "age": 24}, {"name": "Bob", "age": 22}, {"name": "Charlie", "age": 23}]
students_sorted = sorted(students, key=lambda x: x['age'])
print("Sorted students by age:", students_sorted)
