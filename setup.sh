#!/bin/bash

# Install OpenJDK (Java)
sudo apt-get update
sudo apt-get install openjdk-11-jdk -y

#jre and allure 
sudo apt-get install default-jre
wget https://github.com/allure-framework/allure2/releases/download/2.27.0/allure_2.27.0-1_all.deb
sudo dpkg -i allure_2.27.0-1_all.deb
rm -r allure*.deb

# Verify installation
allure --version

pip3 install -r requirements.txt