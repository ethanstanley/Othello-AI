import sys
import random
import time
neighbors = {0: [1, 8, 9], 1: [2, 0, 8, 9, 10], 2: [3, 1, 9, 10, 11], 3: [4, 2, 10, 11, 12], 4: [5, 3, 11, 12, 13], 5: [6, 4, 12, 13, 14], 6: [7, 5, 13, 14, 15], 7: [6, 15, 14], 8: [9, 0, 1, 16, 17], 9: [10, 8, 2, 1, 0, 16, 17, 18], 10: [11, 9, 3, 2, 1, 17, 18, 19], 11: [12, 10, 4, 3, 2, 18, 19, 20], 12: [13, 11, 5, 4, 3, 19, 20, 21], 13: [14, 12, 6, 5, 4, 20, 21, 22], 14: [15, 13, 7, 6, 5, 21, 22, 23], 15: [14, 7, 6, 23, 22], 16: [17, 8, 9, 24, 25], 17: [18, 16, 10, 9, 8, 24, 25, 26], 18: [19, 17, 11, 10, 9, 25, 26, 27], 19: [20, 18, 12, 11, 10, 26, 27, 28], 20: [21, 19, 13, 12, 11, 27, 28, 29], 21: [22, 20, 14, 13, 12, 28, 29, 30], 22: [23, 21, 15, 14, 13, 29, 30, 31], 23: [22, 15, 14, 31, 30], 24: [25, 16, 17, 32, 33], 25: [26, 24, 18, 17, 16, 32, 33, 34], 26: [27, 25, 19, 18, 17, 33, 34, 35], 27: [28, 26, 20, 19, 18, 34, 35, 36], 28: [29, 27, 21, 20, 19, 35, 36, 37], 29: [30, 28, 22, 21, 20, 36, 37, 38], 30: [31, 29, 23, 22, 21, 37, 38, 39], 31: [30, 23, 22, 39, 38], 32: [33, 24, 25, 40, 41], 33: [34, 32, 26, 25, 24, 40, 41, 42], 34: [35, 33, 27, 26, 25, 41, 42, 43], 35: [36, 34, 28, 27, 26, 42, 43, 44], 36: [37, 35, 29, 28, 27, 43, 44, 45], 37: [38, 36, 30, 29, 28, 44, 45, 46], 38: [39, 37, 31, 30, 29, 45, 46, 47], 39: [38, 31, 30, 47, 46], 40: [41, 32, 33, 48, 49], 41: [42, 40, 34, 33, 32, 48, 49, 50], 42: [43, 41, 35, 34, 33, 49, 50, 51], 43: [44, 42, 36, 35, 34, 50, 51, 52], 44: [45, 43, 37, 36, 35, 51, 52, 53], 45: [46, 44, 38, 37, 36, 52, 53, 54], 46: [47, 45, 39, 38, 37, 53, 54, 55], 47: [46, 39, 38, 55, 54], 48: [49, 40, 41, 56, 57], 49: [50, 48, 42, 41, 40, 56, 57, 58], 50: [51, 49, 43, 42, 41, 57, 58, 59], 51: [52, 50, 44, 43, 42, 58, 59, 60], 52: [53, 51, 45, 44, 43, 59, 60, 61], 53: [54, 52, 46, 45, 44, 60, 61, 62], 54: [55, 53, 47, 46, 45, 61, 62, 63], 55: [54, 47, 46, 63, 62], 56: [57, 48, 49], 57: [58, 56, 50, 49, 48], 58: [59, 57, 51, 50, 49], 59: [60, 58, 52, 51, 50], 60: [61, 59, 53, 52, 51], 61: [62, 60, 54, 53, 52], 62: [63, 61, 55, 54, 53], 63: [62, 55, 54]}
CONSTRAINTS = [[[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]], [[0, 8, 16, 24, 32, 40, 48, 56], [1, 9, 17, 25, 33, 41, 49, 57], [2, 10, 18, 26, 34, 42, 50, 58], [3, 11, 19, 27, 35, 43, 51, 59], [4, 12, 20, 28, 36, 44, 52, 60], [5, 13, 21, 29, 37, 45, 53, 61], [6, 14, 22, 30, 38, 46, 54, 62], [7, 15, 23, 31, 39, 47, 55, 63]], [[2, 9, 16], [3, 10, 17, 24], [4, 11, 18, 25, 32], [5, 12, 19, 26, 33, 40], [6, 13, 20, 27, 34, 41, 48], [7, 14, 21, 28, 35, 42, 49, 56], [57, 50, 43, 36, 29, 22, 15], [58, 51, 44, 37, 30, 23], [59, 52, 45, 38, 31], [60, 53, 46, 39], [61, 54, 47]], [[0, 9, 18, 27, 36, 45, 54, 63], [1, 10, 19, 28, 37, 46, 55], [2, 11, 20, 29, 38, 47], [3, 12, 21, 30, 39], [4, 13, 22, 31], [5, 14, 23], [58, 49, 40], [59, 50, 41, 32], [60, 51, 42, 33, 24], [61, 52, 43, 34, 25, 16], [62, 53, 44, 35, 26, 17, 8]]]
seqMoves = []
findAvSpots = {}
changeBoardSpots = {}
def prioritizeMoves(brd, tkn, moves):
    enemy = "XO"[tkn == 'X']
    posWeight = [10, -6, 2, 2, 2, 2, -6, 10,
                -6, -10, -1, -1, -1, -1, -10, -6,
               2, -1, 1, 0, 0, 1, -1, 2,
               2, -1, 0, 1, 1, 0, -1, 2,
               2, -1, 0, 1, 1, 0, -1, 2,
               2, -1, 1, 0, 0, 1, -1, 2,
               -6, -10, -1, -1, -1, -1, -10, -6,
               10, -6, 2, 2, 2, 2, -6, 10]
    weights = {}
    for m in moves:
        weights[m] = 0
    for mv in moves:
        newb = changeBoard(brd, tkn, mv)
        numMovesTkn = findAvailableSpots(newb, tkn)
        numMovesEn = findAvailableSpots(newb, enemy)
        weights[mv] += posWeight[mv]
        if len(numMovesEn) == 0:
            weights[mv] += 5
        elif len(numMovesEn) < 3 and numMovesEn < numMovesTkn:
            weights[mv] += 3
        elif len(numMovesEn) < len(numMovesTkn):
            weights[mv] += 2
        elif len(numMovesEn) == len(numMovesTkn):
            weights[mv] = weights[mv]
        elif len(numMovesEn) - 3 > len(numMovesTkn):
            weights[mv] -= 3
        else:
            weights[mv] -= 2

        if (newb.count(tkn) - newb.count(enemy)) - (brd.count(tkn) - brd.count(enemy)) > 10:
            weights[mv] += 5
        elif (newb.count(tkn) - newb.count(enemy)) - (brd.count(tkn) - brd.count(enemy)) > 5:
            weights[mv] += 3
        elif (newb.count(tkn) - newb.count(enemy)) - (brd.count(tkn) - brd.count(enemy)) > 0:
            weights[mv] += 1
        else:
            weights[mv] = weights[mv]

    returnlist = []
    while len(weights) > 0:
        max_value = max(weights.values())  # maximum value
        max_keys = [k for k, v in weights.items() if v == max_value]
        returnlist += max_keys
        for key in max_keys:
            weights.pop(key, None)
    return returnlist

