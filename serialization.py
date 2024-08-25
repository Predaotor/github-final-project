import json
import os 


def save_user_data():
    user_list=[]
    
    while True:
        name=input("enter name (or quit to exit the program): ")
        
        if name.lower()=="quit":
            break 
        
        email=input("Enter email: ")
        contact=input("Enter phone number: ")
        
        # Creating dictionary 
        user_data={
            "name":name,
            "email":email,
            "contact":contact
        }
        
        user_list.append(user_data)
        
    if os.path.exists("user_data.json"):
        
        with open("user_data.json", "r")as file:
            
            existing_data=json.load(file)
            user_list.extend(existing_data)
            
    with open("user_data.json", "w")as file:
        
            json.dump(user_list, file, indent=4)
            
    print("User data saved successfully")
            
            

def read_user_data():
    
    
    if not os.path.exists("user_data.json"):
        
        print("No user data found")
        return 
    
    with open("user_data.json", "r")as file:
        user_list=json.load(file)
        
        for user_data in user_list:
            
            print("Name:",user_data["name"])
            print("Email:",user_data["email"])
            print("Contact:",user_data["contact"])
            print("\n")

def edit_user(name):
    
        if  not os.path.exists("user_data.json"): 
            
            print("user_data File not found ")
            return False
        
        with open("user_data.json", "r")as file:
            user_list=json.load(file)
        
        
        for user_data in user_list:
            
            if user_data["name"].lower()==name.lower():
                
                email=input("Enter updated email: ")
                contact=input(" Enter Updated contact: ")
            
                user_data["email"]=email
                user_data["contact"]=contact
          
            
            
                with open("user_data.json", "w")as file:
                  json.dump(user_list, file, indent=4)
            
                print("User data updated successfully")
                return True
        
        print("User Not found")
        return False


def delete_user(name):
    if  not os.path.exists("user_data.json"): 
            
            print("user_data File not found ")
            return False
        
    with open("user_data.json", "r")as file:
            user_list=json.load(file)
            
    for user_data in user_list:
        
        if user_data['name'].lower()==name.lower():
            
                user_list.remove(user_data)
                
                with open("user_data.json", "w") as file:
                  json.dump(user_list, file, indent=4)
                
                print("User removed successfully ")
                return True 
            
        print("User not found")
        return False
                

# main execution
  
save_user_data()

delete_name=input("Enter user you want to remove: ")
delete_user(delete_name)

name_to_edit=input("Enter name which you want to edit data for: ")

if edit_user(name_to_edit):
    
  read_user_data()
  
else:
    print("No changes made. ")