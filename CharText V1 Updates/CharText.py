"""
Character Text and Graphics
Supports The Mark of a Hero versions 0.12.2 and below
"""
confirm = input("\nCharText:"
                "\nThis version of CharText supports TMoaH version 0.12.2 and below.\n\n\n")


class Sys:
    """System messages"""
    s000 = ("\n  vvvvvvvvv"
            "\n> Caution!! <"
            "\n  ^^^^^^^^^\n"
            "\nThis game is built with the font 'Consolas' in mind. Without it can cause some missing textures and size"
            "\nproblems. If 'Consolas' is unavailable, try to find a suitable monospaced font that works the best.\n"
            "\nTest: ﬓﬔﬕﬖ█▓▒░■□Ξ‼⌠⌡╭╮╰╯─│┌┐└┘├┤┬┴┼╌╬━┃┏┓┗┛┣┫┳┻╋ḻᶸλɅ‗ᴜ≥ꞈ╷╴"
            "\n      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"
            "\nCheck that each character aligns with each arrow."
            "\nif any of these characters appear as question mark,"
            "\nor the characters don't align with the arrow, please use a different font"
            "\nIf everything looks okay, then..."
            "\n⌠Press enter to continue...⌡")
    qq00 = "You completed '{}'"  # add name
    q000 = "You got a new quest! You can view your quest log by pressing {}!"  # add key layout in main program
    q001 = "Get 'Clear Leaf' from Ravia"
    i000 = "You got an item! You can view your items by pressing {}!"
    i001 = "Clear Leaf"
    i002 = "Blunt Stick"


