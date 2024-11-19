start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
primeNo = []
count=0
for j in range(start, end + 1):
    if j > 1:
        is_prime = True
        for i in range(2, int(j ** 0.5) + 1):
            if j % i == 0:
                is_prime = False
                break
        if is_prime:
            primeNo.append(j)
            count += 1
print(f"Prime numbers in the range {primeNo} and count is {count}")
