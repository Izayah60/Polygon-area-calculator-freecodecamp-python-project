class Rectangle:
  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __repr__(self):
    return f"Rectangle(width={self.width}, height={self.height})"

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return (self.width * self.height)

  def get_perimeter(self):
    return (2 * self.width) + (2 * self.height)

  def get_diagonal(self):
    return (((self.width ** 2) + (self.height ** 2)) ** .5)

  def get_picture(self):
    if self.width > 50 or self.height > 50:
      return "Too big for picture."
    picture = ""
    for item in range(self.height):
      picture += "*" * self.width + "\n"
    return picture

  def get_amount_inside(self, shape):
    inside_area = shape.width * shape.height
    outside_area = self.get_area()
    return outside_area // inside_area
    

# r = Rectangle(12, 10)
# print(r.get_amount_inside(13, 15))



class Square(Rectangle):
  def __init__(self, side):
    super().__init__(side, side)
  def __repr__(self):
    return f"Square(side={self.width})"
    
  def set_side(self, side):
    self.width = side
    self.height = side

  def set_width(self,side):
    self.set_side(side)

  def set_height(self,side):
    self.set_side(side)

