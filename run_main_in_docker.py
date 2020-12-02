import os


container_id='peterpirogtf/rllib:latest'
#docker_cmd=f"sudo docker run -v `pwd`:`pwd` -w `pwd` --gpus all -it --rm {container_id} python 'main_ddpg.py'"


docker_cmd=f"sudo docker run -v `pwd`:`pwd` -w `pwd` --gpus all -it --rm {container_id} python '01_basics.py'"
os.system(docker_cmd)

#TODO:
#convert actor model to Functional or sequential form to save and load as one file
# add nosie for observations
#monit number of steps before fail