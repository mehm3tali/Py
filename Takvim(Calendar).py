print("Takvimini oluşturmak istediğiniz senenin bilgilerini giriniz.")
yıl= int(input(" ilk olarak seneyi Giriniz."))

ay = int(input("İkinci olarak ayı sayı olarak giriniz:"))
import calendar

if ay<12 :{

print (calendar.month(yıl,ay))

}
else :{
    print("Ay değeri 12 den büyük olamaz")
}
print("Program  60 saniye sonra kendini otomatik olarak kapatacaktır."  )


import time 
time.sleep(60)




