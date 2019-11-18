
FROM jupyterhub/jupyterhub:1.0.0

RUN pip install notebook==6.0.1
RUN pip install oauthenticator==0.9.0

RUN apt-get update
RUN apt-get install -y vim
RUN apt-get install sudo
RUN apt-get install -y curl
RUN apt-get install -y lsb-core

RUN curl -sSL https://sdk.cloud.google.com | bash
ENV PATH $PATH:/root/google-cloud-sdk/bin
