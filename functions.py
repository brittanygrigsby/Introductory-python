#Functions
#Is a block of code which only runs when it's called
#We can pass data, known as parameters and the function can return data as a result

#Simple function without parameters
def my_function():
    print("This is my function")

def other_function():
    print("This is another function!")

#functions with parameters
def print_full_name(fname, flast_name):
    print(f"The name is: {fname} {flast_name}")

#print_full_name("Brittany", "Grigsby")
#print_full_name(flast_name="Grigsby", fname="Brittany")

#Functions that returns something
def get_full_name(fname, flast_name):
    return f"{fname} {flast_name}"

full_name= get_full_name("Brittany", "Grigsby") #Brittany Grigsby
print(full_name)

