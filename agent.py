from world import *

class Agent():
  def __init__(self,alpha=0.01,eps=0.1,gamma=0.95):
    self.alpha=alpha
    self.gamma=gamma
    self.eps=eps
    self.action_space=[-1,0,1]
    self.q=[]
    self.pmax=1.2
    self.pmin=-1.2
    self.vmax=0.07
    self.vmin=-0.07
    self.tile_num=6
    self.offset=[[0.02/2,-0.0015/2],[0.02*3/2,0.0015/2],[-0.02/2,0.0015*(-3)/2],[-0.02/2,0.0015/2],[0.02/2,3/2*0.015],[0.02*(-3)/2,-0.0015/2]]
    for i in range(self.tile_num):
      self.q.append(defaultdict(int))

  def q_value(self,pos,vel,a):
    q=0
    l=self.give_code(pos,vel)
    for i in range(self.tile_num):
      q+=self.q[i][l[i][0],l[i][1],a]
    return q/self.tile_num

  def give_code(self,pos,vel):
    assert(self.tile_num==len(self.offset))
    l=[]
    for i in range(self.tile_num):
      offset=self.offset[i]
      pos_code=math.floor(pos-self.pmin-offset[0]/((self.pmax-self.pmin)/100))
      vel_code=math.floor(vel-self.vmin-offset[1]/((self.vmax-self.vmin)/100))
      l.append([pos_code,vel_code])
    return l

  def greedy(self,pos,vel):
    best=-1
    mx=self.q_value(pos,vel,best)
    for a in self.action_space:
      if(self.q_value(pos,vel,a)>mx):
        mx=self.q_value(pos,vel,a)
        best=a
    return best

  def e_greedy(self,pos,vel):
    if(np.random.rand()>self.eps):
      return self.greedy(pos,vel)
    else :
      return random.choice(self.action_space)

  def update(self,pos,vel,a,R,pos1,vel1,a1):
    # a simple TD(0) update
    l=self.give_code(pos,vel)
    l1=self.give_code(pos1,vel1)

    for i in range(self.tile_num):
      target=self.q[i][l1[i][0],l1[i][1],a1]
      self.q[i][l[i][0],l[i][1],a]+=self.alpha*(R+self.gamma*target-self.q[i][l[i][0],l[i][1],a])