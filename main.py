"""
Name(s): Arabelle Choo
Name of Project: The Hangman of my Blood, Sweat, and Tears
"""
import random

print("let's play hangman") 

def theman(trials): #makes the man 

  hanging = [

              """

                  _________
                  |/      |
                  |     (-_-)
                  |      \|/
                  |       |
                  |      / \\
                  |
                __|____

 

        """,

        """

                   __________
                  |/      |
                  |      (_)
                  |      \|/
                  |       |
                  |      /
                  |
                __|____

 

        """,

        """

                    _________
                  |/      |
                  |      (_)
                  |      \|/
                  |       |
                  |      
                  |
                __|____

        """,

        """

                   _________
                  |/      |
                  |      (_)
                  |      \|/
                  |      
                  |     
                  |
                __|____

        """,

        """

                   _________
                  |/      |
                  |      (_)
                  |      \|/
                  |      
                  |     
                  |
                __|____

        """,

        """

                   _________
                  |/      |
                  |      (_)
                  |      \|
                  |      
                  |     
                  |
                __|____

        """,

        """

                   _________
                  |/      |
                  |      (_)
                  |       |
                  |      
                  |      
                  |
                __|____

        """,

        """       

                    _________
                  |/      |
                  |      (_)
                  |     
                  |      
                  |      
                  |
                __|____

        """,

        """

                   _________
                  |/     
                  |     
                  |     
                  |      
                  |     
                  |
                __|____

        """

  ]

 

  return hanging[trials]

 

def word_selected(fname): #selects the word to be guessed (list.txt must be in lowercase letters)

  word_file = open('list.txt', 'r+')

  answer = random.choice(word_file.read().split())

  word_file.close()

  return answer

 

answer = word_selected('list.txt')
#print(answer)

def mystery_word(): #converts it into underscores to show the number of letters

  mystery_word = []

  for i in range(len(answer)):

    mystery_word.append('_')

  return ''.join(mystery_word)

mystery_word = mystery_word()

print(mystery_word)

trials = 8

word_guess = list(mystery_word)

while trials > 0:

    if ''.join(word_guess) == answer:

      print("You got it!")

      break

    letter_guess = input("guess a letter: \n")

 

    letter_guess = letter_guess.lower()

 

    if len(letter_guess) == 1:

 

      if letter_guess in answer:

        print('Correct')

        for i in range(len(answer)):

         if list(answer)[i] == letter_guess:

           word_guess[i] = letter_guess

        print(''.join(word_guess))

      elif letter_guess not in answer:

          print('wrong!')

          trials -= 1

          print(theman(trials))

    else:

      print('only one letter at a time, please')


if trials == 0:

  print('Game over')

#spaces don't work, only one letter can be inputted at a time, it doesn't matter whether the inputted letter is upper or lowercase
