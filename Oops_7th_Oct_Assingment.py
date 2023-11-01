#!/usr/bin/env python
# coding: utf-8

# In[22]:


class Bankaccount:
    
    def __init__(self, account_number, account_holder_name, balance):
        self.account_number = account_number
        self.account_holder_name = account_holder_name
        self.balance = balance

    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited {amount} rupees into {self.account_number}.")
        else:
            print("Invalid amount. Please enter a positive value.")
        
    def withdraw(self,amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f"Successfully withdraw {amount} rupees from {self.account_number}.")
        else:
            print("Invalid amount. Please enter a positive value that is less than or equal to your balance.")        


# In[23]:


obj_bankacc = Bankaccount(2344566, 'harshwardhan',100)


# In[24]:


obj_bankacc.deposit(100)


# In[25]:


obj_bankacc.withdraw(20)


# In[36]:


class employee_management:
    
    def __init__(self, employee_ID, employee_name, employee_salary):
        self.employee_ID = employee_ID
        self.employee_name = employee_name
        self.employee_salary = employee_salary
        
    def bonus(self, salary):
        if salary<=10000:
            salary = self.employee_salary*0.10
            print(f"Employee ID :{self.employee_ID} Employee name :{self.employee_name} Salary :{self.employee_salary} Yearly bonus :{salary}")
        elif salary<=20000:
            salary = self.employee_salary*0.20
            print(f"Employee ID :{self.employee_ID} Employee name :{self.employee_name} Salary :{self.employee_salary} Yearly bonus :{salary}")
        elif salary<=30000:
            salary = self.employee_salary*0.30
            print(f"Employee ID :{self.employee_ID} Employee name :{self.employee_name} Salary :{self.employee_salary} Yearly bonus :{salary}")
        elif salary<=40000:
            salary = self.employee_salary*0.40
            print(f"Employee ID :{self.employee_ID} Employee name :{self.employee_name} Salary :{self.employee_salary} Yearly bonus :{salary}")
        elif salary<=50000:
            salary = self.employee_salary*0.50
            print(f"Employee ID :{self.employee_ID} Employee name :{self.employee_name} Salary :{self.employee_salary} Yearly bonus :{salary}")
        else:
            print("This could not be a salary")
    


# In[37]:


obj_employee = employee_management(1246464, "harshwardhan", 45000)


# In[38]:


obj_employee.bonus(45000)


# In[22]:


class VehicleRentalSystem:

    def __init__(self, vehicles):
        self.vehicles = vehicles
        self.rented_vehicles = []

    def rent_vehicle(self, name, customer):
        for vehicle in self.vehicles:
            if vehicle["name"] == name:
                self.vehicles.remove(vehicle)
                vehicle["customer"] = customer
                self.rented_vehicles.append(vehicle)
                return f"{customer} rented {name} for ${vehicle['price']} per day."
        return f"Sorry, {name} is not available for rent."

    def return_vehicle(self, name):
        for vehicle in self.rented_vehicles:
            if vehicle["name"] == name:
                self.rented_vehicles.remove(vehicle)
                del vehicle["customer"]
                self.vehicles.append(vehicle)
                return f"{name} has been returned."
        return f"Sorry, {name} is not rented from us."

    def display_vehicles(self):
        if len(self.vehicles) == 0:
            return "Sorry, we have no vehicles available for rent."
        table = "| Name | Type | Price |\n|------|------|-------|\n"
        for vehicle in self.vehicles:
            table += f"| {vehicle['name']} | {vehicle['type']} | ${vehicle['price']} |\n"
        return table


# In[23]:


obj_vehicle = VehicleRentalSystem([
    {'name':'avon','type': '2 wheel', 'price': 100}, 
    {'name':'auto','type': '3 wheel', 'price': 200}, 
    {"name": "Bike", "type": "Mountain", "price": 20}, 
    {"name": "Car", "type": "SUV", "price": 60}])


# In[24]:


obj_vehicle.rent_vehicle("avon","harsh")


# In[25]:


obj_vehicle.return_vehicle("Bike")


# In[26]:


obj_vehicle.display_vehicles()


# In[38]:


# Define a class for the book
class Book:

    # Define an initializer for the book
    def __init__(self, title, author):
        self.title = title # The title of the book
        self.author = author # The author of the book
        self.available = True # The availability of the book

    # Define a method to display the book information
    def display(self):
        print(self.title + " by " + self.author)

# Define a class for the library
class Library:

    # Define an initializer for the library
    def __init__(self):
        self.books = [] # A list of books in the library

    # Define a method to add books to the library
    def add_book(self, book):
        self.books.append(book) # Add the book to the list
        print(book.title + " has been added to the library.")

    # Define a method to borrow books from the library
    def borrow_book(self, title):
        # Loop through the books in the library
        for book in self.books:
            # If the title matches and the book is available, set the availability to false and return a confirmation message
            if book.title == title and book.available:
                book.available = False
                print("You have borrowed " + book.title + ".")
                return
        # If the title does not match or the book is not available, return an error message
        print("Sorry, " + title + " is not available for borrowing.")

    # Define a method to display available books in the library
    def display_books(self):
        # If there are no books in the library, return a message
        if len(self.books) == 0:
            print("The library has no books.")
            return
        # Otherwise, create a table with the title and author of each available book
        print("| Title | Author |")
        print("|-------|--------|")
        for book in self.books:
            if book.available:
                print("| " + book.title + " | " + book.author + " |")


# In[39]:


obj_Library = Library()


# In[40]:


obj_Library.add_book(Book("The Catcher in the Rye", "J.D. Salinger"))


# In[41]:


