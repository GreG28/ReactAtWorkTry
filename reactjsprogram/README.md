# DockerFile pour apprendre React avec le cours disponible sur [reactjsprogram.com](http://reactjsprogram.com)


## Création de l'environnement

Pour commencer à utiliser le projet vous devez construire l'image docker

```
$> sudo docker build -t react-js-programm .
```

Se placer dans le répertoire "dev"

```
$> cd dev
```

Ensuite vous pouvez lancez le conteneur

```
$> sudo docker run --rm -it -v `pwd`:/usr/local/sbin react-js-programm
```

Cette commande à également montée le répertoire courant vers le dossier de travail dans le conteneur

Pour plus d'informations concernant l'utilisation de Docker veuillez lire [ceci](../README.md)

# TODO LIST

- [x] Créer DockerFile
