"""
< Constalia The Mark of a Hero >

by FOKKUSU~
Ver: 0.13.X

description: Using what I've learnt with BattleShell and Maze Game, I've created a turn-based RPG
"""
import random
from CharText2 import *
# variable listing
Loop = True
Control = True
dialogue = False
Door = True
CurQue = ["Empty", "Empty", "Empty", "Empty", "Empty"]  # Quest list
ProQue = [0, 0, 0, 0, 0]
# 0 = empty, 1 = inactive, 2 = active, 3 = complete, 4 = remove
CurInv = ["Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty", "Empty"]  # Inventory list
ProInv = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# 0 = empty, 1 = weapon, 2 = consumable, 3 = item, 4 = quest item, 5 = special item
map0, map1, map2, map3, map4, map5, map6, map7, map8, map9 = "E", "E", "E", "E", "E", "E", "E", "E", "E", "E"
ran = int(0)


# other stuff
class Quest:
    # Four states: Inactive, Active, Complete, Remove
    # Inactive: quest not activated
    # Active: quest in progress
    # Complete: quest completed
    # Remove: quest no longer completable
    GetClearLeaf = "Inactive"  # Quest to get Clear Leaf for Rubi


class Inventory:
    ItemClearLeaf = False  # clear leaf item
    TypeClearLeaf = int(4)
    ItemBluntStick = False  # blunt stick item
    TypeBluntStick = int(1)


# Character info:
class CFiray:
    Sta = int(20)
    MaxSta = int(20)


# Functions
def readFile(file_name):
    file = open(file_name, 'r')
    content = list()
    for line in file:
        print(line)
        content.append(line)
    file.close()
    return content


def writeFile(file_name, messages):
    file = open(file_name, 'w')
    for item in messages:
        file.write(item)
        file.write("\n") #including new line for each item
    file.close()


def loader(n):
    global ran
    global map0, map1, map2, map3, map4, map5, map6, map7, map8, map9
    if n == 1:  # Used in: Mithavil
        ran = random.randint(1, 100)
        if ran <= 25:
            map5 = "ﬓ"  # River/lake
        elif 25 < ran <= 50:
            map5 = "ﬔ"
        elif 50 < ran <= 75:
            map5 = "ﬕ"
        elif 75 < ran:
            map5 = "ﬖ"
        map0 = " "  # Empty space
        map1 = "҈"  # pathway
        map2 = "■"  # house
        map3 = "⌠"  # farm
        map4 = "▓"  # bridge
        map6 = "‼"  # sign
        map7 = "□"  # door
        map8 = "Ξ"  # exit
        map9 = "█"  # boundary
        return
    elif n == 2:  # Used in: Home
        map0 = "░"  # space
        map1 = "▒"  # character
        map2 = "■"  # bed
        map3 = "╬"  # table
        map4 = "┃"  # locked vertical door
        map5 = "━"  # locked horizontal door
        map6 = "│"  # vertical door
        map7 = "─"  # horizontal door
        map8 = "Ξ"  # exit
        map9 = "█"  # boundary


def area(n):
    if n == 0:  # Mithavil no
        nope = [2, 3, 5, 6, 9]
        return nope
    elif n == 1:  # Home and Ravia's house no
        nope = [1, 2, 3, 4, 5, 9]
        return nope


# Map
class Mithavil:
    MG = int(1)  # Map group
    MN = int(0)  # Map number
    ML = int(1)  # Map loader number, just in case the graphics have to change
    Name = "Mithavil"
    # Key 0 = space, 1 = path, 2 = house, 3 = farm, 4 = bridge, 5 = river/lake, 6 = sign, 7 = door, 8 = exit, 9 = bound
    # Count  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
    grid = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 0
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 1
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 2
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 3
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 7, 0, 0, 0, 0, 0, 9, 9, 9],  # 4
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 8, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 9, 9, 9],  # 5
            [9, 9, 4, 4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 9, 9],  # 6
            [9, 9, 4, 4, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 9, 9, 9],  # 7
            [9, 9, 4, 4, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 4, 5, 5, 0, 9, 9, 9],  # 8
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 4, 0, 0, 0, 9, 9, 9],  # 9
            [9, 9, 5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 9, 9],  # 10
            [9, 9, 0, 5, 5, 5, 5, 4, 5, 5, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 9, 9],  # 11
            [9, 9, 0, 0, 0, 0, 0, 4, 0, 0, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 9, 9, 9],  # 12
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 9, 9],  # 13
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 1, 0, 0, 0, 0, 0, 9, 9, 9],  # 14
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 1, 0, 0, 2, 2, 2, 9, 9, 9],  # 15
            [9, 9, 0, 0, 2, 2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 5, 5, 5, 5, 5, 5, 0, 0, 1, 1, 1, 7, 2, 2, 2, 9, 9, 9],  # 16
            [9, 9, 0, 0, 2, 2, 7, 1, 1, 1, 8, 2, 2, 2, 0, 0, 5, 5, 5, 5, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 17
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 18
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 1, 7, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 19
            [9, 9, 0, 2, 2, 2, 7, 1, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 20
            [9, 9, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 21
            [9, 9, 0, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 22
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9],  # 23
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9],  # 24
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9],  # 25
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 9, 9, 9],  # 26
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 27
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 28
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 29
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 30
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 31
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 32
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 33
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 34
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]  # 35
    '''visual
    000000000011111111112222222222333
    012345678901234567890123456789012
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 00
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 01
    XX                             XX 02
    XX   FFFFFFHHH      HHHH       XX 03
    XX   FFFFFFHHH      HHHHD      XX 04
    XX   FFFFFF D       HHHH P     XX 05
    XXBB       PP             P    XX 06
    XXBBPP     P              B  RRXX 07
    XXBB  PPPPP             RRBRR  XX 08
    XX     P           RRRRR  B    XX 09
    XXR    B        RRR       P    XX 10
    XX RRRRBRR   RRR          P    XX 11
    XX     B  RRR    LLL      P    XX 12
    XX     P        LLLLL    P     XX 13
    XX     P       LLLLLLL  P      XX 14
    XX      P      LLLLLLL  P  HHH XX 15
    XX  HH  P  HHH LLLLLL  PPPDHHH XX 16
    XX  HHDPPPDHHH  LLLLL P        XX 17
    XX      P        LLL  P        XX 18
    XX      PPDHHH        P        XX 19
    XX HHHDPP  HHH       P         XX 20
    XX HHH  P           P          XX 21
    XX HHH  PP        PPP          XX 22
    XX       P       PPPP  HHHHHHH XX 23
    XX       P      P   P  HHHHHHH XX 24
    XX       P     P    PPDHHHHHHH XX 25
    XX        P S P        HHHHHHH XX 26
    XX         PPPP                XX 27
    XX          P  P               XX 28
    XX          P   PP             XX 29
    XX          PSS                XX 30
    XX          P                  XX 31
    XX          T                  XX 32
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 33
    XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX 34
    F = Farm
    B = Bridge
    P = Path
    R = River
    H = House
    D = Door
    L = Lake
    S = Sign
    T = To next map
    '''


