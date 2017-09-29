# master = "chair"
# word = list(master)
# length = len(word)
# right = list("_" * length)
# finished = False
#import sy
#stillAlive = False

#Declare values
tables=[]
joins=[]
joinType=["INNER JOIN","RIGHT JOIN","LEFT JOIN","FULL OUTER JOIN"]
stillAlive = True

#--------------------------------------------
#  Prompt for User database and table Input
#--------------------------------------------

DBInput = input("Database being accessed:")
tableInput = input('Insert table to select from:')
DBTable = DBInput + ".dbo" + "." + tableInput
tables.append(DBTable)

#--------------------------------------------
#  Multiple Joins Step/Loop
#--------------------------------------------

while stillAlive == True:
    keepGoing = input("Do you need to join to another table Y/N:")
    if keepGoing not in ("Y", "N"):
        print("Invalid value entered: " + str(keepGoing))
        stillAlive = False
    else:
        joinInput = input("How would you like to join to the next table.(I, R, L, F)?:")
        for character in joinInput:
            if character not in ('I','R','L','F'):
                print("Invalid value entered: " + str(character))
        joins.append(joinInput)
        DBInput = input("Database being accessed:")
        tableInput = input('Insert table to select from:')
        DBTable = DBInput + ".dbo" + "." + tableInput
        tables.append(DBTable)

print("""
SELECT * 
FROM """ + tables[0] + " " + joinType[0] + " " + tables[1] + " ON " + "????? = ?????")

#while stillAlive == "Y":
#    joinType = input("How would you like to join to the table.(I, R, L, F)?:")
#    if joinType == "I":
#        joinType = list("INNER JOIN")
#    elif joinType == "R":
#        joinType = list("RIGHT JOIN")
#    elif joinType == "L":
#        joinType = list("LEFT JOIN")
#    else:
#        joinType == list("FULL OUTER JOIN")


