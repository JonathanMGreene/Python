# master = "chair"
# word = list(master)
# length = len(word)
# right = list("_" * length)
# finished = False

stillAlive = False
DBInput = input("Database being accessed:")
tableInput = input("Insert table to select from:")
DBTable = DBInput + ".dbo" + "." + tableInput
stillAlive = "Y"
while stillAlive == "Y":
    stillAlive = input("Do you need to join to another table Y/N:")
    joinType = input("How would you like to join to the table.(I, R, L, F)?:")
    if joinType == "I":
                joinType = "INNER JOIN"
                tableInput2 = input("Insert table to join to:")
                DBTable2 = DBInput + ".dbo" + "." + tableInput2
    stillAlive = input("Do you need to join to another table Y/N:")
else:
    stillAlive = "N"
print("SELECT * FROM " + DBTable + " " + joinType + " " + DBTable2 + " ON " + "????? = ?????")


# while finished == False:
#    guess = input("Guess a letter!")
#    if guess not in master:
#        print("This letter is not in the word.")
#    for letter in word:
#            if letter == guess:
#                index = word.index(guess)
#                right[index] = guess
#                word[index] = "_"
#                print(right)
#            if list(master) == right:
#                print("You win!")
#                finished = True
