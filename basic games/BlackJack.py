import random
            
class Cards:
    
    deck = [('A',11,1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('K',10),('Q',10),('J',10)]*4

    def __init__(self):
        random.shuffle(Cards.deck)
        
    def stand(self):
        pass
    

class Play(Cards):
    
    player_cards = []
    computer_cards = []
    
    def __init__(self):
        Cards.__init__(self)
    
    def player_hit(self):
        hit_card = random.choice(Cards.deck)
        Play.player_cards.append(hit_card)
        Cards.deck.remove(hit_card)
        return hit_card
    
    def computer_hit(self):
        hit_card = random.choice(Cards.deck)
        Play.computer_cards.append(hit_card)
        Cards.deck.remove(hit_card)
        return hit_card
    
    def player_hand(self):
        return Play.player_cards
    
    def computer_hand(self):
        return Play.computer_cards
    
    def restart(self):
        Play.player_cards = []
        Play.computer_cards = []
        Cards.deck = [('A',11,1),('2',2),('3',3),('4',4),('5',5),('6',6),('7',7),('8',8),('9',9),('K',10),('Q',10),('J',10)]*4

class Player:
    
    def __init__(self,num):
        self.num = num
        print(f'You have {self.num} credits!')
        
    def bet(self,amt):
        if amt <= self.num:
            print(f'Your bet is {amt} credits')
            self.num = self.num - amt
            print(f'Your balance is {self.num} credits')
        else: 
            print('Insufficient credits!')
        
    def win(self,cash):
        self.num = self.num + (2 * cash)
        print('You have won!')
        print(f'Your balance  is {self.num} credits')
    
    def loss(self,cash):
        print('You have lost!')
        print(f'Your balance  is {self.num} credits')
        
    def push(self,cash):
        print('PUSH!')
        self.num = self.num + cash
        print(f'Your balance  is {self.num} credits')
    
    def game_over(self):
        over = input('Do you want to continue playing? y/n: \n')
        if self.num<=0 or over == 'n':
            print('Game Over!')
            return True
        return False
        
def win_condition_comp(p_hand):
    p_total = 0
    for item in p_hand:
        p_total = p_total + item[1]
    for item in p_hand:
        if item[0] == 'A' and p_total > 21:
            p_total = p_total - 10 
        
    if p_total > 21:
        print('The computer has won!')
        print(p_hand)
        print(f'Your total is {p_total}')
        return True
    return False

def win_condition_player(p_hand,c_hand):
    p_total = 0
    c_total = 0
    for item in p_hand:
        p_total = p_total + item[1]
    while ('A',11,1) in p_hand and p_total > 21:
        p_total = p_total - 10
        p_hand.remove(('A',11,1))
    for item in c_hand:
        c_total = c_total + item[1]
    while ('A',11,1) in c_hand and c_total > 21:
        c_total = c_total + 10
        c_hand.remove(('A',11,1))
        while True:
            for item in c_hand:
                c_total = c_total + item[1]
            if c_total <= 17:
                play.computer_hit()
            else:
                break
    if c_total > 21 or p_total >= c_total:
        print('The player has won!')
        print(p_hand)
        print(f'Your total is {p_total}')
        print(c_hand)
        print(f'Computer total is {c_total}')
        return True
    elif p_total > 21 or c_total > p_total:
        print('The computer has won!')
        print(p_hand)
        print(f'Your total is {p_total}')
        print(c_hand)
        print(f'Computer total is {c_total}')
        return False

print('Welcome to BlackJack \n')
print('--------------- \n')

def game():
    play = Play()
    credits = int(input('Enter the amount of money you want credits for: \n'))
    player = Player(credits)
    cont = True
    while cont:
        cont = False
        play.restart()
        b = int(input('How much do you want to bet? \n'))
        player.bet(b)
        play.player_hit()
        play.computer_hit()
        play.player_hit()
        play.computer_hit()
        p = play.player_hand()
        c = play.computer_hand()
        print(f'Your initial hand is {p}')
        print(f'The computer hand is {c[0]}')
        w = False
        while True:
            ch = input('Do you want to hit or stand? \n')
            if ch.lower() == 'hit':
                play.player_hit()
                if win_condition_comp(play.player_hand()):
                    w = win_condition_comp(play.player_hand())
                    player.loss(b)
                    break
                print('Your hand is: ')
                print(play.player_hand())
                continue
            elif ch.lower() == 'stand':
                play.stand()
                print('Your hand is: ')
                print(play.player_hand())
                break
        
        while True and not w:
            c_total = 0
            for item in play.computer_hand():
                c_total = c_total + item[1]
            if c_total <= 17:
                play.computer_hit()
                print('The computer hand is: ')
                print(play.computer_hand())
            else:
                break
        w2 = None
        if not w:
            w2 = win_condition_player(play.player_hand(),play.computer_hand())
        
        if w2 == True:
            player.win(b)
        elif w2 == False:
            player.loss(b)
        
        if not player.game_over():
            cont = True
               
game()

    