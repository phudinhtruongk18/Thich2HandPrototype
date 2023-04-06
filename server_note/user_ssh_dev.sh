!# /bin/bash

sudo useradd --create-home --user-group --shell /bin/bash --groups docker dev_deploy
sudo usermod --lock dev_deploy

sudo -i -u dev_deploy
ssh-keygen -t ed25519 -f ~/.ssh/id_dev_deploy -C "dev_deploy@server"

# cat .ssh/id_dev_deploy.pub > .ssh/authorized_keys
# cat .ssh/id_dev_deploy
