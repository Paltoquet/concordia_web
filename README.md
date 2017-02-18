# concordia_web

Serveur Web mettant à disposition les différents relevés des capteurs de la raspberry
Assurez vous que l'addresse a bien été ajoutée au serveur WCOMP

##Access

Différentes routes sont à votre disposition en `GET` depuis votre navigateur

- / page d'acceuil
- /api/config pour mettre à jour votre configuration
- /api/sensor_name pour visualiser les données

Vous pouvez poster de nouvelles données en réalisant un `PUT` sur 
- /api/sensor_name en fournissant un JSON au bon format

##Installation

- `Clonez` le répertoire
- Run `run.bat`


