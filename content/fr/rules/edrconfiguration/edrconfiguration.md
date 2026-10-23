File: rules/edrconfiguration/edrconfiguration.md

# ![](../../images/menu/menu_edr.png ':size=50') Configuration EDR

La détection et réponse aux incidents sur les terminaux (EDR) supervise les terminaux Windows à la recherche d’activités suspectes et peut réagir automatiquement lorsqu’une menace est détectée. Configurez l’EDR par groupe afin que la réponse corresponde à la gravité de la détection.

> [!IMPORTANT]
> L’EDR doit être disponible pour votre entreprise et activé pour le groupe sélectionné sous **Sécurité > Configuration de groupe**. Seuls les groupes pour lesquels l’EDR est activé apparaissent sur cette page.

## Configurer l’EDR pour un groupe

1. Accédez à **Sécurité > EDR > Configuration EDR**.

![Configuration EDR](./screenshots/edr_configuration.png ':size=700')

2. Sélectionnez le groupe que vous souhaitez configurer.
3. Utilisez le bouton bascule d’une carte de détection pour activer ou désactiver cette détection.
4. Pour chaque détection activée, choisissez la réponse automatique pour chaque niveau de gravité : **Faible**, **Moyen**, **Élevé** ou **Critique**.
5. Cochez **Notification par e-mail** pour chaque niveau de gravité pour lequel une alerte doit être envoyée.
6. Sélectionnez **Soumettre** pour appliquer la configuration.

![Configuration EDR avec les paramètres de détection des fichiers malveillants](./screenshots/edrconfiguration.png ':size=700')

> [!NOTE]
> L’activation d’une détection sans sélection d’action de réponse enregistre tout de même les détections dans la page de supervision EDR correspondante. Aucune action de réponse automatique n’est appliquée.

> [!TIP]
> Commencez par la supervision ou par des réponses moins perturbatrices, examinez les détections, puis activez des réponses plus fortes pour les niveaux de gravité supérieurs. Cela permet de réduire les perturbations dues aux faux positifs.

### Notifications par e-mail

Chaque catégorie de détection comporte un bouton bascule **Notification par e-mail** pour les niveaux de gravité **Faible**, **Moyen**, **Élevé** et **Critique**. Cela inclut la détection des anomalies de fichiers et Windows Defender.

Les e-mails sont envoyés aux contacts de notification EDR configurés pour l’entreprise. Une détection correspondante peut envoyer un e-mail même si aucune action de réponse automatique n’est sélectionnée. La désactivation d’une option de notification par e-mail ne désactive ni la supervision ni les actions de réponse. Les options de notification par e-mail sont également disponibles sans accès SASE.

Lorsqu’un appareil appartient à plusieurs groupes, les notifications par e-mail sont activées si un groupe applicable les active pour cette catégorie et ce niveau de gravité. La catégorie de détection doit être activée dans la configuration effective. Un événement envoie un e-mail par contact, même si plusieurs groupes correspondent. Ces paramètres s’appliquent aux appareils utilisateurs et aux serveurs.

Les combinaisons de catégories et de niveaux de gravité existantes configurées pour désactiver l’accès SASE sont activées par défaut pour les notifications par e-mail après la mise à niveau. Les autres combinaisons sont désactivées par défaut. Vérifiez ces paramètres après la mise à niveau.

### Actions de réponse

| Action                     | Résultat                                                                                                                                                                     |
| -------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Mise en quarantaine**    | Met le fichier détecté en quarantaine sur le terminal.                                                                                                                       |
| **Désactiver SASE**        | Supprime l’accès SASE de l’appareil concerné. L’intervention d’un administrateur peut être nécessaire avant que l’appareil puisse se reconnecter.                              |
| **Verrouillage**           | Verrouille le réseau sur le terminal. Un administrateur doit rétablir la connexion réseau Windows, par exemple en réactivant la carte réseau dans le Gestionnaire de périphériques. |

Vous pouvez sélectionner plusieurs actions de réponse disponibles pour un même niveau de gravité.

