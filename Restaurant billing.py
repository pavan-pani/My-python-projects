print('''Hello....
Wel come to FRINDES Hotel''')

#Storing Menu
tiff={'idli':30,'idli+vada':35,'Masala Dosa':30,'Onion Dosa':50,'Set Dosa':40,'Puri':40,'Upma':30}
veg={'Full Meals':70,'Half Meals':50,'Veg Biriyani':90,'Curd Rise':40,'Masala Rise':30,
     'Gobi Rise':50,'Tamota Rise':40,'Chapthi':20,'Roti':20,'Parota':30}
nonveg={'Chicken Biriyani':110,'Special Biriani':130,'Kushka':60,'Egg Rise':50}
count,bill=0,0
totalBill={}
print("\n",'*'*20,"Tiffen items",'*'*20,"\n")
print("""Item ----> rate
""")
#Displying Menu
for i in tiff:
    count=count+1
    print(count,") ",i,"--->",tiff[i])

print("\n",'*'*20,"Veg items",'*'*20,"\n")
for i in veg:
    count=count+1
    print(count,") ",i,"--->",veg[i])
print("\n",'*'*20,"Non Veg items",'*'*20,"\n")
for i in nonveg:
    count=count+1
    print(count,") ",i,"--->",nonveg[i])


    
while True:
    try:
        myeat=int(input("Enter the item number : "))
    except:
        print("-"*10,"enter the valid key","-"*10)
        
    #tiffin Items collection 
    if 1<=myeat<=6:
        f=0    
        for i in tiff:
            f+=1
            if myeat==f:
                bill+=tiff[i]
                totalBill.setdefault(i,tiff[i])

    #veg Items collection 
    elif 8<=myeat<=17:
        f=7   
        for i in veg:
            f+=1
            if myeat==f:
                bill+=veg[i]
                totalBill.setdefault(i,veg[i])

    #Non veg Items collection
    elif 18<=myeat<=21:
        f=17    
        for i in nonveg:
            f+=1
            if myeat==f:
                bill+=nonveg[i]
                totalBill.setdefault(i,nonveg[i])
    else:
        print("****Enter the correct option according into Menu*****")

    onemore=input("press *any key* to place one more order or Press (B) to get bill : ")
    if onemore=='B':
        break
    else:
        continue
    
#printing the bill
gst=0.12*bill
print("\n Your Bill : \n")
for i in totalBill:
    print(i,"------",totalBill[i])
print("GST%  ",gst)   
print("_"*30)
print("The total amount is :  ",bill+gst)

print("\n\n Thank Q, visit again \U0001f600 \n")
print(" \n*********  ಈ ಸಲ ಕಪ್ ನಮ್ದೆ ********** \n\n")






            

 
    
