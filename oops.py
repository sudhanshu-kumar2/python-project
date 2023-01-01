# defining calss
class soft:
#class attribute
    als="This is class attribute"

    #defining instancing
    def __init__(self,name,age,postn,salary):  #self represent instance
        #instance attributes
        self.nam=name
        self.age=age
        self.postn=postn
        self.salary=salary
    # instance method
    def code(self):
        print(f"{self.nam} is writing code..")

    def code_lang(self,lang):
        print(f"{self.nam} is writing code in {lang} ")
    
    def bio_data(self):
        return (f"name={self.nam} age={self.age} position ={self.postn} salary={self.postn}")

    #instead of above we can use this whenever object a string
    #dunder method
    def __str__(self):
        
        x=(f"name={self.nam} age={self.age} position ={self.postn} salary={self.postn}")
        return x

    #comparing method
    #print(o1==o2) --> false it compare memory addresses---> now
    def __eq__(self,other):
        return self.nam==other.nam and self.age==other.age
    

    @staticmethod
    def en_sal(age):
        if age<25:
            return "salary=15000"
        elif age<56:
            return "Salary=35000"
        else:
            return "salary=6000"



#creating instance``
o1=soft("Raman",17,"sen",1000)
o2=soft("Raman",17,"sen",1000)
print(o1.nam,o1.age)  #raman 17
print(o1.als)    #"This is class attribute"

#calling fn
o1.code()  #code(o1)-->soft-->instance attriibute  raman is writing code.
o1.code_lang("Python") # raman write code in python
print(o1.bio_data())
print(o1)
print(o1==o2)# after __eq__

print(o1.en_sal(30))
print(soft.en_sal(30))

#**********************  inherientance *******************************************

class employee:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def work(self):
        print(f"{self.name} is working ....")
    
class software(employee):
    #overwriting parent class 
    def __init__(self,name,age,salary,level):
        super().__init__(name,age,salary)
        self.level=level
    def debug(self):
        print("{} is debuging".format(self.name))
    def work(self):
        print(f"{self.name} is coding ....") #overwriting work parent class

class Desiner(employee):
    def work(self):
        print(f"{self.name} is drawing ....") #oveerwriting work parent class
s1=software("Ram",25,35000,"junior")
print(s1.name,s1.age)
s1.work()
print(s1.level)
s1.debug()

emp=[software("Ram",25,35000,"junior"),software("max",25,35000,"junior"),Desiner("joe",25,35000)]
def motivat(el):
    for empl in el:
        empl.work()
motivat(emp)


#********************************** encapsulation **********************
class emp:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self._salary=4000  #no acess outside class  by self.salary use self._salary partially private
        self.__bug_solvd=10  
    #setter
    def getslry(self):
        return self._salary
    #getter
    def setslry(self,val):
        self._salary=val

e1=emp("Raman ",35)
print(e1.name,e1.age)
e1.setslry(5000)
print(e1.getslry())  #5000
