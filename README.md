# ReactAtWorkTry


## Création de l'environnement

Pour commence à utiliser le projet vous devez construire l'image docker

```
$> sudo docker build -t react-devteam .
```

Pour supprimmer toutes les images existantes : `sudo docker rmi --force=true $(sudo docker images -q)`

Ensuite vous pouvez lancez le conteneur pour avoir le serveur RestFull Flask

```
$> sudo docker run --rm -it react-devteam
```

ou bien de cette façon pour monter les répertoire courant vers le répertoire `/usr/local/sbin` du conteneur

```
$> sudo docker run --rm -it -v `pwd`:/usr/local/sbin react-devteam
```


Démmarer le conteneur et rediriger le port 8080 de l'host vers le port 80 du conteneur
```
$> sudo docker run --rm -it -v `pwd`:/usr/local/sbin --net=host -p 8080:80 react-devteam
```

Démmarer le conteneur et rediriger le port 8080 de l'host vers le port 80 du conteneur
```
$> sudo docker run --rm -it -v `pwd`:/usr/local/sbin --net=host -p 8080:80 react-devteam
```


## Trouver l'IP du conteneur

```
$> ip addr show
$> 125: eth0@if126: <BROADCAST,UP,LOWER_UP> mtu 1500 qdisc noqueue state UP group default
    link/ether 02:42:ac:11:00:3d brd ff:ff:ff:ff:ff:ff
    inet 172.17.0.61/16 scope global eth0
       valid_lft forever preferred_lft forever
    inet6 fe80::42:acff:fe11:3d/64 scope link
       valid_lft forever preferred_lft forever
```
ici il s'agit de `172.17.0.61`

## Lancement du serveur Flask-RESTful sur le port : 80

Pour plus d'informations sur le fonctionnement de Flask-RESTful cliquez [ici](http://flask-restful-cn.readthedocs.org/en/latest/ "Flask-RESTful - User’s Guide").

```
$> cd api
$> python api.py
```

De plus, j'ai utilisé une wrapper qui permet de créer automatiquement une documentation Swagger.

Le projet est disponible [ici](https://github.com/rantav/flask-restful-swagger "Github - flask-restful-swagger").

La documentation de l'API est disponible à l'adresse suivante `/api/spec.html`

# TODO LIST

- [x] Créer DockerFile
- [x] Mettre à jours la documentation du projet
- [ ] Mettre à jours la documentation de l'API
- [x] Créer une tâche dans le script au démarrage du conteneur
- [x] Ecrire script pour lancer le serveur Flask-RESTful pour l'API
- [ ] Nettoyer l'API pour enlever les exemples de Flask-RESTful
- [ ] Ranger le projet pour mieux séparer l'api du front React
- [ ] Monter séparement les volumes pour mieux maitriser les impacts
- [ ] Définir les objectifs du projet pour la fin
- [ ] Ajouter les packages aux dépendances
