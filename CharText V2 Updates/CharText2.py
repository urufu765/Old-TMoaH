"""
Character Text and Graphics
Supports The Mark of a Hero from version 0.13 to version 0.13.1
all versions prior to 0.13 doesn't support this.
"""
confirm = input("\nCharText2:"
                "\nThis version of CharText2 supports TMoaH 0.13 to 0.13.1."
                "\nVersions prior to 0.13.1 are not supported.\n\n\n")


class Sys:
    """System messages"""
    sCon = ("\n  vvvvvvvvv"
            "\n> Caution!! <"
            "\n  ^^^^^^^^^\n"
            "\nThis game is built with the font 'Consolas' in mind. Without it can cause some missing textures and size"
            "\nproblems. If 'Consolas' is unavailable, try to find a suitable monospaced font that works the best.\n"
            "\nTest: |ﬓﬔﬕﬖ█▓▒░■□|Ξ‼⌠⌡╭╮╰╯─│|┌┐└┘├┤┬┴┼╌|═║╔╗╚╝╟╠╢╣|╧╩╬╞╡━┃┏┓┗|┛┣┫┳┻╋ḻᶸλɅ|‗ᴜ≥ꞈ╷╴|"
            "\n      |^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^^^^^^|^^^^^^|\n"
            "\nCheck that each character aligns with each arrow,"
            "\nand the top vertical lines aligns with the bottom vertical lines."
            "\nif any of these characters appear as question mark,"
            "\nor the characters don't align with the arrow, please use a different font"
            "\nIf everything looks okay, then..."
            "\n⌠Press enter to continue...⌡")
    qXXX = "You completed '{}'"  # add name
    q0000 = "You got a new quest! You can view your quest log by pressing {}!"  # add key layout in main program
    q0001 = "Get 'Clear Leaf' from Ravia"
    i0000 = "You got an item! You can view your items by pressing {}!"
    i0001 = "Clear Leaf"
    i0002 = "Blunt Stick"


class Firay:
    """Golden Retriever"""
    """facial expression"""
    # normal
    e00 = ("\n╔═════╗"
           "\n║ __  ║"
           "\n║⌡| |_║"
           "\n║   _/╟────────────────────────────────╖"
           "\n║   \ ║ Firay                          ║")
    # Mhm
    e01 = ("\n╔═════╗"
           "\n║ __  ║"
           "\n║⌡ᴜ ᴜ_║"
           "\n║   _/╟────────────────────────────────╖"
           "\n║   \ ║ Firay                          ║")
    # suspicious
    e02 = ("\n╔═════╗"
           "\n║ __  ║"
           "\n║⌡ᴛ ᴛ_║"
           "\n║   _/╟────────────────────────────────╖"
           "\n║   \ ║ Firay                          ║")
    # thinking
    e03 = ("\n╔═════╗"
           "\n║ __  ║"
           "\n║⌡- -_║"
           "\n║   _/╟────────────────────────────────╖"
           "\n║   \ ║ Firay                          ║")
    # exhausted
    e04 = ("\n╔═════╗"
           "\n║ __  ║"
           "\n║⌡≥ ḻ_║"
           "\n║ᶸ  _/╟────────────────────────────────╖"
           "\n║   \ ║ Firay                          ║")
    # slightly confused/not amused
    e05 = ("\n╔═════╗"
           "\n║ __  ║"
           "\n║⌡| ᴛ_║"
           "\n║   _/╟────────────────────────────────╖"
           "\n║   \ ║ Firay                          ║")
    """Talking"""
    # Low stamina
    t000 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Can't do this forever...             ║"
            "\n║ Maybe after a little rest would do.. ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    # interacting with Rubi in home
    # Getting quest "get clear leaf"
    '''═ ║ ╔ ╗ ╚ ╝ ╟ ╠ ╢ ╣ ╧ ╩ ╬ ╞ ╡'''
    t001 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Yup~!                                ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t002 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ ...?                                 ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t003 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Yup!.....                            ║"
            "\n║ wait... where was Ravia's house?     ║"
            "\n║ I can't remember..                   ║"
            "\n╚════════════════╡....╞════════════════╝")
    # finishing quest "get clear leaf"
    t004 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Got the leaf!...                     ║"
            "\n║ What's it for?                       ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t005 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ What's a 'spirit page'?              ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t006 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Huh..                                ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t007 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ ........?                            ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t008 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Yup!                                 ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    # quest complete interaction
    t009 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ I shouldn't disturb Rubi...          ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    # interacting with John in home
    t010 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Hey John!                            ║"
            "\n║ How's the morning been?              ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t011 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Do you just never talk?              ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    # interacting with Ravia
    t012 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ I was wondering if you have any      ║"
            "\n║ Clear Leaf to spare?                 ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    t013 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ What a coincidence!                  ║"
            "\n║ I was going to ask to lend me one... ║"
            "\n║ Rubi's favor actually.               ║"
            "\n╚════════════════╡....╞════════════════╝")
    """Interacting"""
    # interacting with beds in home
    i001 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ This is my bed...                    ║"
            "\n║ It's where I sleep.                  ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    i002 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ This is Rubi's bed...                ║"
            "\n║ It's where she is supposed to sleep. ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    i003 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ That is... if she's not in middle of ║"
            "\n║ something important...               ║"
            "\n║ Like always..                        ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    # interacting with table in home
    i004 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ This is a table..                    ║"
            "\n║ It's where me and Rubi eat..         ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    i005 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Half of the table is usually         ║"
            "\n║ occupied by non-food stuff such as   ║"
            "\n║ magical candles and books.....       ║"
            "\n╚════════════════╡....╞════════════════╝")
    i006 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ *Sigh.*                              ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    # interacting with lake/river in Mithavil
    i007 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ I'd love to dive into the chilly     ║"
            "\n║ water...                             ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    i008 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ But I can't.                         ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚════════════════╡....╞════════════════╝")
    i009 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ Because I'd drown.                   ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")
    # interacting with a table in Ravia's House
    i010 = ("\n╠═════╩════════════════════════════════╣"
            "\n║ It's a table...                      ║"
            "\n║                                      ║"
            "\n║                                      ║"
            "\n╚═════╡Press Enter to Continue...╞═════╝")


