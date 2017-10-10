tables=[]
joins=[]
joinType=["INNER JOIN","RIGHT JOIN","LEFT JOIN","FULL OUTER JOIN"]
stillAlive = True
DBInput = ''
tableInput = ''

#--------------------------------------------
#  Prompt for User database and table Input
#--------------------------------------------

#DBInput = input("Database being accessed:")
#tableInput = input('Insert table to select from:')
#DBTable = DBInput + ".dbo" + "." + tableInput
#tables.append(DBTable)

#--------------------------------------------
# get_table function
#
#  Prompt for User database and table Input
#--------------------------------------------
def get_table(DBInput,tableInput):
    DBInput = input("Database being accessed:")
    tableInput = input('Insert table to select from:')
    DBTable = DBInput + ".dbo" + "." + tableInput
    print(DBTable)
    return DBTable


#--------------------------------------------
#  Call DB and Table function
#--------------------------------------------

tables.append(get_table(DBInput,tableInput))

#--------------------------------------------
#  Multiple Joins Step/Loop
#--------------------------------------------

while stillAlive == True:
    keepGoing = input("Do you need to join to another table Y/N:")
    if keepGoing not in ("Y", "N"):
        print("Invalid value entered: " + str(keepGoing))
        stillAlive = False
    elif keepGoing == "N":
        stillAlive = False
    else:
        joinInput = input("How would you like to join to the next table.(I, R, L, F)?:")
        for character in joinInput:
            if character not in ('I','R','L','F'):
                print("Invalid value entered: " + str(character))
        joins.append(joinInput)
        tables.append(get_table(DBInput, tableInput))
        print(tables)
      #  DBInput = input("Database being accessed:")
      #  tableInput = input('Insert table to select from:')
      #  DBTable = DBInput + ".dbo" + "." + tableInput
      #  tables.append(DBTable)

print("""
SELECT * 
FROM """ + tables[0] + " " + joinType[0] + " " + tables[1] + " ON " + "????? = ?????")




