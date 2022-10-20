nama = input("masukkan nama anda :")
nilai = int(input("masukkan nilai anda :"))

if(nilai>=100):
    print("selamat {} nilai anda adalah A+".format(nama))
elif(nilai>90):
    print("selamat {} nilai anda adalah A".format(nama))
elif(nilai>80):
    print("selamat {} nilai anda adalah B".format(nama))
elif(nilai>70):
    print("selamat {} nilai anda adalah C".format(nama))
elif(nilai>60):
    print("selamat {} nilai anda adalah D".format(nama))
else:
    print("mohon maaf {} anda tinggal kelas".format(nama))
    
