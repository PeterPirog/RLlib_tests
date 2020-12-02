import os

try:
    os.system('ray stop')
except:
    pass
os.system('ray start --head')
os.system('rllib train --run=A2C --env=CartPole-v0')
os.system('ray stop')


