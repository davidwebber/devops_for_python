# devops_for_python

Source code for a talk given Sept 12, 2024 to the Madison Python meetup group.  [The slides are here](https://docs.google.com/presentation/d/1cAMi5Bdfh6kbpHf4BgFQsk_2rY-3LdT5Hi6bVLpGOec/edit#slide=id.p).  This code was developed on Ubuntu 24.04, and should work on any Debian-based distribution.


## Setup 

These instructions assume a command prompt on Ubuntu 24.04

   $ sudo apt install make ipython3 curl docker.io python3-venv docker-compose-v2
   $ python3 -m venv .venv
   $ . .venv/bin/activate
   $ pip install ./dict_cache
   $ pip install ./flask_app
   $ sudo snap install google-cloud-cli --classic

