## @file triangle_adt.py
#  @title triangle_adt
#  @author Michael Hammal

from enum import Enum, auto
from itertools import permutations
import math

## @brief This class represents the different types of triangles
#  @details This class represents the set of equilateral, isosceles, 
#  scalene, and right triangles
class TriType(Enum):
    equilat = auto()
    isosceles = auto()
    scalene = auto()
    right = auto()

## @brief This class represents a triangle
#  @details This class represents a triangle using its three side lengths
class TriangleT:

  ## @brief Constructor for triangle_adt
  #  @details Constructor accepts three parameters of type integer 
  #  for the 3 side lenghts of the triangle. Assumes that the user inputs integers
  #  @param a side length 1
  #  @param b side length 2
  #  @param c side length 3
  def __init__(self, a, b, c):
    self.s = (a, b, c)

  ## @brief Returns the three sides of the triangle as a tuple
  #  @details Assumes the user inputs a valid triangle
  #  @return (a,b,c) tuple representing the sides of the triangle
  def get_sides(self):
    return self.s

  ## @brief This function compares two triangles
  #  @details This function utilizes the permutations library to compare
  #  all possible triangles given the side lengths. Assumes the user inputs a valid triangle
  #  @param t TriangleT object
  #  @return True if the two triangles are equal and False otherwise
  def equal(self, t):
    ## Create a list of the possible triangles    
    perm = permutations(t.get_sides())
    return (self.s in list(perm))

  ## @brief This function calculates the perimeter of the triangle
  #  @details Assumes the user inputs a valid triangle
  #  @return An integer value of the perimeter of the triangle
  def perim(self):
    return sum(list((self.get_sides())))

  ## @brief This function calculates the area of the triangle
  #  @details This function utlizes the formula obtained from 
  #  https://www.mathopenref.com/heronsformula.html to calculate the 
  #  area of the triangle. Assumes the user inputs a valid triangle
  #  @return A float representing the area of the triangle
  def area(self):
    ## Get all the sides of the triangle    
    sides = self.get_sides()
    ## Assign each side to a separate variable    
    a, b, c = sides[0] , sides[1] , sides[2]
    ## Perimeter divided by 2
    s = self.perim() / 2
    return float(math.sqrt((s*(s-a)*(s-b)*(s-c))))  

  ## @brief This function checks if a triangle is valid
  #  @details This function checks if a triangle is valid by checking sides is 
  #  greater than the third. Assumes the user inputs integers
  #  @return True if the triangle is valid and False otherwise
  def is_valid(self):
    ## Get all the sides of the triangle    
    sides = self.get_sides()
    ## Assign each side to a separate variable     
    a, b, c = sides[0] , sides[1] , sides[2]
    if a + b > c and b + c > a and a + c > b:
      return True
    return False 

  ## @brief This function determines the type of the triangle
  #  @details This function determines the type of the triangle using
  #  the enumerated type class TriType defined above. The function returns
  #  a right triangle no matter if the triangle is isosceles or scalene.
  #  Assumes the user inputs a valid triangle
  #  @return A TriType object representing the type of triangle
  def tri_type(self):
    ## Get all the sides of the triangle 
    sides = self.get_sides()    
    ## Assign each side to a separate variable  
    a, b, c = sides[0] , sides[1] , sides[2]
    if a == b and b == c and a == c:
      return TriType.equilat
    if (a**2 + b**2) == c**2 or (b**2 + c**2) == a**2 or (a**2 + c**2) == b**2:
      return TriType.right # Assuming the triangle is either isosceles or scalene
    if (a == b and b != c and a != c) or (a != b and b == c and a != c) or (a != b and b != c and a == c):
      return TriType.isosceles   
    return TriType.scalene 