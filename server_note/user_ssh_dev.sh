!# /bin/bash

# vars
thich2hand_url="https://github.com/phudinhtruongk18/Thich2Hand"

# install docker compose no confirm
# sudo curl -fsSL https://get.docker.com | bash
sudo apt-get update && sudo apt-get install docker-compose -y
# install nginx
sudo apt-get install nginx -y

# config 2 nginx files in nginx folder

# create users
sudo useradd --create-home --user-group --shell /bin/bash --groups docker dev_deploy
sudo usermod --lock dev_deploy

sudo -i -u dev_deploy
ssh-keygen -t ed25519 -f ~/.ssh/id_dev_deploy -C "dev_deploy@server" -N ""

cat .ssh/id_dev_deploy.pub > .ssh/authorized_keys
cat .ssh/id_dev_deploy


sudo -i -u dev_deploy
git clone https://github.com/phudinhtruongk18/Thich2Hand

exit

sudo useradd --create-home --user-group --shell /bin/bash --groups docker staging_deploy
sudo usermod --lock staging_deploy

sudo -i -u staging_deploy
ssh-keygen -t ed25519 -f ~/.ssh/id_staging_deploy -C "staging_deploy@server" -N ""
cat .ssh/id_staging_deploy.pub > .ssh/authorized_keys\
cat .ssh/id_staging_deploy

sudo -i -u staging_deploy
git clone https://github.com/phudinhtruongk18/Thich2Hand
exit

