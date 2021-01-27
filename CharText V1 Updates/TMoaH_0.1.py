"""
< The Mark of a Hero >

by FOKKUSU~
Ver: 0.X

description: Using what I've learnt with BattleShell and Maze Game, I've created a turn-based RPG
"""
import random
# variable listing
Loop = True
map0, map1, map2, map3, map4, map5, map6, map7, map8, map9 = "", "", "", "", "", "", "", "", "", ""
ran = int(0)


# Map function
def loader(n):
    global ran
    global map0, map1, map2, map3, map4, map5, map6, map7, map8, map9
    if n == 1:
        if ran <= 25:
            map0 = "ᵩ"  # Empty space
            map5 = "ﬓ"  # River/lake
        elif 25 < ran <= 50:
            map0 = " "
            map5 = "ﬔ"
        elif 50 < ran <= 75:
            map0 = " "
            map5 = "ﬕ"
        elif 75 < ran:
            map0 = " "
            map5 = "ﬖ"
        map1 = "░"  # pathway
        map2 = "■"  # house
        map3 = "⌠"  # farm
        map4 = "▓"  # bridge
        map6 = "‼"  # sign
        map7 = "□"  # door
        map8 = "Ξ"  # exit
        map9 = "█"  # boundary
        return
    elif n == 2:
        map0 = " "  # space
        map1 = "◘"  # character
        map2 = "■"  # bed
        map3 = "╬"  # table
        map4 = ""  # unused
        map5 = ""  # unused
        map6 = "│"  # vertical door
        map7 = "─"  # horizontal door
        map8 = "□"  # exit
        map9 = "█"  # boundary