class Firay:
    """Golden Retriever"""
    """facial expression"""
    # normal
    e000 = "╭─────╮"
    e001 = "│ __  │"
    e002 = "│⌡| |_│"
    e003 = "│   _/├────────────────────────────────╮"
    e004 = "│   \ │ Firay                          │"
    # Mhm
    e010 = "╭─────╮"
    e011 = "│ __  │"
    e012 = "│⌡ᴜ ᴜ_│"
    e013 = "│   _/├────────────────────────────────╮"
    e014 = "│   \ │ Firay                          │"
    # suspicious
    e020 = "╭─────╮"
    e021 = "│ __  │"
    e022 = "│⌡ᴛ ᴛ_│"
    e023 = "│   _/├────────────────────────────────╮"
    e024 = "│   \ │ Firay                          │"
    # thinking
    e030 = "╭─────╮"
    e031 = "│ __  │"
    e032 = "│⌡- -_│"
    e033 = "│   _/├────────────────────────────────╮"
    e034 = "│   \ │ Firay                          │"
    # exhausted
    e040 = "╭─────╮"
    e041 = "│ __  │"
    e042 = "│⌡≥ ḻ_│"
    e043 = "│ᶸ  _/├────────────────────────────────╮"
    e044 = "│   \ │ Firay                          │"
    # slightly confused/not amused
    e050 = "╭─────╮"
    e051 = "│ __  │"
    e052 = "│⌡| ᴛ_│"
    e053 = "│   _/├────────────────────────────────╮"
    e054 = "│   \ │ Firay                          │"
    """Talking"""
    # Low stamina
    t005 = "├─────┴────────────────────────────────┤"
    t006 = "│ Can't do this forever...             │"
    t007 = "│ Maybe after a little rest would do.. │"
    t008 = "│                                      │"
    t009 = "└─────┤Press Enter to Continue...├─────┘"
    # interacting with Rubi in home
        # Getting quest "get clear leaf"
    t000 = "├─────┴────────────────────────────────┤"
    t001 = "│ Yup~!                                │"
    t002 = "│                                      │"
    t003 = "│                                      │"
    t004 = "└────────────────┤....├────────────────┘"
    t030 = "├─────┴────────────────────────────────┤"
    t031 = "│ ...?                                 │"
    t032 = "│                                      │"
    t033 = "│                                      │"
    t034 = "└────────────────┤....├────────────────┘"
    t040 = "├─────┴────────────────────────────────┤"
    t041 = "│ Yup!.....                            │"
    t042 = "│ wait... where was Ravia's house?     │"
    t043 = "│ I can't remember..                   │"
    t044 = "└────────────────┤....├────────────────┘"
        # finishing quest "get clear leaf"
    t070 = "├─────┴────────────────────────────────┤"
    t071 = "│ Got the leaf!...                     │"
    t072 = "│ What's it for?                       │"
    t073 = "│                                      │"
    t074 = "└────────────────┤....├────────────────┘"
    t080 = "├─────┴────────────────────────────────┤"
    t081 = "│ What's a 'spirit page'?              │"
    t082 = "│                                      │"
    t083 = "│                                      │"
    t084 = "└────────────────┤....├────────────────┘"
    t090 = "├─────┴────────────────────────────────┤"
    t091 = "│ Huh..                                │"
    t092 = "│                                      │"
    t093 = "│                                      │"
    t094 = "└────────────────┤....├────────────────┘"
    t100 = "├─────┴────────────────────────────────┤"
    t101 = "│ ........?                            │"
    t102 = "│                                      │"
    t103 = "│                                      │"
    t104 = "└────────────────┤....├────────────────┘"
    t110 = "├─────┴────────────────────────────────┤"
    t111 = "│ Yup!                                 │"
    t112 = "│                                      │"
    t113 = "│                                      │"
    t114 = "└─────┤Press Enter to Continue...├─────┘"
    # quest complete interaction
    t120 = "├─────┴────────────────────────────────┤"
    t121 = "│ I shouldn't disturb Rubi...          │"
    t122 = "│                                      │"
    t123 = "│                                      │"
    t124 = "└─────┤Press Enter to Continue...├─────┘"
    # interacting with John in home
    t010 = "├─────┴────────────────────────────────┤"
    t011 = "│ Hey John!                            │"
    t012 = "│ How's the morning been?              │"
    t013 = "│                                      │"
    t014 = "└────────────────┤....├────────────────┘"
    t020 = "├─────┴────────────────────────────────┤"
    t021 = "│ Do you just never talk?              │"
    t022 = "│                                      │"
    t023 = "│                                      │"
    t024 = "└────────────────┤....├────────────────┘"
    # interacting with Ravia
    t050 = "├─────┴────────────────────────────────┤"
    t051 = "│ I was wondering if you have any      │"
    t052 = "│ Clear Leaf to spare?                 │"
    t053 = "│                                      │"
    t054 = "└────────────────┤....├────────────────┘"
    t060 = "├─────┴────────────────────────────────┤"
    t061 = "│ What a coincidence!                  │"
    t062 = "│ I was going to ask to lend me one... │"
    t063 = "│ Rubi's favor actually.               │"
    t064 = "└────────────────┤....├────────────────┘"
    """Interacting"""
    # interacting with beds in home
    i000 = "├─────┴────────────────────────────────┤"
    i001 = "│ This is my bed...                    │"
    i002 = "│ It's where I sleep.                  │"
    i003 = "│                                      │"
    i004 = "└─────┤Press Enter to Continue...├─────┘"
    i010 = "├─────┴────────────────────────────────┤"
    i011 = "│ This is Rubi's bed...                │"
    i012 = "│ It's where she is supposed to sleep. │"
    i013 = "│                                      │"
    i014 = "└────────────────┤....├────────────────┘"
    i020 = "├─────┴────────────────────────────────┤"
    i021 = "│ That is... if she's not in middle of │"
    i022 = "│ something important...               │"
    i023 = "│ Like always..                        │"
    i024 = "└─────┤Press Enter to Continue...├─────┘"
    # interacting with table in home
    i030 = "├─────┴────────────────────────────────┤"
    i031 = "│ This is a table..                    │"
    i032 = "│ It's where me and Rubi eat..         │"
    i033 = "│                                      │"
    i034 = "└────────────────┤....├────────────────┘"
    i040 = "├─────┴────────────────────────────────┤"
    i041 = "│ Half of the table is usually         │"
    i042 = "│ occupied by non-food stuff such as   │"
    i043 = "│ magical candles and books.....       │"
    i044 = "└────────────────┤....├────────────────┘"
    i050 = "├─────┴────────────────────────────────┤"
    i051 = "│ *Sigh.*                              │"
    i052 = "│                                      │"
    i053 = "│                                      │"
    i054 = "└─────┤Press Enter to Continue...├─────┘"
    # interacting with lake/river in Mithavil
    i060 = "├─────┴────────────────────────────────┤"
    i061 = "│ I'd love to dive into the chilly     │"
    i062 = "│ water...                             │"
    i063 = "│                                      │"
    i064 = "└────────────────┤....├────────────────┘"
    i070 = "├─────┴────────────────────────────────┤"
    i071 = "│ But I can't.                         │"
    i072 = "│                                      │"
    i073 = "│                                      │"
    i074 = "└────────────────┤....├────────────────┘"
    i080 = "├─────┴────────────────────────────────┤"
    i081 = "│ Because I'd drown.                   │"
    i082 = "│                                      │"
    i083 = "│                                      │"
    i084 = "└─────┤Press Enter to Continue...├─────┘"
    # interacting with a table in Ravia's House
    i090 = "├─────┴────────────────────────────────┤"
    i091 = "│ It's a table...                      │"
    i092 = "│                                      │"
    i093 = "│                                      │"
    i094 = "└─────┤Press Enter to Continue...├─────┘"


