import datetime
class Person:
    def __init__(self,first_name,last_name,address,ids,telephone,email,birthdate):
        self.__first_name = first_name
        self.__last_name = last_name
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
    def first_name(self):
        return self.__first_name  
    @first_name.setter   
    def first_name(self, first_namez:str):
        print("@firstName.setter class method called")
        self.__first_name = first_namez

    @property
    def email(self):
        return self.__email
    @email.setter     
    def email(self, email:str):
        print("@Email.setter class method called")
        self.__email = email
 
    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter 
    def last_name(self, last_namez:str):
        print("@LastName.setter class method called")
        self.__last_name = last_namez

    @property
    def Id(self):
        return self.__ids
    @Id.setter    
    def Id(self, id:int):
        print("@Id.setter class method called")
        self.__ids = id


    @property
    def Address(self):
        return self.__address
    @Address.setter
    def Address(self, address:str):
        print("@Address.setter class method called")
        self.__address = address

class employee(Person):
    def __init__(self,first_name, last_name, ids, address, base_salary, seniority):
        super().__init__(first_name, last_name, ids, address)
        self.__base_salary = base_salary
        self.__seniority = seniority

    @property
    def BaseSalary(self):
        return self.__base_salary

    @BaseSalary.setter
    def BaseSalary(self, salary:int):
        print("@BaseSalary.setter class method called")
        self.__base_salary = salary

    @property
    def Seniority(self):
        return self.__seniority

    @Seniority.setter
    def Seniority(self, seniority:int):
        print("@Seniority.setter class method called")
        self.__seniority = seniority

  


class Student(Person):
    def __init__(self,first_name,last_name,address,ids,courses,year,telephone,email,birthdate):
        super().__init__(first_name, last_name,address,ids,telephone,email,birthdate)
        self.__courses = courses
        self.__year = year

    @property
    def courses(self):
        return self.__courses
    @courses.setter    
    def courses(self,courses:str):
        print("@courses.setter class method called")
        self.__courses=courses


    @property    
    def year(self):
        return self.__year
    @year.setter
    def year(self,year:int):
        print("@Year.setter class method called")
        self.__year=year



    def takes_courses_from(self,lect1):
        for target_list in self.courses:
            if(target_list in lect1.rate_for):
                return target_list

class Lecturer(Person):
    def __init__(self,first_name,last_name,ids,address,rate_for,hour,telephone,email,birthdate):
        super().__init__(first_name,last_name,ids,address,telephone,email,birthdate)
        self.__rate_for = rate_for
        self.__hour=hour

    @property
    def rate_for(self):
        return self.__rate_for
    @rate_for.setter
    def rate_for(self, rate_for:str ):
        print("@RateFor.setter class method called")
        self.rate_for = rate_for

    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self, hour):
        print("@Hour.setter class method called")
        self.__hour = hour


    def taught_students(self,std1:Student,std2:Student):
        for target_list in self.rate_for:
            if(target_list in std1.courses and target_list in std2.courses):
                return (target_list)
                
        
    def teaches_something(self,std1):
        for target_list in self.rate_for:
            if(target_list in std1.courses):
                return True
        return False

    
student1 = Student("Muhammad","Ben-Ami","15","Some street 13 at Some City",('Python','Java'),2020,"054950","saas@asas","15.9.1994")
student2 = Student("Iris","York","16","Some street 14 at Some City",('Python','C#'),2020,"054950","saas@asas","15.9.1994")
lecturer1 = Lecturer('Whoever','Ben-Zakkai','19','Some addr',('Python','Advanced Algorithms'),2020,"054950","saas@asas","15.9.1994")


if lecturer1.teaches_something(student1) :
    print(f'{lecturer1.first_name} {lecturer1.last_name} teaches {student1.takes_courses_from(lecturer1)}')
print(f' {student1.first_name} and {student2.first_name} study {lecturer1.taught_students(student1,student2)} from {lecturer1.first_name}')

person1 = Person("משולם","שירלי","רח' שבי בשקט 13","012 12345678","sh.meshulam@example.com",205431447,datetime.date(1992, 3, 12))
print(person1.first_name)
print(person1.email)
print(person1.age)