class Home:
    MG = int(1)  # Map group
    MN = int(1)  # Map number
    ML = int(2)  # Map loader
    Name = "Firay's Home"
    # Key 0 = space, 1 = character, 2 = bed, 3 = table, 6 = Vdoor, 7 = Hdoor, 8 = exit, 9 = bound
    # Count  0  1  2  3  4  5  6  7  8  9 10 11 12 13
    grid = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 0
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 1
            [9, 9, 2, 2, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9],  # 2
            [9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9],  # 3
            [9, 9, 9, 7, 9, 9, 9, 9, 0, 0, 0, 2, 9, 9, 9],  # 4
            [9, 9, 0, 0, 0, 0, 0, 9, 0, 0, 0, 2, 9, 9, 9],  # 5
            [9, 9, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 9, 9, 9],  # 6
            [9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9, 9],  # 7
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 8
            [9, 9, 0, 0, 3, 3, 3, 1, 0, 0, 0, 0, 9, 9, 9],  # 9
            [9, 9, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 9, 9, 9],  # 10
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 0, 8, 0, 9, 9, 9],  # 11
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 12
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 13
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]  # 14
    """visual
    00000000001111
    01234567890123
    XXXXXXXXXXXXXX 00
    XXXXXXXXXXXXXX 01
    XXBB   XXXXXXX 02
    XX     XXXXXXX 03
    XXXDXXXX   BXX 04
    XX     X F BXX 05
    XX     D    XX 06
    XX     XXXXXXX 07
    XX          XX 08
    XX  TTTC    XX 09
    XX  TTT     XX 10
    XX      C D XX 11
    XXXXXXXXXXXXXX 12
    XXXXXXXXXXXXXX 13
    """


class Raviahouse:
    MG = int(1)  # Map group
    MN = int(2)  # Map number
    ML = int(2)  # Map loader
    Name = "Ravia's House"
    # Key 0 = space, 1 = char, 2 = bed, 3 = table, 4 = LVdoor, 5 = LHdoor, 6 = Vdoor, 7 = Hdoor, 8 = exit, 9 = bound
    # Count  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14
    grid = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 0
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 1
            [9, 9, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 9, 9],  # 2
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 9, 9, 9],  # 3
            [9, 9, 9, 9, 9, 5, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 4
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 5
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 9, 9, 9],  # 6
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 9, 9, 9],  # 7
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 9, 9, 9],  # 8
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 9, 9, 9],  # 9
            [9, 9, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 10
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9, 9],  # 11
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 12
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 13
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]  # 14
    """visual
    0000000000111111
    0123456789012345
    XXXXXXXXXXXXXXXX 00
    XXXXXXXXXXXXXXXX 01
    XXBB        TXXX 02
    XX          TXXX 03
    XXXXXLXXXXXXXXXX 04
    XX           XXX 05
    XX     C     XXX 06
    XX   TTTT    XXX 07
    XX   TTTT    XXX 08
    XX   TTTT    XXX 09
    XXD          XXX 10
    XX           XXX 11
    XXXXXXXXXXXXXXXX 12
    XXXXXXXXXXXXXXXX 13
    XXXXXXXXXXXXXXXX 14
    """


# Main code
if __name__ == '__main__':
    file_name = "save.txt"

    messages = list()
    for number in range(0,501):
        message = "This is message number " + str(number)
        messages.append(message)

    # We send the file name and the content to include in a list


    # we read the file and put the content in a list
    fromFile = readFile(file_name)

    for item in fromFile:
        print(item)
