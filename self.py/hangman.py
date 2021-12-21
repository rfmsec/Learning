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
if len(gussed_letter) == 1:
    if gussed_letter.lower() in 'abcdefghijqlmnopqrstuvwxyz':
        print(gussed_letter.lower())
    else:
        print("E2")
else:
    ENGLISH_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    not_english = False
    for letter in gussed_letter.lower():
        if letter in ENGLISH_LETTERS:
            pass
        else:
            not_english = True
    print("E3" if not_english else "E1")