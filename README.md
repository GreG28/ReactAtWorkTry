# ReactAtWorkTry


## Création de l'environnement

Pour commence à utiliser le projet vous devez construire l'image docker

```
$ sudo docker build -t react-devteam .
```

Ensuite vous pouvez lancez le conteneur pour avoir le serveur RestFull Flask

```
$ sudo docker run --rm -it react-devteam
```

## Trouver l'IP du conteneur

```
$ ip addr show
$ 125: eth0@if126: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:3d brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.61/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:3d/64 scope link
       valid_lft forever preferred_lft forever
```
ici il s'agit de `172.17.0.61`

## Lancement du serveur Flask-RESTful

Pour plus d'informations sur le fonctionnement de Flask-RESTful cliquez [ici](http://flask-restful-cn.readthedocs.org/en/latest/ "Flask-RESTful - User’s Guide").

```
python api.py
```
