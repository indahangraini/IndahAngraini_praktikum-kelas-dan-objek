class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungkeliling(self):
      return 2* self.phi * self.jarijari
   def hitungluas(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   #Keliling Lingkaran
   lingkaransatu = lingkaran(3.14, 35)
   print ('Keliling Lingkaran')
   print('Objek lingkaransatu')
   print('phi\t:', lingkaransatu.phi)
   print('jarijari\t:', lingkaransatu.jarijari)
   print('Keliling lingkaran\t=', lingkaransatu.hitungkeliling())

   lingkarandua = lingkaran(3.14, 15)

   print("\nObjek lingkarandua")
   print('phi\t:', lingkarandua.phi)
   print('jarijari\t:', lingkarandua.jarijari)
   print("Keliling lingkaran\t=", lingkarandua.hitungkeliling())
   lingkaransatu = lingkaran(3.14, 30)

   #Luas Lingkaran
   print ('Luas Lingkaran')
   print('Objek lingkaransatu')
   print('phi\t: ', lingkaransatu.phi)
   print('jarijari\t: ', lingkaransatu.jarijari)
   print('Luas lingkaran\t= ', lingkaransatu.hitungluas())

   lingkarandua = lingkaran(3.14, 27)

   print("\nObjek lingkarandua")
   print('phi\t: ', lingkarandua.phi)
   print('jarijari\t: ', lingkarandua.jarijari)
   print("Luas lingkaran\t= ", lingkarandua.hitungluas())


if __name__ == "__main__":
   main()
