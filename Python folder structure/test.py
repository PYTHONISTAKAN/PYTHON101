
user = {
    "username": "atakan",
    "password": "123456",
    "email": "atakanguven42@gmail.com",
    "phone": "000000"
}

for i in user:
    print(i)
for key, value in user.items():
    print(key, ":", value)

x = input("Lutfen isminizi giriniz ")
print(" hos geldin "+ x  +" basarilar..")


while (True):
    
    a = int(input("1st number: "))
    b = int(input("2nd number: "))

    c= a+b
    if(c%2==0):
        print("sayilarin toplamlari cift")
    else:
        print("sayilarin toplamlari tek")

    print("sayilarin sifirdan en buyugune gore siralanmasi")
    liste=[]
    i=0
    if (a < b): 
        for i in range (i,b+1):
            liste.append(i)
            print (liste)
    elif(b < a):
        for i in range (i,a+1):
            liste.append(i)
            print (liste)
    else:
        for i in range(i,a+1):
            liste.append(i)
            print (liste)

    x= input("cikis icin 'quit' yazin. devam etmek icin gecin. ")
    if (x=='quit'):
        break
    else:
        continue
