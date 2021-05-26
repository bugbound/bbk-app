echo Installing components...
apt update 
apt -y install apt-transport-https gnupg2 curl 
#curl -s https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - 
cat /app/apt-key.gpg | apt-key add - 
echo "deb http://apt.kubernetes.io/ kubernetes-xenial main" | tee -a /etc/apt/sources.list.d/kubernetes.list 
apt update
apt -y install kubectl
kubectl get pods

chmod a+rx /app/run_pinky_script.sh

echo starting pinky api
cd /app
gunicorn --bind 0.0.0.0:8000 --log-level=DEBUG wsgi:app

