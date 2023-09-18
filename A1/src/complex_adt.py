## @file complex_adt.py
#  @title complex_adt
#  @author Michael Hammal

import math

## @brief This class represents complex numbers
#  @details This class represents the imaginary and real parts
#  of a complex number using two floats 

class ComplexT:

  ## @brief Constructor for complex_adt
  #  @details Construct accepts two parameters of type float
  #  representing the real and imaginary parts of a complex number
  #  @param x real part of the complex number
  #  @param y imaginary part of the complex number
  def __init__(self, x, y):
    self.x = x
    self.y = y
    
  ## @brief Returns the real part of the complex number
  #  @return A float representing the real part of the complex number
  def real(self):
    return self.x

  ## @brief Returns the imaginary part of the complex number
  #  @return A float representing the imaginary part of the complex number
  def imag(self):
    return self.y

  ## @brief This getter function returns the magnitude of the complex number
  #  @return A float representing the magnitude of the complex number
  def get_r(self):
    return float(math.sqrt(self.x*self.x + self.y*self.y))

  ## @brief This getter function returns the argument of the complex number
  #  @details This function assumes that the real part of the complex number is not 0
  #  @return A float representing the argument of the complex number
  def get_phi(self):
    return float(math.atan(self.y/self.x))

  ## @brief This function compares two complex numbers
  #  @details This function compares the real parts and imaginary parts of two complex numbers
  #  @param c ComplexT object
  #  @return True if the two complex numbers are equal and False otherwise
  def equal(self, c):
    return (self.x == c.real()) and (self.y == c.imag())

  ## @brief This function computes the complex conjugate of a complex number
  #  @return A ComplexT object representing the complex conjugate of the complex number
  def conj(self):
    return ComplexT(self.x, -1 * self.y) #FIXED

  ## @brief This function adds two complex numbers
  #  @return A ComplexT object representing the sum of two complex numbers
  def add(self, a):
    return ComplexT(self.x + a.real(), self.y + a.imag())
    
  ## @brief This function subtracts two complex numbers
  #  @return A ComplexT object representing the difference between two complex numbers
  def sub(self, a):
    return ComplexT(self.x - a.real(), self.y - a.imag())

  ## @brief This function multiplies two complex numbers
  #  @details This function multiplies two complex numbers using the formula obtained from https://bit.ly/3qVhkal
  #  @return A ComplexT object representing the multiplication of two complex numbers
  def mult(self, a):
    return ComplexT(self.x * a.real() - self.y * a.imag(), self.y * a.real() + self.x * a.imag())

  ## @brief This function calculates the reciprocal of a complex number
  #  @details This function returns the reciprocal of a complex number using the formula obtained from 
  #  http://www.suitcaseofdreams.net/Reciprocals.htm
  #  @return A CompleXT object representing the reciprical of the complex number
  def recip(self):
    return ComplexT(self.x/((self.x)**2+(self.y)**2), -1 * self.y/((self.x)**2+(self.y)**2))

  ## @brief This function one complex number by another
  #  @details This function divides one complex number by another using the formula obtained from https://bit.ly/2YeUYV3
  #  @return A ComplexT object representing the division of two complex numbers
  def div(self, a):
    s = float(a.real()**2 + a.imag()**2)    
    return ComplexT((self.x * a.real() + self.y * a.imag())/s, (self.y * a.real() - self.x * a.imag())/s)

  ## @brief This function calculates the positive square root of a complex number
  #  @details This function computes the positive square root of a complex number using the formula obtained from https://bit.ly/3pzaAhS 
  #  @return A ComplexT object representing the positive square root of the complex number
  def sqrt(self):
    return ComplexT(math.sqrt(0.5*(self.x+math.sqrt(self.x**2 + self.y **2))), (self.y/2)*math.sqrt(2/(self.x+math.sqrt(self.x**2+self.y**2))))
                 