#importing NumPy Library
import numpy as m

#assigning zeros to seats
seats=m.zeros([20,20], dtype=int) 
alp=65
count2nd=0 #counting seats for 2nd class 
count1st=0  #counting seats for 1st class 
n=[]    #list for storing Seat Numbers 



#display function to display the seats
def displySeats():
    #Printing the seats in 0's form
    print("-"*15,"2nd Class 150 Rs","-"*15)
    for i in range(20):
        print(chr(alp+i),end=" ")
    print()
    for i in range(20):
        if i==10:
            print("-"*15,"1st Class 100 Rs","-"*15)
            for a in range(20):
                print(chr(alp+a),end=" ")
            print()
        print(*seats[i],"<---",i)#chr(alp+i))

#Fuction call
displySeats()


#function for billing
def billing():
    bill=(count1st*100)+(count2nd*150) #calucating total amount   
    gst=0.12*bill #assining GST values
    print("\n Your Bill : \n")
    print("Number of Seats you booked in 1st class --> ",count1st," (",count1st*100,"=",count1st,"*100)")
    print("Number of Seats you booked in 2nd class --> ",count2nd," (",count2nd*150,"=",count2nd,"*150)")
    print("GST%  ------->                                   ",gst)
    print("____"*20)
    print("Total amount----->                               ",bill+gst)
    print("\n your seats is :",end=" ")
    #printing the seat from list where we stored
    for i in n:
        print(i,end=",")
    
        
    #thank you Statemnt with emoj
    print("\n\n Thank Q, visit again \U0001f600 \n")
    


#booking prosess start from here
    
try:  #using expection handling for exicute the code smothly
    
    while(True): #while loop is always True for booking N number os seats

        #taking inputs as Rows & Colom
        numrow=int(input("Enter The Seat Number according to Row: "))
        numcol=input("Enter The Seat Number according to collum : ").upper()

        
        if (len(str(numrow))==1 or len(str(numrow))==2) and len(numcol)==1:
            numcol=ord(numcol)-65
        else:
            print("Please enter valid seat or according into Row & collom")
            continue
        

        if numrow<=19 or numcol<=20:
            if seats[numrow,numcol]==0:
                seats[numrow,numcol]=1 #assining 1 to booked seat
                #counting number of seats booked
                if numrow<=9:
                    count2nd+=1
                else:
                    count1st+=1
                numcol=chr(numcol+65)
                #adding number of seats booked
                n.append(str(numrow)+numcol)
            else:
                print("The seat already booked, try with other seat")
                continue  
        else:
            print("Sorry you enterd a out of range in seats")

           
           #telling user to seat booked Successfully
        print(count1st+count2nd," tickets Booked Successfully")

        
        print("****"*20)
         #Asking user to book few more seats or bill
        print("""Enter 'B' to get your ticket and bill
Enter 'S' to disply the seats
Enter any number to continue Booking :""")
        onemore=input()
        
        if onemore=='B' or onemore=='b':
            billing() #function call for printing bill
            
        if onemore=='S' or onemore=='s':
            displySeats()  #function call for diaplying seats
        else :
            continue
        
except:
    #whatever the error raise this stetament will print 
    print("Please enter valid seat or according into Row & collom....")



    