obj_Library.borrow_book("The Hunger Games")


# In[42]:


obj_Library.display_books()


# In[ ]:





# In[1]:


# Define a class for products
class Product:
    # Initialize the product with a name, a price, and a quantity
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    # Return a string representation of the product
    def __str__(self):
        return f"{self.name}: ${self.price}, {self.quantity} in stock"

# Define a class for inventory system
class Inventory:
    # Initialize the inventory with an empty dictionary of products
    def __init__(self):
        self.products = {}

    # Add a product to the inventory, or update its quantity if it already exists
    def add_product(self, product):
        if product.name in self.products:
            self.products[product.name].quantity += product.quantity
        else:
            self.products[product.name] = product

    # Update the quantity of a product in the inventory, or remove it if it becomes zero or negative
    def update_product(self, name, quantity):
        if name in self.products:
            self.products[name].quantity += quantity
            if self.products[name].quantity <= 0:
                del self.products[name]

    # Display the available products in the inventory
    def display_products(self):
        for product in self.products.values():
            print(product)


# In[13]:


p1 = Product("Laptop", 200, 10)
p2 = Product("Computer", 500, 20)
p3 = Product("TV", 300, 15)


# In[14]:


obj_inventry = Inventory()


# In[15]:


obj_inventry.display_products()


# In[17]:


obj_inventry.add_product(p1)


# In[18]:


obj_inventry.add_product(p2)


# In[19]:


obj_inventry.add_product(p3)


# In[20]:


obj_inventry.display_products()


# In[21]:


obj_inventry.update_product("TV" , -2)


# In[22]:


obj_inventry.display_products()


# In[24]:


class Shape:
    
    def __init__(self, length, width ,height):
        self.length = length
        self.width = width
        self.height = height
        
    def area_of_shape(self):
        self.area = 2*((self.length * self.width) + (self.width * self.height) + (self.height * self.length))
        print(f"Area of shape = {self.area}")
        
    def perimeter_of_shape(self):
        self.perimeter = 4 * (self.length * self.width * self.height)
        print(f"Perimeter of shape = {self.perimeter}")


# In[25]:


obj_shape = Shape(2, 3, 4)


# In[26]:


obj_shape.area_of_shape()


# In[27]:


obj_shape.perimeter_of_shape()


# In[32]:


class Student_Management:
    
    
    def __init__(self, student_ID, student_name):
        self.student_ID = student_ID
        self.student_name = student_name
        
    def calculate_average_grade(self, math_mark, science_mark, english_mark, history_mark, geography_mark):
        self.math_mark = math_mark
        self.science_mark = science_mark
        self.english_mark = english_mark
        self.history_mark = history_mark
        self.geography_mark = geography_mark
        self.average_mark = ((self.math_mark+self.science_mark+self.english_mark+self.history_mark+self.geography_mark)/5)
        print(f"Average grade of student {self.average_mark}")
        
    def display_student_details(self):
        print(f"Name of student {self.student_ID}")
        print(f"Student name {self.student_name}")
        print(f"Average grade {self.average_mark}")


# In[33]:


obj_stud = Student_Management(12345, "Harshwardhan")


# In[34]:


obj_stud.calculate_average_grade(22,34,45,56,67)


# In[35]:


obj_stud.display_student_details()


# In[11]:


class Email_Mangement:
    
    def __init__(self, sender, recipient, subject):
        self.sender = sender
        self.recipient = recipient
        self.subject = subject
        
    def send_email(self, email_body):
        #self.subject = subject
        self.email_body = email_body
        print(f"email sent to {self.recipient}")
        
    def display_email_details(self):
        print(f"To : {self.recipient}")
        print(f"From : {self.sender}")
        print(f"Subject : {self.subject}")
        print(f"{self.email_body}")
        


# In[12]:


obj_email = Email_Mangement("Harsh@gmail.com", "harshwardhan@gmail.com", "regarding teaching OOPS")


# In[13]:


obj_email.send_email("Hi this is form test email")


# In[14]:


obj_email.display_email_details()


# In[16]:


class Social_Media_Profile:
    
    def __init__(self, username):
        self.username = username
        self.posts = []

    def add_post(self, post):
        self.posts.append(post)

    def display_posts(self):
        print(f"{self.username}'s posts:")
        for post in self.posts:
            print(post)

    def search_posts(self, keyword):
        print(f"Searching for '{keyword}' in {self.username}'s posts:")
        for post in self.posts:
            if keyword in post:
                print(post)


# In[17]:


obj_social = Social_Media_Profile("harshwardhan")


# In[18]:


obj_social.add_post("This is my first post")


# In[19]:


obj_social.display_posts()


# In[20]:


obj_social.add_post("this is my last post")


# In[21]:


obj_social.display_posts()


# In[22]:


obj_social.search_posts("last")


# In[23]:


class ToDo_List:
    
    def __init__(self):
        self.tasks = []

    def add_task(self, name, due_date):
        task = {"name": name, "due_date": due_date, "completed": False}
        self.tasks.append(task)

    def mark_task(self, name):
        for task in self.tasks:
            if task["name"] == name:
                task["completed"] = True
                break

    def display_tasks(self):
        print("Pending Tasks:")
        for task in self.tasks:
            if not task["completed"]:
                print(f"- {task['name']} (due: {task['due_date']})")


# In[24]:


obj_todo = ToDo_List()


# In[28]:


obj_todo.add_task("read a book", 23)


# In[29]:


obj_todo.add_task("write a book", 25)


# In[30]:


obj_todo.display_tasks()


# In[31]:


obj_todo.mark_task("read a book")


# In[32]:


obj_todo.display_tasks()


# In[ ]:




