#!/bin/bash

pyenv install -l | grep -E " +2.7.3$" > /dev/null
if [ $? -eq 0 ]; then
	pyenv install -s 2.7.3
	if [ -e "/home/student/.pyenv/versions/python2" ]; then
		echo "python2 virtualenv already exists"
	else
		pyenv virtualenv 2.7.3 python2
	fi
fi

pyenv install -l | grep -E " +3.7.3$" > /dev/null
if [ $? -eq 0 ]; then
	pyenv install -s 3.7.3
	if [ -e "/home/student/.pyenv/versions/python3" ]; then
		echo "python3 virtualenv already exists"
	else
		pyenv virtualenv 3.7.3 python3
	fi
fi  

echo "Installed envs are: "
pyenv versions | grep python2
pyenv versions | grep python3







