# Journalisation

Cette section présente les emplacements où trouver les fichiers journaux de Jimber SASE sur les appareils utilisateur et les serveurs, sur différentes plateformes. Un accès adéquat à ces journaux est essentiel pour dépanner l’application et superviser son comportement.

### Présentation des types de journaux

- **Journaux du client :** enregistrent des informations sur le démarrage et le fonctionnement de l’application **_<span style="color: darkblue;">Jimber SASE Client</span>_** sur les appareils utilisateur.
- **Journaux du serveur :** consignent des informations détaillées sur le composant côté serveur de la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**.
- **Journaux du service :** contiennent des informations sur le **_<span style="color: darkblue;">Jimber SASE Service</span>_**, le service local en arrière-plan chargé de gérer la connectivité et d’autres tâches essentielles.
- **Journaux du lanceur :** suivent les activités liées au lancement et à la mise à jour des applications Jimber.
- **Journaux de débogage :** fichiers vides spéciaux qui activent une journalisation plus détaillée dans les autres fichiers journaux lorsqu’ils sont présents.

> [!WARNING]
> Le fichier `debug.log` lui-même ne contient **aucun** journal. Lorsqu’il est présent, il active plutôt une journalisation détaillée dans les couches client, serveur et service afin de faciliter le diagnostic des problèmes

---

### Activation de la journalisation de débogage

Pour activer une journalisation de débogage étendue, créez un fichier **vide** nommé `debug.log` dans le répertoire approprié pour votre plateforme :

- **Windows :** `%PROGRAMFILES%\Jimber\`
- **Linux / macOS / contrôleurs réseau :** `/var/log/jimber/`

Une fois le fichier créé, le système produira des journaux plus détaillés qui peuvent aider à repérer les problèmes.

---

### Emplacements des fichiers journaux par plateforme

#### Windows

##### Bureau (appareils utilisateur)
- Journal du client : `%LocalAppData%\Jimber\client.log`
- Journal du service : `%PROGRAMFILES%\Jimber\service.log`
- Journal du lanceur : `%PROGRAMFILES%\Jimber\launcher.log`
- Fichier déclencheur de débogage : `%PROGRAMFILES%\Jimber\debug.log`

##### Serveur
- Journal du serveur : `%PROGRAMFILES%\Jimber\server.log`
- Journal du lanceur : `%PROGRAMFILES%\Jimber\launcher.log`
- Fichier déclencheur de débogage : `%PROGRAMFILES%\Jimber\debug.log`

---

#### Linux

##### Bureau (appareils utilisateur)
- Journal du client : `~/.local/share/jimber/client.log`
- Journal du service : `/var/log/jimber/service.log`
- Journal du lanceur : `/var/log/jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/jimber/debug.log`

##### Serveur
- Journal du serveur : `/var/log/jimber/server.log`
- Journal du lanceur : `/var/log/jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/jimber/debug.log`

---

#### macOS

##### Bureau (appareils utilisateur)
- Journal du client : `~/Library/Application Support/Jimber/client.log`
- Journal du service : `/var/log/Jimber/service.log`
- Journal du lanceur : `/var/log/Jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/Jimber/debug.log`

---

#### Contrôleur réseau / NIAC / Synology / Raspberry Pi

- Journal du serveur : `/var/log/jimber/service.log`
- Journal du lanceur : `/var/log/jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/jimber/debug.log`

---

### Remarques et bonnes pratiques

- Il est recommandé de créer le fichier `debug.log` uniquement lors du dépannage de problèmes spécifiques, car cela augmente le niveau de détail des journaux et peut générer des fichiers journaux volumineux.
- Dans les environnements de production, supervisez et archivez régulièrement les journaux afin d’éviter une utilisation excessive de l’espace disque.
- Lorsque vous signalez des problèmes au support, joindre les fichiers journaux pertinents (en particulier lorsque la journalisation de débogage est activée) accélérera le diagnostic.