class Rubi:
    """Samoyed"""
    """facial expression"""
    # normal
    e00 = ("\n╭─────╮"
           "\n│λꞈꞈλ │"
           "\n│ | |ꞈ│"
           "\n│  ꞈꞈ/├────────────────────────────────╮"
           "\n│   \ │ Rubi                           │")
    # happy
    e01 = ("\n╭─────╮"
           "\n│λꞈꞈλ │"
           "\n│ ᴖ ᴖꞈ│"
           "\n│  ꞈꞈ/├────────────────────────────────╮"
           "\n│   \ │ Rubi                           │")
    # slightly confused
    e02 = ("\n╭─────╮"
           "\n│λꞈꞈλ │"
           "\n│ ᴛ |ꞈ│"
           "\n│  ꞈꞈ/├────────────────────────────────╮"
           "\n│   \ │ Rubi                           │")
    # irritated
    e03 = ("\n╭─────╮"
           "\n│λꞈꞈλ │"
           "\n│ ᴛ ᴛꞈ│"
           "\n│  ꞈꞈ/├────────────────────────────────╮"
           "\n│   \ │ Rubi                           │")
    # meh
    e04 = ("\n╭─────╮"
           "\n│λꞈꞈλ │"
           "\n│ - -ꞈ│"
           "\n│  ꞈꞈ/├────────────────────────────────╮"
           "\n│   \ │ Rubi                           │")
    """Talking"""
    # interacting with Firay in home
        # giving quest
    t000 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Good morning~                        │"
            "\n│ Had a good night sleep?              │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t001 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Lovely~                              │"
            "\n│ Now off with ya!                     │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t002 = ("\n├─────┴────────────────────────────────┤"
            "\n│ ...!                                 │"
            "\n│ Wait!                                │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t003 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Could you get me a clear leaf for    │"
            "\n│ me? I think Raiva has some to spare. │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t004 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Her house should be the first house  │"
            "\n│ across the river...                  │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t005 = ("\n├─────┴────────────────────────────────┤"
            "\n│ That is if she hasn't moved again    │"
            "\n│ because her house is 'haunted with   │"
            "\n│ ghosts of wind'...                   │"
            "\n└────────────────┤....├────────────────┘")
    t006 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Whatever that means..                │"
            "\n│ Now off you go!                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")
    t007 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Lovely day, ain't it?                │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")
    # ending quest
    t008 = ("\n├─────┴────────────────────────────────┤"
            "\n│ It's the most essential ingredient   │"
            "\n│ that I need to make the              │"
            "\n│ 'Spirit page'.                       │"
            "\n└────────────────┤....├────────────────┘")
    t009 = ("\n├─────┴────────────────────────────────┤"
            "\n│ It's a piece of paper that,          │"
            "\n│ according to the legends, stores the │"
            "\n│ spirit of the user.                  │"
            "\n└────────────────┤....├────────────────┘")
    t010 = ("\n├─────┴────────────────────────────────┤"
            "\n│ But so far, nobody has been able to  │"
            "\n│ use this piece of paper.             │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t011 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Supposedly, no one but the           │"
            "\n│ Riaceovians can use the 'Spirit-     │"
            "\n│ page'...                             │"
            "\n└────────────────┤....├────────────────┘")
    t012 = ("\n├─────┴────────────────────────────────┤"
            "\n│ But Riaceovians had disappeared a    │"
            "\n│ long time ago...                     │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t013 = ("\n├─────┴────────────────────────────────┤"
            "\n│ .....                                │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t014 = ("\n├─────┴────────────────────────────────┤"
            "\n│ I should start putting the materials │"
            "\n│ together... would you mind playing   │"
            "\n│ outside just for a while?            │"
            "\n└────────────────┤....├────────────────┘")


