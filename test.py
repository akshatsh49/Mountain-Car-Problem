from agent import *

# load agent
ag=Agent()
f='agent.sav'
file=open(f,'rb')
ag=pickle.load(file)
file.close()

w=World(0,0)
max_len=1000
ep_list=[]
x_list=[]
vel_list=[]
crosses_over_origin = -2 # to ignore first 2 values

for step in range(5*max_len):
  ep_list.append([w.pos,w.vel])
  x_list.append(w.pos)
  vel_list.append(w.vel)
  a=ag.greedy(w.pos,w.vel)
  nextp,nextv,R=w.move(a)

  if(nextp*w.pos<=0):
    crosses_over_origin+=1

  a_next=ag.greedy(nextp,nextv)
  ag.update(w.pos,w.vel,a,R,nextp,nextv,a_next)
  w.pos=nextp
  w.vel=nextv
  if(R==0):
    ep_list.append([w.pos,w.vel])
    x_list.append(w.pos)
    vel_list.append(w.vel)
    break

  elif(w.pos<=w.pmin):
    w.vel=0

print('Crosses over origin : {}'.format(crosses_over_origin))
print(len(ep_list))

fig=plt.figure()
w = animation.HTMLWriter(fps=10)
cam=Camera(fig)

for i in range(len(x_list)//10):
  plt.plot( np.arange(-1.2,1.2,step=0.01),1-np.cos(np.arange(-1.2,1.2,step=0.01)), 'r')
  plt.xlabel('X')
  plt.ylabel('Y=1-cos(x)')
  temp=x_list[10*i:10*i+10]
  y_list=1-np.cos(temp)
  plt.scatter(temp , y_list)
  cam.snap()

anim=cam.animate(interval = 50, repeat = True, repeat_delay = 500)
anim.save('animate.html',writer=w)

"""
lessons learnt : don't be a hero, use openAI Gym for visual simulations ;)
although we were able to get fairly intuitive animations using celluloid and matplotlib
"""

file=open(f,'wb')
pickle.dump(ag,file)
file.close()