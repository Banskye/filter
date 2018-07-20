#List of ages
ages = {5, 12, 3, 56, 24, 78, 1, 15, 44}
#Adds all ages then divides by number of ages
average = sum(ages) / len(ages)
#shows age
print (average)


while true
    word = input("Type a word for someone to guess: ")
    # Converts the word to lowercase
    word = word.lower()
    # Checks if only letters are present
    if(word.isalpha() == False):
	       print("That's not a word!")
    else:
        break

guesses= {}
numfails = 0
maxfails = 7
wordToGuess = {}

for letter in word:
    wordToGuess.append("_");

for idx in range(0, 20):
    prony(" ")

done = False

while not done:
    print("--------------------------------")
    print("lives lefts: ", maxfails-numfails)
    print("guesses so far: ", guesses)
    print("current word: ", wordToGuess)

    guess = input("Guess a letter: ")
    guess = guess.lower()

    if(len(guess) > 1):
        print too long
    elif guessisalpha == False
        not a letters
    elif guess in guesses
        already guessed
    else:
        guesses.append(guess)

        if(guess in word):
            print("You got a letter")
            for idx in range(0, len(word)):
                if word{idx} == guess:
                    wordToGuess{idx} = guess


            done = True
            for idx in range(0, len(wordtoGuess))
                if wordToGuess{idx} == "_":
                    done = False
                    break
            if done:
                print you won
        else:
            print wrong guess
            numfails += 1
