# ![](../../images/menu/menu_edr.png ':size=50') Configuration EDR

La détection et réponse aux incidents sur les appareils (EDR) supervise les appareils Windows à la recherche d’activités suspectes et peut réagir automatiquement lorsqu’une menace est détectée. Configurez l’EDR par groupe afin que la réponse corresponde à la gravité de la détection.

> [!IMPORTANT]
> L’EDR doit être disponible pour votre entreprise et activé pour le groupe sélectionné sous **Sécurité > Configuration de groupe**. Seuls les groupes pour lesquels l’EDR est activé apparaissent sur cette page.

## Configurer l’EDR pour un groupe

1. Accédez à **Sécurité > EDR > Configuration EDR**.
2. Sélectionnez le groupe que vous souhaitez configurer.
3. Utilisez le commutateur d’une carte de détection pour activer ou désactiver cette détection.
4. Pour chaque détection activée, choisissez la réponse automatique pour chaque niveau de gravité : **Faible**, **Moyenne**, **Élevée** ou **Critique**.
5. Sélectionnez **Envoyer** pour appliquer la configuration.

![Configuration EDR avec les paramètres de détection de fichiers malveillants](./screenshots/edrconfiguration.png ':size=1000')

> [!NOTE]
> Si vous activez une détection sans sélectionner d’action de réponse, les détections sont tout de même consignées dans la page de supervision EDR correspondante. Aucune réponse automatique n’est appliquée.

> [!TIP]
> Commencez par la supervision ou par des réponses moins perturbatrices, examinez les détections, puis activez des réponses plus fortes pour les niveaux de gravité élevés. Cela permet de limiter les perturbations dues aux faux positifs.

### Actions de réponse

| Action                  | Résultat                                                                                                                                                                  |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Quarantaine**         | Met en quarantaine le fichier détecté sur l’appareil.                                                                                                                     |
| **Désactiver SASE**     | Supprime l’accès SASE de l’appareil concerné. Une intervention de l’administrateur peut être nécessaire avant que l’appareil puisse se reconnecter.                       |
| **Verrouillage**        | Verrouille le réseau sur l’appareil. Un administrateur doit rétablir la connexion réseau Windows, par exemple en réactivant l’adaptateur réseau dans le Gestionnaire de périphériques. |

Vous pouvez sélectionner plusieurs actions de réponse disponibles pour un même niveau de gravité.

> [!WARNING]
> **Désactiver SASE** interrompt l’accès via Jimber SASE, tandis que **Verrouillage** interrompt toutes les connexions réseau sur l’appareil. Testez ces réponses sur un groupe limité avant de les activer à grande échelle.

## Types de détection

### Détection de fichiers malveillants

Analyse les fichiers à la recherche de contenu malveillant. Sélectionnez un niveau de sensibilité, puis configurez la réponse pour chaque niveau de gravité.

- **Standard** fournit le niveau de détection de base.
- **Étendue** effectue une détection plus large.
- **Élevée** fournit la détection la plus large et peut entraîner davantage de faux positifs.

Réponses disponibles : **Quarantaine**, **Désactiver SASE** et **Verrouillage**.

### Détection des anomalies réseau

Détecte les comportements réseau suspects sur l’appareil. Configurez **Désactiver SASE** et **Verrouillage** indépendamment pour chaque niveau de gravité.

![Paramètres de détection des anomalies réseau](./screenshots/network-anomaly-detection.png ':size=1000')

### Fichiers binaires non signés

Détecte les fichiers exécutables et les bibliothèques qui ne disposent pas d’une signature numérique approuvée. Configurez **Quarantaine** indépendamment pour chaque niveau de gravité.

![Paramètres de détection des fichiers binaires non signés et des anomalies de fichiers](./screenshots/unsigned-binaries-file-anomaly.png ':size=1000')

### Détection des anomalies de fichiers

Détecte les activités inhabituelles sur les fichiers et les consigne pour examen. Cette détection ne comporte aucune action de réponse automatique configurable.

### Windows Defender

Supervise les événements pris en charge de Microsoft Defender Antivirus. Configurez **Désactiver SASE** et **Verrouillage** indépendamment pour chaque niveau de gravité.

![Paramètres de Windows Defender](./screenshots/windows-defender.png ':size=1000')

> [!NOTE]
> Si un appareil appartient à plusieurs groupes, sa configuration EDR combine les détections et les actions de réponse activées dans ces groupes. La détection de fichiers malveillants utilise le niveau de sensibilité configuré le plus élevé.

## Examiner les détections

Ouvrez la page correspondante sous **Supervision > EDR** pour examiner les détections, leur gravité, l’appareil concerné et l’action effectuée. Consultez la [documentation sur la supervision](/./monitoring/monitoring.md) pour en savoir plus.

## Liste blanche EDR

La liste blanche EDR empêche qu’un fichier approuvé déclenche la détection de fichiers malveillants. Une entrée de liste blanche s’applique au hachage SHA-256 du fichier ; toute version modifiée du fichier nécessite donc une nouvelle entrée.

> [!WARNING]
> N’ajoutez à la liste blanche que les fichiers que vous avez vérifiés et auxquels vous faites confiance. Un fichier inscrit sur la liste blanche est exclu de la détection de fichiers malveillants.

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
