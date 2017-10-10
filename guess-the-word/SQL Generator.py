tables=[]
joins=[]
joinType=["INNER JOIN","RIGHT JOIN","LEFT JOIN","FULL OUTER JOIN"]
#joinType = {"I": "INNER JOIN", "L": "LEFT JOIN", "R": "RIGHT JOIN", "F": "FULL OUTER JOIN"}
stillAlive = True
DBInput = ''
tableInput = ''
joinInput = ''
header = ''

#--------------------------------------------
# get_table function
#
#  Prompt for User database and table Input
#--------------------------------------------

def get_table(DBInput,tableInput):
    while len(DBInput) <= 1 or len(tableInput) <= 1:    # need to work on this loop
        DBInput = input("Database being accessed:")
        if len(DBInput) <= 1:
            print("Invalid Database name " + str(DBInput) + " entered:")
        tableInput = input('Insert table to select from:')
        if len(tableInput) <= 1:
            print("Invalid table name " + str(tableInput) + " entered:")
    DBTable = DBInput + ".dbo" + "." + tableInput
    return DBTable

#--------------------------------------------
# get_join function
#
#  Prompt for User database and table Input
#--------------------------------------------
def get_join(joinInput):
    joinInput = input("How would you like to join to the next table.(I, R, L, F)?:")
    for character in joinInput:
        if character not in ('I', 'R', 'L', 'F'):
            print("Invalid value entered: " + str(character))
    return joinInput

#--------------------------------------------
# get_header function
#
#
#--------------------------------------------
def get_header( ):
    print("ServerName")
    print("/* This is a test stored prod */")
    return header


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
        # --------------------------------------------
        #  Call DB and Table function
        # --------------------------------------------
        joins.append(get_join(joinInput))
        # --------------------------------------------
        #  Call join function
        # --------------------------------------------
        tables.append(get_table(DBInput, tableInput))
        print(joins)
        print(tables)
        print(len(tables))
if len(tables) == 0:
    print("No table was entered. Please enter at least one table!")
elif len(tables) == 1:
    get_header()
    print("""
    SELECT * 
    FROM """ + tables[0])
else:
    get_header()
    print("""
    SELECT * 
    FROM """ + tables[0] + " " + joinType[0] + " " + tables[1] + " ON " + "????? = ?????")




