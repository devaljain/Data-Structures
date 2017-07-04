def moveTower(height,fromTower,toTower,withTower):
    if height>=1:
        moveTower(height-1,fromTower,withTower,toTower)
        moveDisk(fromTower,toTower)
        moveTower(height-1,withTower,toTower,fromTower)

def moveDisk(frm,to):
    print("Moving disk from"+frm+"to"+to)

moveTower(3,"A","B","C")
