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
#   Asked for TA help - Aaron Christian
#
# licensed under a Creative Commons
# Attribution-Noncommercial-Share Alike 3.0 United States License.
####################################################################################

import turtle
import random


def get_angle():
    """
    This is a fruitful function and will return the angle based on a random side

    :param: None
    :return: angle: the angle for the shape
    """
    side = random.randrange(4, 10)   # we want the side variable to have a random number between 4 and 10
    angle = 360//side               # then to have the angle we will need the floor division just to have an int instead of a float
    return angle                     # we return angle to have a fruitful function


def moving_around(greg):
    """
    this function will move the turtle to different parts of the screen and will start drawing there

    :param: greg: the turtle name
    :return: None
    """
    greg.penup()         # we penup so our drawings are not recorded
    greg.goto(random.randint(-300, 300), random.randint(-300, 300))   # the turtle finds a random point on the screen to start drawing
    greg.pendown()    # pen down to start drawing again


def draw_shape(greg, colors):
    """
    Draws a randomly colored shapes using the turtle library

    :param: greg: the turtle name
    :param: colors: choosing different colors from a list
    :return: None
    """

    while True:                                   # this will be an infinite loop because it is always True
        color = random.choice(colors)             # Choose a random color from the color list in main
        greg.color(color)                         # the turtle chooses that random color as its color
        ang = random.randrange(45, 146)           # our angle for turning each time is going to be random so the shape is different
        angle = get_angle()                       # to have the number of repetition we refer back to our fruitful function
        if ang % 2 == 0:                          # if the ang as a random number is divisible by 2
            greg.begin_fill()                     # start filling the shapes
        for num in range(angle):                  # repeat this for the number of anlge
            greg.forward(80)                      # go forward 80 units
            greg.left(ang)                        # turn left for the amount of ang
        greg.end_fill()                           # end filling if you have filled anything
        moving_around(greg)                       # move to another point of the screen for different shapes


def main():
    """
    The main function which draws different shapes until the user force closes it

    :return: None
    """
    greg = turtle.Turtle()             # greg is assigned as the turtle
    colors = ["red", "green", "blue", "orange", "purple", "pink", "yellow"]  # we have a list of colors to randomly choose from
    greg.speed(10)                     # the speed of the turtle because we have large number of repetitions
    wn = turtle.Screen()               # wn is assigned as the screen of our turtle
    wn.bgcolor("lightblue")            # giving the background color for the screen
    draw_shape(greg, colors)           # calling the function to draw the random shapes

    wn.exitonclick()                  # this function will never be executed because this is an infinite loop and will never exit the previous l
    #  some errors will pop up after closing the screen which will be due the force exit and interrupting the turtle library


if __name__ == "__main__":
    main()
