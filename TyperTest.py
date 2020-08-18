import curses

def ReadyForExit():
	curses.echo()
	stdscr.keypad(False)
	curses.nocbreak()
	curses.endwin()

def redrawString(): 
	map_colors = {
		'green': 2,
		'red': 1
	}
	win.erase()
	for i in range(0, len(characters_typed)):
		win.addch(characters_typed[i][0], curses.color_pair(map_colors.get(characters_typed[i][1])))
	for i in range(len(characters_typed), len(string_to_type)):
		win.addch(string_to_type[i], curses.color_pair(3))


def main():
	global characters_typed
	global stdscr
	global win
	global currentPos
	global string_to_type
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

	window_height=30
	window_width=130

	# Window starts in upper left hand corner.

	window_startx=int((curses.LINES / 2)-(window_height/2))
	window_starty=int((curses.COLS/2)-(window_width/2))
	win=curses.newwin(window_height, window_width, window_startx, window_starty)
	stdscr.border(0)
	string_to_type="""A few words about Dostoevsky himself may help the English reader to understand his work.
Dostoevsky was the son of a doctor. His parents were very hard-working and deeply religious people, but so poor that they lived with their five children in only two rooms. The father and mother spent their evenings in reading aloud to their children, generally from books of a serious character.
Though always sickly and delicate Dostoevsky came out third in the final examination of the Petersburg school of Engineering. There he had already begun his first work, “Poor Folk.”
This story was published by the poet Nekrassov in his review and was received with acclamations. The shy, unknown youth found himself instantly something of a celebrity. A brilliant and successful career seemed to open before him, but those hopes were soon dashed. In 1849 he was arrested. """

	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
	redrawString()
	
	while True:
		key = win.getkey()
		if key == '':
			ReadyForExit()
			print(characters_typed)
			exit(1)
		elif key == '':
			if currentPos==0:
				pass
			else:
				currentPos-=1
				characters_typed.pop()
			redrawString()

		elif key == string_to_type[currentPos]:
			characters_typed.append((key, "green"))
			redrawString()
			currentPos+=1
		else:
			characters_typed.append((key, "red"))
			redrawString()
			currentPos+=1

		if currentPos == len(string_to_type):
			ReadyForExit()
			exit(0)

	ReadyForExit()
	print(characters_typed)
	exit(0)


if __name__ == "__main__":
	main()
