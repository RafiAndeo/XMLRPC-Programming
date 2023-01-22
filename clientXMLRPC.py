import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://127.0.0.1:8008/")

nama = []
noCalon = []

n = int(input("Masukkan jumlah calon: "))
for i in range(n):
    x = input("Masukkan nama calon: ")
    nama.append(x)
    y = input("Masukkan nomor calon: ")
    noCalon.append(y)
    proxy.reqDaftarCalon(nama, noCalon)

pilihan = int(input("Masukkan nomor calon yang dipilih: "))
proxy.reqPilihCalon(pilihan)
print("Terima kasih atas partisipasi Anda!")
print("Anda telah memilih calon nomor", pilihan)