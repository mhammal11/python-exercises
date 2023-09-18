## @file Shape.py
#  @title Shape
#  @author Michael Hammal
#  @brief This class provides the Shape interface
#  @details This class provides the Shape interface with abstract methods

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    ## @brief Generic getter method for x coordinate of the center of mass
    #  @return x coordinate of the center of mass
    def cm_x(self):
        pass

    @abstractmethod
    ## @brief Generic getter method for y coordinate of the center of mass
    #  @return y coordinate of the center of mass
    def cm_y(self):
        pass

    @abstractmethod
    ## @brief Generic getter method for the mass
    #  @return mass of the shape
    def mass(self):
        pass

    @abstractmethod
    ## @brief Generic getter method for moment of inertia
    #  @return Moment of inertia
    def m_inert(self):
        pass
