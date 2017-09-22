master = input("Enter a word:")
print("/n" * 50)
word = list(master)
length = len(word)
right = list("_" * length)
finished = False
while finished == False:
    guess = input("Guess a letter!")
    if guess not in master:
        print("This letter is not in the word.")
    for letter in word:
            if letter == guess:
                index = word.index(guess)
                right[index] = guess
                word[index] = "_"
                print(right)
                if list(master) == right:
                    print("You win!")
                    again=input("Again? y/n ")
                    if again == "y":
                       master = input("Enter a word:")
                       print("/n" * 50)
                       word = list(master)
                       length = len(word)
                       right = list("_" * length)
                    else:
                        finished = True