#!/bin/bash
cd /home/ec2-user/
curl -sSL https://raw.githubusercontent.com/helm/helm/master/scripts/get-helm-3 | bash
curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.12.0/kind-linux-amd64
wget https://github.com/rfmsec/Learning/raw/master/flask-kubeapi.zip
chmod +x ./kind && mv ./kind /usr/local/bin/
yum install -y docker
service docker start
chkconfig docker on
/usr/local/bin/kind create cluster
unzip flask-kubeapi.zip
helm install flask-kubeapi ./flask-kubeapi