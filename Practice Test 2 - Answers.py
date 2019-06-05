print("Hello World")
#Q1 
def sum_neighbours(lit):
    new_lit = []
    if len(lit) == 1:
          return lit
      for i in range(len(lit)):
          if i == 0:
              new_lit.append(lit[0] + lit[1])
          elif i == (len(lit) - 1):
              new_lit.append(lit[i] + lit[i-1])
          else:
              new_lit.append(lit[i-1] + lit[i] + lit[i+1])

      return new_lit


  #Q2 
  #log(n)

  #Q3
  #n

  #Q5
  #n^2

  #Q6 
  def get_min(t):
      if t.get_left() == None:
          return t.get_data()
      else:
          return get_min(t.get_left())

  #Q7
  #n^2

  #Q9
  #2^n

  #Q11
  #1

  #Q12-14 #Needs 15
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.dist= 0 

    def __str__(self):
        return str((self.x, self.y))
    def __repr__(self):
        return "Point(" + str(self.x) + ", " + str(self.y) + ")"
    def get_x(self):
        return self.x
    def get_y(self):
        return self.y
    def move(self, dx, dy):
        self.x = self.x + dx
        self.y = self.y + dy
    def move_to(self, newx, newy):
        self.x = newx
        self.y = newy

    def distance(self, r):
        self.dist = ((r.get_x()-self.x)**2 + (r.get_y()-self.y)**2)**(1/2)
        return round(self.dist, 2)
    def isNearBy(self, r):
        if self.distance(r) < 5:
            return True
        else:
            return False
    def __add__(self, other):
        if type(other) == int or type(other) == float:
            newx = self.x + other
            newy = self.y + other
        else:
            newx = self.x + other.x
            newy = self.y + other.y

        return Point(newx, newy)
 #Q16 Error in here but i felt like I was close which is super annoying 
def evaluate_postfix_expression(expression):
    postfix = my_stack_module.Stack()
    for element in expression:
        if type(element) == int:
            postfix.push(element)
        else:
            if postfix.size() < 2 and type(element) != int:
                return "Error: too few oprands!"
            else:
                v1 = postfix.pop()
                v2 = postfix.pop()
                if element == '+':
                    postfix.push(v1 + v2)
                elif element == '-':
                    postfix.push(v2 - v1)
                elif element == '*':
                    postfix.push(v1 * v2)
                elif element == '/':
                    postfix.push(v2 / v1)
                elif element == '^':
                    postfix.push(v2**v1)

    if postfix.size() == 1:
        return postfix.pop()
    else:
        return "Error"
            


exp = ['2', '4', '*', '^']
print(exp, evaluate_postfix_expression(exp))

          
  #Q17
  #n*log(n)


