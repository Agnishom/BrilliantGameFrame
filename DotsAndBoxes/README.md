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

* We're playing the game on a grid of 9 by 9 dots. In other words, there will be exactly 81 boxes at the end of the game.
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
* 
