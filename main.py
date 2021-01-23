from agent import *

training_eps=10000
test_runs=5
max_len=1000
testing_steps=[]
ag=Agent()

for episode in range(training_eps):
  w=World(0,0)
  for step in range(max_len):
    a=ag.e_greedy(w.pos,w.vel)
    nextp,nextv,R=w.move(a)
    a_next=ag.e_greedy(nextp,nextv)
    ag.update(w.pos,w.vel,a,R,nextp,nextv,a_next)
    w.pos=nextp
    w.vel=nextv
    if(R==0):
      break
    elif(w.pos<=w.pmin):
      w.vel=0 # the car bumps to a stop 

  """
  running agent after each simulation
  multiple runs to get a better estimate of agent performance at this episode
  test_run_list stores the corresponding "test_run" number of values
  """
  test_run_list=[]
  for run in range(test_runs):
    w=World(0,0)
    for step in range(max_len):
      a=ag.greedy(w.pos,w.vel)
      nextp,nextv,R=w.move(a)
      a_next=ag.greedy(nextp,nextv)
      """
      The next command is required even in test case because the agent must learn to move in the environment every time it interacts with it. If it encounters a state upon which it is not trained well the agent would fail repeatedly across test runs unless we update it between runs.
      """
      ag.update(w.pos,w.vel,a,R,nextp,nextv,a_next) 

      w.pos=nextp
      w.vel=nextv
      if(R==0):
        break
      elif(w.pos<w.pmin):
        w.vel=0
    test_run_list.append(step)
  testing_steps.append(mean(test_run_list))

  if(episode%1000==0):
    print('Done episode {}'.format(episode))    

# save agent
f='agent.sav'
file=open(f,'wb')
pickle.dump(ag,file)
file.close()

# plot peformance of agent with training episodes
plt.plot(range(1,1+len(testing_steps)),testing_steps,label='No. of steps')
plt.title('No. of steps to reach terminal states vs. training episodes')
plt.xlabel('Training Episodes')
plt.ylabel('No. of steps')
plt.legend()
plt.savefig('No_steps_vs_training_eps.png')