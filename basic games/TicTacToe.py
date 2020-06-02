#function to print the board 
def printBoard(ipList=[' ']*10):
    print(f' {ipList[7]} | {ipList[8]} | {ipList[9]} ')
    print('-----------')
    print(f' {ipList[4]} | {ipList[5]} | {ipList[6]} ')
    print('-----------')
    print(f' {ipList[1]} | {ipList[2]} | {ipList[3]} ')

#welcome message and instructions
print('Welcome to TicTacToe! \n')
print('I\u0332n\u0332s\u0332t\u0332r\u0332u\u0332c\u0332t\u0332i\u0332o\u0332n\u0332s\u0332: \n')
print('This game can be played by two players on the same computer! \n')
print("You can choose either 'X' or 'O' as your character. \n")
print('When your turn comes press the number corresponding to the below layout to place your character at that position. \n')
printBoard(list(range(0,10)))

#function to check if the character selected by the player is valid
def checkInput(char):
    return char in ['X','x','o','O']

#choosing the characters
p1 = input('Player 1, which character do you choose? X/O? \n')
while checkInput(p1) == False:
    print('Invalid Character \n')
    p1 = input('Player 1, please choose a valid character! X/O? \n')
if p1 in ['x','X']:
    p1 = 'X'
    p2 = 'O'
else:
    p1 = 'O'
    p2 = 'X'
print(f'Player 1 is {p1} and Player 2 is {p2}\n')

#initializing the global variables
turn = 1
ipList = [' ']*10
ipList[0] = 'a'
winner = []

#function to get the input position from the user
def play():
    global turn
    if turn%2 != 0:
        index = int(input('Player 1, where do you wanna place your character? \n'))
        if ipList[index] == ' ':
        	ipList[index] = p1
        	printBoard(ipList)
        else:
        	print('Enter a different position')
        	turn = turn-1
    else:
        index = int(input('Player 2, where do you wanna place your character? \n'))
        if ipList[index] == ' ':
        	ipList[index] = p2
        	printBoard(ipList)
        else:
        	print('Enter a different position')
        	turn = turn-1
    turn = turn+1

#function to determine if either player has won
def winCondition(ipList = [' '] *10):
    for x,y,z in zip(ipList[1::3],ipList[2::3],ipList[3::3]):
        if x==y and x==z and x in ['X','O']:
            winner.append(x)
            return True
    for x,y,z in zip(ipList[1:4],ipList[4:7],ipList[7:10]):
        if x==y and x==z and x in ['X','O']:
            winner.append(x)
            return True
    temp1 = ipList[1::4]
    temp2 = ipList[3:8:2]
    if temp1 == ['X']*3 or temp2 == ['X']*3:
        winner.append('X')
    elif temp1 == ['O']*3 or temp2 == ['O']*3:
        winner.append('O')
    return temp1 == ['X']*3 or temp1 == ['O']*3 or temp2 == ['X']*3 or temp2 == ['O']*3        

#function to check if the player wants to restart
def restart():
    r = input('Do you want to restart the game? y/n? \n')
    return r=='y'
    
#function which integrates all the previously defined functions and runs the game
def runGame():
    global turn,ipList
    while winCondition(ipList) == False and ' ' in ipList:
        play()
    if winCondition(ipList) == True:
        print('We have a winner! \n')
        if p1 in winner:
            print('The winner is Player 1! \n')
        elif p2 in winner:
            print('The winner is Player 2! \n')
    elif winCondition(ipList) == False and ' ' not in ipList:
        print('It is a draw match! \n')
    ipList = [' ']*10
    ipList[0] = 'a'
    turn = 1
    r = restart()
    if r == True:
    	runGame()
    elif r == False:
        print('Thanks for playing the game!')

#calling the runGame function to start the game
runGame()