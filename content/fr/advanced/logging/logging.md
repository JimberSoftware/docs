# Journalisation

Cette section présente les emplacements où trouver les fichiers journaux de Jimber SASE sur les appareils utilisateur et les serveurs, sur différentes plateformes. Un accès adéquat à ces journaux est essentiel pour dépanner l’application et superviser son fonctionnement.

### Présentation des types de journaux

- **Journaux client :** enregistrent des informations sur le démarrage et le fonctionnement de l’application `Jimber SASE Client` sur les appareils utilisateur.
- **Journaux serveur :** enregistrent des informations sur le composant côté serveur de `Jimber SASE Platform`.
- **Journaux du service :** contiennent des informations sur le `Jimber SASE Service`, le service d’arrière-plan local chargé de gérer la connectivité et d’autres tâches essentielles.
- **Journaux du lanceur :** retracent les activités liées au lancement et à la mise à jour des applications Jimber.
- **Journaux de débogage :** fichiers spéciaux vides qui, lorsqu’ils sont présents, activent une journalisation plus détaillée dans les autres fichiers journaux.

> [!WARNING]
> Le fichier `debug.log` lui-même ne contient **aucun** journal. En revanche, lorsqu’il est présent, il active une journalisation détaillée dans les couches client, serveur et service afin de faciliter le diagnostic des problèmes.

---

### Activation de la journalisation de débogage

Pour activer une journalisation de débogage étendue, créez un fichier **vide** nommé `debug.log` dans le répertoire approprié pour votre plateforme :

- **Windows :** `%PROGRAMFILES%\Jimber\`
- **Linux / macOS / Contrôleurs réseau :** `/var/log/jimber/`

Une fois le fichier créé, le système produira des journaux plus détaillés qui pourront aider à identifier les problèmes.

---

### Emplacements des fichiers journaux par plateforme

#### Windows

##### Poste de travail (appareils utilisateur)
- Journal client : `%LocalAppData%\Jimber\client.log`
- Journal du service : `%PROGRAMFILES%\Jimber\service.log`
- Journal du lanceur : `%PROGRAMFILES%\Jimber\launcher.log`
- Fichier déclencheur de débogage : `%PROGRAMFILES%\Jimber\debug.log`

##### Serveur
- Journal serveur : `%PROGRAMFILES%\Jimber\server.log`
- Journal du lanceur : `%PROGRAMFILES%\Jimber\launcher.log`
- Fichier déclencheur de débogage : `%PROGRAMFILES%\Jimber\debug.log`

---

#### Linux

##### Poste de travail (appareils utilisateur)
- Journal client : `~/.local/share/jimber/client.log`
- Journal du service : `/var/log/jimber/service.log`
- Journal du lanceur : `/var/log/jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/jimber/debug.log`

##### Serveur
- Journal serveur : `/var/log/jimber/server.log`
- Journal du lanceur : `/var/log/jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/jimber/debug.log`

---

#### macOS

##### Poste de travail (appareils utilisateur)
- Journal client : `~/Library/Application Support/Jimber/client.log`
- Journal du service : `/var/log/Jimber/service.log`
- Journal du lanceur : `/var/log/Jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/Jimber/debug.log`

---

#### Contrôleur réseau / NIAC / Synology / Raspberry Pi

- Journal serveur : `/var/log/jimber/service.log`
- Journal du lanceur : `/var/log/jimber/launcher.log`
- Fichier déclencheur de débogage : `/var/log/jimber/debug.log`

---

### Remarques et bonnes pratiques

- Il est recommandé de créer le fichier `debug.log` uniquement pour dépanner des problèmes spécifiques, car il augmente le niveau de détail des journaux et peut générer des fichiers journaux volumineux.
- Dans les environnements de production, supervisez et archivez régulièrement les journaux afin d’éviter une utilisation excessive de l’espace disque.
- Lorsque vous signalez des problèmes à l’assistance, incluez les fichiers journaux pertinents (en particulier lorsque la journalisation de débogage est activée) afin d’accélérer le diagnostic.
