import gym
import numpy as np

import utils

# OpenAI gym je knihovna, ktera poskytuje radu ruznych prostredi pro 
# zpetnovazebni uceni. Hlavni vyhodou je, ze ke vsem prostredim potom poskytuje
# stejne rozhrani. Implemetace ruznych typu zpetnovazebniho uceni je potom 
# celkem jednoducha a obecna.

# Vytvorme si jednoduche prostredi, ktere jsme si ukazovali na prednasce - 
# MountainCar (https://gym.openai.com/envs/MountainCar-v0/). 
env = gym.make('MountainCar-v0')

# Prostor pozorovani a prostor akci muzeme snadno ziskat pomoci nasledujicich
# dvou radek.
print('observation space:', env.observation_space)
print('observation space low:', env.observation_space.low)
print('observation space high:', env.observation_space.high)
print('action space:', env.action_space)

# Pred spustenim simulace prostredi je potreba ho resetovat - tim dostaneme 
# prvni pozorovani.
obs = env.reset()
print('initial observation:', obs)

# OpenAI gym umoznuje i snadno ziskat nahodnou akci pomoci metody sample()
action = env.action_space.sample()

# Akci na prostredi aplikujeme pomoci metody step(action), dostaneme nove 
# pozorovani, okamzitou odmenu, informaci o konci simulace a dalsi info.
obs, r, done, info = env.step(action)
print('next observation:', obs)
print('reward:', r)
print('done:', done)
print('info:', info)

# Muzeme si napsat obecnou tridu pro agenta, ktery se chova nahodne. Muzete ho
# pozdeji pouzit jako zaklad pro zpetnovazebniho agenta

class RandomAgent:
  
    def __init__(self, actions):
        self.actions = actions
    
    def act(self, observe, reward, done):
        return self.actions.sample()
    
    def stop_episode(self):
        pass

agent = RandomAgent(env.action_space)


# Pri trenovani agenta potom budeme potrebovat odehrat mnoho iteraci - to muzeme
# udelat napriklad podobne jako nize.

import qlearning

sd = qlearning.StateDiscretizer(np.array([env.observation_space.low, env.observation_space.high]).T, [20, 20])
agent = qlearning.QLearningAgent(env.action_space, sd, train=True)

total_rewards = []
for i in range(10000):
    obs = env.reset()
    agent.stop_episode()
    
    done = False
    r = 0
    R = 0 # celkova odmena - jen pro logovani, nepouziva se jinde
    t = 0 # cislo kroku - take se nepouziva primo
    
    while not done:
        action = agent.act(obs, r, done)
        obs, r, done, _ = env.step(action)
        R += r
        t += 1

    total_rewards.append(R)

agent.train = False
import matplotlib.pyplot as plt

utils.show_animation(agent, env, steps=200, episodes=5)

# zobrazime graf uceni - show nam zaroven zajisti, ze program neskonci, dokud 
# nezavreme graf
plt.plot(utils.moving_average(total_rewards, 100))
plt.show() 

env.close()