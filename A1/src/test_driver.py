## @file test_driver.py
#  @title test_driver 
#  @autor Michael Hammal

import math
from complex_adt import ComplexT
from triangle_adt import TriangleT, TriType

# Equivalence function 
def aprx_eq(a, b):
      return (a - b)/a <= 0.00001

# ---------------------------------
# Test case counter
# ---------------------------------
# Counts the number of passed and failed test cases 
passed = 0
failed = 0

print("---------------------------------")
print("complex_adt test cases")
print("---------------------------------")

print("---------------------------------")
print("Test cases for real")
print("---------------------------------")
a = ComplexT(4.0, 3.0)
if a.real() == 4.0:
  print("real test passes")
  passed = passed + 1
else:
  print("real test FAILS")
  failed = failed + 1

a = ComplexT(-4.0, 3.0)
if a.real() == -4.0:
  print("real test passes")
  passed = passed + 1
else:
  print("real test FAILS")
  failed = failed + 1  

print("---------------------------------")
print("Test cases for imag")
print("---------------------------------") 
if a.imag() == 3.0:
  print("imag test passes")
  passed = passed + 1
else:
  print("imag test FAILS")
  failed = failed + 1

a = ComplexT(-4.0, -3.6)
if a.imag() == -3.6:
  print("imag test passes")
  passed = passed + 1
else:
  print("imag test FAILS")
  failed = failed + 1

print("---------------------------------")
print("Test cases for get_r")
print("---------------------------------") 
a = ComplexT(4.0, 3.0)
if a.get_r() == 5.0:
  print("get_r test passes")
  passed = passed + 1
else:
  print("get_r test FAILS")
  failed = failed + 1  

a = ComplexT(5.0, 7.0)
if aprx_eq(a.get_r(), math.sqrt(74)):
  print("get_r test passes")
  passed = passed + 1
else:
  print("get_r test FAILS")
  failed = failed + 1  

print("---------------------------------")
print("Test cases for get_phi")
print("---------------------------------")
a = ComplexT(2.0,1.0)
if abs(a.get_phi() - 0.46365) <= 0.00001:
  print("get_phi test passes")
  passed = passed + 1
else:
  print("get_phi test FAILS")
  failed = failed + 1 

a = ComplexT(3.5,-2.5)
if abs(a.get_phi() - (-1 * 0.620249)) <= 0.00001:
  print("get_phi test passes")
  passed = passed + 1
else:
  print("get_phi test FAILS")
  failed = failed + 1   

print("---------------------------------")
print("Test cases for equal")
print("---------------------------------")
a = ComplexT(4.0, 3.0)
b = ComplexT(4.0,3.0)
if a.equal(b):
  print("equal test passess")
  passed = passed + 1
else:
  print("equal test FAILS")
  failed = failed + 1

a = ComplexT(-4.2, -3.1)
b = ComplexT(-4.2, -3.1)  
if a.equal(b):
  print("equal test passess")
  passed = passed + 1
else:
  print("equal test FAILS")
  failed = failed + 1  

print("---------------------------------")
print("Test cases for conj")
print("---------------------------------")
a = ComplexT(4.0, 3.0)
if a.conj().real() == 4.0 and a.conj().imag() == -3.0:
  print("conj test passess")
  passed = passed + 1
else:
  print("conj test FAILS")
  failed = failed + 1

a = ComplexT(4.0, -3.0)
if aprx_eq(a.conj().real(), 4.0) and aprx_eq(a.conj().imag(), 3.0):
  print("conj test passess")
  passed = passed + 1
else:
  print("conj test FAILS")
  failed = failed + 1       

print("---------------------------------")
print("Test cases for add")
print("---------------------------------")
a = ComplexT(1.0, 2.0)
b = ComplexT(0.5, -0.5)
c = a.add(b)
if (not(c.real() == 1.5) and (c.imag() == 1.5)):
  print("add test FAILS")
  failed = failed + 1