class John:
    """German Shepard"""
    """Facial expressions"""
    e00 = ("\n╭─────╮"
           "\n│Aꞈ_A │"
           "\n│ | |‗│"
           "\n│  __/├────────────────────────────────╮"
           "\n│   \ │ John                           │")
    e01 = ("\n╭─────╮"
           "\n│Aꞈ_A │"
           "\n│ - -‗│"
           "\n│  __/├────────────────────────────────╮"
           "\n│   \ │ John                           │")
    """Talking"""
    t000 = ("\n├─────┴────────────────────────────────┤"
            "\n│ ...                                  │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t001 = ("\n├─────┴────────────────────────────────┤"
            "\n│ ....                                 │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")


class Ravia:
    """Unknown breed"""
    """Facial expressions"""
    # normal
    e00 = ("\n╭─────╮"
           "\n│ __  │"
           "\n│╯| |_│"
           "\n│   _/├────────────────────────────────╮"
           "\n│^^^\ │ Ravia                          │")
    # happy
    e01 = ("\n╭─────╮"
           "\n│ __  │"
           "\n│╯ᴖ ᴖ_│"
           "\n│   _/├────────────────────────────────╮"
           "\n│^^^\ │ Ravia                          │")
    """Talking"""
    # Interacting with Firay
    t000 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Heyyy!!! What brings you here?       │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t001 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Oh! I do have a spare Clear Leaf!    │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└────────────────┤....├────────────────┘")
    t002 = ("\n├─────┴────────────────────────────────┤"
            "\n│ In fact,                             │"
            "\n│ You can have it, since I don't have  │"
            "\n│ any use for it!                      │"
            "\n└────────────────┤....├────────────────┘")
    t003 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Here you go!                         │"
            "\n│ Tell Rubi I said Hi!!!               │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")
    t004 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Hello again!                         │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")
    t005 = ("\n├─────┴────────────────────────────────┤"
            "\n│ Hello~!                              │"
            "\n│                                      │"
            "\n│                                      │"
            "\n└─────┤Press Enter to Continue...├─────┘")


'''preset
e00 = ("\n╭─────╮"
       "\n│Ʌ__Ʌ │"
       "\n│ | |_│"
       "\n│   _/├────────────────────────────────╮"
       "\n│   \ │ name                           │")
t000 = ("\n├─────┴────────────────────────────────┤"
        "\n│                                      │"
        "\n│                                      │"
        "\n│                                      │"
        "\n└────────────────┤....├────────────────┘")
t001 = ("\n├─────┴────────────────────────────────┤"
        "\n│                                      │"
        "\n│                                      │"
        "\n│                                      │"
        "\n└─────┤Press Enter to Continue...├─────┘")
i000 = ("\n├─────┴────────────────────────────────┤"
        "\n│                                      │"
        "\n│                                      │"
        "\n│                                      │"
        "\n└────────────────┤....├────────────────┘")
i001 = ("\n├─────┴────────────────────────────────┤"
        "\n│                                      │"
        "\n│                                      │"
        "\n│                                      │"
        "\n└─────┤Press Enter to Continue...├─────┘")
e00 = ("\n╔═════╗"
       "\n║Ʌ__Ʌ ║"
       "\n║ | |_║"
       "\n║   _/╟────────────────────────────────╖"
       "\n║   \ ║ name                           ║")
t000 = ("\n╠═════╩════════════════════════════════╣"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n╚════════════════╡....╞════════════════╝")
t001 = ("\n╠═════╩════════════════════════════════╣"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n╚═════╡Press Enter to Continue...╞═════╝")
i000 = ("\n╠═════╩════════════════════════════════╣"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n╚════════════════╡....╞════════════════╝")
i001 = ("\n╠═════╩════════════════════════════════╣"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n║                                      ║"
        "\n╚═════╡Press Enter to Continue...╞═════╝")
'''
