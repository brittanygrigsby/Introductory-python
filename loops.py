#For loop
#Is used fo riterating over a sequence (list, tuples, dictionaries, set, strings)

fruits_list = ["apple","banana","cherry","orange","grapes"] 

my_dictionary= {
"brand":"Ford",
"model":"Mustang",
"year":1964,
"colors":["red","white","blue","black"]
}

for fruit in fruits_list:
    if fruit == "cherry":
        #break
        continue
    print(fruit)

    print("-------------")
    for items in my_dictionary:
        print(f"Keys only: {items} | Retrieving the value: {my_dictionary[items]}")
    
   
    print("-------------")

    for x in "iteration":
        print(x)


    print("-------------")
    for number in range(0, len(fruits_list)):
        print(fruits_list[number])

    # range (START_VALUE, STOP_VALUE, STEPS OR INCREMENTS)
    for number in range(0,len(fruits_list),2):
        print(fruits_list[number])