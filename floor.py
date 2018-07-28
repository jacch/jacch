#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create('192.168.1.113',4717)

class mic:
    x=0
    y=0
    z=0
    u=1
    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        print self.u

    def playerpostion(self):
        x,y,z=mc.entity.getPos(self.u)
        self.x=x
        self.y=y
        self.z=z
        print x,y,z

    def getblockinfo(self,x,y,z):
        p=mc.getBlockWithData(x,y,z)
        return p


    def build2(self,item,y):
        for fg in range(0,10+1):
            for kk in range(0,10+1):
                block=m.getblockinfo(self.x+kk-5,self.y+y,self.z+fg-5)
                if block.id==0:
                    mc.setBlock(self.x+kk-5,self.y+y,self.z+fg-5,item)
 
        
        
m=mic()
m.playerid('jacch')
for a in range(0,1):
    m.playerpostion()
    m.build2(2,-1)
    m.build2(2,-2)
    m.build2(2,-3)
    m.build2(2,-4)
    time.sleep(5)

