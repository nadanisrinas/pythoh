from abc import abstractmethod


class Warga: 
    def __init__(self, NIK: str): 
        self.NIK = NIK 

    # def nyoblos(self, pilihan: str):
    #     self.pilihan = pilihan 
    #     print(f"{self.nik} memlilih {pilihan}")
        
    @abstractmethod
    def nyoblos(self, pilihan: str):
        pass

class Satpam(Warga):
    def __init__(self, NIK: str, id_satpam): 
        self.nik = NIK 
        Warga.__init__(self,NIK)
        self.id_satpam = id_satpam
    def jaga_tpu(self, tempat:str): 
        print(f"{self.id_satpam} jaga di {tempat}")

class Petugas(Warga):
    def __init__(self, NIK: str, id_petugas): 
        self.nik = NIK 
        Warga.__init__(self,NIK)
        self.id_petugas = id_petugas
    def ngitung_suara(self, daftar_suara, tempat:str): 
        self.ngitung_suara = {}
        self.rekap_suara["tempat"] = tempat

        for suara in daftar_suara: 
            if suara in self.rekap_suara:
                self.rekap_suara[suara] += 1
            else: 
                self.rekap_suara[suara] = 1
        self.rekap_suara

class TNI(Warga): 
        def __init__(self, NIK: str, id_tni): 
            Warga.__init__(self,NIK)
            self.id_tni = id_tni

        def nyoblos(self, pilihan: str):
            self.pilihan = pilihan 
            print(f"{self.NIK} tidak bisa memlilih karena terdeteksi id tni {self.id_tni}")

mukhlis = Satpam("12334343", "satpam1232424")
print(mukhlis.NIK)
mukhlis.nyoblos("megawati")
mukhlis.jaga_tpu("sukamaju")


# mukhlis = Satpam("12334343", "satpam1232424")
# print(mukhlis.NIK)
# print(mukhlis.id_satpam)


# joko = TNI("12334343", "satpam1232424")
# joko.nyoblos("megawati")