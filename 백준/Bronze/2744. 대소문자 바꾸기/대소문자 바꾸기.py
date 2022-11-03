a = input()
b = ""

for i in range(len(a)) :
    if a[i].isupper() == True :
        b += a[i].lower()
    else :
        b += a[i].upper()
        
print(b)