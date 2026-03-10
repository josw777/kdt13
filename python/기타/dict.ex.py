lux1 = dict(health=490,mana=334,melee=550,armor=18.72)
print(lux1)
lux2 = dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
print(lux2)
lux3 = dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
print(lux3)
lux4 = dict({'health':490,'mana':334,'melee':550,'armor':18.72})
print(lux4)
lux5 = {'health':490,
        'mana':334,
        'melee':550,
        'armor':18.72}
print(lux5)

print("=========\n")

dct = {}
dct['id'] = 'hong'
dct['pw'] = '1234'
print(dct)
dct['email'] = 'hong@gmail.com'
print(dct)
dct['id'] = 'lee'
print(dct)
del dct['email']
print(dct)