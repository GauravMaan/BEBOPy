# def mui(n):
#     return lambda x:x*n
# ans=mui(5)
# print(ans(5))
def outer(n):
    def inner(m):
        return f"Outer variable: {n}, Inner variable: {m}"
    return inner

nested = outer("Hello")
result = nested("World")
print(result)