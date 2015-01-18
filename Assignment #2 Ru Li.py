_author_ = "Li, Ru"
_date_ = "Monday, October 15, 2012"
_version_ = "2.0"
_filename_ = "Assignment #2 Ru Li.py"
_description_ = "Assignment #2"

class rectangle:
    x = 0
    y = 0
    h = 0
    l = 0
    def __init__(self,n,d,s,f):
        self.x = n
        self.y = d
        self.w = s
        self.l = f
    def __str__(self):
        return "base:("+str(self.x)+","+str(self.y)+") w:"+str(self.w)+" h:"+str(self.l)
    def area(self):
        return "Area: "+str(self.w*self.l)
    def perimeter(self):
        return "Perimeter: "+str(self.w*2+self.l*2)
    def intersection(self, other):
        # self_lines gets the equation of all the lines on the sides of a square
        #       _ _y1_ _
        #      |        |
        #   x1 |  self  |
        #      |        |x2
        #      |_ _ _ __|
        #          y2
        # self_lines = [x1,x2,y1,y2]
        # so that means:
        # self_lines[0] = self.x1
        # and so on
        #
        # Will be refered to as self.x1, self.x2, self.y1 and self,y2 in later comments
        # From this method, we find the two x values that intersect and the two y values that intersect. With the 4 numbers, we find diagonally opposite points on the square that overlaps and use those coordinates to find the area of that square        
        #               _ _ _ _ 
        #         (c)->|       |
        #      (e)_ _ _|_ _(a) |
        #          |   |   |   |
        #          |   |_ _|_ _|_(f)
        #          | (b)   |
        #          |_ _ _ _|<-(d)
        #
        # Using the method, we find the x values (c and d) c = x1 and d = x2
        # Then the method finds the y values (e and f) e = y1 and f = y2
        # Connecting the x and y values, we get the (a) coordinate and the (b) coordinate (diagonally opposite from each other) 
        # Using those 2 points, we can find the area of the overlapping square
        self_lines = [self.x,self.x+self.w,self.y+self.l,self.y]
        other_lines = [other.x,other.x+other.w,other.y+other.l,other.y]
        # if self.x1 is between other.x1 and other.x2 and self.x2's value is bigger on the x axis than other.x1(which means it's also bigger than other.x2)
        # s = self square
        # o = other square
        #   |<-other.x1        
        #   |         |<-other.x2
        #   |      _ _|_ _      
        #   |     |   |   |     
        #   |  x1 |   |   | x2  
        #   |     |s  |   |     
        #   |     |_ _|_ _|     
        #   |         |         
        #   |         |
        # it will look something like this. We don't know where the y values are yet.
        # Looks like the overlapping square's x values are self.x1 and other.x2
        if self_lines[0] >= other_lines[0] and self_lines[0] <= other_lines[1] and self_lines[1] >= other_lines[1]:
            # set x1 to self.x1 and x2 to other.x2 to be used later to find the coordinate
            x1=self_lines[0]
            x2=other_lines[1]
            # the following if statements covers the following scenarios
            # - if self.y1 is between other.y1 and other.y2
            # y1 = self.y1
            # y2 = other.y2
            #   _ _ _ _
            #  |o      |
            #  |    _ _|_ _y1
            #  |   |   |   |
            #  |_ _|_ _|   |
            #      |     s |
            #      |_ _ _ _| 
            #
            # - if self.y2 is between other.y1 and other.y2
            # y1 = self.y2
            # y2 = other.y1
            #       _ _ _ _
            #      |      s|
            #   _ _|_ _    |
            #  |o  |   |   |
            #  |   |_ _|_ _|
            #  |       |   y2
            #  |_ _ _ _|
            #
            # - if both self y1 and y2 are outside other y1 and y2
            # y1 = other.y1
            # y2 = other.y2
            #       _ _ _ _ y1
            #   _ _|_ _    |
            #  |       |   | 
            #  |       |  s|
            #  |o      |   |
            #  |_ _ _ _|   |
            #      |_ _ _ _| 
            #               y2
            # 
            # - if both self y1 and y2 are inside other y1 and y2
            # y1 = self.y1
            # y2 = other.y2
            #   _ _ _ _
            #  |    _ _|_ _ y1
            #  |   |   |   |
            #  |o  |   |  s|
            #  |   |   |   |
            #  |   |_ _|_ _|
            #  |_ _ _ _|    y2
            # 
            if  self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
        # This time, we're considering if the other square was to the right of the self square
        # if self.x2 is between other.x1 and other.x2 and self.x1's value is smaller on the x axis than other.x1(which means it's also smaller than other.x2) 
        #            |       |
        #  other.x1->|       |
        #       _ _ _|_      |other.x2
        #      |     | |     |
        #   x1 |     | | x2  |
        #      |self | |     |
        #      |_ _ _|_|     |
        #            |       |
        #            |       |
        # this time it's:
        # x1 = self.x2
        # x2 = other.x1
        elif self_lines[1] >= other_lines[0] and self_lines[1] <= other_lines[1] and self_lines[0] <= other_lines[0]:
            x1=self_lines[1]
            x2=other_lines[0]
            # same thing as above for finding the two y values
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
        # for the next two if statements we're checking if self.x1 and self.x2 is both outside or both inside other.x1 and other.x2
        elif self_lines[0] >= other_lines[0] and self_lines[1] <= other_lines[1]:
            x1=self_lines[0]
            x2=self_lines[1]
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
        elif self_lines[0] <= other_lines[0] and self_lines[1] >= other_lines[1]:
            x1=other_lines[0]
            x2=other_lines[1]
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
        else:
            # if there's no overlap, values are 0
            y1=0
            y2=0
            x1=0
            x2=0
        area_overlap = abs(x2 - x1) * abs(y2 - y1)
        if area_overlap == 0:
            return "No overlap"
        else:
            return "area of overlap is "+str(area_overlap)
    def total_perimeter(self,other):
        # recycled code from intersection method
        # use coordinates to find perimeter this time
        self_lines = [self.x,self.x+self.w,self.y+self.l,self.y]
        other_lines = [other.x,other.x+other.w,other.y+other.l,other.y]      
        if self_lines[0] >= other_lines[0] and self_lines[0] <= other_lines[1] and self_lines[1] >= other_lines[1]:
            x1=self_lines[0]
            x2=other_lines[1]
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
        elif self_lines[1] >= other_lines[0] and self_lines[1] <= other_lines[1] and self_lines[0] <= other_lines[0]:
            x1=self_lines[1]
            x2=other_lines[0]
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
        elif self_lines[0] >= other_lines[0] and self_lines[1] <= other_lines[1]:
            x1=self_lines[0]
            x2=self_lines[1]
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
        elif self_lines[0] <= other_lines[0] and self_lines[1] >= other_lines[1]:
            x1=other_lines[0]
            x2=other_lines[1]
            if self_lines[2] <= other_lines[2] and self_lines[2] >= other_lines[3] and self_lines[3] <= other_lines[3]:
                y1=self_lines[2]
                y2=other_lines[3]
            if self_lines[3] <= other_lines[2] and self_lines[3] >= other_lines[3] and self_lines[2] >= other_lines[2]:
                y1=self_lines[3]
                y2=other_lines[2]
            if self_lines[2] >= other_lines[2] and self_lines[3] <= other_lines[3]:
                y1=other_lines[2]
                y2=other_lines[3]
            if self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
                y1=self_lines[2]
                y2=self_lines[3]
        else:
            y1=0
            y2=0
            x1=0
            x2=0
        # perimeter of square 1 + perimeter of square 2 - perimeter of overlapping square = total perimeter
        t_perimeter = self.w*2+self.l*2+other.l*2+other.w*2
        perimeter_overlap = abs((x2 - x1))*2+abs((y2 - y1))*2
        return "Total perimeter is "+str(t_perimeter-perimeter_overlap)   
    def contains(self,other):
        self_lines = [self.x,self.x+self.w,self.y+self.l,self.y]
        other_lines = [other.x,other.x+other.w,other.y+other.l,other.y]
        # if every self x and y value is smaller than or equal to its corresponding other square x and y value then returns true
        if self_lines[0] >= other_lines[0] and self_lines[1] <= other_lines[1] and self_lines[2] <= other_lines[2] and self_lines[3] >= other_lines[3]:
            return True
        # perspective of the other square
        elif other_lines[0] >= self_lines[0] and other_lines[1] <= self_lines[1] and other_lines[2] <= self_lines[2] and other_lines[3] >= self_lines[3]:
            return True
        else:
            return False


        
f = rectangle(0,0,4,4)
g = rectangle(2,2,4,4)



print (f)
print (g)
print (f.area())
print (g.area())
print (f.perimeter())
print (g.perimeter())
print (f.intersection(g))
print (g.intersection(f))
print (f.total_perimeter(g))
print (g.total_perimeter(f))
print (f.contains(g))
print (g.contains(f))
