import random
name=input("PLEASE ENTER YOUR RESPACTIVE NAME = ").upper()
print(" HELLO",name,"WELCOME TO THE GAME :- HANGMAN")
image= ['''
    +---+
    |   |
        |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
        |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /    |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|   |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
        |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
        |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   /    |
        =========''', '''
    +---+
    |   |
    0   |
   /|\  |
    |   |
   / \  |
        =========''', '''
	
''']

def word():
    words="Rose Morigold Jasmine Sunflower Lotus daisy Lahalia Lily Palash Crocus"
    data=words.split()
    list=[]
    for i in data:
        list.append(i)
    secret_word=random.choice(list)
    return secret_word.lower()
def hangman():
    turns=9
    print(" PLEASE TRY TO GUESS RIGHT WORD ,AND YOU HAVE",turns,"ATTEMPT")
    secretword=word()
    tries=len(secretword)
    x=secretword
    b=[]
    for i in x:
        b.append(i)
    # print("your secret word is :-",b)
    print("YOUR WORD LENGTH IS THAT :-",len(secretword))
    lenword=""
    for i in range(len(secretword)):
        lenword=lenword+"_"
    lenwordlist=[]
    for i in lenword:
        lenwordlist.append(i)
    print(lenwordlist)
    print("              ")
    a=len(secretword)
    guesslist=[]
    while 8>0:
        guess=input("PLEASE GUESS LETTER OF SECRET WORD ")
        if len(guess)==1 and guess.isalpha():
            if guess in guesslist:
                print("YOU ALREADY GUESS THIS LETTER")
            else:
                guesslist.append(guess)
            if guess in secretword:
                print("GOOD JOB ",guess," LETTER IS IN SECRET WORD")
                for i in range(len(secretword)):
                   if secretword[i]==guess:
                       lenwordlist[i]=guess
                print("YOUR GUESSING WORD = ", lenwordlist)
                print("    ")
            if b==lenwordlist:
                print("*CONGRSTILATION YOU WON  *")
                break
            elif guess not in secretword:
                print("OOPS!,YOUR GUESS LETTER ",guess,"NOT IN SECRET WORD AND YOU HAVE LOST ONE CHANCE")
                turns=turns-1
                if turns==8:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS")
                    print(image[0])
                if turns==7:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS")
                    print(image[1])
                if turns==6:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS")
                    print(image[2])
                if turns==5:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS")
                    print(image[3])
                if turns==4:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS")
                    print(image[4])
                if turns==3:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS")
                    print(image[5])
                if turns==2:
                    print(" NOW YOU HAVE ONLY ",turns,"TURNS" ,"HANGMAN IS ON HIS LAST BREATH")
                    print(image[6])
                if turns==1:
                    print(" NOW YOU HAVE ONLY  ",turns,"turn")
                    print(image[7])
                    print("OOPS!,SORRY YOU ARE A LOOSER .TRY NEXT TIME")
                    break
        else:
            print("SORRY!, IT IS NOT VALID ",guess,"PLEASE GUESS ONLY ONE LETTER IN SMALL ALPHABET")   
           
        a=a-1
hangman()
def play_again():
    while True:
        again=input("If you Want to play again press y for yes or N of No  =") 
        if again=="y":
            hangman()
        else:
            break 