var c = document.getElementById("myCanvas");
var ctx = c.getContext("2d");
ctx.beginPath();
ctx.fillStyle = "#3D9970";
ctx.lineWidth = 3;
ctx.strokeStyle = "silver"
height = 75;
width = 75;
userblack = document.getElementById("playa1").innerHTML.substring(19)
userwhite = "Guest"
if(document.getElementById("thing").innerHTML.substring(19) != '<input id="nameis" type="text" placeholder="INSERT NAME..." style="height:25px; width:75px; background-color: silver; border-color: silver;">  <button id="ok" onclick="confirmed()">OK</button>')
	userwhite = document.getElementById("thing").innerHTML.substring(19)

namecall = {"black": userblack, "white": userwhite}
getWins(userblack)
for(var x = 0; x < 8; x++)
{
    for(var y = 0; y < 8; y++)
    {
        ctx.fillRect(x*width, y*height, x*width+width, y*height + height);
        ctx.strokeRect(x*width, y*height, x*width+width, y*height + height);
    }
}
filled = {}
document.addEventListener("click", printMousePos);
for(var id = 0; id < 64; id++)
{
    filled[id] = false
}
othelloturn = "X"
var xid = [495, 570, 645, 720, 795, 870, 945, 1020]
var yid = [175, 250, 325, 400, 475, 550, 625, 700]
var begin = [0, 75, 150, 225, 300, 375, 450, 525, 600]
var centersX = [37, 112, 187, 262, 337, 412, 487, 562]
var centersY = [37, 112, 187, 262, 337, 412, 487, 562]
othellocolor = {"X":"black", "O":"white"}
document.getElementById("turn").innerHTML = namecall[othellocolor[othelloturn]] + "'s Turn"
board = "...........................OX......XO..........................."
getBoard(userblack)
console.log(document.getElementById("boardy").innerHTML) 
makeBoard(board)
possibleMoves = [19, 26, 37, 44]

CONSTRAINTS = [[[0, 1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14, 15], [16, 17, 18, 19, 20, 21, 22, 23], [24, 25, 26, 27, 28, 29, 30, 31], [32, 33, 34, 35, 36, 37, 38, 39], [40, 41, 42, 43, 44, 45, 46, 47], [48, 49, 50, 51, 52, 53, 54, 55], [56, 57, 58, 59, 60, 61, 62, 63]], 
[[0, 8, 16, 24, 32, 40, 48, 56], [1, 9, 17, 25, 33, 41, 49, 57], [2, 10, 18, 26, 34, 42, 50, 58], [3, 11, 19, 27, 35, 43, 51, 59], [4, 12, 20, 28, 36, 44, 52, 60], [5, 13, 21, 29, 37, 45, 53, 61], [6, 14, 22, 30, 38, 46, 54, 62], [7, 15, 23, 31, 39, 47, 55, 63]], 
[[2, 9, 16], [3, 10, 17, 24], [4, 11, 18, 25, 32], [5, 12, 19, 26, 33, 40], [6, 13, 20, 27, 34, 41, 48], [7, 14, 21, 28, 35, 42, 49, 56], [57, 50, 43, 36, 29, 22, 15], [58, 51, 44, 37, 30, 23], [59, 52, 45, 38, 31], [60, 53, 46, 39], [61, 54, 47]], 
[[0, 9, 18, 27, 36, 45, 54, 63], [1, 10, 19, 28, 37, 46, 55], [2, 11, 20, 29, 38, 47], [3, 12, 21, 30, 39], [4, 13, 22, 31], [5, 14, 23], [58, 49, 40], [59, 50, 41, 32], [60, 51, 42, 33, 24], [61, 52, 43, 34, 25, 16], [62, 53, 44, 35, 26, 17, 8]]]