def convert(move):
    return move + 2 * (move//8) + 11

def evaluateBoard(brd, tkn, avSpotsTkn, avSpotsEnemy):
    heuristicValue = 0
    optkn = "XO"[tkn == "X"]
    if len(avSpotsTkn) + len(avSpotsEnemy) != 0:
        heuristicValue += 100 * ((len(avSpotsTkn) - len(avSpotsEnemy))/ (len(avSpotsTkn) + len(avSpotsEnemy)))
    cornersOp = []
    cornersTkn = []
    for spot in [0, 7, 56, 63]:
        if brd[spot] == tkn:
            cornersTkn.append(spot)
        elif brd[spot] == optkn:
            cornersOp.append(spot)
    if len(cornersOp) + len(cornersTkn) > 0:
        heuristicValue += 100 * (len(cornersTkn) - len(cornersOp)) / (len(cornersTkn) + len(cornersOp))
    heuristicValue += 100 * ((brd.count(tkn) - brd.count(optkn))/(brd.count(tkn) + brd.count(optkn)))
    badSpotCountTkn = 0
    badSpotCountEnemy = 0
    safeSpotTkn = 0
    safeSpotEnemy = 0
    for badspot in [1, 6, 8, 9, 14, 15, 48, 49, 54, 55, 57, 62]:
        if badspot in {1, 8, 9}:
            if brd[badspot] == tkn:
                if 0 in cornersTkn:
                    safeSpotTkn += 1
                else:
                    badSpotCountTkn += 1
            elif brd[badspot] == optkn:
                if 0 in cornersOp:
                    safeSpotEnemy += 1
                else:
                    badSpotCountEnemy += 1
        if badspot in {6, 14, 15}:
            if brd[badspot] == tkn:
                if 7 in cornersTkn:
                    safeSpotTkn += 1
                else:
                    badSpotCountTkn += 1
            elif brd[badspot] == optkn:
                if 7 in cornersOp:
                    safeSpotEnemy += 1
                else:
                    badSpotCountEnemy += 1
        if badspot in {48, 49, 57}:
            if brd[badspot] == tkn:
                if 56 in cornersTkn:
                    safeSpotTkn += 1
                else:
                    badSpotCountTkn += 1
            elif brd[badspot] == optkn:
                if 56 in cornersOp:
                    safeSpotEnemy += 1
                else:
                    badSpotCountEnemy += 1
        if badspot in {54, 55, 62}:
            if brd[badspot] == tkn:
                if 63 in cornersTkn:
                    safeSpotTkn += 1
                else:
                    badSpotCountTkn += 1
            elif brd[badspot] == optkn:
                if 63 in cornersOp:
                    safeSpotEnemy += 1
                else:
                    badSpotCountEnemy += 1
    if badSpotCountEnemy + badSpotCountTkn > 0:
        heuristicValue += 100 * ((badSpotCountEnemy - badSpotCountTkn)/(badSpotCountEnemy + badSpotCountTkn))
    if safeSpotTkn + safeSpotEnemy > 0:
        heuristicValue += 50 * ((safeSpotTkn - safeSpotEnemy)/(safeSpotEnemy + safeSpotTkn))
    return heuristicValue
def evalalp(brd, tkn):
    table = [20, -3, 2, 2, 2, 2, -3, 20,
             -3, -10, -1, -1, -1, -1, -10, -3,
             2, -1, 1, 0, 0, 1, -1, 2,
             2, -1, 0, 1, 1, 0, -1, 2,
             2, -1, 0, 1, 1, 0, -1, 2,
             2, -1, 1, 0, 0, 1, -1, 2,
             -3, -10, -1, -1, -1, -1, -10, -3,
             20, -3, 2, 2, 2, 2, -3, 20]
    it = "XO"[tkn == 'X']
    good = 0
    bad = 0
    for index, tok in enumerate(brd):
        if tkn == tok:
            good += table[index]
        elif it == tok:
            bad += table[index]
    return good - bad

def makePosition(value):
    if value[0] not in "0123456789":
        letter = ord(value[0].upper()) - 65
        pos = int(value[1]) - 1
        posit = pos * 8 + letter
    else:
        posit = int(value)
    return posit

def printBoard(board):
    print("")
    for x in range(0, 63, 8):
        stringToPrint = " "
        for y in range(x, x+8):
            stringToPrint += board[y] + " "
        stringToPrint += "         "
        print(stringToPrint)
    print("")

def findAvailableSpots(board, token):
    global findAvSpots
    if (board, token) in findAvSpots:
        return findAvSpots[board, token]
    opLocs = []
    avSpots = []
    for tokFinder in range(0, 64):
        if board[tokFinder] != token and board[tokFinder] != ".":
            opLocs.append(tokFinder)
    for op in opLocs:
        constraintsIn = []
        for constraint in CONSTRAINTS:
            for c in constraint:
                if op in c:
                    constraintsIn.append(c)
        neighs = neighbors[op]
        openNeighs = []
        for neigh in neighs:
            if board[neigh] == '.':
                openNeighs.append(neigh)
        if len(openNeighs) == 0:
            continue
        for neigh in openNeighs:
            typeOfNeigh = ""
            for C in constraintsIn:
                ind = -1
                if neigh in C:
                    ind = C.index(neigh)
                if ind != -1:
                    if C[ind - 1] == op:
                        for nextind in range(ind - 1, -1, -1):
                            if board[C[nextind]] == token:
                                avSpots.append(neigh)
                                break
                            if board[C[nextind]] == '.':
                                break
                    else:
                        for nextind in range(ind + 1, len(C)):
                            if board[C[nextind]] == token:
                                avSpots.append(neigh)
                                break
                            if board[C[nextind]] == '.':
                                break
                    break
    findAvSpots[(board, token)] = set(avSpots)
    return findAvSpots[(board, token)]

def changeBoard(board, token, position):
    indiciesToChange = [position]
    optoken = 'X' if token == "O" else "O"
    for constraint in CONSTRAINTS:
        for c in constraint:
            if position in c:
                i = c.index(position)
                oploc = []
                for nindex in range(i + 1, len(c)):
                    if board[c[nindex]] == '.':break
                    elif board[c[nindex]] == optoken: oploc.append(c[nindex])
                    else:
                        indiciesToChange = indiciesToChange + oploc
                        break
                oploc = []
                for nindex in range(i - 1, -1, -1):
                    if board[c[nindex]] == '.': break
                    elif board[c[nindex]] == optoken: oploc.append(c[nindex])
                    else:
                        indiciesToChange = indiciesToChange + oploc
                        break

    for thing in indiciesToChange:
        board = board[:thing] + token + board[thing + 1:]
    return board

def getScore(board):
    return ((sum([1 for x in board if x =="X"])), sum([1 for y in board if y == "O"]))

def findBestMove(board, token):
    CORNERS = {0, 7, 56, 63}
    nextCORNERS = {1, 6, 8, 9, 14, 15, 48, 49, 54, 55, 57, 62}
    bestMove = -1
    safeMoves = []
    revisedMoves = []
    tokensBefore = board.count('X')
    cornersCAPPED = set([t for t in CORNERS if board[t] == token])
    avMoves = list(findAvailableSpots(board, token))
    top = sum([1 for x in CONSTRAINTS[0][0] if board[x] == '.'])
    bot = sum([1 for x in CONSTRAINTS[0][7] if board[x] == '.'])
    left = sum([1 for x in CONSTRAINTS[1][0] if board[x] == '.'])
    right = sum([1 for x in CONSTRAINTS[1][7] if board[x] == '.'])
    for index, tok in enumerate(avMoves):
        if tok in CORNERS:
            return tok
        if tok not in nextCORNERS:
            revisedMoves.append(tok)
        else:
            if tok in {1, 8, 9} and board[0] == token:
                safeMoves.append(tok)
            elif tok in {6, 14, 15} and board[7] == token:
                safeMoves.append(tok)
            elif tok in {48, 49, 57} and board[56] == token:
                safeMoves.append(tok)
            elif tok in {54, 55, 62} and board[63] == token:
                safeMoves.append(tok)
        if tok in CONSTRAINTS[0][0] and top == 1:
            safeMoves.append(tok)
        if tok in CONSTRAINTS[0][7] and bot == 1:
            safeMoves.append(tok)
        if tok in CONSTRAINTS[1][0] and left == 1:
            safeMoves.append(tok)
        if tok in CONSTRAINTS[1][7] and right == 1:
            safeMoves.append(tok)


    if len(safeMoves) > 0:
        return safeMoves[random.randint(0, len(safeMoves) - 1)]             #Find which moves are best here
    if len(revisedMoves) > 0:
        return revisedMoves[random.randint(0, len(revisedMoves) - 1)]
    return avMoves.pop()


def alphabetaa(brd, tkn, lowerBnd, upperBnd):
    enemy = "XO"[tkn == 'X']
    tkSpots = findAvailableSpots(brd, token)
    if len(tkSpots) == 0:
        if len(findAvailableSpots(brd, enemy)) == 0:
            return [brd.count(tkn) - brd.count(enemy)]
        ab = alphabetaa(brd, enemy, -upperBnd, -lowerBnd) # game not over
        return [-ab[0]] + ab[1:] + [-1]
    best = [lowerBnd-1]
    for mv in tkSpots:
        ab = alphabetaa(changeBoard(brd,tkn,mv), enemy, -upperBnd, -lowerBnd)
        ab[0] = -ab[0]
        score = ab[0]
        if score > upperBnd:
            return [score] # Vile to the caller
        if score < lowerBnd:
            continue # Not an improvement
        best = max(best, ab) + [mv]
        lowerBnd = score+1
    return best


def alphabeta(brd, tkn, depth, first, lowerBnd, upperBnd):
    enemy = "XO"[tkn == 'X']
    tkSpots = findAvailableSpots(brd, tkn)
    tkEnemy = set([])
    if first == True:
        tkSpots = prioritizeMoves(brd, tkn, tkSpots)
    if len(tkSpots) == 0:
        tkEnemy = findAvailableSpots(brd, enemy)
        if len(tkEnemy) == 0:
            if brd.count(tkn) > brd.count(enemy):
                return [10000]
            else:
                return [-10000]
        if depth == 0:
            first = True
            return [evaluateBoard(brd, tkn, tkSpots, tkEnemy)]
        ab = alphabeta(brd, enemy, depth - 1, False, -upperBnd, -lowerBnd) # game not over
        return [-ab[0]] + ab[1:] + [-1]
    best = [lowerBnd-1]
    if depth == 0:
        return [evaluateBoard(brd, tkn, tkSpots, tkEnemy)]
    for mv in tkSpots:
        newB = changeBoard(brd,tkn,mv)
        ab = alphabeta(newB, enemy, depth - 1, False, -upperBnd, -lowerBnd)
        ab[0] = -ab[0]
        score = ab[0]
        if score > upperBnd:
            return [score] # Vile to the caller
        if score < lowerBnd:
            continue # Not an improvement
        best = [score] + ab[1:] + [mv]
        lowerBnd = score+1
    return best

class Strategy():
    def best_strategy(self, board, player, best_move, running):
        board = board.replace("?", "")
        board = board.replace("@", "X")
        board = board.replace("o", "O")
        board = board.replace("0", "O")

        if player == '@':
            player = "X"
        elif player == "o" or player == "0":
            player = "O"

        thing = findBestMove(board, player)
        if thing != -1:
            best_move.value = convert(thing)

        if board.count('.') < 13:
            n = alphabetaa(board, player, -65, 65)
            best_move.value = convert(n.pop())
        else:
            for depth in range(1, 10):
                midgame = alphabeta(board, player, depth, True, -10000, 10000)
                best_move.value = convert(midgame.pop())

def main(board, token):
    print("here")
    thing = findBestMove(board, token)
    print(thing)
    if board.count('.') < 13:
        n = alphabetaa(board, token, -65, 65)
        print(n)
    else:
        print(findAvailableSpots(board, token))
        for depth in range(1, 10):
            midgame = alphabeta(board, token, depth, True, -10000, 10000)
            print("Score: ", midgame[0], "Rest: ", midgame[1:])

if __name__ == "__main__":
    board = sys.argv[1]
    token = sys.argv[2]
    main(board, token)
