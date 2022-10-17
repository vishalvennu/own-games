import random
import random
hangmanPics = ['''
    +--+
       |
       |
       |
      ===
      ''', '''
    +--+
    O  |
       |
       |
      ===
      ''', '''
    +--+
    O  |
    |  |
       |
      ===
      ''', '''
    +--+
    O  |
    |\ |
       |
      ===
      ''', '''
    +--+
    O  |
   /|\ |
       |
      ===
      ''', '''
    +--+
    O  |
   /|\ |
   /   |
      ===
      ''', '''
    +--+
    O  |
   /|\ |
   / \ |
      ===
      ''']

wordsList = "mark peasant lake asylum positive ally thick pursuit back charismatic shoot frighten opera civilian assessment hell aloof problem spill go wound tax drum chord trolley last tell will wire structure crew image low kid slave cattle temple persist banish invasion fascinate grateful nap excavation respectable dead trade hunting consensus disappoint".split()



def getRandomWord(wordsList):
    return (wordsList[random.randint(0,len(wordsList)-1)])

def displayGame(letter, secretWord, missedLetters, eval):

  if letter not in list(secretWord):
        missedLetters = missedLetters + list(letter)

  print (secretWord)
  print (hangmanPics[len(missedLetters)])

  

  for i in range(len(secretWord)):
    if letter == secretWord[i]:
      eval = eval[:i] + secretWord[i] + eval[i+1:]
    if('_' not in eval):
      print ("You won!")
      break
  
  
  print (eval)
  print ('missed letters:', end="")
  print (missedLetters) 

  
    # chances = len(missedLetters)
    # print (hangmanPics[chances])
    

  return (eval, missedLetters)

    

missedLetters=[]
secretWord = getRandomWord(wordsList)
eval = "_"*len(secretWord)

while (len(missedLetters) <= 6):
  letter = input()
  if(letter in missedLetters):
    print ("Already entered; Try a different alphabet.")
    continue
  
  eval, missedLetters = displayGame(letter, secretWord, missedLetters, eval)
