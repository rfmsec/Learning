HANGMAN_ASCII_ART = """Welcome to the game Hangman
  _    _                                         
 | |  | |                                        
 | |__| | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 |  __  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 | |  | | (_| | | | | (_| | | | | | | (_| | | | |
 |_|  |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/"""

MAX_TRIES = 6

STRIKE1 = ("""    x-------x""")

STRIKE2 = ("""    x-------x
    |
    |
    |
    |
    |""")

STRIKE3 = ("""    x-------x
    |       |
    |       0
    |
    |
    |""")

STRIKE4 = ("""    x-------x
    |       |
    |       0
    |       |
    |
    |""")

STRIKE5 = ("""    x-------x
    |       |
    |       0
    |      /|\
    |
    |""")

STRIKE6 = ("""    x-------x
    |       |
    |       0
    |      /|\
    |      /
    |""")

STRIKE7 = ("""    x-------x
    |       |
    |       0
    |      /|\
    |      / \
    |""")

print(HANGMAN_ASCII_ART)
print(MAX_TRIES)
gussed_letter = input("Guess a letter: ")
print(gussed_letter).lower()
