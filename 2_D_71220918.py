n1 = input("Masukan nama pemain pertama: ")
n2 = input("Masukan nama pemain kedua: ")
n3 = input("Masukan nama pemain ketiga: ")
a1 = int(input("Masukan jumlah kartu pemain pertama: "))
a2 = int(input("Masukan jumlah kartu pemain kedua: "))
a3 = int(input("Masukan jumlah kartu pemain ketiga: "))

if (a1> (a2 and a3)):
    print(n1, "menang dengan jumlah kartu sebanyak", a1)
elif (a2 (a1 and a3)):
    print(n2, "menang dengan jumlah kartu sebanyak", a2)
elif (a3> (a1 and a2)):
    print(n3, "menang dengan jumlah kartu sebanyak", a3)
elif (a1>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
elif (a2>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
elif (a3>21):
    print("Jumlah kartu yang dimiliki melebihi batas")
