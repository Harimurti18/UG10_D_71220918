def menu():
    print ("\(^o^) Selamat datang di Kalkulator Sederhana (^o^)/")
    print ("Ketik 1 untuk menghitung penjumlahan.")
    print ("Ketik 2 untuk menghitung pengurangan.")
    print ("Ketik 3 untuk menghitung perkalian.")
    print ("Ketik 4 untuk menghitung pembagian.")
    print ("Ketik 5 untuk menghitung sisa hasil bagi(modulus).")
    print ("Ketik 6 untuk menghitung pemangkatan.")

def penjumlahan():
    n=int(input("Masukan bilangan pertama: "))
    n1=int(input("Masukan bilangan kedua: "))
    h = n+n1
    print ("Hasil dari",n,"dijumlahkan dengan",n1,"adalah",h)

def pengurangan():
    n=int(input("Masukan bilangan pertama: "))
    n1=int(input("Masukan bilangan kedua: "))
    h = n-n1
    print ("Hasil dari",n,"dikurangkan dengan",n1,"adalah",h)

def perkalian():
    n=int(input("Masukan bilangan pertama: "))
    n1=int(input("Masukan bilangan kedua: "))
    h= n*n1
    print ("Hasil dari",n,"dikalikan dengan",n1,"adalah",h)

def pembagian():
    n=int(input("Masukan bilangan pertama: "))
    n1=int(input("Masukan bilangan kedua: "))
    h= n/n1
    print ("Hasil dari",n,"dibagi dengan",n1,"adalah",h)

def sisa():
    n=int(input("Masukan bilangan pertama: "))
    n1=int(input("Masukan bilangan kedua: "))
    h= n%n1
    print ("Hasil dari",n,"dimodulus dengan",n1,"adalah",h)

def pangkat():
    n=int(input("Masukan bilangan pertama: "))
    n1=int(input("Masukan bilangan kedua: "))
    h= n**n1
    print ("Hasil dari",n,"dipangkatkan dengan",n1,"adalah",h)

menu()
pilih = int(input("Masukan pilihan Anda: "))
if pilih == 1:
    penjumlahan()
elif pilih == 2:
    pengurangan()
elif pilih == 3:
    perkalian()
elif pilih == 4:
    pembagian()
elif pilih == 5:
    sisa()
elif pilih == 6:
    pangkat()
else:
    print ("inputan salah")