class Rubi:
    """Samoyed"""
    """facial expression"""
    # normal
    e000 = "╭─────╮"
    e001 = "│λꞈꞈλ │"
    e002 = "│ | |ꞈ│"
    e003 = "│  ꞈꞈ/├────────────────────────────────╮"
    e004 = "│   \ │ Rubi                           │"
    # happy
    e010 = "╭─────╮"
    e011 = "│λꞈꞈλ │"
    e012 = "│ ᴖ ᴖꞈ│"
    e013 = "│  ꞈꞈ/├────────────────────────────────╮"
    e014 = "│   \ │ Rubi                           │"
    # slightly confused
    e020 = "╭─────╮"
    e021 = "│λꞈꞈλ │"
    e022 = "│ ᴛ |ꞈ│"
    e023 = "│  ꞈꞈ/├────────────────────────────────╮"
    e024 = "│   \ │ Rubi                           │"
    # irritated
    e030 = "╭─────╮"
    e031 = "│λꞈꞈλ │"
    e032 = "│ ᴛ ᴛꞈ│"
    e033 = "│  ꞈꞈ/├────────────────────────────────╮"
    e034 = "│   \ │ Rubi                           │"
    # meh
    e040 = "╭─────╮"
    e041 = "│λꞈꞈλ │"
    e042 = "│ - -ꞈ│"
    e043 = "│  ꞈꞈ/├────────────────────────────────╮"
    e044 = "│   \ │ Rubi                           │"
    """Talking"""
    # interacting with Firay in home
        # giving quest
    t000 = "├─────┴────────────────────────────────┤"
    t001 = "│ Good morning~                        │"
    t002 = "│ Had a good night sleep?              │"
    t003 = "│                                      │"
    t004 = "└────────────────┤....├────────────────┘"
    t010 = "├─────┴────────────────────────────────┤"
    t011 = "│ Lovely~                              │"
    t012 = "│ Now off with ya!                     │"
    t013 = "│                                      │"
    t014 = "└────────────────┤....├────────────────┘"
    t020 = "├─────┴────────────────────────────────┤"
    t021 = "│ ...!                                 │"
    t022 = "│ Wait!                                │"
    t023 = "│                                      │"
    t024 = "└────────────────┤....├────────────────┘"
    t030 = "├─────┴────────────────────────────────┤"
    t031 = "│ Could you get me a clear leaf for    │"
    t032 = "│ me? I think Raiva has some to spare. │"
    t033 = "│                                      │"
    t034 = "└────────────────┤....├────────────────┘"
    t040 = "├─────┴────────────────────────────────┤"
    t041 = "│ Her house should be the first house  │"
    t042 = "│ across the river...                  │"
    t043 = "│                                      │"
    t044 = "└────────────────┤....├────────────────┘"
    t050 = "├─────┴────────────────────────────────┤"
    t051 = "│ That is if she hasn't moved again    │"
    t052 = "│ because her house is 'haunted with   │"
    t053 = "│ ghosts of wind'...                   │"
    t054 = "└────────────────┤....├────────────────┘"
    t060 = "├─────┴────────────────────────────────┤"
    t061 = "│ Whatever that means..                │"
    t062 = "│ Now off you go!                      │"
    t063 = "│                                      │"
    t064 = "└─────┤Press Enter to Continue...├─────┘"
    t070 = "├─────┴────────────────────────────────┤"
    t071 = "│ Lovely day, ain't it?                │"
    t072 = "│                                      │"
    t073 = "│                                      │"
    t074 = "└─────┤Press Enter to Continue...├─────┘"
        # ending quest
    t080 = "├─────┴────────────────────────────────┤"
    t081 = "│ It's the most essential ingredient   │"
    t082 = "│ that I need to make the              │"
    t083 = "│ 'Spirit page'.                       │"
    t084 = "└────────────────┤....├────────────────┘"
    t090 = "├─────┴────────────────────────────────┤"
    t091 = "│ It's a piece of paper that,          │"
    t092 = "│ according to the legends, stores the │"
    t093 = "│ spirit of the user.                  │"
    t094 = "└────────────────┤....├────────────────┘"
    t100 = "├─────┴────────────────────────────────┤"
    t101 = "│ But so far, nobody has been able to  │"
    t102 = "│ use this piece of paper.             │"
    t103 = "│                                      │"
    t104 = "└────────────────┤....├────────────────┘"
    t110 = "├─────┴────────────────────────────────┤"
    t111 = "│ Supposedly, no one but the           │"
    t112 = "│ Riaceovians can use the 'Spirit-     │"
    t113 = "│ page'...                             │"
    t114 = "└────────────────┤....├────────────────┘"
    t120 = "├─────┴────────────────────────────────┤"
    t121 = "│ But Riaceovians had disappeared a    │"
    t122 = "│ long time ago...                     │"
    t123 = "│                                      │"
    t124 = "└────────────────┤....├────────────────┘"
    t130 = "├─────┴────────────────────────────────┤"
    t131 = "│ .....                                │"
    t132 = "│                                      │"
    t133 = "│                                      │"
    t134 = "└────────────────┤....├────────────────┘"
    t140 = "├─────┴────────────────────────────────┤"
    t141 = "│ I should start putting the materials │"
    t142 = "│ together... would you mind playing   │"
    t143 = "│ outside just for a while?            │"
    t144 = "└────────────────┤....├────────────────┘"