# Map
class Mithavil:
    MN = int(1)  # Map number
    MT = int(0)  # Map layer
    ML = int(1)  # Map loader number, just in case the graphics have to change
    Name = "Mithavil"
    # Key 0 = space, 1 = path, 2 = house, 3 = farm, 4 = bridge, 5 = river/lake, 6 = sign, 7 = door, 8 = exit, 9 = bound
    # Count  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
    grid = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 0
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 1
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 2
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 3
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 3, 3, 2, 2, 2, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 7, 0, 0, 0, 0, 0, 0, 9, 9],  # 4
            [9, 9, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 7, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 0, 1, 0, 0, 0, 0, 0, 9, 9],  # 5
            [9, 9, 4, 4, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 9],  # 6
            [9, 9, 4, 4, 1, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 4, 0, 0, 5, 5, 9, 9],  # 7
            [9, 9, 4, 4, 0, 0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 4, 5, 5, 0, 0, 9, 9],  # 8
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 4, 0, 0, 0, 0, 9, 9],  # 9
            [9, 9, 5, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 9],  # 10
            [9, 9, 0, 5, 5, 5, 5, 4, 5, 5, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 9],  # 11
            [9, 9, 0, 0, 0, 0, 0, 4, 0, 0, 5, 5, 5, 0, 0, 0, 0, 5, 5, 5, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 9, 9],  # 12
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 9, 9],  # 13
            [9, 9, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 9, 9],  # 14
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 1, 0, 0, 2, 2, 2, 0, 9, 9],  # 15
            [9, 9, 0, 0, 2, 2, 0, 0, 1, 0, 0, 2, 2, 2, 0, 5, 5, 5, 5, 5, 5, 0, 0, 1, 1, 1, 7, 2, 2, 2, 0, 9, 9],  # 16
            [9, 9, 0, 0, 2, 2, 7, 1, 1, 1, 7, 2, 2, 2, 0, 0, 5, 5, 5, 5, 5, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 17
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 5, 5, 5, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 18
            [9, 9, 0, 0, 0, 0, 0, 0, 1, 1, 7, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 19
            [9, 9, 0, 2, 2, 2, 7, 1, 1, 0, 0, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 20
            [9, 9, 0, 2, 2, 2, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 21
            [9, 9, 0, 2, 2, 2, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 22
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 9, 9],  # 23
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 9, 9],  # 24
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 1, 7, 2, 2, 2, 2, 2, 2, 2, 0, 9, 9],  # 25
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 6, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 9, 9],  # 26
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 27
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 28
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 29
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 6, 6, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 30
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 31
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 32
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 33
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]  # 34
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
    MN = int(1)  # Map number
    MT = int(1)  # Map layer
    ML = int(2)  # Map loader
    Name = "Firay's Home"
    # Key 0 = space, 1 = character, 2 = bed, 3 = table, 6 = Vdoor, 7 = Hdoor, 8 = exit, 9 = bound
    # Count 0  1  2  3  4  5  6  7  8  9 10 11 12 13
    grid = [[9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 0
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 1
            [9, 9, 2, 2, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9],  # 2
            [9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9],  # 3
            [9, 9, 9, 7, 9, 9, 9, 9, 0, 0, 0, 2, 9, 9],  # 4
            [9, 9, 0, 0, 0, 0, 0, 9, 0, 0, 0, 2, 9, 9],  # 5
            [9, 9, 0, 0, 0, 0, 0, 6, 0, 0, 0, 0, 9, 9],  # 6
            [9, 9, 0, 0, 0, 0, 0, 9, 9, 9, 9, 9, 9, 9],  # 7
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 9, 9],  # 8
            [9, 9, 0, 0, 3, 3, 3, 1, 0, 0, 0, 0, 9, 9],  # 9
            [9, 9, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 9, 9],  # 10
            [9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 8, 0, 9, 9],  # 11
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9],  # 12
            [9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9, 9]]  # 13
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
    XX  TTTR    XX 09
    XX  TTT     XX 10
    XX        D XX 11
    XXXXXXXXXXXXXX 12
    XXXXXXXXXXXXXX 13
    """


M = Home()
R = int(5)
C = int(9)
while Loop is True:
    MAP = False
    North = R - 1
    South = R + 1
    West = C - 1
    East = C + 1
    MapN = R - 2  # only used in map
    MapS = R + 2  # only used in map
    MapW = C - 2  # only used in map
    MapE = C + 2  # only used in map
    while MAP is not True:  # This creates a 5x5 grid.
        if M.ML == 1:
            loader(1)
        elif M.ML == 2:
            loader(2)
        View = [[1, 2, 3, 4, 5],
                [6, 7, 8, 9, 10],
                [11, 12, 13, 14, 15],
                [16, 17, 18, 19, 20],
                [21, 22, 23, 24, 25]]
        A = int(0)  # Column counter
        D = int(1)  # Row 1
        E = int(1)  # Row 2
        F = int(1)  # Row 3
        G = int(1)  # Row 4
        H = int(1)  # Row 5
        # printing grid:
        View1 = [M.grid[MapN][MapW], M.grid[MapN][West], M.grid[MapN][C], M.grid[MapN][East], M.grid[MapN][MapE]]
        View2 = [M.grid[North][MapW], M.grid[North][West], M.grid[North][C], M.grid[North][East], M.grid[North][MapE]]
        View3 = [M.grid[R][MapW], M.grid[R][West], M.grid[R][C], M.grid[R][East], M.grid[R][MapE]]
        View4 = [M.grid[South][MapW], M.grid[South][West], M.grid[South][C], M.grid[South][East], M.grid[South][MapE]]
        View5 = [M.grid[MapS][MapW], M.grid[MapS][West], M.grid[MapS][C], M.grid[MapS][East], M.grid[MapS][MapE]]
        while D != 6:  # Row 1 generator
            ran = random.randint(1, 100)
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
        while E != 6:  # Row 2 generator
            ran = random.randint(1, 100)
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
        while F != 6:  # Row 3 generator
            ran = random.randint(1, 100)
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
        while G != 6:  # Row 4 generator
            ran = random.randint(1, 100)
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
        while H != 6:  # Row 5 generator
            ran = random.randint(1, 100)
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
        MAP = True
    print("\n      <<[MAP]>>"
          "\n ┏━━━━━━NORTH━━━━━━┓ "
          "\n ┃ {0}{0}{0}{1}{1}{1}{2}{2}{2}{3}{3}{3}{4}{4}{4} ┃ "
          "\n ┃ {0}{0}{0}{1}{1}{1}{2}{2}{2}{3}{3}{3}{4}{4}{4} ┃ "
          "\n ┃ {5}{5}{5}{6}{6}{6}{7}{7}{7}{8}{8}{8}{9}{9}{9} ┃ "
          "\n W {5}{5}{5}{6}{6}{6}{7}{7}{7}{8}{8}{8}{9}{9}{9} E "
          "\n E {10}{10}{10}{11}{11}{11}Ʌ̼Ʌ{13}{13}{13}{14}{14}{14} A "
          "\n S {10}{10}{10}{11}{11}{11}YOU{13}{13}{13}{14}{14}{14} S "
          "\n T {15}{15}{15}{16}{16}{16}{17}{17}{17}{18}{18}{18}{19}{19}{19} T "
          "\n ┃ {15}{15}{15}{16}{16}{16}{17}{17}{17}{18}{18}{18}{19}{19}{19} ┃ "
          "\n ┃ {20}{20}{20}{21}{21}{21}{22}{22}{22}{23}{23}{23}{24}{24}{24} ┃ "
          "\n ┃ {20}{20}{20}{21}{21}{21}{22}{22}{22}{23}{23}{23}{24}{24}{24} ┃ "
          "\n ┗━━━━━━SOUTH━━━━━━┛"
          .format(View[0][0], View[0][1], View[0][2], View[0][3], View[0][4],
                  View[1][0], View[1][1], View[1][2], View[1][3], View[1][4],
                  View[2][0], View[2][1], View[2][2], View[2][3], View[2][4],
                  View[3][0], View[3][1], View[3][2], View[3][3], View[3][4],
                  View[4][0], View[4][1], View[4][2], View[4][3], View[4][4]))
    Continue = input("Press enter to continue")
    if Continue in "LOl":
        print("lol")
    elif Continue not in "LOl":
        Loop = False


"""Change-log
0.1: Started project, and made visual map"""