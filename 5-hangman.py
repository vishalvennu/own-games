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

def displayGame(letter, secretWord, missedLetters, final):

  if letter not in list(secretWord):
        missedLetters = missedLetters + list(letter) # or missedLetters.append(letter)

  print (secretWord)
  print (hangmanPics[len(missedLetters)])

  for i in range(len(secretWord)):
    if letter == secretWord[i]:
      final = final[:i] + secretWord[i] + final[i+1:]
    if('_' not in final):
      print ("You won!")
      break
  
  print (final)
  print ('missed letters:', end="")
  print (missedLetters) 
    
  return (final, missedLetters)


missedLetters=[]
secretWord = getRandomWord(wordsList)
final = "_"*len(secretWord)
print(final)

while (len(missedLetters) <= 6):
  letter = input()
  if(letter in missedLetters):
    print (f"Already entered {letter}; Try a different alphabet.")
    continue
  
  final, missedLetters = displayGame(letter, secretWord, missedLetters, final)

print ("You lost!")