import random

ogrenciSayisi = random.randint(10,15)

notlar = list()

sayacAA = 0
sayacBA = 0
sayacBB = 0
sayacCB = 0
sayacCC = 0

for i in range(ogrenciSayisi):
    data = random.randint(50,100)
    notlar.append(data)
    print(notlar[i])
    if notlar[i] >= 50 and notlar[i] < 60:
        sayacCC += 1
    elif notlar[i] >= 60 and notlar[i] < 70:
        sayacCB += 1
    elif notlar[i] >= 70 and notlar[i] < 80:
        sayacBB += 1
    elif notlar[i] >= 80 and notlar[i] < 90:
        sayacBA += 1
    else:
        sayacAA += 1

print("\n50 - 59 ->{}".format(sayacCC*'#'))
print("60 - 69 ->{}".format(sayacCB*'#'))
print("70 - 79 ->{}".format(sayacBB*'#'))
print("80 - 89 ->{}".format(sayacBA*'#'))
print("90 - 100 ->{}".format(sayacAA*'#'))
