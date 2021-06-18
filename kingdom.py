import fun_with
mi=fun_with.make_item
mh=fun_with.make_hero
mw=fun_with.make_wepon

# \\HERO (name,Class,hp,mp,powers,invintory)//

ike=mh("ike","roug",10,15,"in plain sight",[])
zeb=mh("zeb","bard",20,10,"sing",[])
jim=mh('jim',"paliden",50,5,"devine smite",[])
teea=mh('teea',"wizard",15,25,'arctic blast',[])
# \\item (name,hp,color,price) //
# head

hat_r=mi("hat",1,"red",1)
# chest

robe_of_protection=mi("robr of protection",3,"purple",10)
shirt=mi("shirt",5,"blue",3)
# legs

# feet

# glove

# \\WEPOM (name,ability,damadge,duribility,weekness)//
excaliber = mw("excaliber","purifying blast",30,100,"good")




zeb.invintory.append(excaliber)
teea.invintory.append(robe_of_protection)
zeb.invintory.append(shirt)
jim.invintory.append("flask")

print(ike.Class)
print(zeb.name,zeb.Class,zeb.invintory)
print(teea.invintory)