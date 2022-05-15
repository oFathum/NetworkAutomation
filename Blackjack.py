import random
info=0
currCard=0
hands= []
hand1= []
handD= []
playb=0
playbb=0
dealp=0
dealb=0
dealt=0
forp=0
prin=0
double= 0
shufdeck= []
deck= ['King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts', '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts',
           '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades', 'Jack Of Spades', '10 Of Spades', '9 Of Spades',
           '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades', '3 Of Spades', '2 Of Spades', 'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs',
           'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs',
           'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds',
           '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts',
           '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades',
           'Jack Of Spades', '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades', '3 Of Spades', '2 Of Spades',
           'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs',
           '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds',
           '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts',
           'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts', '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts', '3 Of Hearts', '2 Of Hearts',
           'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades', 'Jack Of Spades', '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades',
           '4 Of Spades', '3 Of Spades', '2 Of Spades', 'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs',
           '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds',
           '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds',
           'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts', '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts',
           '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades', 'Jack Of Spades', '10 Of Spades', '9 Of Spades', '8 Of Spades',
           '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades', '3 Of Spades', '2 Of Spades', 'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs',
           '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds',
           'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds',
           '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts', '8 Of Hearts',
           '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades', 'Jack Of Spades',
           '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades', '3 Of Spades', '2 Of Spades', 'Ace Of Spades',
           'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs',
           '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds',
           '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts',
           '10 Of Hearts', '9 Of Hearts', '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts',
           'King Of Spades', 'Queen Of Spades', 'Jack Of Spades', '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades',
           '3 Of Spades', '2 Of Spades', 'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs',
           '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds',
           '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds',
           'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts', '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts',
           '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades', 'Jack Of Spades', '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades',
           '6 Of Spades', '5 Of Spades', '4 Of Spades', '3 Of Spades', '2 Of Spades', 'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs',
           '9 Of Clubs', '8 Of Clubs', '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds',
           'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds',
           '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts', '10 Of Hearts', '9 Of Hearts', '8 Of Hearts',
           '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts', 'King Of Spades', 'Queen Of Spades', 'Jack Of Spades',
           '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades', '3 Of Spades', '2 Of Spades', 'Ace Of Spades',
           'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs', '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs',
           '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds', '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds',
           '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds', 'King Of Hearts', 'Queen Of Hearts', 'Jack Of Hearts',
           '10 Of Hearts', '9 Of Hearts', '8 Of Hearts', '7 Of Hearts', '6 Of Hearts', '5 Of Hearts', '4 Of Hearts', '3 Of Hearts', '2 Of Hearts', 'Ace Of Hearts',
           'King Of Spades', 'Queen Of Spades', 'Jack Of Spades', '10 Of Spades', '9 Of Spades', '8 Of Spades', '7 Of Spades', '6 Of Spades', '5 Of Spades', '4 Of Spades',
           '3 Of Spades', '2 Of Spades', 'Ace Of Spades', 'King Of Clubs', 'Queen Of Clubs', 'Jack Of Clubs', '10 Of Clubs', '9 Of Clubs', '8 Of Clubs', '7 Of Clubs',
           '6 Of Clubs', '5 Of Clubs', '4 Of Clubs', '3 Of Clubs', '2 Of Clubs', 'Ace Of Clubs', 'King Of Diamonds', 'Queen Of Diamonds', 'Jack Of Diamonds', '10 Of Diamonds',
           '9 Of Diamonds', '8 Of Diamonds', '7 Of Diamonds', '6 Of Diamonds', '5 Of Diamonds', '4 Of Diamonds', '3 Of Diamonds', '2 Of Diamonds', 'Ace Of Diamonds']
def shuffle():
    rand= 0
    shuf= 0
    while shuf < 416:
        rand= random.randint(0, 415)
        shuf= shuf+1
        if rand not in shufdeck:
            shufdeck.append(rand)
            print(str(len(shufdeck))+' Cards Shuffled')
        else:
            rand= random.randint(0, 415)
            shuf= shuf-1