proceed = input(Sys.sCon)
print("\n" * 200)
while Control is True:
    print("╭─────────────────────────────────────────────────────────────╮\n"
          "│System Message: There are four control schemes               │\n"
          "│that you can choose from.                                    │\n"
          "├─────────────────────────────────────────────────────────────┤\n"
          "│Please select from one of the four listed:                   │\n"
          "├─────────────────────────────────────────────────────────────┤\n"
          "│          UP   ╷ DOWN  ╷ LEFT  ╷ RIGHT ╷ QUEST  ╷ INVENTORY  │\n"
          "├─┬─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
          "│1│NSWE: (N)orth│(S)outh│(W)est │(E)ast │(Q)uest │(I)nventory │\n"
          "├─┼─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
          "│2│UDLR: (U)p   │(D)own │(L)eft │(R)ight│(Q)uest │(I)nventory │\n"
          "├─┼─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
          "│3│WSAD: (W)    │(S)    │(A)    │(D)    │(Q)     │(E)         │\n"
          "├─┼─────────────┼───────┼───────┼───────┼────────┼────────────┤\n"
          "│4│NUMP: (8)    │(2),(5)│(4)    │(6)    │(*)     │(/)         │\n"
          "╰─┴─────────────┴───────┴───────┴───────┴────────┴────────────╯\n")
    CTRL = input("Your choice of input: ")
    if CTRL == "1":
        Up = ["N", "n", "North", "north", "NORTH"]
        Down = ["S", "s", "South", "south", "SOUTH"]
        Left = ["W", "w", "West", "west", "WEST"]
        Right = ["E", "e", "East", "east", "EAST"]
        LungeUp = ["NN", "nn", "Nn", "nN", "Lunge North", "lunge north", "LUNGE NORTH", "Lunge north"]
        LungeDown = ["SS", "ss", "Ss", "sS", "Lunge South", "lunge south", "LUNGE SOUTH", "Lunge south"]
        LungeLeft = ["WW", "ww", "Ww", "wW", "Lunge West", "lunge west", "LUNGE WEST", "Lunge west"]
        LungeRight = ["EE", "ee", "Ee", "eE", "Lunge East", "lunge east", "LUNGE EAST", "Lunge east"]
        Que = ["Q", "q", "Quest", "quest", "QUEST"]
        Inv = ["I", "i", "Inventory", "inventory", "INVENTORY"]
        print("You have selected NSWE\n")
        proceed = input("Press enter to continue...")
        Control = False
    elif CTRL == "2":
        Up = ["U", "u", "Up", "up", "UP"]
        Down = ["D", "d", "Down", "down", "DOWN"]
        Left = ["L", "l", "Left", "left", "LEFT"]
        Right = ["R", "r", "Right", "right", "RIGHT"]
        LungeUp = ["UU", "uu", "Uu", "uU", "Lunge Up", "lunge up", "LUNGE UP", "Lunge up"]
        LungeDown = ["DD", "dd", "Dd", "dD", "Lunge Down", "lunge down", "LUNGE DOWN", "Lunge down"]
        LungeLeft = ["LL", "ll", "Ll", "lL", "Lunge Left", "lunge left", "LUNGE LEFT", "Lunge left"]
        LungeRight = ["RR", "rr", "Rr", "rR", "Lunge Right", "lunge right", "LUNGE RIGHT", "Lunge right"]
        Que = ["Q", "q", "Quest", "quest", "QUEST"]
        Inv = ["I", "i", "Inventory", "inventory", "INVENTORY"]
        print("You have selected UDLR\n")
        proceed = input("Press enter to continue...")
        Control = False
    elif CTRL == "3":
        Up = ["W", "w"]
        Down = ["S", "s"]
        Left = ["A", "a"]
        Right = ["D", "d"]
        LungeUp = ["WW", "ww", "Ww", "wW"]
        LungeDown = ["SS", "ss", "Ss", "sS"]
        LungeLeft = ["AA", "aa", "Aa" "aA"]
        LungeRight = ["DD", "dd", "Dd", "dD"]
        Que = ["Q", "q"]
        Inv = ["E", "e"]
        print("You have selected WSAD\n")
        proceed = input("Press enter to continue...")
        Control = False
    elif CTRL == "4":
        Up = "8"
        Down = ["2", "5"]
        Left = "4"
        Right = "6"
        LungeUp = "88"
        LungeDown = ["22", "55"]
        LungeLeft = "44"
        LungeRight = "66"
        Que = "*"
        Inv = "/"
        Sav = "+"
        print("You have selected NUMPAD\n")
        proceed = input("Press enter to continue...")
        Control = False
    else:
        print("Invalid!")
