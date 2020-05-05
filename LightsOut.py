"""
author:
	Made with <3 by Advik

description:
	Lights out is a puzzle game where your goal is to turn off all the lights.
	whenever you click a light, that light and all its adjacent lights get toggled.
	if you are confused and cant solve then press <space> to let the AI solve the grid.
	increase GRID_LEN and INITIAL_MOVES to increase difficulty.

inspiration:
	https://codeforces.com/problemset/problem/275/A

reference:
	https://en.wikipedia.org/wiki/Lights_Out_(game)
	and some stackoverflow posts... :P
"""
from tkinter import messagebox
import tkinter as tk

import functools
import itertools
import random
import time

# increase GRID_LEN and INITIAL_MOVES to increase difficulty.
GRID_LEN = 4  # this is the size of the grid. a value of 5 means a grid of 5x5
INITIAL_MOVES = 7  # how many random moves to make in the start (to shuffle the board).
DEBUG = False  # DEBUG mode

GRID_PADDING = 10
BACKGROUND_COLOR_GRID = 'cyan'
ON = 'yellow'
OFF = '#eee'
ACTIVECOLOR = 'tomato'


class LightsOut(tk.Frame):
	def __init__(self, *args, **kwargs):
		tk.Frame.__init__(self, *args, **kwargs)
		self.grid()
		self.master.title("Lights Out - Switch Off All The Lights")
		self.master.resizable(False, False)
		self.master.bind('<Escape>', lambda i: self.quit())
		self.master.bind('<space>', self.ai)

		self.AI_PLAYING = False  # it determines whether a human player is playing or AI
		self.buttons = []
		self.matrix = [[0] * GRID_LEN for _ in range(GRID_LEN)]
		self.init_grid()
		self.new_game()

	def init_grid(self):
		"""draw the grid"""
		background = tk.Frame(self)
		background.grid()
		frame1 = tk.Frame(background)
		frame1.grid()
		self.moves = tk.IntVar(value=0)
		tk.Label(frame1, text='MOVES:', fg='tomato', font=("Helvetica", 14)).grid(row=0, column=0)
		tk.Label(frame1, textvariable=self.moves, font=("Helvetica", 36, "bold"), fg='tomato').grid(row=0, column=1)
		frame2 = tk.Frame(background, bg=BACKGROUND_COLOR_GRID)
		frame2.grid()
		for i in range(GRID_LEN):
			tmp = []
			for j in range(GRID_LEN):
				cell = tk.Button(frame2, bg=OFF, activebackground=ACTIVECOLOR, width=10, height=4, command=functools.partial(self.handler, i, j))
				cell.grid(row=i, column=j, padx=GRID_PADDING, pady=GRID_PADDING)
				tmp.append(cell)
			self.buttons.append(tmp)
		frame3 = tk.Frame(background)
		frame3.grid()
		tk.Button(frame3, text="Reset", command=self.new_game, bg='#444', fg='tomato', font=("Verdana", 16)).grid(padx=10, pady=10)

	def new_game(self):
		"""start a new game"""
		self.moves.set(0)
		self.lights = random.sample(list(itertools.product(range(GRID_LEN), range(GRID_LEN))), INITIAL_MOVES)
		for i, j in self.lights:
			self.toggle_light(i, j)
			print(GRID_LEN * i + j + 1)
		print('---')
		self.update_grid()

	def toggle_light(self, i, j):
		"""toogle light at self.matrix[i][j] and all its adjacent lights"""
		self.matrix[i][j] = not self.matrix[i][j]
		if i in range(0, GRID_LEN - 1):
			self.matrix[i + 1][j] = not self.matrix[i + 1][j]
		if j in range(0, GRID_LEN - 1):
			self.matrix[i][j + 1] = not self.matrix[i][j + 1]
		if i in range(1, GRID_LEN):
			self.matrix[i - 1][j] = not self.matrix[i - 1][j]
		if j in range(1, GRID_LEN):
			self.matrix[i][j - 1] = not self.matrix[i][j - 1]

	def update_grid(self):
		"""update the game grid using the game matrix"""
		lights_out = True
		for i, row in enumerate(self.buttons):
			for j, cell in enumerate(row):
				if self.matrix[i][j]:
					bg = ON
					lights_out = False
				else:
					bg = OFF
				text = str(GRID_LEN * i + j + 1) if DEBUG else ''
				cell.config(bg=bg, text=text)
		if lights_out:  # game over
			self.congratulate()

	def handler(self, i, j):
		"""handle button clicks"""
		self.toggle_light(i, j)
		if not self.AI_PLAYING:
			self.lights.append((i, j))
		self.moves.set(self.moves.get() + 1)
		self.update_grid()

	def congratulate(self):
		"""congratulate user that (s)he won the game"""
		if messagebox.askyesno('You Won!', 'do you want to play again?'):
			self.new_game()
		else:
			self.quit()

	def invoke_button(self, button):
		button.invoke()
		bg = button.cget('bg')
		button.config(relief="sunken", bg=ACTIVECOLOR)
		self.master.update_idletasks()
		time.sleep(.4)
		button.config(relief="raised", bg=bg)

	def ai(self, event=None):
		"""remeber the moves used to shuffle the board and play those commands back so as to solve the board."""
		raise NotImplementedError("This feature is not available yet!")
		# self.AI_PLAYING = True
		# for i, j in self.lights:
		# 	self.invoke_button(self.buttons[i][j])
		# self.congratulate()


if __name__ == '__main__':
	LightsOut().mainloop()
