
print("Yooo")
try:
    print(10/0)
    print(10/5)
    print(10/0)
# except:
#    print("wrong code")
except Exception as a:
    print(a)

n=10
n1=0
try:
    ans=n-n1
    print(ans)
except Exception as a:
    print(a)
else:
    print("koi exception nhi hai")
finally:
    print("chal gya code")
