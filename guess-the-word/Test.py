#boring = False
#beloved = True
#if not boring or beloved:
#    print("watch movie ")
#if not boring and beloved:
#    print("but ask them first")

#a = True
#b = True
#if a and b:
#    print("a and b are true")
#if a or b:
#    print("a, b, or both are true")

#score = 200
#try:
#    score
#    print(str(score))
#except:
#    print("score wasn't set")
#    score = 100



#try:
#    print(number)
#except:
#    print("number wasn't set")


#use If statements for and booleans
#love = False
#score = 90
#if love == True:
#    print("Aww!")
#elif love == False and score < 100:
#    print("Go for it")
#else:
#    print("Won!")

#start from back of a list
#l = ["a","b","c","d","j","m"]
#print(l[-1])

#Add to a list
#romance = ["Juno", "Her", "Chocolat"]
#romance.append("Alien")
#print(len(romance))

#add mutliple lists to a single list and access by indexs.
#l1 = ["a","b", "c", "d"]
#l2 = ["z","g","m"]
#l3 = [22,3,6,0.1,2,"Hello",1]
#listlist = [l1,l2,l3]
#print(listlist[2][1])


#using tuples for read only values becuase values can not be changed
#tup1 = ("America","conq. 1492")
#tup2 = ("light","222 km/s")
#print(tup2[1])

#index using tuple
#myTuple = ("north","south")
#print(myTuple[0:1])

#turn a tumple into a list and change a value
#mytuple = ("Ann", "Ben","Chen")
#mylist = list(mytuple)
#mylist[1]= "Bob"
#print(mylist)


#list stored multiple values at once and accessed and changed
#shoppinglist = ["ham","eggs","flour"]
#shoppinglist.append([3,"a",True])
#print(shoppinglist)


# for loop will loop 4 times
#for i in range(4):
#    print(i)

#for loop with list
#mylist= ["me", "you", "we","us"]
#for element in mylist:
#    print(element)

#for loop with index counter
#mylist = [13,21,4,7]
#changes = [5,4,3,2]
#for i in range(len(mylist)):
#    mylist[i] += changes[i]
#    print(str(mylist[i]))

#tell loop to stop
#for i in range(8):
#    print(i)
#    if i == 4:
#        break


#while loop
#temperature = 60
#summer = True
#while temperature >= 60:
#    temperature -= 1
#summer = False
#print(temperature)

#infinite while loop never true
#d = 0
#while d >= 0:
#    d += 1
#    print(d)

#interate over a string
#text = "One ring to rule them all"
#found = False
#for character in text:
#    if character == "z":
#        found = True
#print("Found: " + str(found))

#loop within a loop
#students = [
#    ["John", "CS"],
#    ["Lisa", "Physics"]]
#for i in range(len(students)):
#    for j in range(len(students[i])):
#        print(students[i][j])

#loop until conditions are true
#for i in range(3):
#    print("for loop #" + str(i))
#bee = "bee"
#while bee != "beeeee":
#    bee += "e"
#    print(bee)

#get list of values
#n = {"one": "un", "two": "deux"}
#print(n["one"])


#get list of keys
#n = {"one": "un", "two": "deux"}
#print(n.keys())

#use keyword to loop through dictionary keys
#nicknames = {"Arthur": "Art", "Lancelot": "Lance"}
#print("Arthur" in nicknames)

# get length of dictionary
#n = {"one": "un", "two": "deux"}
#print(len(n))

#add value to dictionary
#n = {"one": "un", "two": "deux"}
#n.update({"three": "trois"})
#print(n)

#remove value from dictionary
#n = {"one": "un", "two": "deux"}
#element = n.pop("one")
#print(element)

#create dictionary, define a value, and pop the element.
#dict ={}
#dict["name"] = "Win"
#if "name" in dict.keys():
#    element = dict.pop("name")
#print(element)
