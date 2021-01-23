# Mountain-Car-Problem

## Introduction
An implementation of the mountain car problem from [Reinforcement Learning: An Introduction](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) Ch 10 Example 10.1
<img src="https://camo.githubusercontent.com/ab2f04f7d151d12ec546618cd588bccf3492b669a83a4951eabc194deb4a2747/68747470733a2f2f692e696d6775722e636f6d2f4e594d735171582e706e67" width=300 align="center"/>


#### A Brief Description of the Problem
The problem involves a car starting at point (0,0) on a hill of shape y = 1-cos(x). The car must cross over some fixed point by applying throttle which changes the car's tangential velocity. The catch is that the agent can't cross the hill by continuously applying a positive throttle and must learn to gather momentum by oscillating around the starting position.

## The environment 
The shape of our hill is y = 1-cos(x) which is different from the book. We choose this as it is easy to calculate the slope of the hill and hence to calculate the tangential retardation caused by gravity. As proof of concept, we don't use any function approximation or deep RL techniques and decide to work with a 2D discretized state space. We use tile-coding as described in [Reinforcement Learning: An Introduction](https://web.stanford.edu/class/psych209/Readings/SuttonBartoIPRLBook2ndEd.pdf) Ch 9

## The Agent
The Sarsa algorithm is used.

## Results
<img src="https://github.com/akshatsh49/Mountain-Car-Problem/blob/master/animate.gif" width='400'>
If you made it to the end you would have noticed that the task is completed.</br>
The agent learns to gain momentum around the origin.
Used celluloid and the scatter module from matplotlib.pyplot to get an animation of the episode.


## Future Work
The present implementation can be improved upon by implementing the following points
* Using queuing techniques like priority sweeping
* Using function approximations and Deep RL techniques which are known to work better than space discretization.
