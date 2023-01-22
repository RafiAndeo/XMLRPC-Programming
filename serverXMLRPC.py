from xmlrpc.server import SimpleXMLRPCServer

list_pilihan = []
list_nama = []
list_noCalon = []
hasil = []

def reqDaftarCalon(list_nama, list_noCalon):
    print("Berikut daftar calon yang tersedia: ")
    n = len(list_nama)
    for i in range(n):
        print(list_noCalon[i], "dengan nama: ", list_nama[i])
    return list_nama, list_noCalon

def reqPilihCalon(pilihan):
    list_pilihan.append(pilihan)
    print("Berikut daftar pilihan calon: ", list_pilihan)
    return list_pilihan

server = SimpleXMLRPCServer(("127.0.0.1", 8008))
server.register_function(reqDaftarCalon, "reqDaftarCalon")
server.register_function(reqPilihCalon, "reqPilihCalon")
server.serve_forever()