class John:
    """German Shepard"""
    """Facial expressions"""
    e000 = "╭─────╮"
    e001 = "│Aꞈ_A │"
    e002 = "│ | |‗│"
    e003 = "│  __/├────────────────────────────────╮"
    e004 = "│   \ │ John                           │"
    e010 = "╭─────╮"
    e011 = "│Aꞈ_A │"
    e012 = "│ - -‗│"
    e013 = "│  __/├────────────────────────────────╮"
    e014 = "│   \ │ John                           │"
    """Talking"""
    t000 = "├─────┴────────────────────────────────┤"
    t001 = "│ ...                                  │"
    t002 = "│                                      │"
    t003 = "│                                      │"
    t004 = "└────────────────┤....├────────────────┘"
    t010 = "├─────┴────────────────────────────────┤"
    t011 = "│ ....                                 │"
    t012 = "│                                      │"
    t013 = "│                                      │"
    t014 = "└─────┤Press Enter to Continue...├─────┘"


class Ravia:
    """Unknown breed"""
    """Facial expressions"""
    # normal
    e000 = "╭─────╮"
    e001 = "│ __  │"
    e002 = "│╯| |_│"
    e003 = "│   _/├────────────────────────────────╮"
    e004 = "│^^^\ │ Ravia                          │"
    # happy
    e010 = "╭─────╮"
    e011 = "│ __  │"
    e012 = "│╯ᴖ ᴖ_│"
    e013 = "│   _/├────────────────────────────────╮"
    e014 = "│^^^\ │ Ravia                          │"
    """Talking"""
    # Interacting with Firay
    t000 = "├─────┴────────────────────────────────┤"
    t001 = "│ Heyyy!!! What brings you here?       │"
    t002 = "│                                      │"
    t003 = "│                                      │"
    t004 = "└────────────────┤....├────────────────┘"
    t010 = "├─────┴────────────────────────────────┤"
    t011 = "│ Oh! I do have a spare Clear Leaf!    │"
    t012 = "│                                      │"
    t013 = "│                                      │"
    t014 = "└────────────────┤....├────────────────┘"
    t020 = "├─────┴────────────────────────────────┤"
    t021 = "│ In fact,                             │"
    t022 = "│ You can have it, since I don't have  │"
    t023 = "│ any use for it!                      │"
    t024 = "└────────────────┤....├────────────────┘"
    t030 = "├─────┴────────────────────────────────┤"
    t031 = "│ Here you go!                         │"
    t032 = "│ Tell Rubi I said Hi!!!               │"
    t033 = "│                                      │"
    t034 = "└─────┤Press Enter to Continue...├─────┘"
    t040 = "├─────┴────────────────────────────────┤"
    t041 = "│ Hello again!                         │"
    t042 = "│                                      │"
    t043 = "│                                      │"
    t044 = "└─────┤Press Enter to Continue...├─────┘"
    t050 = "├─────┴────────────────────────────────┤"
    t051 = "│ Hello~!                              │"
    t052 = "│                                      │"
    t053 = "│                                      │"
    t054 = "└─────┤Press Enter to Continue...├─────┘"


'''preset
e000 = "╭─────╮"
e001 = "│Ʌ__Ʌ │"
e002 = "│ | |_│"
e003 = "│   _/├────────────────────────────────╮"
e004 = "│   \ │ name                           │"
t000 = "├─────┴────────────────────────────────┤"
t001 = "│                                      │"
t002 = "│                                      │"
t003 = "│                                      │"
t004 = "└────────────────┤....├────────────────┘"
t010 = "├─────┴────────────────────────────────┤"
t011 = "│                                      │"
t012 = "│                                      │"
t013 = "│                                      │"
t014 = "└─────┤Press Enter to Continue...├─────┘"
i000 = "├─────┴────────────────────────────────┤"
i001 = "│                                      │"
i002 = "│                                      │"
i003 = "│                                      │"
i004 = "└────────────────┤....├────────────────┘"
i010 = "├─────┴────────────────────────────────┤"
i011 = "│                                      │"
i012 = "│                                      │"
i013 = "│                                      │"
i014 = "└─────┤Press Enter to Continue...├─────┘"
'''
