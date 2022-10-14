import random
import random
hangmanPics = ['''
    +--+
       |
       |
       |
      ===''', '''
    +--+
    O  |
       |
       |
      ===''', '''
    +--+
    O  |
    |  |
       |
      ===''', '''
    +--+
    O  |
    |\ |
       |
      ===''', '''
    +--+
    O  |
   /|\ |
       |
      ===''', '''
    +--+
    O  |
   /|\ |
   /   |
      ===''', '''
    +--+
    O  |
   /|\ |
   / \ |
      ===''']

wordsList = "mark peasant lake asylum positive ally thick pursuit back charismatic shoot frighten opera civilian assessment hell aloof problem spill go wound tax drum chord trolley last tell will wire structure crew image low kid slave cattle temple persist banish invasion fascinate grateful nap excavation respectable dead trade hunting consensus disappoint".split()

missedLetters=[]
def getRandomWord(wordsList):
    return (wordsList[random.randint(0,len(wordsList)-1)])

def displayGame(letter, secretWord):
    
    if letter not in list(secretWord):
        missedLetters = missedLetters + letter
        print (missedLetters)
    # chances = len(missedLetters)
    # print (hangmanPics[chances])

letter = input()