def deal():
    playordeal=0
    dealtcard= ''
    global currCard
    for x in range(4):
        dealtcard= deck[shufdeck[currCard]]
        if playordeal == 0:
            hand1.append(dealtcard)
            playordeal= 1
        else:
            handD.append(dealtcard)
            playordeal= 0
        currCard= currCard+1
def get_value():
    global prin
    global hand1
    global handD
    global hand1s
    global handDs
    global hand1A
    global handDA
    global dealt
    global forp
    global dealp
    global dealb
    global playb
    global playbb
    hand1s= 0
    handDs= 0
    hand1A= 0
    handDA= 0
    hand1s= 0
    handDs= 0
    countC = 0
    hands=[]
    hands.append(hand1)
    hands.append(handD)
    
    for cardpair in hands:
        countC= countC+1
        for card in cardpair:
            if countC == 1:
                if card[0] in ('1', 'Q', 'K', 'J'):
                    hand1s= hand1s+10
                elif card[0] == 'A':
                    hand1s= hand1s+11
                    hand1A= hand1A+1
                else:
                    hand1s= hand1s+int(card[0])
            if countC == 2:
                if card[0] in ('1', 'Q', 'K', 'J'):
                    handDs= handDs+10
                elif card[0] == 'A':
                    if handDs > 10:
                        handDs= handDs+1
                    else:
                        handDs= handDs+11
                        handDA= handDA+1
                else:
                    handDs= handDs+int(card[0])
            if countC == 3:
                pass 
    while hand1A > 0:
        if hand1s > 21:
            hand1s=hand1s-10
            hand1A=hand1A-1
        elif hand1s == 21 and dealt==0:
            playb=1
            playbb=1
            prin=1
            blackjack()
            break
        else:
            break
    if hand1s == 21:
        playb=1
        prin=1
        forped()
    if forp == 0:
        if hand1s > 21:
            hand1s= 0
            prin=1
            playb=1
            playbust()
    while handDA > 0:
        if handDs > 21:
            handDs=handDs-10
            handDA=handDA-1
        elif handDs == 21 and dealt == 0:
            dealb=1
            forp=1
            prin=1
            blackjack()
            break
        elif handDs >= 17:
            dealp=1
            break
        else:
            break
    if handDs == 21:
        dealp=1
    if handDs >= 17:
        dealp=1
        pass
    if handDs > 21:
        handDs= 0
        dealp=1
    if prin==0:  
        if (forp == 0 or playb == 0) and dealt == 1:
            print("Dealer's Cards: Showing The "+str(handD[0]))
            print("Your Hand: The "+str(hand1))
            if hand1s == 0:
                print("Your Hand Values: Hand Busts")
            else:
                print("Your Hand Values: "+str(hand1s))
            
        if (forp == 1 or playb == 1) and dealt == 1:
            print("Dealer's Cards: "+str(handD))
            if handDs == 0:
                print("Dealer's Cards: Hand Busts")
            else:
                print("Your Hand Values: "+str(handDs))
            print("Your Hand: "+str(hand1))
            if hand1s == 0:
                print("Your Hand Values: Hand Busts")
            else:
                print("Your Hand Values: "+str(hand1s))
            
        if (forp == 0 or playb == 0) and dealt == 0:
            print("Dealer's Cards: Showing The "+str(handD[0]))
            print("Your Hand: The "+str(hand1[0])+' and The '+str(hand1[1]))
            if hand1s == 0:
                print("Your Hand Values: Hand Busts")
            else:
                print("Your Hand Values: "+str(hand1s))
            dealt= 1

def blackjack():
    global hand1
    global handD
    global hand1s
    global handDs
    global hand1A
    global handDA
    global dealt
    global forp
    global dealp
    global dealb
    global playbb
    if playbb == 1 and dealb == 0:
        print("Dealer's Cards: "+str(handD))
        print("Dealer's Hand Value: "+str(handDs))
        print("Your Hand: "+str(hand1))
        print("Your Hand Values: Blackjack")
        print(' - '*25)
        print('You Have Blackjack, Congrats.')
        return
    if playbb == 1 and dealb == 1:
        print("Dealer's Cards: "+str(handD))
        print("Dealer's Hand Value: Blackjack")
        print("Your Hand: "+str(hand1))
        print("Your Hand Values: Blackjack")
        print(' - '*25)
        print('Pushed Blackjacks, Rare Outcome.')
        return
    if playbb == 0 and dealb == 1:
        print("Dealer's Cards: "+str(handD))
        print("Dealer's Hand Value: Blackjack")
        print("Your Hand: "+str(hand1))
        print("Your Hand Values: "+str(hand1s))
        print(' - '*25)
        print('Dealer Blackjack, Bad Luck.')
        return
