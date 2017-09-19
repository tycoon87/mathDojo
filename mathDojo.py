class math(object):
    def __init__(self,add,subtract,num):
        self.add = add
        self.subtract = subtract
        self.num = num
        
    def add(self, x, y, args):
        num = x + y
        return self
math
add(2,3) 
print num
##        
##**************************************************
##create an instance
#class MathDojo(object):
##    initial the instance
#    def __init__(self):
##        set instance variable
#        self.result = 0
##    create a function for the instance
#    def add(self, *args):
##        for loop for "args"
#        for i in args:
##            if the type of i is a list or if type i is a tuple
#            if type(i) == list or type(i) == tuple:
##                start nested for loop
#                for k in i:
##                    set result to be k
#                    self.result += k
##            outherwise
#            else:
##                set result to be i
#                self.result += i
#        return self