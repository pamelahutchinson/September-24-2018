

class Person():
    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0

    def add_friend(self,person):
        self.friends.append(person.name)

    def num_friends(self):
        print(len(self.friends))

    def describe_person(self):
        print("Name : " + self.name)
        print("Email: " + self.email)
        print("Phone: " + self.phone)
    
    def print_contact_info(self):
            print(self.name + "'s " + "email: " + self.email + ", " + self.name +"'s " + "phone number: " + self.phone)
    
    def greet(self, other_person):
        print("Hello %s, I am %s!"%(other_person.name, self.name))
        self.greeting_count += 1
        #print("Number of times greeted: ",self.greeting_count)

    def __repr__(self):
        return "Name = {0}, Email = {1}, Phone = {2}".format(self.name,self.email,self.phone)
        

class Vehicle:
    def __init__(self,make,model,year):
        self.make = make
        self.model = model
        self.year = year

    def describe_car(self):
        print("Make: " + self.make)
        print("Model: " + self.model)
        print("Year: " + self.year)

    def print_info(self):
        print(self.year,self.model,self.make)

car = Vehicle("Nissan","Leaf","2015")
car.describe_car()
car.print_info()

sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
jordan = Person("Jordan","jordan@aol.com","495-586-3456")

sonny.print_contact_info()
jordan.print_contact_info()

sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)
print("Number of times greeted: ", jordan.greeting_count)

sonny.describe_person()
jordan.describe_person()

#jordan.friends.append(sonny)
# print(len(jordan.friends))
jordan.add_friend(sonny)
jordan.num_friends()

print(jordan)
print(sonny)
