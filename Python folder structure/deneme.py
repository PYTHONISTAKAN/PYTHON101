file = open("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt", "w", encoding="utf-8") #write

file.write("Atakan Guven\n")
file.close()
file = open("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt", "a", encoding="utf-8") #append
file.write("Eren Guven\n")
file.write("Ali Guven\n")
file.write("Fahriye Guven\n")
file.close()

try:
    file= open("logs.txt","r",encoding="utf-8")
except FileNotFoundError:
    print("dosya bulunamadi")

file= open ("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt","r",encoding="utf-8")

icerik = file.read()
print("dosyanin icerigi: ")
print(icerik)


icerik2 = file.read()
print("dosyanin icerigi2: ")
print(icerik2)
file.close()
print("dosyayi ust okumada kapatip-acip tekrar okutmamiz gerekiyordu. bir kere okuyunca sona aliyor")

file= open ("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt","r",encoding="utf-8")

print(file.readline())
print(file.readline())
file.close()

file= open ("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt","r",encoding="utf-8")
print (file.readlines())
file.close()

with open ("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt","r",encoding="utf-8") as file:
    file.seek(5)
    icerik = file.read(10)
    print(icerik)
    file.seek(0)
    icerik2 = file.read(6)
    print(icerik2)

with open("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt","r+",encoding="utf-8") as file:
    liste = file.readlines()
    liste.insert(3,"Pasa Guven\n")
    file.seek(0)
    file.writelines(liste)
    
with open("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/logs.txt","r+",encoding="utf-8") as file:
    print(file.read())