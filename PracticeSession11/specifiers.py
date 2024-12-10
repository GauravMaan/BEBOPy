class AccessSpecifier:
    public_var = "I am a public variable"
    _protected_var = "I am a protected variable"
    __private_var = "I am a private variable"
    def __init__(self, name):
        self.name = name
    def public_method(self):
        return f"Public method: {self.public_var}"
    def _protected_method(self):
        return f"Protected method: {self._protected_var}"
    def __private_method(self):
        return f"Private method: {self.__private_var}"
obj = AccessSpecifier("John")
print(obj.public_var)
print(obj.public_method())
print(obj._protected_var)
print(obj._protected_method())
print(obj._AccessSpecifier__private_var)
print(obj._AccessSpecifier__private_method())