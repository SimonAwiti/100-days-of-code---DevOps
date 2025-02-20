#collections used to sto several entries into a single variable

fruits = ["banana", "apple", "pineable"]
fruits.append("avocado") #adds an element in a list
fruits.remove("banana")
fruits[2]= "pineapple" #changes an element in a list

fruits.insert(2, "coconout")
fruits.sort()
fruits.reverse()

print("banana" in fruits) # returns boolean 

for fruit in fruits:
    
    print (fruits)
    print(len(fruits)) #print the length of the list
   

