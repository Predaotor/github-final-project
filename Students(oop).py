# Creating student class 
class Student:
    def __init__(self, name,age, roll_number):
        self.name=name 
        self.age=age 
        self.roll_number=roll_number 
        
    
# creating school class 
class School:
    def __init__(self):
        self.students={}
    # Adds students into the list  
    def add_student(self, name, age, roll_number):
        student=Student(name, age, roll_number)
        self.students[roll_number]=student
        print("Student added successfully")
    
    #Displays students from the list
    def display_student(self):
        
        for roll_number, student in self.students.items():
            print(f"Name: {student.name}")
            print(f"Age: {student.age}")
            print(f"Roll_number: {student.roll_number}")
            print("-"*10)
            
    # Create method to edit student
    
    def edit_student(self, roll_number, new_name, new_age):
        
            
        if roll_number in self.students:
                
            student=self.students[roll_number]
            student.age=new_age
            student.name=new_name
                
            print(f"Student: {student.name} has successfully updated")
            print()
            return 
            
    def delete_student(self,roll_number ):
        if roll_number in self.students:
               
            del  self.students[roll_number]
            print("Student has been deleted successfully!")
            print()
        
    
#Creating school object
school=School()

# Create choices for users
while True:
    choice=input("Enter your choice: \n1)Add student \n2)Display list of the students \n3) Edit the student \n4)To Delete student by roll_number \n5)Quit ")
    print()
    if choice == "1":
        
     try:   
      name=input("Enter name of the student: ")
      print()
      
      age=int(input("Enter age: "))
      print()
      roll_number=int(input("Enter roll_number: "))
      print()
      school.add_student(name, age, roll_number)
      
     except ValueError as e:
        print(e)
        
    
        
    elif choice =="2": 
        #Create student object and adding it to the school
        
        school.display_student()
        print()
    elif choice == "3":
        try:
         roll_number = int(input("Enter roll_number which you want to edit: "))
         new_name=input("Enter new name for a student: ")
         new_age=int(input("Enter new age for student: "))
         print("<>"*16)
        
         school.edit_student(roll_number,new_name, new_age)
         
        except ValueError as e:
            print(e)
            
    elif choice=="4":
        roll_number=int(input("Enter roll_number you want to delete: "))
        school.delete_student(roll_number)
        
        
    elif choice=="5":
        break