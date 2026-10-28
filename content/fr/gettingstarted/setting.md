# Paramètres importants

## Paramètres du pare-feu

Pour pouvoir utiliser notre plateforme SASE, les ports sortants suivants doivent être autorisés sur votre ou vos pare-feu :

- 51820 UDP 
- 51820 TCP
- 443 TCP

## Spécifications minimales pour un contrôleur réseau sur site
 
 - **Général** :
    - Disque dur de 25 Go

 - **Pour 50 utilisateurs :**
    - 2 CPU
    - 4 Go de RAM


## Variables d’environnement

Le comportement de notre logiciel peut être adapté à l’aide de variables d’environnement spécifiques :

```
JIMBER_PORT=13138
```

Cette variable modifie les ports d’écoute actifs de **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_**. En la définissant, vous activez le port spécifié et les trois ports séquentiels suivants (8000, 8001, 8002, 8003), afin d’optimiser la gestion des ports en fonction de la configuration de votre réseau.

Pour plus d’informations, cliquez [ici](/./advanced/customconfiguration/customconfiguration).
