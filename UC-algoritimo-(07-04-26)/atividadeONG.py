pao = int(input("P:"))
doce = int(input("D:"))
bolo = int(input("B:"))

total = pao + (doce * 2) + (bolo * 3)

if 0 <= pao <= 100 and 0 <= doce <= 100 and 0 <= bolo <= 100:
    if total >= 150:
        print("B")
    elif total >= 120:
        print("D")
    elif total >= 100:
        print("P")
    else:
        print("N")
else:
    print("N")