Char = CFiray()
M = Home()
Q = Quest()
It = Inventory()
R = int(5)
C = int(9)
NO = "You didn't move"  # testing purpose
YA = "You moved"  # testing purpose
Lun = "You lunged!"
while Loop is True:
    if Char.Sta < (Char.MaxSta - 1):
        Char.Sta = (Char.Sta + 2)
    elif Char.Sta < Char.MaxSta:
        Char.Sta = (Char.Sta + 1)
    MAP = False
    Lunge = False  # unused variable for now, might use later on
    North = R - 1
    South = R + 1
    West = C - 1
    East = C + 1
    MapN = R - 2  # used in lunging and map
    MapS = R + 2  # used in lunging and map
    MapW = C - 2  # used in lunging and map
    MapE = C + 2  # used in lunging and map
    Ma2N = R - 3  # only used in map
    Ma2S = R + 3  # only used in map
    Ma2W = C - 3  # only used in map
    Ma2E = C + 3  # only used in map
    if M.MG == 1:
        if M.MN == 0:
            nope = area(0)
            dialogue = True
            Door = True
        elif M.MN in [1, 2]:
            nope = area(1)
            dialogue = True
            Door = True
    while MAP is not True:  # This creates a 7x7 grid. skip this loop since all it does is create graphics
        if M.ML == 1:
            loader(1)  # used in: Mithavil
        elif M.ML == 2:
            loader(2)  # used in: Home
        View = [[1, 2, 3, 4, 5, 6, 7],
                [8, 9, 10, 11, 12, 13, 14],
                [15, 16, 17, 18, 19, 20, 21],
                [22, 23, 24, 25, 26, 27, 28],
                [29, 30, 31, 32, 33, 34, 35],
                [36, 37, 38, 39, 40, 41, 42],
                [43, 44, 45, 46, 47, 48, 49]]
        A = int(0)  # Column counter
        D = int(1)  # Row 1
        E = int(1)  # Row 2
        F = int(1)  # Row 3
        G = int(1)  # Row 4
        H = int(1)  # Row 5
        I = int(1)  # Row 6
        J = int(1)  # Row 7
        # printing grid:
        View1 = [M.grid[Ma2N][Ma2W], M.grid[Ma2N][MapW], M.grid[Ma2N][West], M.grid[Ma2N][C], M.grid[Ma2N][East],
                 M.grid[Ma2N][MapE], M.grid[Ma2N][Ma2E]]
        View2 = [M.grid[MapN][Ma2W], M.grid[MapN][MapW], M.grid[MapN][West], M.grid[MapN][C], M.grid[MapN][East],
                 M.grid[MapN][MapE], M.grid[MapN][Ma2E]]
        View3 = [M.grid[North][Ma2W], M.grid[North][MapW], M.grid[North][West], M.grid[North][C], M.grid[North][East],
                 M.grid[North][MapE], M.grid[North][Ma2E]]
        View4 = [M.grid[R][Ma2W], M.grid[R][MapW], M.grid[R][West], M.grid[R][C], M.grid[R][East],
                 M.grid[R][MapE], M.grid[R][Ma2E]]
        View5 = [M.grid[South][Ma2W], M.grid[South][MapW], M.grid[South][West], M.grid[South][C], M.grid[South][East],
                 M.grid[South][MapE], M.grid[South][Ma2E]]
        View6 = [M.grid[MapS][Ma2W], M.grid[MapS][MapW], M.grid[MapS][West], M.grid[MapS][C], M.grid[MapS][East],
                 M.grid[MapS][MapE], M.grid[MapS][Ma2E]]
        View7 = [M.grid[Ma2S][Ma2W], M.grid[Ma2S][MapW], M.grid[Ma2S][West], M.grid[Ma2S][C], M.grid[Ma2S][East],
                 M.grid[Ma2S][MapE], M.grid[Ma2S][Ma2E]]
        # The "E" that is used in the 'else:' part is for missing texture, if there is any need for that.
        # it's just in case I forget a texture. It'll help because when I test the game, it will show E for missing
        # texture instead of just blank or error.
        while D != 8:  # Row 1 generator
            if View1[A] == 0:
                View[0][A] = map0
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 1:
                View[0][A] = map1
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 2:
                View[0][A] = map2
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 3:
                View[0][A] = map3
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 4:
                View[0][A] = map4
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 5:
                View[0][A] = map5
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 6:
                View[0][A] = map6
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 7:
                View[0][A] = map7
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 8:
                View[0][A] = map8
                A = int(A + 1)
                D = int(D + 1)
            elif View1[A] == 9:
                View[0][A] = map9
                A = int(A + 1)
                D = int(D + 1)
            else:
                View[0][A] = "E"
                A = int(A + 1)
                D = int(D + 1)
        A = int(0)  # Column counter reset
        while E != 8:  # Row 2 generator
            if View2[A] == 0:
                View[1][A] = map0
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 1:
                View[1][A] = map1
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 2:
                View[1][A] = map2
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 3:
                View[1][A] = map3
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 4:
                View[1][A] = map4
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 5:
                View[1][A] = map5
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 6:
                View[1][A] = map6
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 7:
                View[1][A] = map7
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 8:
                View[1][A] = map8
                A = int(A + 1)
                E = int(E + 1)
            elif View2[A] == 9:
                View[1][A] = map9
                A = int(A + 1)
                E = int(E + 1)
            else:
                View[1][A] = "E"
                A = int(A + 1)
                E = int(E + 1)
        A = int(0)  # Column counter reset
        while F != 8:  # Row 3 generator
            if View3[A] == 0:
                View[2][A] = map0
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 1:
                View[2][A] = map1
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 2:
                View[2][A] = map2
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 3:
                View[2][A] = map3
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 4:
                View[2][A] = map4
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 5:
                View[2][A] = map5
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 6:
                View[2][A] = map6
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 7:
                View[2][A] = map7
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 8:
                View[2][A] = map8
                A = int(A + 1)
                F = int(F + 1)
            elif View3[A] == 9:
                View[2][A] = map9
                A = int(A + 1)
                F = int(F + 1)
            else:
                View[2][A] = "E"
                A = int(A + 1)
                F = int(F + 1)
        A = int(0)  # Column counter reset
        while G != 8:  # Row 4 generator
            if View4[A] == 0:
                View[3][A] = map0
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 1:
                View[3][A] = map1
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 2:
                View[3][A] = map2
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 3:
                View[3][A] = map3
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 4:
                View[3][A] = map4
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 5:
                View[3][A] = map5
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 6:
                View[3][A] = map6
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 7:
                View[3][A] = map7
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 8:
                View[3][A] = map8
                A = int(A + 1)
                G = int(G + 1)
            elif View4[A] == 9:
                View[3][A] = map9
                A = int(A + 1)
                G = int(G + 1)
            else:
                View[3][A] = "E"
                A = int(A + 1)
                G = int(G + 1)
        A = int(0)  # Column counter reset
        while H != 8:  # Row 5 generator
            if View5[A] == 0:
                View[4][A] = map0
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 1:
                View[4][A] = map1
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 2:
                View[4][A] = map2
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 3:
                View[4][A] = map3
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 4:
                View[4][A] = map4
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 5:
                View[4][A] = map5
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 6:
                View[4][A] = map6
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 7:
                View[4][A] = map7
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 8:
                View[4][A] = map8
                A = int(A + 1)
                H = int(H + 1)
            elif View5[A] == 9:
                View[4][A] = map9
                A = int(A + 1)
                H = int(H + 1)
            else:
                View[4][A] = "E"
                A = int(A + 1)
                H = int(H + 1)
        A = int(0)  # Column counter reset
        while I != 8:  # Row 6 generator
            if View6[A] == 0:
                View[5][A] = map0
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 1:
                View[5][A] = map1
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 2:
                View[5][A] = map2
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 3:
                View[5][A] = map3
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 4:
                View[5][A] = map4
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 5:
                View[5][A] = map5
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 6:
                View[5][A] = map6
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 7:
                View[5][A] = map7
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 8:
                View[5][A] = map8
                A = int(A + 1)
                I = int(I + 1)
            elif View6[A] == 9:
                View[5][A] = map9
                A = int(A + 1)
                I = int(I + 1)
            else:
                View[5][A] = "E"
                A = int(A + 1)
                I = int(I + 1)
        A = int(0)  # Column counter reset
        while J != 8:  # Row 7 generator
            if View7[A] == 0:
                View[6][A] = map0
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 1:
                View[6][A] = map1
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 2:
                View[6][A] = map2
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 3:
                View[6][A] = map3
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 4:
                View[6][A] = map4
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 5:
                View[6][A] = map5
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 6:
                View[6][A] = map6
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 7:
                View[6][A] = map7
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 8:
                View[6][A] = map8
                A = int(A + 1)
                J = int(J + 1)
            elif View7[A] == 9:
                View[6][A] = map9
                A = int(A + 1)
                J = int(J + 1)
            else:
                View[6][A] = "E"
                A = int(A + 1)
                J = int(J + 1)
        MAP = True
    print("\n" * 200)
    print("\n╭─────────────────────╌╴╴"
          "\n│ Current location: {49}"
          "\n╰─────────────────────╌╴╴"
          "\n         <<[MAP]>>"
          "\n ┏━━━━━━━━━NORTH━━━━━━━━━┓ "
          "\n ┃ {0}{0}{0}{1}{1}{1}{2}{2}{2}{3}{3}{3}{4}{4}{4}{5}{5}{5}{6}{6}{6} ┃ "
          "\n ┃ {0}{0}{0}{1}{1}{1}{2}{2}{2}{3}{3}{3}{4}{4}{4}{5}{5}{5}{6}{6}{6} ┃ "
          "\n ┃ {7}{7}{7}{8}{8}{8}{9}{9}{9}{10}{10}{10}{11}{11}{11}{12}{12}{12}{13}{13}{13} ┃ "
          "\n ┃ {7}{7}{7}{8}{8}{8}{9}{9}{9}{10}{10}{10}{11}{11}{11}{12}{12}{12}{13}{13}{13} ┃ "
          "\n ┃ {14}{14}{14}{15}{15}{15}{16}{16}{16}{17}{17}{17}{18}{18}{18}{19}{19}{19}{20}{20}{20} ┃ "
          "\n W {14}{14}{14}{15}{15}{15}{16}{16}{16}{17}{17}{17}{18}{18}{18}{19}{19}{19}{20}{20}{20} E "
          "\n E {21}{21}{21}{22}{22}{22}{23}{23}{23}ɅꞈɅ{25}{25}{25}{26}{26}{26}{27}{27}{27} A "
          "\n S {21}{21}{21}{22}{22}{22}{23}{23}{23}YOU{25}{25}{25}{26}{26}{26}{27}{27}{27} S "
          "\n T {28}{28}{28}{29}{29}{29}{30}{30}{30}{31}{31}{31}{32}{32}{32}{33}{33}{33}{34}{34}{34} T "
          "\n ┃ {28}{28}{28}{29}{29}{29}{30}{30}{30}{31}{31}{31}{32}{32}{32}{33}{33}{33}{34}{34}{34} ┃ "
          "\n ┃ {35}{35}{35}{36}{36}{36}{37}{37}{37}{38}{38}{38}{39}{39}{39}{40}{40}{40}{41}{41}{41} ┃ "
          "\n ┃ {35}{35}{35}{36}{36}{36}{37}{37}{37}{38}{38}{38}{39}{39}{39}{40}{40}{40}{41}{41}{41} ┃ "
          "\n ┃ {42}{42}{42}{43}{43}{43}{44}{44}{44}{45}{45}{45}{46}{46}{46}{47}{47}{47}{48}{48}{48} ┃ "
          "\n ┃ {42}{42}{42}{43}{43}{43}{44}{44}{44}{45}{45}{45}{46}{46}{46}{47}{47}{47}{48}{48}{48} ┃ "
          "\n ┗━━━━━━━━━SOUTH━━━━━━━━━┛"
          "\n╭─────────────────────╌╴╴"
          "\n│ Stamina: {50}/{51}"
          "\n╰─────────────────────╌╴╴"
          .format(View[0][0], View[0][1], View[0][2], View[0][3], View[0][4], View[0][5], View[0][6],  # Row 1
                  View[1][0], View[1][1], View[1][2], View[1][3], View[1][4], View[1][5], View[1][6],  # Row 2
                  View[2][0], View[2][1], View[2][2], View[2][3], View[2][4], View[2][5], View[2][6],  # Row 3
                  View[3][0], View[3][1], View[3][2], View[3][3], View[3][4], View[3][5], View[3][6],  # Row 4
                  View[4][0], View[4][1], View[4][2], View[4][3], View[4][4], View[4][5], View[4][6],  # Row 5
                  View[5][0], View[5][1], View[5][2], View[5][3], View[5][4], View[5][5], View[5][6],  # Row 6
                  View[6][0], View[6][1], View[6][2], View[6][3], View[6][4], View[6][5], View[6][6],  # Row 7
                  M.Name, Char.Sta, Char.MaxSta))
    Checker = False
    while Checker is False:
        # checks if the user inputs more than 1 letter/number to prevent "pressing-enter-does-something" error
        Move = input("Move where?\n")
        if len(Move) >= 1:
            Checker = True
        else:
            print("Only up, down, left, right please!")
            print("Up:   ", Up)
            print("Down: ", Down)
            print("Left: ", Left)
            print("Right:", Right)
    if Move in Sav:
        save = []
        writeFile(file_name, save)
    elif Move in Que:
        print("\n╭─────────────────────╌╴╴"
              "\n│ Quest-Log:"
              "\n│ 1|{0}"
              "\n│ 2|{1}"
              "\n│ 3|{2}"
              "\n│ 4|{3}"
              "\n│ 5|{4}"
              "\n╰─────────────────────╌╴╴"
              .format(CurQue[0], CurQue[1], CurQue[2], CurQue[3], CurQue[4]))
        proceed = input("Press enter to continue...")
    elif Move in Inv:
        print("\n╭─────────────────────╌╴╴"
              "\n│ Inventory:"
              "\n│ 0|{0}"
              "\n│ 1|{1}"
              "\n│ 2|{2}"
              "\n│ 3|{3}"
              "\n│ 4|{4}"
              "\n│ 5|{5}"
              "\n│ 6|{6}"
              "\n│ 7|{7}"
              "\n│ 8|{8}"
              "\n│ 9|{9}"
              "\n╰─────────────────────╌╴╴"
              .format(CurInv[0], CurInv[1], CurInv[2], CurInv[3], CurInv[4], CurInv[5], CurInv[6], CurInv[7],
                      CurInv[8], CurInv[9]))
        proceed = input("Press enter to continue...")
    elif Move in Up:
        Char.Sta = (Char.Sta - 1)
        if M.grid[North][C] in nope:
            print(NO)
        else:
            R = (R - 1)
            print(YA)
    elif Move in Down:
        Char.Sta = (Char.Sta - 1)
        if M.grid[South][C] in nope:
            print(NO)
        else:
            R = (R + 1)
            print(YA)
    elif Move in Left:
        Char.Sta = (Char.Sta - 1)
        Action = True
        if M.grid[R][West] in nope:
            print(NO)
        else:
            C = (C - 1)
            print(YA)
    elif Move in Right:
        Char.Sta = (Char.Sta - 1)
        if M.grid[R][East] in nope:
            print(NO)
        else:
            C = (C + 1)
            print(YA)
    elif Move in LungeUp and Char.Sta > 2:
        Char.Sta = (Char.Sta - 3)
        if M.grid[North][C] in nope:
            print(NO)
        elif M.grid[MapN][C] in nope:
            R = (R - 1)
            print(YA)
            print(Lun)
        else:
            R = (R - 2)
            print(Lun)
            Lunge = True
    elif Move in LungeDown and Char.Sta > 2:
        Char.Sta = (Char.Sta - 3)
        if M.grid[South][C] in nope:
            print(NO)
        elif M.grid[MapS][C] in nope:
            R = (R + 1)
            print(YA)
            print(Lun)
        else:
            R = (R + 2)
            print(Lun)
            Lunge = True
    elif Move in LungeLeft and Char.Sta > 2:
        Char.Sta = (Char.Sta - 3)
        if M.grid[R][West] in nope:
            print(NO)
        elif M.grid[R][MapW] in nope:
            C = (C - 1)
            print(YA)
            print(Lun)
        else:
            C = (C - 2)
            print(Lun)
            Lunge = True
    elif Move in LungeRight and Char.Sta > 2:
        Char.Sta = (Char.Sta - 3)
        if M.grid[R][East] in nope:
            print(NO)
        elif M.grid[R][MapE] in nope:
            C = (C + 1)
            print(YA)
            print(Lun)
        else:
            C = (C + 2)
            print(Lun)
            Lunge = True
    else:
        if Move in LungeUp or Move in LungeDown or Move in LungeLeft or Move in LungeRight:
            A = Firay()
            print("\n" * 200)
            print(A.e04, end='')  # Firay exhausted
            con00 = input(A.t000)
        else:  # do something about this
            print("Available moves:")
            print("Up_________:", Up)
            print("Down_______:", Down)
            print("Left_______:", Left)
            print("Right______:", Right)
            print("Lunge Up___:", LungeUp)
            print("Lunge Down_:", LungeDown)
            print("Lunge Left_:", LungeLeft)
            print("Lunge Right:", LungeRight)
            print("Quest Log__:", Que)
            print("Inventory__:", Inv)
            proceed = input("Press enter to continue...")
    while dialogue is True:  # dialogue
        done = False
        if Move in Up:
            Dia = M.grid[North][C]
            Xa = North
            Xb = C
        elif Move in Down:
            Dia = M.grid[South][C]
            Xa = South
            Xb = C
        elif Move in Left:
            Dia = M.grid[R][West]
            Xa = R
            Xb = West
        elif Move in Right:
            Dia = M.grid[R][East]
            Xa = R
            Xb = East
        elif Move in LungeUp:
            Dia = M.grid[North][C]
            Xa = North
            Xb = C
        elif Move in LungeDown:
            Dia = M.grid[South][C]
            Xa = South
            Xb = C
        elif Move in LungeLeft:
            Dia = M.grid[R][West]
            Xa = R
            Xb = West
        elif Move in LungeRight:
            Dia = M.grid[R][East]
            Xa = R
            Xb = East
        else:
            Dia = M.grid[R][C]
            Xa = R
            Xb = C
        if M.MG == 1:
            if M.MN == 0:
                if Dia == 5:  # encounter with river and lake, Dia is used when there should be 1 dialog for all
                    A = Firay()
                    print("\n" * 200)
                    print(A.e00, end='')
                    con00 = input(A.i007)
                    print(A.e02, end='')
                    con01 = input(A.i008)
                    print(A.e02, end='')
                    con02 = input(A.i009)
                    done = True
                    break
                else:
                    done = True
            if M.MN == 1:
                if Xa == 9 and Xb == 7:  # encounter with Rubi next to table
                    A = Firay()
                    B = Rubi()
                    print("\n" * 200)
                    # make quest getting thing more flexible to allow future additions easily
                    if Q.GetClearLeaf == "Active" and It.ItemClearLeaf is True:
                        print(A.e00, end='')  # quest complete dialogue
                        con00 = input(A.t004)
                        print(B.e00, end='')
                        con01 = input(B.t008)
                        print(A.e05, end='')
                        con02 = input(A.t005)
                        print(B.e00, end='')
                        con03 = input(B.t009)
                        print(B.e00, end='')
                        con04 = input(B.t010)
                        print(A.e00, end='')
                        con05 = input(A.t006)
                        print(B.e00, end='')
                        con06 = input(B.t011)
                        print(B.e00, end='')
                        con07 = input(B.t012)
                        print(B.e04, end='')
                        con08 = input(B.t013)
                        print(A.e05, end='')
                        con09 = input(A.t007)
                        print(B.e00, end='')
                        con10 = input(B.t014)
                        print(A.e00, end='')
                        con11 = input(A.t008)
                        N = int(0)
                        while N <= 4:
                            if CurQue[N] == Sys.q0001:
                                CurQue[N] = str("Empty")
                                ProQue[N] = int(3)
                                print(Sys.qXXX.format(Sys.q0001))
                                Q.GetClearLeaf = "Complete"
                            if CurInv[N] == Sys.i0001:
                                CurInv[N] = str("Empty")
                                ProInv[N] = int(0)
                                It.ItemClearLeaf = False
                            else:
                                N = N + 1
                        proceed = input("Press enter to continue...")
                    elif Q.GetClearLeaf == "Active" and It.ItemClearLeaf is False:
                        print(B.e01, end='')  # when quest has already been given
                        con00 = input(B.t007)
                    elif Q.GetClearLeaf == "Complete":
                        print(A.e00, end='')  # quest is complete
                        con00 = input(A.t009)
                    elif Q.GetClearLeaf == "Inactive":
                        print(B.e00, end='')  # Rubi giving quest
                        con00 = input(B.t000)
                        print(A.e00, end='')
                        con01 = input(A.t001)
                        print(B.e01, end='')
                        con02 = input(B.t001)
                        print(B.e00, end='')
                        con03 = input(B.t002)
                        print(A.e00, end='')
                        con04 = input(A.t002)
                        print(B.e00, end='')
                        con05 = input(B.t003)
                        print(A.e00, end='')
                        con06 = input(A.t003)
                        print(B.e02, end='')
                        con07 = input(B.t004)
                        print(B.e03, end='')
                        con08 = input(B.t005)
                        print(B.e00, end='')
                        con09 = input(B.t006)
                        N = int(0)
                        Empty = False
                        while N <= 4:
                            if ProQue[N] == int(0):
                                CurQue[N] = str(Sys.q0001)
                                ProQue[N] = int(1)
                                Empty = True
                                print(Sys.q0000.format(Que))
                                Q.GetClearLeaf = "Active"
                                break
                            else:
                                N = N + 1
                        if Empty is False:
                            print("\nThere's no space to add a new quest!")
                        proceed = input("Press enter to continue...")
                    done = True
                    break
                elif Xa == 11 and Xb == 8:  # encounter with John at entrance
                    A = Firay()
                    B = John()
                    print("\n" * 200)
                    print(A.e00, end='')
                    con00 = input(A.t010)
                    print(B.e00, end='')
                    con01 = input(B.t000)
                    print(A.e05, end='')
                    con02 = input(A.t011)
                    print(B.e01, end='')
                    con03 = input(B.t001)
                    done = True
                    break
                elif Xa in [4, 5] and Xb == 11:  # encounter with own bed
                    A = Firay()
                    print("\n" * 200)
                    print(A.e00, end='')
                    con00 = input(A.i001)
                    done = True
                    break
                elif Xa == 2 and Xb in [2, 3]:  # encounter with Rubi's bed
                    A = Firay()
                    print("\n" * 200)
                    print(A.e01, end='')
                    con00 = input(A.i002)
                    print(A.e02, end='')
                    con01 = input(A.i003)
                    done = True
                    break
                elif Xa in [9, 10] and Xb in [4, 5, 6]:  # encounter with table
                    A = Firay()
                    print("\n" * 200)
                    print(A.e00, end='')
                    con00 = input(A.i004)
                    print(A.e02, end='')
                    con01 = input(A.i005)
                    print(A.e03, end='')
                    con02 = input(A.i006)
                    done = True
                    break
                else:
                    done = True
            if M.MN == 2:
                if Xa in [7, 8, 9] and Xb in [5, 6, 7, 8]:  # encounter with table
                    A = Firay()
                    print("\n" * 200)
                    print(A.e02, end='')
                    con00 = input(A.i010)
                    done = True
                    break
                elif Xa == 6 and Xb == 7:  # Firay meeting with Ravia
                    A = Firay()
                    B = Ravia()
                    print("\n" * 200)
                    if Q.GetClearLeaf == "Inactive" and It.ItemClearLeaf is False:
                        print(B.e01, end='')  # no quest, no item
                        con00 = input(B.t005)
                    elif It.ItemClearLeaf is True or Q.GetClearLeaf == "Complete":
                        print(B.e01, end='')  # item already given, or quest finished
                        con00 = input(B.t004)
                    elif Q.GetClearLeaf == "Active" and It.ItemClearLeaf is False:
                        print(B.e01, end='')  # quest active and Ravia giving Firay the quest item
                        con00 = input(B.t000)
                        print(A.e00, end='')
                        con01 = input(A.t012)
                        print(B.e00, end='')
                        con02 = input(B.t001)
                        print(B.e00, end='')
                        con03 = input(B.t002)
                        print(A.e00, end='')
                        con04 = input(A.t013)
                        print(B.e01, end='')
                        con05 = input(B.t003)
                        N = int(0)
                        Empty = False
                        while N <= 4:
                            if CurInv[N] == "Empty":
                                CurInv[N] = str(Sys.i0001)
                                ProInv[N] = It.TypeClearLeaf
                                Empty = True
                                print(Sys.i0000.format(Inv))
                                It.ItemClearLeaf = True
                                break
                            else:
                                N = N + 1
                        if Empty is False:
                            print("\nThere's no space for another item!")
                        proceed = input("Press enter to continue...")
                    done = True
                    break
                else:
                    done = True
        if done is True:
            dialogue = False
    while Door is True:
        Za = R
        Zb = C
        if M.MG == 1:
            if M.MN == 0:  # doors for Mithavil
                if Za == 5 and Zb == 12:
                    M = Home()
                    R = int(11)
                    C = int(9)
                    break
                if Za == 17 and Zb == 10:
                    M = Raviahouse()
                    R = int(9)
                    C = int(2)
                    break
                else:
                    break
            if M.MN == 1:  # doors for Home
                if Za == 11 and Zb == 10:
                    M = Mithavil()
                    R = int(6)
                    C = int(12)
                    break
                else:
                    break
            if M.MN == 2:  # doors for Ravia's House
                if Za == 10 and Zb == 2:
                    M = Mithavil()
                    R = int(17)
                    C = int(9)
                else:
                    break
            else:
                break
