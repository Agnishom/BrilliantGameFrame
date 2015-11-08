# Dots and Boxes

Who hasn't played *Dots and Boxes* in his school days at the back of their notebook?

This *Game Frame* focuses on the very game. For those who do not already know, we present the rules of the game once again.

## The Game

Dots and Boxes is a combinatorial strategy game. To begin with, there are two players and a rectangular array of dots.

Each player takes turn to join two adjacent dots by a vertical or a horizontal segment. Anybody who completes a box, gains a score point *and one extra turn to play*.

Here is an example play:

![dotsandboxes](https://upload.wikimedia.org/wikipedia/commons/f/fa/Dots-and-boxes.svg)

The game ends when no more segments can be formed and the one with the maximal number of boxes win.

## Game Frame Specifications

### Game Setup and Notation

* We're playing the game on a grid of 9 by 9 dots. In other words, there will be exactly 64 boxes at the end of the game.
![emptygrid](https://d18l82el6cdm1i.cloudfront.net/uploads/udwu5jm41J-emptygrid.png)
* As depicted above, the boxes will be denoted in chessboard notation. E.g, `E3` or `C7`
* The notation for the moves will be a box name followed by `T` (top), `B` (bottom), `R` (right) or `L` (left) without spaces. For example, the green segment below could be described as `A2R` or `B2L`.
![](https://d18l82el6cdm1i.cloudfront.net/uploads/Lzhch0BmSl-a2r.png)
The opponent could respond with `C2T` or `C3B`
![](https://d18l82el6cdm1i.cloudfront.net/uploads/e6ddXFRk6O-c2t.png)
* We're aware that most moves could be represented in two ways. You will just be required to produce any one of those representations when required. However, since the opponent bot could produce either of the two representations, please be prepared to accept any of them.

### Communication and Game Play

* A program called the *Game Manager*, run on Agnishom's computer does the job of taking in moves from either player, checking if the moves are legal, scoring, etc.
![](https://d18l82el6cdm1i.cloudfront.net/uploads/fxjD5HX3ue-game_arch.png)
* All communication (detailed below) will take place through STDIN and STDOUT. After writing each newline to STDOUT, *please flush it*. The communication channels may not work correctly otherwise. Should you have any problems with this, *let us know*.
* Now, we will detail how each match is played:
 1. The *Game Manager* fires up both bots which are ready to accept input.
 2. The *Game Manager* chooses the first player (Player A) and writes `A` followed by a newline to its STDIN. It also chooses the second player (Player B) and writes `B` followed by a newline to its STDIN.
 3. Player A now produces its first move (followed by a newline) and the move is fed to Player B (through its STDOUT). Next, Player B does the same.
 ![](https://d18l82el6cdm1i.cloudfront.net/uploads/oaOq1BJNS2-board_with_one_fill.png)
 4. WLOG, assume Player A completes a box and gains another turn. In that case, Player A must produce each turn one by one as usual. However, Player B will receive all of player A's moves at once, in one line, each of them separated by spaces.
 5. On the event that the *Game Manager* determines that the game has come to a end, each bot receives `halt` (followed by a newline) in their STDINs. Please make sure that your bot stops execution upon receiving the `halt` command.

For clarification, we will produce an example game and link to the source of the *Game Manager* program.

### Miscellaneous

* We allow C, C++, Java and Python. Should you wish to use any other language, let us know.
* You're only allowed at most 5 seconds per move.
* Violating the time constraint, printing an invalid move, or printing junk data will result the offending party an immediate defeat in the match.

## Game Example and Code Snippets

* See [log](https://github.com/Agnishom/BrilliantGameFrame/blob/master/DotsAndBoxes/log) for a game played by two instances of the [Random Bot](https://github.com/Agnishom/BrilliantGameFrame/blob/master/DotsAndBoxes/randomBot.py)
* [`gameStruct.py`](https://github.com/Agnishom/BrilliantGameFrame/blob/master/DotsAndBoxes/gameStruct.py) contains an implementation of the *Dots and Boxes* data structure. Feel free to use it for your own bot. (If you do so, make sure you have a copy of it in the zip file)
* [`gameManager.py`](https://github.com/Agnishom/BrilliantGameFrame/blob/master/DotsAndBoxes/gameManager.py) is the *Game Manager*

## Participation

* Submissions will be open till November 31, 2015.
* To participate, email the following to us at brilliantgameframe@gmail.com:
 1. Your [Brilliant](http://Brilliant.Org) profile link
 2. A zip file containing the necessary scripts, source codes, etc.
 3. Instructions on how to get the script running.
* Please only send a single email containing your final code.
