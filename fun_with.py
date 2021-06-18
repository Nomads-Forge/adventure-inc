

class the_item(object):
    name=""
    hp=0
    color=''
    price=0
    
    def __init__(self,name,hp,color,price):
        self.name=name
        self.hp=hp
        self.color=color
        self.price=price
class Wepon(object):
    name=''
    ability=''
    damage=0
    duribility=0
    weekness=""
    def __init__(self,name,ability,damadge,duribility,weekness):
        self.name=name
        self.ability=ability
        self.damadge=damadge
        self.duribility=duribility
        self.weekness=weekness
        
class Hero(object):
     name=""
     Class=""
     hp=0
     mp=0
     powers=""
     invintory=[]
     
     def __init__(self,name,Class,hp,mp,powers,invintory):
         self.name=name
         self.Class=Class
         self.hp=hp
         self.mp=mp
         self.powers=powers
         self.invintory=invintory
         
def make_wepon(name,ability,damadge,duribility,weekness):
    wepon=Wepon(name,ability,damadge,duribility,weekness)
    new_wepon=str(wepon.name),str(wepon.damadge) ,"damadge","week VR",wepon.weekness
    return new_wepon

def make_hero(name,Class,hp,mp,powers,invintory):
    hero=Hero(name,Class,hp,mp,powers,invintory)
    return hero

def make_item(name,hp,color,price):
    item=the_item(name,hp,color,price)
    new_item=item.name,str(item.hp)+"hp",item.color,str(item.price)+"G"
    return new_item

