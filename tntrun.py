from mcpi.minecraft import Minecraft
import time
from random import *
mc = Minecraft.create()

mc.setBlocks(-191, -64, -191, 191, 128, 191, 0)
mc.setBlocks(-20, -1, -20, 20, -1, 20, 46)
mc.setBlock(0,5,0,2)
mc.setBlocks(0, 0, 0, 0, 5, 0, 7)

pos = mc.player.getPos()
x, y, z = mc.player.getPos()
selected = 0
#while True:
    #x, y, z = mc.player.getPos()
    #mc.setBlock(x, y-1, z,0)
mc.postToChat('game starts in 5 second')

time.sleep(5)
mc.postToChat('Game started')
while True:
    entityIds = mc.getPlayerEntityIds()
    try:
        
        entityId = entityIds[selected]
        x,y,z = mc.entity.getPos(entityId)
        blockType = mc.getBlock(x,y-.1,z)
        if y < -69:
            mc.player.setPos(randrange(-20,20),20,randrange(-20,20),entityId)
            mc.postToChat('#'+ str(entityId) +' fell in the void')
        if blockType == 0:
            mc.setBlock(x+1, y, z,0)
            mc.setBlock(x-1, y, z,0)
            mc.setBlock(x, y, z+1,0)
            mc.setBlock(x, y, z-1,0)
        mc.setBlock(x, y-.1, z,0)
        selected += 1
    except IndexError:
        time.sleep(.5)
        selected = 0
        

    
   