for(m = 0; m < possibleMoves.length; m++)
{
    mv = possibleMoves[m]
    ctx.fillStyle = "#85E332";
    mvxy = getXY(mv)
    ctx.fillRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
    ctx.strokeRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
}
neighbors = {0: [1, 8, 9], 1: [2, 0, 8, 9, 10], 2: [3, 1, 9, 10, 11], 3: [4, 2, 10, 11, 12], 4: [5, 3, 11, 12, 13], 5: [6, 4, 12, 13, 14], 
6: [7, 5, 13, 14, 15], 7: [6, 15, 14], 8: [9, 0, 1, 16, 17], 9: [10, 8, 2, 1, 0, 16, 17, 18], 10: [11, 9, 3, 2, 1, 17, 18, 19], 
11: [12, 10, 4, 3, 2, 18, 19, 20], 12: [13, 11, 5, 4, 3, 19, 20, 21], 13: [14, 12, 6, 5, 4, 20, 21, 22], 14: [15, 13, 7, 6, 5, 21, 22, 23], 
15: [14, 7, 6, 23, 22], 16: [17, 8, 9, 24, 25], 17: [18, 16, 10, 9, 8, 24, 25, 26], 18: [19, 17, 11, 10, 9, 25, 26, 27], 19: [20, 18, 12, 11, 10, 26, 27, 28], 
20: [21, 19, 13, 12, 11, 27, 28, 29], 21: [22, 20, 14, 13, 12, 28, 29, 30], 22: [23, 21, 15, 14, 13, 29, 30, 31], 23: [22, 15, 14, 31, 30], 24: [25, 16, 17, 32, 33], 
25: [26, 24, 18, 17, 16, 32, 33, 34], 26: [27, 25, 19, 18, 17, 33, 34, 35], 27: [28, 26, 20, 19, 18, 34, 35, 36], 28: [29, 27, 21, 20, 19, 35, 36, 37], 29: [30, 28, 22, 21, 20, 36, 37, 38], 
30: [31, 29, 23, 22, 21, 37, 38, 39], 31: [30, 23, 22, 39, 38], 32: [33, 24, 25, 40, 41], 33: [34, 32, 26, 25, 24, 40, 41, 42], 34: [35, 33, 27, 26, 25, 41, 42, 43], 35: [36, 34, 28, 27, 26, 42, 43, 44], 
36: [37, 35, 29, 28, 27, 43, 44, 45], 37: [38, 36, 30, 29, 28, 44, 45, 46], 38: [39, 37, 31, 30, 29, 45, 46, 47], 39: [38, 31, 30, 47, 46], 40: [41, 32, 33, 48, 49], 41: [42, 40, 34, 33, 32, 48, 49, 50], 
42: [43, 41, 35, 34, 33, 49, 50, 51], 43: [44, 42, 36, 35, 34, 50, 51, 52], 44: [45, 43, 37, 36, 35, 51, 52, 53], 45: [46, 44, 38, 37, 36, 52, 53, 54], 46: [47, 45, 39, 38, 37, 53, 54, 55], 47: [46, 39, 38, 55, 54], 
48: [49, 40, 41, 56, 57], 49: [50, 48, 42, 41, 40, 56, 57, 58], 50: [51, 49, 43, 42, 41, 57, 58, 59], 51: [52, 50, 44, 43, 42, 58, 59, 60], 52: [53, 51, 45, 44, 43, 59, 60, 61], 53: [54, 52, 46, 45, 44, 60, 61, 62], 
54: [55, 53, 47, 46, 45, 61, 62, 63], 55: [54, 47, 46, 63, 62], 56: [57, 48, 49], 57: [58, 56, 50, 49, 48], 58: [59, 57, 51, 50, 49], 59: [60, 58, 52, 51, 50], 60: [61, 59, 53, 52, 51], 61: [62, 60, 54, 53, 52], 
62: [63, 61, 55, 54, 53], 63: [62, 55, 54]}
function printMousePos(event) {
    if(document.getElementById("thing").innerHTML.substring(19) != '<input id="nameis" type="text" placeholder="INSERT NAME..." style="height:25px; width:75px; background-color: silver; border-color: silver;">  <button id="ok" onclick="confirmed()">OK</button>')
        userwhite = document.getElementById("thing").innerHTML.substring(19)
    console.log(document.getElementById("boardy").innerHTML)     
    xspot = -1
    yspot = -1
    index = -1
    if(event.clientX >= 420 && event.clientX <= 1020 && event.clientY >= 100 && event.clientY <= 700)
    {
        for(var id = 0; id < 8; id++){
            if(event.clientX <= xid[id])
            {
                xspot = id
                break;
            }
        }
        for(var newid = 0; newid < 8; newid++){
            if(event.clientY <= yid[newid])
            {
                yspot = newid
                break;
            }
        }
        index = (yspot * 8) + xspot
    }
    possibleMoves = findAvailableSpots(board, othelloturn)
    if(index != -1 && filled[index] === false && possibleMoves.includes(index))
    {
        for(m = 0; m < possibleMoves.length; m++)
        {
            mv = possibleMoves[m]
            ctx.fillStyle = "#3D9970";
            mvxy = getXY(mv)
            ctx.fillRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
            ctx.strokeRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
        }
        filled[index] = true;
        var d = document.getElementById("myCanvas");
        var context = d.getContext("2d");
        color = othellocolor[othelloturn]
        board = changeBoard(board, othelloturn, index)
        if(othelloturn == "X")
            othelloturn = "O"
        else    
            othelloturn = "X"
        makeBoard(board)
        updateBoard(userblack, board)
        getBoard(userblack)
        newscore = getScore(board)
        updateScore(userblack, newscore)
        possibleMoves = findAvailableSpots(board, othelloturn)
        document.getElementById("turn").innerHTML = namecall[othellocolor[othelloturn]] + "'s Turn"
        for(m = 0; m < possibleMoves.length; m++)
        {
            mv = possibleMoves[m]
            ctx.fillStyle = "#85E332";
            mvxy = getXY(mv)
            ctx.fillRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
            ctx.strokeRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
        }
        if(possibleMoves.length == 0)
        {
            if(othelloturn == "X")
                othelloturn = "O"
            else    
                othelloturn = "X"
            possibleMoves = findAvailableSpots(board, othelloturn)
            if(possibleMoves.length == 0)
            {
                if(newscore > 0)
                {
                    updateWins(userblack);
                    document.getElementById("scoreupdate").innerHTML = "";
                }
                else if(newscore == 0)
                    document.getElementById("scoreupdate").innerHTML = "Game is over - tie game."
                else
                {
                    document.getElementById("scoreupdate").innerHTML = userwhite + " WINS!"
                }
            }
            else
            {
                document.getElementById("turn").innerHTML = namecall[othellocolor[othelloturn]] + "'s Turn"
                for(m = 0; m < possibleMoves.length; m++)
                    {
                        mv = possibleMoves[m]
                        ctx.fillStyle = "#85E332";
                        mvxy = getXY(mv)
                        ctx.fillRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
                        ctx.strokeRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
                    }
            }
        }
    }
}

