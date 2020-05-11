import datetime
class Person:
    def __init__(self,firstName,lastName,address,ids,telephone,email,birthdate):
        self.__firstName = firstName
        self.__lastName = lastName
        self.__address = address
        self.__ids = ids
        self.__telephone=telephone
        self.__email = email
        self.__birthdate = birthdate 

    def age(self):
        today=datetime.date.today
        age=today.year-self.__birthdate.year
        if today<datetime.date(today.year,self.__birthdate.month,self.__birthdate.day):
            age -= 1
        return age

    @property
    def FirstName(self):
        print("@property class method called")
        return self.__firstName  
    @FirstName.setter   
    def FirstName(self, firstNamez):
        print("@firstName.setter class method called")
        self.__firstName = firstNamez

    @property
    def Email(self):
        print("@property class method called")
        return self.__email
    @Email.setter     
    def Email(self, email):
        print("@Email.setter class method called")
        self.__email = email
 
    @property
    def LastName(self):
        print("@property class method called")
        return self.__lastName
    @LastName.setter 
    def LastName(self, lastNamez):
        print("@LastName.setter class method called")
        self.__lastName = lastNamez

    @property
    def Id(self):
        print("@property class method called")
        return self.__ids
    @Id.setter    
    def Id(self, id):
        print("@Id.setter class method called")
        self.__ids = id


    @property
    def Address(self):
        print("@property class method called")
        return self.__address
    @Address.setter
    def Address(self, address):
        print("@Address.setter class method called")
        self.__address = address

class employee(Person):
    def __init__(self,firstName, lastName, ids, address, baseSalary, seniority):
        super().__init__(firstName, lastName, ids, address)
        self.__baseSalary = baseSalary
        self.__seniority = seniority

    @property
    def BaseSalary(self):
        print("@property class method called")
        return self.__baseSalary

    @BaseSalary.setter
    def BaseSalary(self, salary):
        print("@BaseSalary.setter class method called")
        self.__base_salary = salary

    @property
    def Seniority(self):
        print("@property class method called")
        return self.__seniority

    @Seniority.setter
    def Seniority(self, seniority):
        print("@Seniority.setter class method called")
        self.__seniority = seniority

  


class Student(Person):
    def __init__(self,FirstName,LastName,address,ids,courses,year,telephone,email,birthdate):
        super().__init__(FirstName, LastName,address,ids,telephone,email,birthdate)
        self.__courses = courses
        self.__year = year

    @property
    def Courses(self):
        print("@property class method called")
        return self.__courses
    @Courses.setter    
    def Courses(self,courses):
        print("@Courses.setter class method called")
        self.courses=courses


    @property    
    def Year(self):
        print("@property class method called")
        return self.__year
    @Year.setter
    def Year(self,year):
        print("@Year.setter class method called")
        self.__year=year



    def takes_courses_from(self,lect1):
        for target_list in self.Courses:
            if(target_list in lect1.RateFor):
                return target_list

class lecture(Person):
    def __init__(self,FirstName,LastName,ids,address,rateFor,hour,telephone,email,birthdate):
        super().__init__(FirstName,LastName,ids,address,telephone,email,birthdate)
        self.__rateFor = rateFor
        self.__hour=hour

    @property
    def RateFor(self):
        print("@property class method called")
        return self.__rateFor
    @RateFor.setter
    def RateFor(self, rateFor ):
        print("@RateFor.setter class method called")
        self.rateFor = rateFor

    @property
    def Hour(self):
        print("@property class method called")
        return self.__hour
    @Hour.setter
    def Hour(self, hour):
        print("@Hour.setter class method called")
        self.__hour = hour


    def taught_students(self,std1,std2):
        for target_list in self.RateFor:
            if(target_list in std1.Courses and target_list in std2.Courses):
                return (target_list)
                
        
    def teaches_something(self,std1):
        for target_list in self.RateFor:
            if(target_list in std1.Courses):
                return True
        return False

    
student1 = Student("Muhammad","Ben-Ami","15","Some street 13 at Some City",('Python','Java'),2020,"054950","saas@asas","15.9.1994")
student2 = Student("Iris","York","16","Some street 14 at Some City",('Python','C#'),2020,"054950","saas@asas","15.9.1994")
lecturer1 = lecture('Whoever','Ben-Zakkai','19','Some addr',('Python','Advanced Algorithms'),2020,"054950","saas@asas","15.9.1994")


if lecturer1.teaches_something(student1) :
    print(f'{lecturer1.FirstName} {lecturer1.LastName} teaches {student1.takes_courses_from(lecturer1)}')
print(f' {student1.FirstName} and {student2.FirstName} study {lecturer1.taught_students(student1,student2)} from {lecturer1.FirstName}')

person1 = Person("משולם","שירלי","רח' שבי בשקט 13","012 12345678","sh.meshulam@example.com",205431447,datetime.date(1992, 3, 12))
print(person1.FirstName)
print(person1.Email)
print(person1.age)
