import re
def hangman(word):
    tries=''
    wrongList=[]
    nospace='_'*len(word)
    list2=list(nospace)
    print(nospace,len(nospace))

    while '_' in list2 :
        guess=input('enter your guess: ')
        if guess=='' or len(guess)>1: 
            guess=input('enter a single letter guess')
        elif guess in list2 or guess in wrongList:
            print('you have entered that guess')
        else:
            # guess=input('enter your guess: ')
       
            indexes = [
                match.start() for match in re.finditer(guess ,word)
            ]
            if guess in word and guess not in list2:
            
                for i in indexes:
                
                    list2[i] = guess
                   
                    print( tries.join(list2))
            else:
                if len(wrongList)<5:
                    wrongList.append(guess)
                    print(tries,wrongList)
                    
                else:
                    wrongList.append(guess)
                    return f'{tries} HangMan died {wrongList}' 

    return f'{tries} HangMan saved {wrongList}'        





        
 
   


print(hangman('blackboard'))