# class employee:
#     emp_count=0
#     def __init__(self,name,desgnation,salary):
#         self.name=name
#         self.desgnation=desgnation
#         self.salary=salary
#         employee.emp_count+=1
#     def display(self):
#         print(f"Employee name={self.name} ")
#         print(f"position ={self.desgnation}")
#         print(f"salary={self.salary}")
#         print()
# e1=employee("Raman","SDE",2500000)
# e2=employee("Aman","intern",670000)
# e3=employee("Rohit","l2",3000000)
# e4=employee("Dinesh","SDE4",1800000)
# print(employee.emp_count)
# e1.display()
# e2.display()
# e3.display()
# e4.display()

# class Circle:
#     pi=3.14
#     def __init__(self,radius) -> None:
#         self.radius=radius
#     def area(self):
#         a=(self.radius**2)*Circle.pi
#         print("are of circle is {}".format(a))
#     def circumfrence(self):
#         c=2*self.pi*self.radius
#         print(f"circumfrance of circle is {c}")
# c1=Circle(7.5)
# c1.area()
# c1.circumfrence()

# class rectangle:
#     def get_data(self):
#         rectangle.length=int(input("Input length   :"))
#         rectangle.breadth=int(input("Entre breadth  :"))
#     def detail(self):
#         print(f"Length : {self.length}")
#         print(f"Breadth :{self.breadth}")
#     def area(self):
#         print(f"Area is {self.length*self.breadth}")
# r1=rectangle()
# r1.get_data()
# r1.detail()
# r1.area()

# class fraction:
#     def get_data(self):
#         self.numenetor=int(input(" Entre numenotor :"))
#         self.denomenator=int(input(" Entre denomentor :"))
#         if (self.denomenator==0):
#             print("fraction is not possible")
#     def sim_d(self):
#         self.num=self.gcd(self.numenetor,self.denomenator)
#         self.n=self.numenetor/self.num
#         self.d=self.denomenator/self.num     
#         print(f" simplified fraction is  :{self.n}/{self.d}")     
#     def gcd(self,a,b):
#         if b==0:
#             return a
#         else:
#             return self.gcd(b,a%b)
# q=fraction()
# q.get_data()
# q.sim_d()

# class bill:
#     item_name=[]
#     item_price=[]
#     bill_name=[]
#     bill_price=[]
#     def get_data(self):
#         self.n=int(input("Enter no of item you want to add  :"))
#         for i in range(self.n):
#             m=(input("Enter item name   :"))
#             self.item_name.append(m)
#             b=float(input("Enter item prince :"))
#             self.item_price.append(b)
#             print()  
#     def display(self):
#         print(f"****************ITEM LIST**********************")
#         print(f"Itemcode \t Itemname \t Price ")
#         for i in range(self.n):
#             print(f"{i}\t\t{self.item_name[i]}\t\t{self.item_price[i]}")
#         print()
#     def pay(self):
#         choice='Y'
#         while choice=="Y":
#             c=int(input("Enter item code from above  :"))
#             self.q=int(input("Enter quantity              :"))
#             self.bill_name.append(c)
#             self.bill_price.append(self.item_price[c]*self.q)
#             choice=input("You want to puchase more press 'Y' ,not press 'N'  :")
#         self.l=len(self.bill_name)
#         print()
#     def display_bill(self):
#         print(f"****************YOUR BILL**********************")
#         print(f" Itemname \t  Quantity \t  price ")
#         for i in range(self.l):
#             print(f"{self.bill_name[i]}\t\t {self.q} \t{self.item_price[i]}")
#         print(f"TOTAL PRICE TO PAY   : {sum(self.bill_price)}")
# c1=bill()
# c1.get_data()
# c1.display()
# c1.pay()
# c1.display_bill()

# class number:
#     def __init__(self):
#         self.val=[]
#     def insert(self):
#         ch="Y"
#         while ch=="Y":
#             v=input("Entre  value :")
#             self.val.append(v)
#             ch=input("Enter Y if you eant to add mor otherwiese N ")
#     def findmax(self):
#         ma=''
#         for i in self.val:
#             if (i>ma):
#                 ma=i
#         print("maximum is  : %r" %ma)
# o1=number()
# o1.insert()
# o1.findmax()

# class string:
#     s=""
#     def __init__(self):
#         self.c=0
#         self.l=0
#         self.u=0
#         self.v=0
#         self.sp=0
#     def get_data(self):
#         self.st=input("Entre string  :")
#         string.s=string.s+self.st
#     def detail(self):
#         for ch in self.s:
#             if ch.islower():
#                 self.l+=1
#             elif ch.isupper():
#                 self.u+=1
#         for ch in self.s:   
#             if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
#                 self.v+=1
#             elif ch==" ":
#                 self.sp+=1
#             else:
#                 self.c+=1
#         print("Number of vowel is  %d" %self.v)
#         print("Number of consonant is %d" %self.c)
#         print("Number of Uppercase is %d" %self.u)
#         print("Number of lowercase is %d" %self.l)
#         print("Number of spaces  is %d" %self.sp)
# o1=string()
# o1.get_data()
# o1.detail()





