######################################################################
# Author: Emily Lovell & Scott Heggen      Elaheh Jamali, Jacob Hill
# Username: lovelle & heggens             Jamalie, Hilljac
#
# Assignment: T07: Turtle Art
#
# Purpose: Create beautiful works of art through code, namely iterations
#
######################################################################
# Acknowledgements:
#   Original Author: Dr. Scott Heggen
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random


def draw_shape(greg):
    # FIXME modify this function so that it's more general
    """
    Draws a randomly colored hexagon using the turtle library

    :param
    :return: None
    """
    greg.color((random.random(), random.random(), random.random()))     # gives the turtle a random color
    while True:
        side = random.randrange(4,10)
        for num in range(side):
            greg.forward(80)
            greg.left(75)           # the angle ensures a perfect


def main():
    # FIXME modify the docstring so it's correct for your code
    """
    The main function which draws exactly 10 hexagons

    :return: None
    """
    greg = turtle.Turtle()
    wn = turtle.Screen()
    draw_shape(greg)

    # for num in range(10):
    #     t.penup()
    #     # Move the turtle to a random place on the screen
    #     t.goto(random.randint(-300, 300), random.randint(-300, 300))
    #     t.pendown()

        # draw_shape(t)

    wn.exitonclick()


if __name__ == "__main__":
    main()
