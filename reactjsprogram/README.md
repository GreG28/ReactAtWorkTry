# DockerFile pour apprendre React avec le cours disponible sur [reactjsprogram.com](http://reactjsprogram.com)


## Création de l'environnement

Pour commencer à utiliser le projet vous devez construire l'image docker

```
$> sudo docker build -t react-js-programm .
```


Sous windows à l'ouverture d'un nouveau shell ou powershell tapez les commande suivantes :

Shell
```
$> docker-machine env --shell cmd default
```

Powershell
```
$> docker-machine env --shell powershell default | Invoke-Expression
```

Se placer dans le répertoire "dev"

```
$> cd dev
```

Ensuite vous pouvez lancez le conteneur

```
$> sudo docker run -it -v `pwd`:/usr/local/sbin/reactjsprogramm -p 8080:8080 react-js-programm
```

Sous windows
```
$> docker run -it -v <path>:/usr/local/sbin/reactjsprogramm -p 8080:8080 react-js-programm
```
Le path doit être écrit de cette manière "/c/Users/gregoire/Documents/ReactAtWorkTry/reactjsprogram/dev"

Pour windows voici quelques liens pour cela fonctionne :
* [port exposure on windows = ?](https://github.com/docker/docker/issues/15740)
* [Container port redirection](https://docs.docker.com/engine/installation/windows/#container-port-redirection)

Cette commande à également montée le répertoire courant vers le dossier de travail dans le conteneur

Pour plus d'informations concernant l'utilisation de Docker veuillez lire [ceci](../README.md)

# Webpack

Commande pour que webpack s'execute dès la modification d'un fichier
```
$> webpack -w
```

# Tips :

La commande suivante permet de changer l'host du serveur et donc d'y accèder depuis l'exterieur du conteneur
```
$> webpack-dev-server --host 0.0.0.0
```

# TODO LIST

- [x] Créer DockerFile
