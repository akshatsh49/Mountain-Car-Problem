from collections import defaultdict
import numpy as np
import random
import math
from statistics import mean
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import seaborn as sns
import pickle
from celluloid import Camera

class World():
  def __init__(self,pos,vel):
    self.action_space=[-1,0,1]
    self.pmax=1.2
    self.pmin=-1.2
    self.vmax=0.07
    self.vmin=-0.07
    self.pos=self.bound_pos(pos)
    self.vel=self.bound_vel(vel)
    self.tile_num=3
    self.offset=[[0,0],[-0.1,0.01],[0.1,-0.01]]
  
  def show(self):
    print('Position is {} Speed is {}'.format(self.pos,self.vel))

  def bound_pos(self,a):
    if(a>self.pmax):
      a=self.pmax
    elif(a<self.pmin):
      a=self.pmin
    return a 
  
  def bound_vel(self,a):
    if(a>self.vmax):
      a=self.vmax
    elif(a<self.vmin):
      a=self.vmin
    return a 
  
  def move(self,a):
    new_pos=self.bound_pos(self.pos+self.vel)
    new_vel=self.bound_vel(self.vel+0.001*a - 0.0025*math.sin(self.pos)/(math.sqrt(1+math.sin(self.pos)**2)) )
    if(new_pos>=self.pmax):
      R=0
    else:
      R=-1
    return new_pos,new_vel,R

  def give_code(self):
    assert(self.tile_num==len(self.offset))
    l=[]
    for i in range(self.tile_num):
      offset=self.offset[i]
      pos=math.floor(self.pos-self.pmin-offset[0]/((self.pmax-self.pmin)/100))
      vel=math.floor(self.vel-self.vmin-offset[1]/((self.vmax-self.vmin)/100))
      l.append([pos,vel])
    return l