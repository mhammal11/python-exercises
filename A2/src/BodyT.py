## @file BodyT.py
#  @title Body
#  @author Michael Hammal
#  @brief This class displays three graphs of the data provided
#  @details This class displays three labelled x-y graphs of

from Shape import *


class BodyT(Shape):

    ## @brief Constructor for BodyT
    #  @details Constructor accepts three parameters
    #  @param x a sequence of real numbers for x coordinates
    #  @param y a sequence of real numbers for y coordinates
    #  @param m a sequence of real numbers for mass
    #  @throws ValueError exception if the sequences are not equal in length
    #  or if the value of the mass is negative
    def __init__(self, x, y, m):
        if (len(x) != len(y)) or (len(y) != len(m)) or (len(x) != len(m)):
            raise ValueError

        for s in m:
            if s < 0:
                raise ValueError

        self.cmx = self.__cm(x, m)
        self.cmy = self.__cm(y, m)
        self.m = sum(m)
        self.moment = self.__mmom(x, y, m) - sum(m)*((self.__cm(x, m))**2 + (self.__cm(y, m))**2)

    ## @brief Getter method for the center of mass in x direction
    #  @return x coordinate of the center of mass
    def cm_x(self):
        return self.cmx

    ## @brief Getter method for the center of mass in y direction
    #  @return y coordinate of the center of mass
    def cm_y(self):
        return self.cmy

    ## @brief Getter method for mass
    #  @return mass of the shape
    def mass(self):
        return self.m

    ## @brief Getter method for moment of inertia
    #  @return Moment of inertia
    def m_inert(self):
        return self.moment

    ## @brief Method for the average center of mass
    #  @return average center of mass
    #  @param z sequence of real numbers
    #  @param m sequence of real numbers
    def __cm(self, z, m):
        return sum(m[i] * z[i] for i in range(len(m))) / sum(m)

    ## @brief Method for the moment of inertia
    #  @return moment of inertia based on x and y values
    #  @param x sequence of real numbers
    #  @param y sequence of real numbers
    #  @param m sequence of real numbers
    def __mmom(self, x, y, m):
        return sum(m[i] * (x[i]**2 + y[i]**2) for i in range (len(m)))
