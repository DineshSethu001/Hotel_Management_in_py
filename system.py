class hotelfarecal:
    def __init__(self,Total='',room_rent=0,game=0,menu=0,dry_wash=0,Additional_service=1800,name='',address="",cindate='',coutdate='',room_no=101):
        print("\n\n*****Welcome to Dinesh Hotel*****\n")
        self.rt=Total
        self.r=menu
        self.t=dry_wash
        self.p=game
        self.s=room_rent
        self.a=Additional_service
        self.name=name
        self.address=address
        self.cindate=cindate
        self.coutdate=coutdate
        self.rno=room_no
    def registerdate(self):
        self.name=input("\nEnter your name:")
        self.address=input("\n Enter your address:")
        self.cindate=input("\n Enter check in date:")
        self.coutdate=input("\n Enter the check put date:")
        print("your room no:",self.rno,"\n")
    def roomrent(self):
        print("we have the following rules for you:")
        print("1.type.A----->rs 6000 pN\-") 
        print("2.type.B----->rs 5000 pN\-")
        print("3.type.C----->rs 3000 pN\-")  
        print("4.type.D----->rs 2000 pN\-") 
        x=int(input("Enter the choice Please-->"))
        n=int(input("how many Night did you stay:"))
        if(x==1):
            print("you have opted room type A:")
            self.s=6000*n
        elif(x==2):
            print("you have opted room type B:")
            self.s=5000*n
        elif(x==3):
            print("you have opted room type C:")
            self.s=3000*n
        elif(x==4):
             print("you have opted room type D:")
             self.s=2000*n
        else:
            print("please choose a room")
        print("you room rent is=",self.s,"\n")
    
    def restaurentbill(self):
        print("*****RESTAUTANT MENU*****")
        print("1.water ----->Rs20",
              "2.tea----->Rs10",
              "3.breakfast combo----->Rs90",
              "4.lunch----->Rs110",
              "5.dinner----->Rs150",
              "6.exit"
            )

        while(1):
            c=int(input("Enter your choice:"))
            if(c==1):
                d=int(input("Enter the quantity:"))
                self.r=self.r+20*d
            elif(c==2):
                d=int(input("Enter the quantity:"))
                self.r=self.r+10*d
            elif(c==3):
                d=int(input("Enter the quantity:"))
                self.r=self.r+90*d
            elif(c==2):
                d=int(input("Enter the quantity:"))
                self.r=self.r+110*d
            elif(c==2):
                d=int(input("Enter the quantity:"))
                self.r=self.r+150*d
            elif(c==6):
                break
            else:
                print("invalid option")
        print("total food cost=Rs",self.r,"\n")
    def laundrybill(self):
        print("*****LAUNDRY MENU*****")
        print("1.Shorts----->Rs:3",
              "2.Trousers----->Rs:4",
              "3.Shirt----->Rs:5",
              "4.jeans----->Rs:6",
              "5.Girlsuit----->Rs:8",
              "6,Exit"
              )
        while(1):
            e=int(input("Enter your choice:"))
            if(e==1):
                f=int(input("Enter the quantity:"))
                self.t=self.t+3*f
            elif(e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+4*f
            elif(e==3):
                f=int(input("Enter the quantity:"))
                self.t=self.t+5*f
            elif(e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+6*f
            elif(e==2):
                f=int(input("Enter the quantity:"))
                self.t=self.t+8*f
            elif(e==6):
                break
            else:
                print("invalid option")
        print("total food eost=Rs",self.t,"\n")
    def gamebill(self):
        print("*****GAME MENU*****")
        print("1.Table tennis----->Rs:60",
              "2.Bowling----->Rs:80",
              "3.Snokker----->70",
              "4.Video games----->Rs:90",
              "5.pool----->50",
              "6.exit")
        while(1):
            g=int(input("Enter your choice:"))
            if(g==1):
                h=int(input("Enter the quantity:"))
                self.p=self.p+20*h
            elif(g==2):
                h=int(input("Enter the quantity:"))
                self.p=self.p+10*h
            elif(g==3):
                h=int(input("Enter the quantity:"))
                self.p=self.p+90*h
            elif(g==2):
                h=int(input("Enter the quantity:"))
                self.p=self.p+110*h
            elif(g==2):
                h=int(input("Enter the quantity:"))
                self.p=self.p+150*h
            elif(g==6):
                break
            else:
                print("invalid option")
        print("total food cost=Rs",self.p,"\n")
    
    def display(self):
        print("*****HOTEL BILL*****")
        print("Customer dtails:")
        print("Customer name:",self.name)
        print("customer address:",self.address)
        print("Chcek in date:",self.cindate)
        print("Check out date:",self.coutdate)
        print("Room No:",self.rno)
        print("Your room rent is:",self.s)
        print("your food bill is:",self.r)
        print("Your Laundary bill is:",self.t)
        print("Your Game bill is:",self.p)
        self.rt=self.s+self.t+self.p+self.r

        print('Your sub total bill is:',self.rt)
        print("Additional Service Charges is",self.a)
        print("Your graduational bill is:",self.rt+self.a,"\n")
        self.rno+=1
def main():
    a=hotelfarecal()

    while(1):
        print("1.Enter Customer data:")
        print("2.calculate rommrent")
        print("3.Calculate restaurant bill")
        print("4.Calculate laundey bill")
        print("5.Calculate Gamebill")
        print("6.show total cost")
        print("7.Exit")

        b=int(input("Enter your choice:"))
        if(b==1):
            a.registerdate()
        if(b==2):
            a.roomrent()
        if(b==3):
            a.restaurentbill()
        if(b==4):
            a.laundrybill()
        if(b==5):
            a.gamebill()
        if(b==6):
            a.display()
        if(b==7):
            quit()

main()