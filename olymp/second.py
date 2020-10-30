crois = int(input())
ecler = int(input())

amount_crois = 0
amount_ecler = 0

if (crois + ecler) % 3 == 0:
    boxes = (crois + ecler) // 3
    if crois < boxes or ecler < boxes:
        print(-1)
    else:
        amount_ecler = (2*ecler - crois) // 3
        amount_crois = (crois - amount_ecler) // 2
        print(amount_crois, amount_ecler)

else:
    print(-1)
