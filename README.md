# Sierpinski-CSCI141-F19-

Name: Dante Bianco

Description: A Python program that draws a Sierpinski Triangle using a method
called a “chaos game”. A chaos game is an example of what’s called a zero-player game, so called
because we set things up a certain way to start, and the “game” unfolds deterministically based on a
set of rules - there are no players involved.
The chaos game is played as follows. The user specifies the window size (say 300 by 300 pixels). Denote
the three corners of an isosceles triangle 1, 2, 3, where corner 1 is at the top center of the screen, corner
2 is in the lower left of the screen, and corner 3 is in the lower right of the screen. First, a point is
chosen at random. Then, at each step of the game, a dot is drawn at the midpoint between the current
location (where the prior dot was drawn) and a randomly-chosen corner of the triangle.