function getXY(index)
{
    return [index%8, Math.floor(index/8)]
}

function makeBoard(board){
    var score = 0
    for(var index = 0; index < 64; index++)
    {
        xy = getXY(index)
        xLoc = xy[0]
        yLoc = xy[1]
        if(board[index] !='.')
        {
            filled[index] = true
            var el = document.getElementById("myCanvas");
            var context = el.getContext("2d");
            context.beginPath();
            context.arc(centersX[xLoc], centersY[yLoc], 32, 0, 2 * Math.PI, false);
            if(board[index] == 'X'){
                context.fillStyle = "black";
                score +=1;
            }
            else{
                context.fillStyle = "white";
                score -=1;
            }
            context.fill();
        }
    }
}
function changeBoard(board, token, position)
{
    var indiciesToChange = []
    indiciesToChange.push(position)
    optoken = 'X' 
    if(token == "X")
        optoken = "O"
    for(var cur = 0; cur <= 3; cur++)
    {
        constraint = CONSTRAINTS[cur]
        for(var co = 0; co < constraint.length; co++)
        {
            c = constraint[co]
            if(c.includes(position))
            {
                i = c.indexOf(position)
                oploc = []
                for(nindex = i + 1; nindex < c.length; nindex++)
                {
                    if(board[c[nindex]] == '.')
                        break;
                    else if(board[c[nindex]] == optoken)
                        oploc.push(c[nindex])
                    else
                    {
                        for(op = 0; op < oploc.length; op++)
                            indiciesToChange.push(oploc[op])
                        break;
                    }
                }
                oploc = []
                for(nindex = i - 1; nindex > -1; nindex -= 1){
                    if(board[c[nindex]] == '.')
                        break
                    else if(board[c[nindex]] == optoken)
                        oploc.push(c[nindex])
                    else
                    {
                        for(op = 0; op < oploc.length; op++)
                            indiciesToChange.push(oploc[op])
                        break
                    }
                }
            }
        }
    }
    for(thing = 0; thing < indiciesToChange.length; thing++)
    {    
        newboard = board.substring(0, indiciesToChange[thing]) + token + board.substring(indiciesToChange[thing] + 1)
        board = newboard
    }   
    return newboard
}
function findAvailableSpots(board, token)
{
    opLocs = []
    avSpots = []
    for(var tokFinder = 0; tokFinder < 64; tokFinder++)
        if(board[tokFinder] != token && board[tokFinder] != ".")
            opLocs.push(tokFinder)
    for(var o = 0; o < opLocs.length; o++)
    {
        op = opLocs[o]
        constraintsIn = []
        for(var con = 0; con < CONSTRAINTS.length; con++)
        {
            constraint = CONSTRAINTS[con]
            for(var d = 0; d < constraint.length; d++)
            {
                c = constraint[d]
                if(c.includes(op))
                    constraintsIn.push(c)
            }
        }
        neighs = neighbors[op]
        openNeighs = []
        for(var nei = 0; nei < neighs.length; nei++)
        {
            neigh = neighs[nei]
            if(board[neigh] == '.')
                openNeighs.push(neigh)
        }
        if(openNeighs.length === 0)
            continue;
        for(var ne = 0; ne < openNeighs.length; ne++)
        {
            neigh = openNeighs[ne]
            var typeOfNeigh = ""
            for(var littleC = 0; littleC < constraintsIn.length; littleC++)
            {
                C = constraintsIn[littleC]
                ind = -1
                if(C.includes(neigh))
                    ind = C.indexOf(neigh)
                if(ind != -1)
                {
                    if(C[ind - 1] == op)
                    {
                        for(var nextind = ind - 1; nextind > -1; nextind += -1)
                        {
                            if(board[C[nextind]] == token)
                            {
                                avSpots.push(neigh)
                                break;
                            }
                            if(board[C[nextind]] == '.')
                                break;
                        }
                    }
                    else
                    {
                        for(var nextin = ind + 1; nextin < C.length; nextin++)
                        {
                            if(board[C[nextin]] == token)
                            {
                                avSpots.push(neigh)
                                break;
                            }
                            if(board[C[nextin]] == '.')
                                break;
                        }
                    }
                    break;
                }
            }
        }
    }
    avSet = new Set(avSpots)
    var myArr = [...avSet];
    return myArr
}

