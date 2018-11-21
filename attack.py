import random #importing random library


playerhp=400 #maximum player hp
enemyattacklow=60 #lowest enemy attack
enemyattackhigh=150 #highest enemy attack

while playerhp >0:
    dmg=random.randrange(enemyattacklow,enemyattackhigh) # chose random points between low atk and high
    playerhp=playerhp-dmg # to reduce the playerhp points due to damage

    if playerhp<=0:
        playerhp=0
        print("enemy attacks for", dmg, "points your hp is", playerhp)
    else:
        print("enemy attacks for", dmg, "points your hp is", playerhp)

    if playerhp <=30:
        print("your hp is low you have", playerhp)
        break #to breaking out of while loop

#*********************************the end*************************************#
