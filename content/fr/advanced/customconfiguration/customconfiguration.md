# Configuration personnalisée

Pour répondre à des exigences spécifiques ou résoudre des problèmes de compatibilité avec d’autres logiciels de votre système, une configuration personnalisée de la **_Plateforme Jimber SASE_** peut être nécessaire. Cette flexibilité est particulièrement utile lors des phases de test ou lorsque vous adaptez le logiciel à des environnements opérationnels spécifiques.

## Variables d’environnement

Le comportement de notre logiciel peut être personnalisé au moyen de variables d’environnement spécifiques :

```
JIMBER_PORT=13138
```

Cette variable modifie les ports d’écoute actifs de la **_Plateforme Jimber SASE_**. En la définissant, vous activez le port spécifié ainsi que les trois ports suivants dans l’ordre (8000, 8001, 8002, 8003), afin d’optimiser la gestion des ports en fonction de la configuration de votre réseau.

Les variables d’environnement se trouvent sous Panneau de configuration, Système. Faites défiler le volet de droite vers le bas, puis cliquez sur Paramètres système avancés.

![settings.png](/screenshots/settings.png ':size=500')

Dans la fenêtre suivante, sélectionnez Paramètres système avancés

![system_properties.png](/screenshots/system_properties.png ':size=300')

Vous pouvez ensuite modifier les variables.

![environment_variables.png](/screenshots/environment_variables.png ':size=500')


> [!WARNING]
> **Attention** ! Veillez à consulter Jimber avant d’utiliser les variables d’environnement suivantes. Elles peuvent perturber votre environnement si elles ne sont pas utilisées correctement.

```
JIMBER_NOUPDATES=true
```

L’activation de cette variable désactive les mises à jour automatiques du logiciel.

```
JIMBER_NOLAUNCHER=true
```

Cette variable permet de démarrer le logiciel sans l’exécutable du lanceur, une approche simplifiée particulièrement utile dans les scénarios de test.