userblack = document.getElementById("playa1").innerHTML.substring(19)
function updateScore(user, sc){
    $.get({url: 'updateScoreOthello', 
    data:{username: user, score: sc},
    success: function(data){
        document.getElementById("scoreupdate").innerHTML = sc;
    },
        error: function(data) {
	   }
    })
}
 function getBoard(user)
{
    $.get({url: 'fetchBoardOthello', 
    data:{username: user},
    success: function(data){
        document.getElementById("boardy").innerHTML = data[0]["board"];
    },
        error: function(data) {
	   }
    })
}
function getWins(user)
{
    $.get({url: 'fetchWinsOthello', 
    data:{username: user},
    success: function(data){
        document.getElementById("userwins").innerHTML = user + " has " + data[0]["wins"] + " wins.";
    },
        error: function(data) {
	   }
    })
}
function updateWins(u){
    $.get({url: 'updateWinsOthello', 
    data:{username: u},
    success: function(data){
        document.getElementById("scoreupdate").innerHTML = u + " wins!";
    },
        error: function(data) {
	   }
    })
}
function updateBoard(u, b){
    $.get({url: 'updateBoardOthello', 
    data:{username: u, board: b},
    success: function(data){
    },
        error: function(data) {
	   }
    })
}

function getScore(board)
{
    xcount = 0
    ocount = 0
    for(x = 0; x < board.length; x++)
    {
        if(board[x] == 'X')
            xcount++
        else if(board[x] == "O")
            ocount++
    }
    return xcount - ocount
}

function doIt()
{   
    ctx.fillStyle = "#3D9970";
    for(var x = 0; x < 8; x++)
    {
        for(var y = 0; y < 8; y++)
        {
            ctx.fillRect(x*width, y*height, x*width+width, y*height + height);
            ctx.strokeRect(x*width, y*height, x*width+width, y*height + height);
        }
    }
    board = document.getElementById("boardy").innerHTML
    makeBoard(board)
    score = getScore(board)
    document.getElementById("scoreupdate").innerHTML = score
    numdots = 0;
    for(index = 0; index < 64; index++)
    {
        if(board[index] = ".")
            numdots++
    }
    if(numdots%2 == 0)
        othelloturn == 'X'
    else
        othelloturn = 'O'
    console.log(othelloturn)
    document.getElementById("turn").innerHTML = namecall[othellocolor[othelloturn]] + "'s Turn"
    possibleMoves = findAvailableSpots(board, othelloturn)
    for(m = 0; m < possibleMoves.length; m++)
    {
        mv = possibleMoves[m]
        ctx.fillStyle = "#85E332";
        mvxy = getXY(mv)
        ctx.fillRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
        ctx.strokeRect(begin[mvxy[0]], begin[mvxy[1]], 75, 75)
    }
}

function confirmed(){
    userwhite = $("#nameis")[0].value
    document.getElementById("thing").innerHTML = "Player 2 (White) : " + userwhite;
}


