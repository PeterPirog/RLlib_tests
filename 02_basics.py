"""
from ray import tune
from ray.rllib.agents.ppo import PPOTrainer
from ray.rllib.agents.ddpg import td3

tune.run(PPOTrainer,
    config={"env": "CartPole-v1",
            "framework": "tfe",
            'num_workers': 4,
            'num_gpus':1
            },
    stop={"training_iteration": 20},
    checkpoint_at_end=True,
    verbose=2            # 2 for INFO; change to 1 or 0 to reduce the output.
    )
"""
import ray
from ray.rllib import agents
ray.init(address='auto', _redis_password='5241590000000000')
trainer = agents.a3c.A2CTrainer(env='CartPole-v0')
