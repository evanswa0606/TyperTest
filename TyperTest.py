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

	window_height=30
	window_width=130

	# Window starts in upper left hand corner.

	window_startx=int((curses.LINES / 2)-(window_height/2))
	window_starty=int((curses.COLS/2)-(window_width/2))
	win=curses.newwin(window_height, window_width, window_startx, window_starty)
	stdscr.border(0)
	string_to_type="""On the 24th of February, 1815, the look-out at Notre-Dame de la Garde signalled the three-master, the Pharaon from Smyrna, Trieste, and Naples. As usual, a pilot put off immediately, and rounding the Château d’If, got on board the vessel between Cape Morgiou and Rion island. Immediately, and according to custom, the ramparts of Fort Saint-Jean were covered with spectators; it is always an event at Marseilles for a ship to come into port, especially when this ship, like the _Pharaon_, has been built, rigged, and laden at the old Phocee docks, and belongs to an owner of the city. The ship drew on and had safely passed the strait, which some volcanic shock has made between the Calasareigne and Jaros islands; had doubled Pomègue, and approached the harbor under topsails, jib, and spanker, but so slowly and sedately that the idlers, with that instinct which is the forerunner of evil, asked one another what misfortune could have happened on board. However, those experienced in navigation saw plainly that if any accident had occurred, it was not to the vessel herself, for she bore down with all the evidence of being skilfully handled, the anchor a-cockbill, the jib-boom guys already eased off, and standing by the side of the pilot, who was steering the _Pharaon_ towards the narrow entrance of the inner port, was a young man, who, with activity and vigilant eye, watched every motion of the ship, and repeated each direction of the pilot.""" 
	curses.init_pair(1, curses.COLOR_RED, curses.COLOR_BLACK)
	curses.init_pair(2, curses.COLOR_GREEN, curses.COLOR_BLACK)
	curses.init_pair(3, curses.COLOR_WHITE, curses.COLOR_BLACK)
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
			characters_typed.append((key, "green"))
			if currentPos==len(string_to_type)-1:
				ReadyForExit()
				exit(0)
			redrawString()
			currentPos+=1
		else:
			characters_typed.append((key, "red"))
			if currentPos==len(string_to_type)-1:
				ReadyForExit()
				exit(0)
			redrawString()
			currentPos+=1


	ReadyForExit()
	exit(0)


if __name__ == "__main__":
	main()
