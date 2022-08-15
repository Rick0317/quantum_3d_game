from ursina import *

class Inventory(Entity):
  def __init__(self):
    super().__init__(
      parent = camera.ui,                                         
      model = 'quad',
      scale = (.8, .5),                                           
      origin = (-.5, .5),                                         
      position = (-.3,.4),                                        
      texture = 'white_cube',                                     
      texture_scale = (5,8),                                      
      color = color.dark_gray 
    )
    self.item_parent = Entity(parent=self, scale=(1/5,1/8)) 

  def append(self, item):                                             
        Button(                                                         
          parent = self.item_parent,                             
          model = 'quad',                                             
          origin = (-.5,.5),                                          
          color = color.random_color(),  
          position = self.find_free_spot(),                             
          z = -.1                                                     
        )
  def find_free_spot(self):                                                      
      taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]    
      for y in range(8):                                                         
          for x in range(5):                                                     
              if not (x,-y) in taken_spots:                                      
                  return (x,-y)        


class ItemBar(Entity):
  def __init__(self):
    super().__init__(
      parent = camera.ui,
      model = 'quad',
      scale = (0.5, 0.1),
      y = -0.46,
      texture = 'white_cube',                                     
      texture_scale = (5,1),                                      
      color = color.dark_gray 
    )
    self.item_parent = Entity(parent=self, scale=(1,1))
    self.icon1 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (2,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon2 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (1,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon3 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (0,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon4 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (-1,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
    self.icon5 = Button(                                                         
      parent = self.item_parent,                             
      model = 'quad',                                             
      origin = (-2,0),
      scale=(1/5, 1),
      color = color.white,
      texture="play_button.png",                               
      z = -.1                                                     
    )
  

