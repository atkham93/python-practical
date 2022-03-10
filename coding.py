# -*- coding: utf-8 -*-
"""
Created on Mon Feb  7 21:42:00 2022

@author: SAN
"""
#03 lesson (working with print) 05.02.2022
print("beshning kvadrati", 5**2, "ga teng")
print("sakkizning kvadrati", 8**2, "ga teng")
print("men seni sevaman, \nsechi?, \nmenga turmushga chiqasanmi?")
print('3x3=',3*3)
print("Nexia", "Tico", 'Damas', "ko'rganlar qilar havas")
print("beshing to`rtinchi darajasi", 5**4, "ga teng")
print("yigirma ikkini to`rtga bo`lganda", 22/4, "chiqadi")
print("tomonlari 125ga teng kvadratning yuzi", 125**2,)
print(11/3)
print(12//5)
print(55**2)
print(88**4)
print("i am living in south korea,\nbut i am from uzbekistan, \nall my family is there now")
print("I am Adam", "i am", 2022-1993,"years old", "my height is",2.00-0.30,"but my weight is 70kg")

#04 lesson (working with variables)
name="Atkham"
surname="Tukhtaev"
fullname="tukhtaev atkham"
age=29
year=1993
hobby="watching,reading and listening"
status= "single"
place_of_living= "south korea, ulsan"
graduation="Ulsan University in IT"
print(name)
print(age)
print(year)
print(hobby)
print(status)
print(place_of_living)
print(graduation)
# Practice
entry="hello world"
print(entry)
news="Inflation in Russia"
print(news)
news='Gold or Dollar?'
print(news)
radius = 5
pi = 3.14159
aylana_yuzi = pi * radius**2
print("Radiusi" , radius, "ga teng aylananing yuzi=", aylana_yuzi)

#05 lesson "String"
smile="☺"
broken_heart="💔"
print("mening ismim"  + name)
print("mening ismim" + ' ' + name)
print(name + surname)
print(name +' ' + surname)
f"{name} {surname}"
print(f"salom, mening ismim {name} siz bilan tanishganimdan hursandman")
print("hello world")
print("hello \tworld")
print("hello \nworld")
print(name.upper())
print(name + surname.upper())
print(fullname.upper())
print(fullname.lower())
print(fullname.title())
print(fullname.capitalize())
fruit="    an apple    "
print(fruit)
print(fruit.lstrip())
print("i love " + fruit.lstrip() +"so much")
print("i love " + fruit.rstrip() + "so much")
print("i love " + fruit.strip() + " so much")
print(" i love " + fruit + "so much")
name=input("what is your name Sir ? ")
print("Hello my name is " + name )
name=input("what is your name?\n>>>")
print("my name is " + name.upper())
age=input("how old are you?")
print("I am " + age)
hobby=input("what is your hobby?")
print("my hobby is " + hobby.title())
status=input("what is your status now ? ")
print("I am " + status.title())
family=input("how many are you in ?")
print("we are " + family.capitalize())
kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
print(kocha + " ko`chasi,", mahalla + " mahallasi,", tuman + " tumani,", viloyat + " viloyati,")
kocha=input("what is your street ? ")
print("my street is " + kocha.title())
mahalla=input("what is your makhalla ? ")
print("my makhalla is " + mahalla.title())
f"{kocha.upper()} {mahalla.title()}"

#06 lesson Numerals
a=15
b=15.5
print(type(a))
t_yil= int(input("Tug`ilgan yilingizni kiriting"))
yosh= 2022 - t_yil
print("Siz", yosh,  "yoshda ekansiz")
fruits=['apple', 'banana', 'pineapple', 'kiwi']
print(fruits)
fruits=['apple', 'banana', 'pineapple', 'kiwi']
print(fruits)

print(fruits[-2])
print(fruits[1])
fruits.append('apelsin')
print(fruits)
fruits.insert(2, 'grape')
print(fruits)

cars=[]
cars.append("bentley")
print(cars)
cars.append("cobalt")
cars.append("matiz")
cars.append("nexia")
print(cars)
del cars[0]
print(cars)
cars.insert(2,'captiva')
print(cars)
cars.remove("matiz")
print(cars)
names=['joni','pulat','sherzod','zafar']
print(names)
print("salom Joni bugun choyxona bormi?")
print("zafar bugun choyxonaga boramiz?")
numbers=[25,4,-88,7.1]
print(numbers)   
numbers.append(99)
print(numbers)
numbers.insert(5,90)
print(numbers)

t_shaxslar=['navai','amir','chingizxan']
z_shaxslar=['mask','jason','selena']
selena= z_shaxslar.pop(2)
amir = t_shaxslar.pop(1)
print(" men tarixiy insonlardan " + amir + " bilan ko`rishgan bo`lardim")
print("hozirgilardan esa " + selena + "bilan ko`rishgan bo`lardim")
friends=[]
friends.append('Sarvar')
friends.append('kurban')
friends.append('boychibor')
print(friends)
friends.remove('kurban')
print(friends)
friends.insert(0,'shalola')
print(friends)
friends.insert(3,'shodi')
print(friends)
cars=['bmw','merc','audi','volvo','porshe']
print(cars)
cars.sort(reverse=True)
print(cars)
print(sorted(cars))

numbers=[12,25,33,-9,87]
print(sorted(numbers))
numbers.sort(reverse=True)
print(numbers)
len(numbers)
print(numbers)
countries=['usa','sweden','cuba','rome']
print(countries)
sorted(countries)
print(countries)

guests=['shodiya','ali','akbar','maya']
for guest in guests:
    print("Hello", guest )
    print("Goodbye", guest)

guests=['shodiya','ali','akbar','maya']
for guest in guests:    
    print(f"Dear {guest.upper()}, we will be offering to our wedding party ")
    print("with best regard,\nMr.Tukhatev")
    
sonlar=list(range(1,13))
for son in sonlar:
    print("f {son} ning kvadrati {son**2} ga teng" )
sonlar1=list(range(1,18))
for s in sonlar1:
    print(f"{s} ning kvadrati {s**2} ga teng")

sonlar1=list(range(18))
sonlar_kvadrati=[]
for s in sonlar1:
    sonlar_kvadrati.append(s**2)
    print(sonlar1)
    print(sonlar_kvadrati)

friends1=[]
print("5 top friends?")
for n in range(5):
    friends1.append(input(f"{n+1} fill in your friends name here:"))
    print(friends1)
new_names=['adam','vali','gena','ani','jony']
for new in new_names:
    print(new_names)
    print("kod 5 marta takrorlandi")
toqlar=list(range(10,100,3))
for t in toqlar:
    print(f"{t} ning kubi {t**3} ga teng")
films=[]
print("5 top movies")
for f in range(5):
    films.append(input(f"{f+1} write your 5 top movies here:"))

    print(films)
    
meeting=[]
print("ask how many people did you meet up?")
for m in range(3):
    meeting.append(input(f"{m+1} fill in your friends name whom you are met"))
    print(meeting)
 
    
 # If Else 
 
avtolar = ['audi', "bmw", 'volvo', 'kia', 'hyundai']
for avto in avtolar:
    if avto == 'bmw':
        print(avto.upper())
    else:
        print(avto.title())
     
ism = input('Ismizngiz nima ?\n>>>')
if ism.lower() != 'adham':
    print( f"Uzr, {ism.title()} biz Adhamni kutyapmiz")
else:
    print("Salom, Adham") 

yosh = int(input("yoshingiz mechida?"))
if yosh >= 18:
    print('Xush kelibsiz bugungi Counter Strike bazmiga!')
else:
    print("aks holda kirish mumkin emas!")

login = input("yangi login tanlang:")
if len(login) <=5:
    print("Login 5 harfdan iborat bo`lsin!")
    
ogin = input("yangi login tanlang:")
if len(login) <=5:
    print("Login 5 harfdan iborat bo`lsin!")
    
yil = int(input("tug`ilgan yilingizni kiriting"))
if 2020-yil<18:
    print(f"yoshingiz {2020-yil}da ekan.")
else:
    print("Xush kelibsiz")
    
yosh = int(input("yoshingiz mechida?"))
if yosh >65:
    print("siz COVID-19 guruhida ekansiz!")

x, y=50, 40
print("x>y") if x>y else print("x<y")

# if elif, and or, boolean.
son = -10
if son<0:
    print("manfiy son")
else:
    print("musbat son")    

yosh = int(input("yoshingiz nechida?"))
if yosh <=4:
    print("sizga kirish bepul")
elif yosh <=12:
    print("sizga kirish 5000 so`m")
else:
    print("sizga kirish 10000 so`m")

yosh = int(input("yoshingiz nechida?"))
if yosh <=4:
    narx = 0
elif yosh <=12:
    narx = 5000
else:
    narx = 10000
print(f"sizga kirish {narx} so`m")    

kun = input("bugun nima kun?")
if kun.lower()== 'shanba' or kun.lower()=='yakshanba':
    print("bugun dam olish kuni")
else:
    print("bugun ish kuni")

kun = input("bugun qanday kun ?")
harorat = float(input("havo harorati qanday?"))
if kun.lower() == 'yakshanba' and harorat>30:
    print("cho`milhani ketdik")
elif kun.lower()=='yakshanba' and harorat<30:
    print("uyda dam olamiz")
    
kun = input("bugun qanday kun ?")
harorat = float(input("havo harorati qanday?"))
if (kun.lower()=='yakshanba' or kun.lower()=='shanba') and harorat>30:
    print("cho`milgani ketdim")
elif (kun.lower()=='yakshanba' or 'shanba') and harorat<30:
    print("uyda dam olamiz")

narh = 15000
choy = True
salad = False
if choy and salad:
    narh= narh + 10000
elif choy or salad:
    narh = narh + 5000
print(f"jami {narh} so`m")

menu = ['osh','palov','shashlik','somsa']
'somsa' in menu
print(menu)

menu = ['osh','palov','shashlik','somsa']
ovqat = input('nima ovqat yeyapsiz?')
if ovqat.lower() in menu:
    print('buyurtma qabul qilindi.')
else:
    print('afsuski bizda bunday ovqatlar yoq')   
    
menu = ['osh','palov','shashlik','somsa']
orders = ['osh','palov','shashlik','somsa', 'manti']
for meal in orders:
    if meal in menu:
        print(f"menuda {meal} bor")
    else:
        print(f"kechirasiz, menuda {meal} yoq")
        


    

   



 
    