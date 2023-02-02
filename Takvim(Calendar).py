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




# import  # using module keyboard
# while True:  # making a loop
#     try:  # used try so that if user pressed other than the given key error will not be shown
#         if keyboard.is_pressed('q'):  # if key 'q' is pressed 
#             print('You Pressed A Key!')
#             break  # finishing the loop
#         else:
#             pass
#     except:
#         break  # if user pressed a key other than the given key the loop will break