nama = input(" nama (andi/budi/citra) :")

if nama =="andi":
   target = 70
elif nama =="budi":
   target = 75 
elif nama == "citra":
   target = 80 
else :
    target =0

if target == 0:
   print ("nama tidak daftar")
else :
   print("target nilai:" ,target)
   percobaan = 0
   nilai = 0
   
   while percobaan < 3 and nilai < target :
        nilai = int(input("masukan nilai: "))
        percobaan += 1

   if nilai >= target :
      print(nama, "berhasil lulus setelah" , percobaan, "kali percobaan!")
   else : 
      print(nama, "tidak lulus setelah" , percobaan, "kali percobaan!")
      

