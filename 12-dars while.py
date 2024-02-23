#while loop



i=0
while i<10:
    i=i+1
    print(i)

# print("""sonning kvadratini hisoblaydigan dastur""")
#
# while True:
#     son=input("son kiritning to'xtatish uchun (exit):")
#     if son=="exit":
#         break
#     else:
#         print(f"{son}ning kvadrati {int(son)**2}")
#
son=0
while son<100:
    son+1
    if son%2==0:
        continue
    else:
        print(son)



son=0
while son<100:
    son=son+1
    if son%2 !=0:
        continue
    else:
       print(son)



# while True:
#     name=input("ismingizni kiriting(dasturni to'xtatish uchun'stop':)")
#     if name=='stop':
#         break
#     age=int(input("yoshingizni kiriting>"))
#     print(f"Sizning ismingiz{name} va yoshingiz {age}da")



# son=float(input("son kiriting>>"))
# yigindi=son
# while True:
#     javob=input("yana son kiritasizmi? (ha/yoq):")
#     if javob.lower()!="ha":
#         break
#     son=float(input("son kiriting>>"))
#     yigindi+=son
# print(f"siz kirittgan sonlar yig'indisi {yigindi}")


#float= 2.1 , 32.0 , 14.9
#int=1 , 2 , 3 , 5 ,7




print("**kalkulator**")
while True:
    a=float(input("a="))
    b=float(input("b="))
    amal=input("(+,-,*,/,stop):")
    if amal=='+':
        print(a+b)
    elif amal=='-':
        print(a-b)
    elif amal=='*':
        print(a*b)
    elif amal=='/':
        print(a/b)
    elif amal=='stop':
        break
    else:
        print("Noto'g'ri amal kiritingiz:")




print("login parol o'yini")
t_login="Ramizjon_54"
t_parol="16072009"
t_hobbi="it"
imkoniyat=3
n=0
while imkoniyat>0:
    n+=1
    print(f"sizda {imkoniyat} ta imkoniyat bor")
    login=input("login kiriting:")
    parol=input("parol kiriting:")
    hobbi=input("hobbini kiritning:")
    if login==t_login and parol==t_parol and hobbi==t_hobbi:
        print(f"siz {n} ta imkoniyatda kirdingiz")
        break
    else:
        print(f"login yoki parol xato")
        imkoniyat -=1
if imkoniyat==0:
    print("sizda imkoniyat qomadi")




