# Segundo Parcial Operativos
### Nombre: Jose Luis Sacanamboy
### Código: 13103010

---------

#Desarrollo
Este parcial consta de la realización de pruebas a través de la herramienta Jenkins, a los servicios que se realizaron en el anterior parcial.

##Configuración Jenkins
Primero se configura la fecha del servidor de Jenkins.

```sh
yum install ntp ntpdate ntp-doc
chkconfig ntpd on
ntpdate pool.ntp.org
/etc/init.d/ntpd start
```
Una vez configurada la hora del servidor proseguimos a instalar el Jenkins.

```sh
yum install java-1.7.0-openjdk
yum install wget -y
yum install git -y
sudo wget -O /etc/yum.repos.d/jenkins.repo http://pkg.jenkins-ci.org/redhat/jenkins.repo
sudo rpm --import https://jenkins-ci.org/redhat/jenkins-ci.org.key
sudo yum install jenkins
```

Se ha instalado el Jenkins correctamente. Proseguimos activar el servicio web de Jenkins y el puerto 8080 por el cual el Jenkins sube.

```sh
chkconfig jenkins on
service jenkins start
iptables -I INPUT 5 -p tcp -m state --state NEW -m tcp --dport 8080 -j ACCEPT
service iptables save
```
Una vez instalado Jenkins continuamos a crear el ambiente virtual con el que correrá Jenkins.

```sh
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py
pip install virtualenv

mkdir /var/lib/jenkins/.virtualenvs
cd /var/lib/jenkins/.virtualenvs
virtualenv testproject
. testproject/bin/activate
```

Activado el ambiente virtual, se sigue la instalación de las dependencias necesarias para la realización de las pruebas.

```sh
pip install xmlrunner
pip install unittest2
pip install pytest
pip install pytest-cov
pip install flask

pip freeze > requirements.txt
```
Finalizado. Ahora se abre el Jenkins por medio de la URL http://192.168.1.64:8080/, esta es respecto a la dirección de la máquina utilizada.

![alt link]()






