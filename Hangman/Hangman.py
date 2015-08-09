from random import choice

#Print out the letters found in the word or '_'
def print_puzzle(word, guesses):
     print ""
     for letter in word:
          if letter in guesses:
               print letter,
          else:
               print "_",
     print "\nAlready guessed: ",
     for guess in guesses:
          print guess,
     print "\n"

def main():
     f = open("wordlist.txt", 'r')      #Open a file for reading
     word_list = f.readlines()          #Put the words in our list
     f.close()                          #Close the file to free up system resources
     word = choice(word_list)           #Get a random word
     word = word[:-1]                   #Remove unnecessary newline character
     guessed_list = []                  #Holds previous guesses
     letters_found = 0                  #Number of letters guessed right
     wrong_guessed = 0                  #Number of wrong guesses

     #Find non-letters before the game starts to avoid confusion
     for letter in word:
          if not letter.isalpha():
               guessed_list.append(letter)
               letters_found += 1

     #Remove potential duplicates in our list
     guessed_list = list(set(guessed_list))

     print_puzzle(word, guessed_list)

     while letters_found != len(word) and wrong_guessed != 5:
          guess = raw_input("Guess a letter: ")
          guess = guess.lower()         #Make the guess lowercase

          if len(guess) != 1:           #Can only guess one thing at a time
               print "Please only guess one letter at a time"
          elif not guess.isalpha():     #Checks that the guess is a letter
               print "Please only guess letters"
          else:
               #If the guess is in our word and we haven't already guessed it
               if (guess in word) and (guess not in guessed_list):
                    letters_found += word.count(guess)
                    guessed_list.append(guess) #Add the guess to our list of previous guesses
               elif guess in guessed_list:
                    wrong_guessed += 1
                    print "Already guessed. {} guesses left".format(5-wrong_guessed)
               else:
                    wrong_guessed += 1
                    guessed_list.append(guess)
                    print "Wrong guess. {} guesses left".format(5-wrong_guessed)

          guessed_list.sort()
          print_puzzle(word, guessed_list)

                    
     if letters_found == len(word):
          print "Congratulations!"
     else:
          print "The word was {}. Try again next time".format(word)


if __name__ == "__main__":
     main()
