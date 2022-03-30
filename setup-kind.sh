#!/bin/bash
cd /home/ec2-user/
curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.12.0/kind-linux-amd64
wget https://github.com/rfmsec/Learning/raw/master/flask-kubeapi.zip
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
echo "export KUBECONFIG = '/home/ec2-user/.kube/config'" >> /etc/bashrc
chmod +x ./kind && mv ./kind /usr/local/bin/
yum install -y docker
service docker start
chkconfig docker on
/usr/local/bin/kind create cluster
unzip flask-kubeapi.zip
helm install flask-kubeapi ./flask-kubeapi
