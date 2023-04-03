import  random

def RPS():
    choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
    all=['paper','scissors','rock',]



    def randomChoicer():
        randomize=random.randint(0, len(all)-1)
        randomChoice=all[randomize]
        return randomChoice


    theRandom=randomChoicer()

    while True:
        
        if choice not in all:
            choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
        else: 
            if(choice == theRandom):

                print('this is a tie!' , choice , 'againest' ,theRandom)
                choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                theRandom=randomChoicer()
                # again=input('do you want to play again? (yes or no): ').lower()
                # if again=='yes':
                #     choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                #     theRandom= randomChoicer()
                # else: 
                #     break
            elif(choice =='rock' ):
                if(theRandom=='scissors'):
                    print('you win! againest', theRandom)
                    # choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                    # theRandom=randomChoicer()
                    again=input('do you want to play again? (yes or no): ').lower()
                    if again=='yes':
                        choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                        theRandom= randomChoicer()
                    else: 
                        break
                elif(theRandom=='paper'):
                    print('you lose! againest', theRandom)
                    choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                    theRandom=randomChoicer()







            elif(choice =='paper' ):
                if(theRandom=='rock'):
                    print('you win! againest', theRandom)
                    # choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                    # theRandom=randomChoicer()
                    again=input('do you want to play again? (yes or no): ').lower()
                    if again=='yes':
                        choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                        theRandom= randomChoicer()
                    else: 
                        break
                elif(theRandom=='scissors'):
                    print('you lose! againest', theRandom)
                    choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                    theRandom=randomChoicer()





            elif(choice =='scissors' ):
                if(theRandom=='paper'):
                    print('you win! againest', theRandom)
                    # choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                    # theRandom=randomChoicer()
                    again=input('do you want to play again? (yes or no): ').lower()
                    if again=='yes':
                        choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                        theRandom= randomChoicer()
                    else: 
                        break
                elif(theRandom=='rock'):
                    print('you lose! againest', theRandom)
                    choice=input('please choose one of the following: Rock,Paper, Scissors: ').lower()
                    theRandom=randomChoicer()


            
            
                
            # else:
            #     print('the game is over!',choice,theRandom)
            #     break

RPS()
