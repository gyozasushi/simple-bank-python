import random



print("Registrasikan akun anda")
print(100*'=')
#data-data regis
data_nama = []
data_rekening = []
pin = []
saldo_awal=[]
#end
rek = random.randint(20000,30000)

nm = input("Masukkan Nama lengkap kamu : ")
np = input ("Masukkan Pin Untuk Atm : ")
sa = input ("Masukkan jumlah saldo awal : ")
data_nama.append(nm)
pin.append(np)
saldo_awal.append(sa)
print("akun telah berhasil terdaftar ")
print("Nomor rekening anda : ",rek)
data_rekening.append(rek)

print('')
login = False
while not login :
    pin_member= input("masukkan pin atm : ")
    pw = pin_member in pin

    if pw == True :
        print("Selamat datang",data_nama[0],"di mesin ATM kami")
        while True:

            def hasil():
                

                print("Silahkan pilih menu : ")
                print("1. Informasi akun")
                print("2. Penarikan Saldo")
                print("3. Setor Tunai")

                c = input("Masukkan pilihan anda: ")
                pilihan = int(c)

                if pilihan == 1:
                    print("Nomor rekening anda:",data_rekening[0])
                    print("Saldo anda adalah:", saldo_awal[0])
                    print("Nama Anda Adalah : ",data_nama[0])

                elif pilihan == 2:
                    x = input("Masukkan jumlah penarikan: ")
                    tarik = int(x)
                    if tarik <= int(saldo_awal[0]):
                        saldo_awal[0] = str(int(saldo_awal[0]) - tarik)
                        print("Penarikan berhasil, saldo anda tersisa:", saldo_awal[0])
                    else:
                        print("Saldo anda tidak mencukupi")

                elif pilihan == 3:
                    x = input("Masukkan jumlah setor tunai: ")
                    setor = int(x)
                    saldo_awal[0] = str(int(saldo_awal[0]) + setor)
                    print("Setor tunai berhasil, saldo anda:", saldo_awal[0])

                else:
                    print("Pilihan tidak valid. Silahkan pilih menu kembali.")

            hasil()

            print("Lanjutkan lagi?")
            a = input("(ya/tidak)")
            jawab = str(a)
            if jawab.lower() != "ya":
                print("Terimakasih Telah menggunakan ATM ini")
                break
        
    else :
        print("pin anda salah, coba lagi")

    