else:
  print("add test passes")
  passed = passed + 1

a = ComplexT(-1.0, -2.0)
b = ComplexT(-0.5, -0.5)
c = a.add(b)
if not((aprx_eq(c.real(), -1.5) and (aprx_eq(c.imag(), -2.5)))):
  print("add test FAILS")
  failed = failed + 1
else:
  print("add test passes")
  passed = passed + 1  

print("---------------------------------")
print("Test cases for sub")
print("---------------------------------")
a = a = ComplexT(1.0, 2.0)
b = ComplexT(0.5, -0.5)
c = a.sub(b)
if not((c.real() == 0.5) and (c.imag() == 2.5)):
  print("sub test FAILS")
  failed = failed + 1
else:
  print("sub test passes")
  passed = passed + 1 

a = a = ComplexT(-1.0, -2.0)
b = ComplexT(-0.5, -0.5)
c = a.sub(b)
if (not((aprx_eq(c.real(), -0.5) and (aprx_eq(c.imag(), -1.5))))):
  print("sub test FAILS")
  failed = failed + 1
else:
  print("sub test passes")
  passed = passed + 1      

print("---------------------------------")
print("Test cases for mult")
print("---------------------------------")
a = ComplexT(1,4)
b = ComplexT(5,1)
c = a.mult(b)
def multTest(x):
  if x.real() == 1 and x.imag() == 21:
    return True
  else:
    return False
if multTest(c):
  print("mult test passes")
  passed = passed + 1
else:
  print("mult test FAILS")
  failed = failed + 1

a = ComplexT(2.7,-1.6)
b = ComplexT(5.5,-3.1)
c = a.mult(b)
if aprx_eq(c.imag(), -17.17) and aprx_eq(c.real(), 9.89):
  print("mult test passes")
  passed = passed + 1
else:
  print("mult test FAILS")
  failed = failed + 1       

print("---------------------------------")
print("Test cases for recip")
print("---------------------------------")
a = ComplexT(4.0, 3.0)
b = a.recip()
def reciprocalTest(c):
    if c.real() == (4/25) and c.imag() == (-3/25):
      return True
    else:
      return False  
if reciprocalTest(b):
  print("recip test passes")
  passed = passed + 1
else:
  print("recip test FAILS")
  failed = failed + 1  

a = ComplexT(1.2, 2.1)
b = a.recip()
def reciprocalTest(c):
    if aprx_eq(c.real(),(8/39)) and aprx_eq(c.imag(),(-14/39)):
      return True
    else:
      return False  
if reciprocalTest(b):
  print("recip test passes")
  passed = passed + 1
else:
  print("recip test FAILS")
  failed = failed + 1  

print("---------------------------------")
print("Test cases for div")
print("---------------------------------")
a = ComplexT(4,2)
b = ComplexT(-1,1)
c = a.div(b)
def divTest(x):
  if x.real() == -1 and x.imag() == -3:
    return True
  else:
    return False
if divTest(c):
  print("div test passes")
  passed = passed + 1
else:
  print("div test FAILS")
  failed = failed + 1 

a = ComplexT(-1.5,2.3)
b = ComplexT(9.2,8.4)
c = a.div(b)
def divTest(x):
  if aprx_eq(x.real(), 69/1940) and aprx_eq(x.imag(), 211/970):
    return True
  else:
    return False
if divTest(c):
  print("div test passes")
  passed = passed + 1
else:
  print("div test FAILS")
  failed = failed + 1   

print("---------------------------------")
print("Test cases for sqrt")
print("---------------------------------")
a = ComplexT(9, 4)
c = a.sqrt()
if (not((aprx_eq(c.real(), 3.06992) and (aprx_eq(c.imag(), 0.65148))))):
  print("sqrt test FAILS")
  failed = failed + 1
else:
  print("sqrt test passes")
  passed = passed + 1
