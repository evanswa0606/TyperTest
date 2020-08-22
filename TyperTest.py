import curses
def ReadyForExit():
	curses.echo()
	stdscr.keypad(False)
	curses.nocbreak()
	curses.endwin()

def redrawString(): 
	win.erase()
	for i in range(0, len(characters_typed)):
		win.addch(string_to_type[i], curses.color_pair(characters_typed[i]))
	win.addch(string_to_type[len(characters_typed)], curses.A_UNDERLINE)
	for i in range(len(characters_typed)+1, len(string_to_type)):
		win.addch(string_to_type[i], curses.color_pair(3))


def main():
	global characters_typed
	global stdscr
	global win
	global currentPos
	global string_to_type
	global accuracy_win
	characters_typed=[] 
	currentPos=0
	keysTyped=""
	stdscr=curses.initscr()

	try:
		curses.start_color()
	except:
		print("Your terminal does not support colors by the curses library.")
		ReadyForExit()
		exit(0)

	curses.noecho()
	stdscr.keypad(True)
	curses.cbreak()
	curses.curs_set(0)
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)

	window_height=30
	window_width=130

	# Window starts in upper left hand corner.

	window_startx=int((curses.LINES / 2)-(window_height/2))
	window_starty=int((curses.COLS/2)-(window_width/2))
	win=curses.newwin(window_height, window_width, window_startx, window_starty)

	win.border(0)

	outer_window_height=32
	outer_window_width=132

	outer_window_startx=int((curses.LINES/2)-(outer_window_height/2))
	outer_window_starty=int((curses.COLS/2)-(outer_window_width/2))

	outer_window=curses.newwin(outer_window_height,outer_window_width,outer_window_startx,outer_window_starty)
	outer_window.border(0)
	outer_window.addch('h')

	accuracy_win_startx=window_startx+window_width+5
	accuracy_win_starty=window_starty+window_height+5
	# The word accuracy is 8 chars long, plus a space, plus 3 digits max
	
	stdscr.border(0)
	string_to_type="It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him."
	redrawString()
	
	while True:
		key = win.getkey()
		if key == '':
			ReadyForExit()
			exit(1)
		elif key == '':
			if currentPos==0:
				pass
			else:
				currentPos-=1
				characters_typed.pop()
			redrawString()

		elif key == string_to_type[currentPos]:
			characters_typed.append(2)
			if currentPos==len(string_to_type)-1:
				ReadyForExit()
				exit(0)
			redrawString()
			currentPos+=1
		else:
			characters_typed.append(1)
			if currentPos==len(string_to_type)-1:
				ReadyForExit()
				exit(0)
			redrawString()
			currentPos+=1


	ReadyForExit()
	exit(0)


if __name__ == "__main__":
	main()
