import curses
import pickle
import random
import time
from curses import textpad

menu = ['Play', 'Exit']
exit_con = False

try:
    filename = 'HighScore'
    infile = open(filename,'rb')
    score_list = pickle.load(infile)
    infile.close()
except FileNotFoundError:
    score_list = [0]

def print_menu(stdscr, current_row_idx):
	curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
	height,width = stdscr.getmaxyx()
	for idx,item in enumerate(menu):
		if idx == current_row_idx:
			stdscr.attron(curses.color_pair(1))
			stdscr.addstr(height//2 + idx, width//2 - len(item), item)
			stdscr.attroff(curses.color_pair(1))
		else:
			stdscr.addstr(height//2 + idx, width//2 - len(item), item)
	stdscr.refresh()
	

def act_menu(stdscr,current_row_idx):
	if menu[current_row_idx] == 'Play':

		stdscr.clear()
		def food(box,snake_body):
			y = random.randint(box[0][0]+1, box[1][0]-1)
			x = random.randint(box[0][1]+1, box[1][1]-1)
			food_location = [y,x]
			while food_location in snake_body:
				food(box,snake_head)   
			return food_location

		def main1(stdscr):
			global score_list
			curses.curs_set(0)
			stdscr.nodelay(1)
			stdscr.timeout(100)

			curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
			curses.init_pair(2, curses.COLOR_WHITE, curses.COLOR_BLACK)

			height , width = stdscr.getmaxyx()
			box = [[3,3],[height-3,width-3]]
			textpad.rectangle(stdscr, box[0][0], box[0][1], box[1][0], box[1][1])

			snake_body = [ [height//2,width//2+1] , [height//2,width//2] , [height//2,width//2-1] ]
			direction = curses.KEY_RIGHT


			stdscr.attron(curses.color_pair(1))
			stdscr.addch(snake_body[0][0], snake_body[0][1], curses.ACS_DIAMOND)
			stdscr.attroff(curses.color_pair(1))


			stdscr.attron(curses.color_pair(2))
			for item in snake_body[1:]:
				stdscr.addch(item[0], item[1], curses.ACS_DIAMOND)
			stdscr.attroff(curses.color_pair(2))

			welcome_text = 'Welcome to SNAKE game!'
			stdscr.addstr(1,width//2 - len(welcome_text)//2, welcome_text)

			score = 0
			score_text = "Score: {}".format(score)
			stdscr.addstr(2, width - len(score_text) - 5, score_text)

			high_score_text = "High Score: {}".format(score_list[0])
			stdscr.addstr(2, 5, high_score_text)

			food_location = food(box,snake_body)
			stdscr.addch(food_location[0],food_location[1],curses.ACS_LANTERN)

			while True:

				key = stdscr.getch()
				if key in [curses.KEY_RIGHT, curses.KEY_LEFT, curses.KEY_DOWN, curses.KEY_UP]:
					direction = key
        
				snake_head = snake_body[0] 

				if direction == curses.KEY_RIGHT:
					snake_head = [snake_body[0][0], snake_body[0][1]+1]
				elif direction == curses.KEY_LEFT:
					snake_head = [snake_body[0][0], snake_body[0][1]-1]
				elif direction == curses.KEY_UP:
					snake_head = [snake_body[0][0]-1, snake_body[0][1]]
					time.sleep(0.01)
				elif direction == curses.KEY_DOWN:
					snake_head = [snake_body[0][0]+1, snake_body[0][1]]
					time.sleep(0.01)

				stdscr.attron(curses.color_pair(1))
				stdscr.addch(snake_head[0], snake_head[1], curses.ACS_DIAMOND)
				stdscr.attroff(curses.color_pair(1))
				snake_body.insert(0,snake_head)

				if snake_head == food_location:
					score += 1
					score_text = "Score: {}".format(score)
					stdscr.addstr(2, width - len(score_text) - 5, score_text)

					food_location = food(box,snake_body)
        
					stdscr.addch(food_location[0],food_location[1],curses.ACS_LANTERN)
            
				else:
					stdscr.addch(snake_body[-1][0], snake_body[-1][1], ' ')
					snake_body.pop()

				stdscr.attron(curses.color_pair(2))
				for item in snake_body[1:]:
					stdscr.addch(item[0], item[1], curses.ACS_DIAMOND)
				stdscr.attroff(curses.color_pair(2))

				if snake_body[0][0] in [box[0][0], box[1][0]] or snake_body[0][1] in [box[0][1], box[1][1]] or snake_body[0] in snake_body[1:]:
					score_list.append(score)
					score_list.sort()
					temp = [score_list[-1]]
					score_list = temp
					if score in score_list:
						stdscr.addstr(height//2, width//2 - len('Congrats! You got the High Score!')//2, 'Congrats! You got the High Score!')	
						over_text = 'GAME OVER!'
						stdscr.addstr(height//2 + 1, width//2 - len(over_text)//2, over_text)
						exit_text = 'Press Esc key to exit'
						stdscr.addstr(height//2 + 2, width//2 - len(exit_text)//2, exit_text)
					else:
						over_text = 'GAME OVER!'
						stdscr.addstr(height//2, width//2 - len(over_text)//2, over_text)
						exit_text = 'Press Esc key to exit'
						stdscr.addstr(height//2 + 1, width//2 - len(exit_text)//2, exit_text)
						
					stdscr.nodelay(0)
					ch = stdscr.getch()
					while ch != 27:
						ch = stdscr.getch()
					

					break
		curses.wrapper(main1)
		

def main(stdscr):
	global exit_con
	stdscr.clear()

	curses.curs_set(0)
	stdscr.box('|','-')


	height,width = stdscr.getmaxyx()

	th = height
	tw = width + 52

    #S
	stdscr.addch(th//4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4, curses.ACS_BLOCK)

	tw = tw + 24
	
	#N
	stdscr.addch(th//4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 4, curses.ACS_BLOCK)
	
	tw = tw + 24

	#A
	stdscr.addch(th//4, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 4, curses.ACS_BLOCK)

	tw = tw + 24

	#K
	stdscr.addch(th//4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 3, curses.ACS_BLOCK)
	
	tw = tw + 20

	#E
	stdscr.addch(th//4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 1, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 1 , curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 3, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 1, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 2, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 3, curses.ACS_BLOCK)
	stdscr.addch(th//4, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 2, tw//4 + 4, curses.ACS_BLOCK)
	stdscr.addch(th//4 + 4, tw//4 + 4, curses.ACS_BLOCK)
	
	

	current_row = 0

	print_menu(stdscr, current_row)

	while True:

		key = stdscr.getch()

		if key == curses.KEY_UP and current_row > 0:
			current_row -= 1
		elif key == curses.KEY_DOWN and current_row < len(menu) - 1:
			current_row += 1
		elif key == 10 or key == 13 or key == curses.KEY_ENTER:
			if current_row == 0:
				act_menu(stdscr,current_row)
				break
			elif current_row == len(menu)-1:
				exit_con = True
				break
		print_menu(stdscr, current_row)



while exit_con == False:
	curses.wrapper(main)

filename = 'HighScore'
outfile = open(filename,'wb')
pickle.dump(score_list,outfile)
outfile.close()