a = ComplexT(6, 3)
c = a.sqrt()
if (not((aprx_eq(c.real(), 2.52073) and (aprx_eq(c.imag(), 1.191012))))):
  print("sqrt test FAILS")
  failed = failed + 1
else:
  print("sqrt test passes")
  passed = passed + 1        

print("")
print("---------------------------------")
print("triangle_adt test cases")
print("---------------------------------")
s = TriangleT(5,4,3)
x = TriangleT(3,5,4)
z = TriangleT(1,2,3)
y = TriangleT(4,3,5)

print("---------------------------------")
print("Test cases for get_sides")
print("---------------------------------")
if s.get_sides() == (5,4,3):
  print("get_sides test passes")
  passed = passed + 1
else:
  print("get_sides test FAILS") 
  failed = failed + 1 

if x.get_sides() == (3,5,4):
  print("get_sides test passes")
  passed = passed + 1
else:
  print("get_sides test FAILS") 
  failed = failed + 1 

print("---------------------------------")
print("Test cases for equal")
print("---------------------------------")
if s.equal(x):
  print("equal test passes")
  passed = passed + 1
else:
  print("equal test FAILS")
  failed = failed + 1  

if s.equal(y):
  print("equal test passes")
  passed = passed + 1
else:
  print("equal test FAILS")
  failed = failed + 1   

if s.equal(z):
  print("equal test FAILS")
  failed = failed + 1         
else:
  print("equal test passes")
  passed = passed + 1        

print("---------------------------------")
print("Test cases for perim")
print("---------------------------------")
if s.perim() == 12: 
  print("perim test passes")
  passed = passed + 1
else:
  print("perim test FAILS")
  failed = failed + 1    

if x.perim() != 12:
  print("perim test FAILS")
  failed = failed + 1        
else:
  print("perim test passes")
  passed = passed + 1

print("---------------------------------")
print("Test cases for area")
print("---------------------------------")
if s.area() == 6.0:
  print("area test passes")
  passed = passed + 1
else:
  print("area test FAILS")
  failed = failed + 1    

t = TriangleT(24,25,15)
if aprx_eq(t.area(), 174.5394):
  print("area test passes")
  passed = passed + 1
else:
  print("area test FAILS")
  failed = failed + 1 

print("---------------------------------")
print("Test cases for is_valid")
print("---------------------------------")
if s.is_valid():
  print("is_valid test passes")
  passed = passed + 1
else:
  print("is_valid test FAILS")
  failed = failed + 1   

if not(z.is_valid()):
  print("is_valid test passes")
  passed = passed + 1
else:
  print("is_valid test FAILS")
  failed = failed + 1     

print("---------------------------------")
print("Test cases for tri_type")
print("---------------------------------") 
s = TriangleT(3,3,3)
if s.tri_type() == TriType.equilat:
  print("tri_type test passes")
  passed = passed + 1
else:
  print("tri_type test FAILS")
  failed = failed + 1     
s = TriangleT(4,4,3)
if s.tri_type() == TriType.isosceles:
  print("tri_type test passes")
  passed = passed + 1
else:
  print("tri_type test FAILS")
  failed = failed + 1     
s = TriangleT(3,4,5)
if s.tri_type() == TriType.right:
  print("tri_type test passes")
  passed = passed + 1
else:
  print("tri_type test FAILS")
  failed = failed + 1    
s = TriangleT(6,4,3)
if s.tri_type() == TriType.scalene:
  print("tri_type test passes")
  passed = passed + 1
else:
  print("tri_type test FAILS")
  failed = failed + 1   
s = TriangleT(4,3,4)
if s.tri_type() == TriType.isosceles:
  print("tri_type test passes")
  passed = passed + 1
else:
  print("tri_type test FAILS")
  failed = failed + 1    

print("")
print("---------------------------------")
print("Test case counter")
print("---------------------------------")
print("Number of passed test cases:", passed)
print("Number of failed test cases:", failed)
