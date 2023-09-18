## @file TriangleT.py
#  @title TriangleT
#  @author Michael Hammal
#  @brief This class displays three graphs of the data provided
#  @details This class displays three labelled x-y graphs of the

from Shape import *


class TriangleT(Shape):

    ## @brief Constructor for TriangleT
    #  @details Constructor accepts four parameters
    #  @param x x coordinate
    #  @param y y coordinate
    #  @param s side length
    #  @param m mass
    #  @throws ValueError exception if s (side length) or m (mass) are negative
    def __init__(self, x, y, s, m):
        if (s < 0) or (m < 0):
            raise ValueError

        self.x = x
        self.y = y
        self.s = s
        self.m = m

    ## @brief Getter method for x coordinate of the center of mass
    #  @return x coordinate of the center of mass
    def cm_x(self):
        return self.x

    ## @brief Getter method for y coordinate of the center of mass
    #  @return y coordinate of the center of mass
    def cm_y(self):
        return self.y

    ## @brief Getter method for the mass
    #  @return mass of the shape
    def mass(self):
        return self.m

    ## @brief Getter method for moment of inertia
    #  @return Moment of inertia
    def m_inert(self):
        return (self.m * (self.s)**2) / 12