def hit1():
    global dealt
    global forp
    global playb
    global double
    global hand1
    global handD
    global hand1s
    global handDs
    global hand1A
    global handDA
    global currCard
    global deck
    global shufdeck
    if playb == 0:
        hand1.append(deck[shufdeck[currCard]])
        currCard= currCard+1

def hitD():
    global dealt
    global forp
    global dealp
    global playb
    global double
    global hand1
    global handD
    global hand1s
    global handDs
    global hand1A
    global handDA
    global currCard
    global deck
    global shufdeck
    if dealp == 0 and playb == 0:
        handD.append(deck[shufdeck[currCard]])
        currCard= currCard+1

def playbust():
    global forp
    global playb
    global playbb
    global dealp
    global dealt
    global hand1
    global handD
    global hand1s
    global handDs
    global prin
    forp=1
    prin=1
    print("Dealer's Cards: "+str(handD))
    print("Dealer's Hand Value: "+str(handDs))
    print("Your Hand: "+str(hand1))
    print("Your Hand Values: Hand Busts")
    print(' - '*25)
    print('You loss, Bad Luck.')
    return
def forped():
    global forp
    global playb
    global playbb
    global dealp
    global dealt
    global hand1
    global handD
    global hand1s
    global handDs
    global prin
    forp=1
    prin=1
    if dealp == 0 or playb == 0:
        while dealp == 0:
            if playb==1:
                break
            else:
                hitD()
                get_value()
    else:
        get_value()
    print(' - '*25)
    print(' - '*25)
    print(' - '*25)
    print("Dealer's Cards: "+str(handD))
    if handDs == 0:
        print("Dealer's Cards: Hand Busts")
    else:
        print("Your Hand Values: "+str(handDs))
    print("Your Hand: "+str(hand1))
    if hand1s == 0:
        print("Your Hand Values: Hand Busts")
    else:
        print("Your Hand Values: "+str(hand1s))
    print(' - '*25)
    if int(hand1s) > int(handDs):
        print('You Won, Congrats!')
    elif int(hand1s)+playbb == int(handDs)+dealb:
        print('You Pushed Dealer, Tied Hands.')        
    else:
        print('You loss, Bad Luck.')
    return
def play():
    import time
    global double
    global currCard
    global handD
    global playb
    global playbb
    global dealb
    global info
    global forp
    hitl=('y','Y','yes','Yes','yeah','Yeah','h','H','hit','Hit','p','P','play','Play')
    foldl=('n','N','no','No','nah','Nah','f','F','fold','Fold','pass','Pass')
    if info ==0:
        hitl=('y','Y','yes','Yes','yeah','Yeah','h','H','hit','Hit','p','P','play','Play')
        foldl=('n','N','no','No','nah','Nah','f','F','fold','Fold','pass','Pass')
        print(' - '*25)
        print('To hit, the accepted values are: y, Y, yes, Yes, yeah, Yeah, h, H, hit, Hit, p, P, play, and Play.')
        print('To fold, the accepted values are: n, N, no, No, nah, Nah, f, F, fold, Fold, pass, and Pass')
        #print('To double, the accepted values are: u, U, up, Up, d, D, double, Double, down, Down, double down, Double Down')
        print(' - '*25)
        info=1
        input('Understood? Input anything to continue. ')
        shuffle()
        deal()
        if playbb==0 and dealb==0:
            get_value()
    if playbb==0 and dealb==0:
        call= input("What's the call? ")
    if call.strip() in hitl:
        print(' - '*25)
        hit1()
        get_value()
        time.sleep(1)
        if forp == 0 and playb == 0 and playbb == 0:
            play()
        
    if call.strip() in foldl:
        forped()
play()
