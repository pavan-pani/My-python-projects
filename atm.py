import time
atmpin=[1111,2222,3333,4444,5555] #default pins

print('Hello... \nwelcome to the ATM')
time.sleep(3)#time dealy
print("\n\nPleas chose your language\n")
print("kannada ---> 1")
print("English ---> 2")
print("Hindi -----> 3")
lang=int(input('Enter here :'))
#this code display the kannada text
if lang==1:
    pin=int(input("ನಿಮ್ಮ ಪಿನ್ ನಮೂದಿಸಿ : "))
    if len(str(pin))!=4:
        print("**********ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಪಿನ್ ನಮೂದಿಸಿ**********")
    elif pin in atmpin:
        print("\nನಿಮ್ಮ ಉದ್ದೇಶವನ್ನು ಆರಿಸಿ : \n")
        print("Withdraw      -------> 1")
        print("ಪಿನ್ ಬದಲಾವಣೆ   -----> 2")
        print("ಮಿನಿಸ್ಟೇಟ್ಮೆಂಟ್ --------> 3\n")
        secstep=int(input("ಇಲ್ಲಿ ನಮೂದಿಸಿ : "))
        if secstep==1:
            for i in range(0,5):
                amount=int(input("ಮೊತ್ತವನ್ನು ನಮೂದಿಸಿ : "))
                if amount%100!=0:
                    print("\n**********ದಯವಿಟ್ಟು 100 ರ ಗುಣಾಕಾರವನ್ನು ನಮೂದಿಸಿ**********\n")
                    continue
                elif amount>15000:
                    print("\n**********ಗರಿಷ್ಠ ಮಿತಿ 15000 ಮಾತ್ರ**********\n")
                else:
                    print("Loading.......")
                    time.sleep(4)
                    print("\nದಯವಿಟ್ಟು ನಿಮ್ಮ ಹಣವನ್ನು ಸಂಗ್ರಹಿಸಿ...\n")
                    time.sleep(2)
                    break
        elif secstep==2:
            pinchange=int(input("ನಿಮ್ಮ ಹಳೆಯ ಪಿನ್ ಅನ್ನು ನಮೂದಿಸಿ : "))
            pinstr=str(pinchange)
            if len(pinstr)==4:
                if pinchange in atmpin:
                    newpin=int(input("4 ಅಂಕಿಯ ಹೊಸ ಪಿನ್ ನಮೂದಿಸಿ : "))
                    new=atmpin.index(pinchange)
                    atmpin[new]=newpin
                    print("\n----ಪಿನ್ ಬದಲಾವಣೆ ಯಶಸ್ವಿಯಾಗಿ ಪೂರ್ಣಗೊಂಡಿದೆ----\n")
                else:
                    print("\n**********ದಯವಿಟ್ಟು ಸರಿಯಾದ ಪಿನ್ ನಮೂದಿಸಿ**********\n")
            else:
                print("\n**********ದಯವಿಟ್ಟು ಮಾನ್ಯವಾದ ಪಿನ್ ನಮೂದಿಸಿ**********\n")
        elif secstep==3:
            print("\nಕ್ಷಮಿಸಿ, ನಿಮ್ಮ ಸಚಿವಾಲಯವನ್ನು ಮುದ್ರಿಸಲು ಯಂತ್ರದಲ್ಲಿ ಹೆಚ್ಚಿನ ಪತ್ರಿಕೆಗಳಿಲ್ಲ...\n")                  
    else:
        print("\n**********ದಯವಿಟ್ಟು ಎಟಿಎಂ ಕಾರ್ಡ್ ಅನ್ನು ಮಾಲೀಕರಿಗೆ ಹಿಂತಿರುಗಿಸಿ**********\n")




#this code display the English text
if lang==2:
    pin=int(input("enter your pin : "))
    if len(str(pin))!=4:
        print("\n**********please enter a valid pin**********\n")
    elif pin in atmpin:
        print("choose your purpose :\n")
        print("Withdraw      -----> 1")
        print("Pin Change    -----> 2")
        print("Ministatement -----> 3\n")
        secstep=int(input("enter here : "))
        
        if secstep==1:
            for i in range(0,5):
                amount=int(input("Enter the amount : "))
                if amount%100!=0:
                    print("\n\n**********Please enter the multipule of 100's**********\n\n")
                    continue
                elif amount>15000:
                    print("\n\n**********maximum limit is 15000 only**********\n\n")
                else:
                    print("Loading.....")
                    time.sleep(4)
                    print("\nPlease collect your cash...")
                    time.sleep(2)
                    break
        elif secstep==2:
            pinchange=int(input("Enter your old pin : "))
            pinstr=str(pinchange)
            if len(pinstr)==4:
                if pinchange in atmpin:
                    newpin=int(input("Enter 4 digit new pin : "))
                    new=atmpin.index(pinchange)
                    atmpin[new]=newpin
                    print("\n-----Pin change successfully completed-----\n")
                else:
                    print("\n**********Please enter correct pin**********\n")
            else:
                print("\nplease enter a valid pin\n")
        elif secstep==3:
            print("\nSorry, no more papers in machine to print your ministatement\n")                   
    else:
        print("\n**********Please return back the ATM card to owner**********\n")

#this code display the hindi text
if lang==3:
    pin=int(input("अपना पिन दर्ज करो : "))
    if len(str(pin))!=4:
        print("कृपया एक मान्य पिन दर्ज करें")
    elif pin in atmpin:
        print("cअपने उद्देश्य को पूरा करें")
        print("Withdraw      -----> 1")
        print("पिन बदलें   -----> 2")
        print("Ministatement -----> 3")
        secstep=int(input("यहाँ से प्रवेश करें : "))
        
        if secstep==1:
            for i in range(0,5):
                amount=int(input("राशि दर्ज करें : "))
                if amount%100!=0:
                    print("कृपया 100 के गुणा में प्रवेश करें")
                    continue
                elif amount>15000:
                    print("अधिकतम सीमा 15000 ही है")
                else:
                    print("Loading.....")
                    time.sleep(4)
                    print("कृपया अपना कैश जमा करें")
                    time.sleep(2)
                    break
        elif secstep==2:
            pinchange=int(input("अपना पुराना पिन डालें : "))
            pinstr=str(pinchange)
            if len(pinstr)==4:
                if pinchange in atmpin:
                    newpin=int(input("4 अंक नया पिन दर्ज करें : "))
                    new=atmpin.index(pinchange)
                    atmpin[new]=newpin
                    print("पिन परिवर्तन सफलतापूर्वक पूरा हुआ")
                else:
                    print("कृपया सही पिन दर्ज करें")
            else:
                print("कृपया एक मान्य पिन दर्ज करें")
        elif secstep==3:
            print("क्षमा करें, आपके मंत्रालयों को मुद्रित करने के लिए मशीन में कोई और कागजात नहीं है")                   
    else:
        print("कृपया स्वामी को एटीएम कार्ड वापस करें ")
        
time.sleep(1)     
print("Thanks for Transaction...")
