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


