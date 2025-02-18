def primes(start, end):
    demo = []
    for i in range(start, end + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                demo.append(i)
    return demo
start = 1
end = 20
print(primes(start, end))
