#https://towardsdatascience.com/ray-and-rllib-for-fast-and-parallel-reinforcement-learning-6d31ee21c96c
#https://github.com/ray-project/ray/issues/10466

#You should start ray instance using ray start --head or ray start --address="[your head node address]" on your node.

# rllib train --run PPO --env CartPole-v1 --stop='{"training_iteration": 20}' --ray-address auto --checkpoint-freq 10 --checkpoint-at-end

import ray
from ray.rllib import agents
ray.init(address='auto', _redis_password='5241590000000000') # Skip or set to ignore if already called  ray.init(address='auto', _redis_password='5241590000000000')
config = {'gamma': 0.9,
          'lr': 1e-2,
          'num_workers': 4,
          'num_gpus': 1,
          'train_batch_size': 1000,
          'model': {
              'fcnet_hiddens': [128, 128]
          }}
trainer = agents.ppo.PPOTrainer(env='CartPole-v0', config=config) #CartPole-v0
results = trainer.train()
"""
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
tune.run(PPOTrainer,
    config={"env": "CartPole-v1",'num_workers': 4},
    stop={"training_iteration": 20},
    checkpoint_at_end=True,
    verbose=2            # 2 for INFO; change to 1 or 0 to reduce the output.
    )
    
"""