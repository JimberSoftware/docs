File: rules/edrconfiguration/edr_configuration_new.md

# ![](../../images/menu/menu_edr.png ':size=50') Configuration EDR

La détection et réponse sur les terminaux (EDR) surveille les terminaux Windows afin de repérer les activités suspectes et peut réagir automatiquement lorsqu’une menace est détectée. Configurez l’EDR par groupe afin que la réponse soit adaptée à la gravité de la détection.

> [!IMPORTANT]
> L’EDR doit être disponible pour votre entreprise et activé pour le groupe sélectionné dans **Sécurité > Configuration de groupe**. Seuls les groupes pour lesquels l’EDR est activé apparaissent sur cette page.

## Configurer l’EDR pour un groupe

1. Accédez à **Sécurité > EDR > Configuration EDR**.
2. Sélectionnez le groupe que vous souhaitez configurer.
3. Utilisez l’interrupteur d’une carte de détection pour activer ou désactiver cette détection.
4. Pour chaque détection activée, choisissez la réponse automatique pour chaque niveau de gravité : **Faible**, **Moyen**, **Élevé** ou **Critique**.
5. Sélectionnez **Soumettre** pour appliquer la configuration.

![Configuration EDR avec les paramètres de détection des fichiers malveillants](./screenshots/edrconfiguration.png ':size=1000')

> [!NOTE]
> L’activation d’une détection sans sélectionner de mesure de réponse enregistre tout de même les détections sur la page de supervision EDR correspondante. Aucune réponse automatique n’est appliquée.

> [!TIP]
> Commencez par la supervision ou par des réponses moins perturbatrices, examinez les détections, puis activez des réponses plus fortes pour les niveaux de gravité élevés. Cela aide à limiter les perturbations dues aux faux positifs.

### Mesures de réponse

| Mesure | Résultat |
|---|---|
| **Quarantaine** | Met en quarantaine le fichier détecté sur le terminal. |
| **Désactiver SASE** | Supprime l’accès SASE de l’appareil concerné. L’intervention d’un administrateur peut être nécessaire avant que l’appareil puisse se reconnecter. |
| **Verrouillage** | Bloque le réseau sur le terminal. Un administrateur doit rétablir la connexion réseau Windows. |

Vous pouvez sélectionner plusieurs mesures de réponse disponibles pour un même niveau de gravité.

> [!WARNING]
> **Désactiver SASE** interrompt l’accès via Jimber SASE, tandis que **Verrouillage** interrompt toutes les connexions réseau sur le terminal. Testez ces réponses avec un groupe limité avant de les activer à grande échelle.

## Types de détection

### Détection des fichiers malveillants

Recherche les contenus malveillants dans les fichiers. Sélectionnez un niveau de sensibilité, puis configurez la réponse pour chaque niveau de gravité.

- **Standard** fournit le niveau de détection de base.
- **Étendu** effectue une détection plus large.
- **Élevé** fournit la détection la plus large et peut générer davantage de faux positifs.

Réponses disponibles : **Quarantaine**, **Désactiver SASE** et **Verrouillage**.

### Détection des anomalies réseau

Détecte les comportements réseau suspects sur le terminal. Configurez **Désactiver SASE** et **Verrouillage** indépendamment pour chaque niveau de gravité.

![Paramètres de détection des anomalies réseau](./screenshots/network-anomaly-detection.png ':size=1000')

### Fichiers binaires non signés

Détecte les fichiers exécutables et les bibliothèques qui ne possèdent pas de signature numérique fiable. Configurez **Quarantaine** indépendamment pour chaque niveau de gravité.

![Paramètres de détection des fichiers binaires non signés et des anomalies de fichiers](./screenshots/unsigned-binaries-file-anomaly.png ':size=1000')

### Détection des anomalies de fichiers

Détecte les activités inhabituelles sur les fichiers et les enregistre pour examen. Cette détection ne comporte aucune mesure de réponse automatique configurable.

### Windows Defender

Surveille les événements pris en charge de Microsoft Defender Antivirus. Configurez **Désactiver SASE** et **Verrouillage** indépendamment pour chaque niveau de gravité.

![Paramètres de Windows Defender](./screenshots/windows-defender.png ':size=1000')

> [!NOTE]
> Si un terminal appartient à plusieurs groupes, sa configuration EDR combine les détections et les mesures de réponse activées dans ces groupes. La détection des fichiers malveillants utilise le niveau de sensibilité configuré le plus élevé.

## Examiner les détections

Ouvrez la page correspondante sous **Supervision > EDR** pour examiner les détections, leur gravité, l’appareil concerné et la mesure appliquée. Consultez la [documentation sur la supervision](/./monitoring/monitoring.md) pour plus d’informations.

## Liste d’autorisation EDR

La liste d’autorisation EDR empêche qu’un fichier fiable déclenche la détection des fichiers malveillants. Une entrée de la liste d’autorisation s’applique au hachage SHA-256 du fichier ; une version modifiée du fichier nécessite donc une nouvelle entrée.

> [!WARNING]
> N’ajoutez à la liste d’autorisation que les fichiers que vous avez vérifiés et auxquels vous faites confiance. Un fichier ajouté à la liste est exclu de la détection des fichiers malveillants.

### Créer une entrée dans la liste d’autorisation

1. Accédez à **Sécurité > EDR > Liste d’autorisation EDR**.
2. Sélectionnez **+ Créer**.
3. Saisissez un nom de fichier reconnaissable.
4. Saisissez le hachage SHA-256 du fichier.
5. Enregistrez l’entrée.

![Créer une entrée dans la liste d’autorisation EDR](./screenshots/create_whitelist.png ':size=500')

Sous Windows, vous pouvez calculer le hachage dans PowerShell :

```powershell
Get-FileHash -Algorithm SHA256 "C:\path\to\file.exe"
