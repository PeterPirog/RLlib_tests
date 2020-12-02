#Use existing docker image as a base
FROM tensorflow/tensorflow:2.3.1-gpu

#Download and install dependencies
RUN export python=python3
RUN apt-get update
RUN apt-get install -y libgl1-mesa-dev
RUN python3 -m pip install --upgrade pip
RUN python3 -m pip install --upgrade setuptools
RUN pip install torch===1.7.0+cu110 torchvision===0.8.1+cu110 torchaudio===0.7.0 -f https://download.pytorch.org/whl/torch_stable.html
RUN pip install ray[rllib]

#RUN ray start --head
# Container start command
#CMD ["sh"]


CMD ["ray start --head"]



#command to build new image:
#sudo docker build -t peterpirogtf/rllib:latest .

#How to push docker image to hub

#login by:
# docker login
# docker push peterpirogtf/rllib:latest
#https://stackoverflow.com/questions/41984399/denied-requested-access-to-the-resource-is-denied-docker