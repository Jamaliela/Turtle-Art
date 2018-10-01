######################################################################
# Author: Emily Lovell & Scott Heggen      TODO: Change this to your names
# Username: lovelle & heggens             TODO: Change this to your usernames
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


def draw_hexagon(turt):
    # FIXME modify this function so that it's more general
    """
    Draws a randomly colored hexagon using the turtle library

    :param turt: a turtle object to draw with
    :return: None
    """
    turt.color((random.random(), random.random(), random.random()))     # gives the turtle a random color

    for num in range(6):
        turt.forward(50)
        turt.left(60)           # the angle ensures a perfect hexagon


def main():
    # FIXME modify the docstring so it's correct for your code
    """
    The main function which draws exactly 10 hexagons

    :return: None
    """
    t = turtle.Turtle()
    wn = turtle.Screen()

    # Draws 10 hexagons
    for num in range(10):
        t.penup()
        # Move the turtle to a random place on the screen
        t.goto(random.randint(-300, 300), random.randint(-300, 300))
        t.pendown()

        draw_hexagon(t)

    wn.exitonclick()


if __name__ == "__main__":
    main()
