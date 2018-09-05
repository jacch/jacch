#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from mcpi.minecraft import Minecraft

import time
mc = Minecraft.create('192.168.1.113',4713)

class mic:
    x=0
    y=0
    z=0
    u=1
    def playerid(self,n):
        self.u=mc.getPlayerEntityId(n)
        print "Account ID:"
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


    def find_item(self,item):
        result=0
        for xx in range(0,10+1):
            for zz in range(0,10+1):
              for yy in range(0,5):
              
                block=m.getblockinfo(self.x+xx-5,self.y+yy,self.z+zz-5)
                if block.id==item:
                    result =1
      if result==1:
        retuen true
      else
        return false
        
        
m=mic()
m.playerid('jacch') 
m.playerpostion()
m.find_item(2)

