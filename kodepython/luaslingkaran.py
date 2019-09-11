class lingkaran(object):
   def __init__(self, p, r):
      self.phi = p
      self.jarijari = r
   def hitungluas(self):
      return self.phi * self.jarijari * self.jarijari

def main():
   lingkaransatu = lingkaran(3.14, 30)

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