> [!WARNING]
> **Désactiver SASE** interrompt l’accès via Jimber SASE, tandis que **Verrouillage** interrompt toute activité réseau sur le terminal. Testez ces réponses avec un groupe restreint avant de les activer à grande échelle.

## Types de détection

### Détection des fichiers malveillants

Analyse les fichiers à la recherche de contenu malveillant. Sélectionnez un niveau de sensibilité, puis configurez la réponse pour chaque niveau de gravité.

- **Standard** fournit le niveau de détection de base.
- **Étendue** effectue une détection plus large.
- **Élevée** fournit la détection la plus large et peut générer davantage de faux positifs.

Réponses disponibles : **Mise en quarantaine**, **Désactiver SASE** et **Verrouillage**.

![Paramètres de détection des fichiers malveillants](./screenshots/malicious_file.png ':size=700')

### Détection des anomalies réseau

Détecte les comportements réseau suspects sur le terminal. Configurez **Désactiver SASE** et **Verrouillage** indépendamment pour chaque niveau de gravité.

![Paramètres de détection des anomalies réseau](./screenshots/anomaly_detection.png ':size=700')

### Fichiers binaires non signés

Détecte les fichiers exécutables et les bibliothèques qui ne disposent pas d’une signature numérique fiable. Configurez **Mise en quarantaine** indépendamment pour chaque niveau de gravité.

![Paramètres de détection des fichiers binaires non signés et des anomalies de fichiers](./screenshots/unsigned_binaries.png ':size=700')

### Détection des anomalies de fichiers

Détecte les activités inhabituelles sur les fichiers et les enregistre pour examen. Cette détection ne comporte aucune action de réponse automatique configurable. Les notifications par e-mail peuvent être activées pour chaque niveau de gravité.

![Paramètres de détection des anomalies de fichiers](./screenshots/file_anomaly_detection.png ':size=700')

### Windows Defender

Supervise les événements pris en charge par Microsoft Defender Antivirus. Configurez **Désactiver SASE** et **Verrouillage** indépendamment pour chaque niveau de gravité.

![Paramètres de Windows Defender](./screenshots/windows_defender.png ':size=700')

> [!NOTE]
> Si un terminal appartient à plusieurs groupes, sa configuration EDR combine les détections activées et les actions de réponse de ces groupes. La détection des fichiers malveillants utilise le niveau de sensibilité configuré le plus élevé.

## Examiner les détections

Ouvrez la page correspondante sous **Supervision > EDR** pour examiner les détections, leur gravité, l’appareil concerné et l’action effectuée. Consultez la [documentation sur la supervision](/./monitoring/monitoring.md) pour en savoir plus.

## Liste blanche EDR

La liste blanche EDR empêche qu’un fichier de confiance déclenche la détection des fichiers malveillants. Une entrée de liste blanche s’applique au hachage SHA-256 du fichier ; toute version modifiée du fichier nécessite donc une nouvelle entrée.

> [!WARNING]
> N’ajoutez à la liste blanche que les fichiers que vous avez vérifiés et auxquels vous faites confiance. Un fichier ajouté à la liste blanche est exclu de la détection des fichiers malveillants.

### Créer une entrée de liste blanche

1. Accédez à **Sécurité > EDR > Liste blanche EDR**.
2. Sélectionnez **+ Créer**.
3. Saisissez un nom de fichier reconnaissable.
4. Saisissez le hachage SHA-256 du fichier.
5. Enregistrez l’entrée.

![Créer une entrée de liste blanche EDR](./screenshots/create_whitelist.png ':size=500')

Sous Windows, vous pouvez calculer le hachage dans PowerShell :

```powershell
Get-FileHash -Algorithm SHA256 "C:\path\to\file.exe"
```

### Modifier une entrée de liste blanche

Sélectionnez l’icône de modification dans la ligne de l’entrée pour changer son nom de fichier. Le hachage SHA-256 ne peut pas être modifié. Pour utiliser un autre hachage, créez une nouvelle entrée de liste blanche.

![Modifier une entrée de liste blanche EDR](./screenshots/edit_whitelist.png ':size=500')
