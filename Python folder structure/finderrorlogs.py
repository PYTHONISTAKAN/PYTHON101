log = file = open("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/Python folder structure/testlogs.txt", "r", encoding="utf-8")
errors = file = open("C:/Users/qxtel/Documents/AtakanPHYTON/denemeler/Python folder structure/errors.txt", "w", encoding="utf-8")

line_number = 1
for line in log:
    # satırı kelimelere böl ve küçük harfe çevir
    words = line.lower().split()
    
    # eğer kelimeler arasında "error" varsa yaz
    if "error" in words:
        errors.write(str(line_number) + ": " + line)
    
    line_number += 1

log.close()
errors.close()