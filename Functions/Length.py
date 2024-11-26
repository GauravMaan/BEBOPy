city=["baltan","haryana","panchkula","goa"]
def length(city):
    return len(city)
sort=sorted(city,key=length,reverse=True)
print(sort)