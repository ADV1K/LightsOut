# LightsOut
Lights out is a puzzle game where your goal is to turn off all the lights.

![working version of Lights Out Game](LightsOut.gif?raw=true)

## Update
Added a reset button to reset the grid and start a new game.

## Inspiration
so recently i was solving a codeforces problem with the same name and i thought why not create a game like this.
> https://codeforces.com/problemset/problem/275/A

## Playing the game
To play the game you can just run the python file directly like this
```bash
$ git clone https://github.com/ADV1K/LightsOut/
$ cd LightsOut/
$ python LightsOut.py
```
but if you like something simple you can just download the `LightsOut.exe`

## Difficulty
The grid size is set to 4x4 on purpose because most people (including me) could not solve a 5x5 grid. If you want to increase the difficulty then you can increase the `GRID_LEN` variable in the source code. you can also control the number of random moves which are made in the start by changing the `INITIAL_MOVES` variable in the source code.

## Ahh... this game is so hard.
well yes and no. if you want some hints then you can see the console output. the console output contains the moves made by the program to shuffle the board. set `DEBUG` to `True` in the source code and click the numbers which are printed in the console. Be sure to restart the game first 

## AI
I am still figuring out a way to solve the board without human intervention by using some clever algorithms.