"""Change-log
0.1: Started project, and made visual map
0.2: Added movement
0.3: Added speech
0.4: Graphic improvement?
0.5: more coding stuff, specifically labeling and doors
0.5.1: Added location name and changed the control settings graphics
0.5.2: Text for table, and more graphic improvements
0.6: River text
0.6.1: Minor text shenanigans
0.6.2: Added E to more stuff
0.7: Map redesigned for 7 by 7 grid, better suited for viewing since tunnel vision does no justice.
0.7.1: Started changing map to 7x7 grid
0.7.2: Implemented in visual map
0.7.3: Added John
0.7.4: Added more comments for easier interpretation
0.8: Started lunge
0.8.1: Fixed problem where Xa and Xb aren't defined
0.8.2: Added lunge to all control schemes
0.9: Added stamina
0.9.1: Added text for stamina
0.9.2: Minor graphic improvements
0.9.3: Fixed Xa and Xb undefined bug
0.9.4: Added system message to check font
0.10: Started quest thing
0.10.1: fixed version number and changed stamina regen
0.10.2: Mapped key for quest
0.10.3: Minor bug fixes
0.10.4: Applied quest thing for all control schemes
0.11: Started Inventory thing
0.11.1: Added Ravia's home
0.11.2: Switched graphic things around
0.11.3: changed the way chatting works
0.11.4: Ravia interaction added
0.11.5: bug fixes
0.11.6: Added Rubi dialogue for when quest complete and changed quest status
0.11.7: Programmed quest complete
0.12: integrated inventory to all control schemes
0.12.1: did something about the control visual
# Big change here
0.13: Completely redid how text is loaded and printed, and changed some visuals to distinguish Firay
0.13.1: Fixed new line error and extended NUMP to NUMPAD
0.13.2: Made maps more distinguishable
0.14: Started save function
"""