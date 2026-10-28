# Haute disponibilité des contrôleurs réseau

La haute disponibilité (HA) permet d’exécuter deux contrôleurs réseau en paire actif/veille.
Le contrôleur réseau principal gère le trafic en fonctionnement normal. Le
contrôleur réseau secondaire reste en veille et prend le relais lorsqu’il ne
parvient plus à joindre le contrôleur principal.

Les deux contrôleurs réseau utilisent le même jeton de contrôleur réseau et communiquent
via une liaison physique HA dédiée. Les battements de cœur transmis via cette liaison
sont authentifiés à l’aide du jeton partagé.

## Fonctionnement du basculement

- Le contrôleur principal fonctionne normalement et envoie un battement de cœur authentifié toutes les secondes.
- Le contrôleur secondaire maintient toutes ses interfaces, à l’exception de ses interfaces de bouclage et HA, désactivées
  tant que le contrôleur principal est disponible.
- Après trois sessions de battement de cœur consécutives ayant échoué, le contrôleur secondaire réactive ses
  interfaces réseau et devient actif.
- Lorsque le contrôleur principal revient et envoie trois battements de cœur consécutifs indiquant qu’il est prêt, le contrôleur secondaire arrête ses services actifs, effectue le nettoyage et repasse en veille.

La liaison HA utilise `198.51.100.1/30` sur le contrôleur principal, `198.51.100.2/30` sur le
contrôleur secondaire et le port TCP `49152`. Ces paramètres sont appliqués automatiquement. Ne
configurez pas manuellement d’adresses IP sur les interfaces HA.

> [!WARNING]
> Le contrôleur secondaire considère toute perte de la connexion HA comme une défaillance du contrôleur principal. Utilisez une liaison
> physique dédiée et fiable afin d’éviter que les deux contrôleurs réseau ne deviennent
> actifs en même temps.

## Prérequis

Avant de commencer, vérifiez que :

- Deux contrôleurs réseau sont installés et disposent d’une connectivité WAN et LAN
  équivalente.
- Les deux contrôleurs réseau utilisent le même jeton de contrôleur réseau.
- Une interface réseau physique dédiée est disponible sur chaque contrôleur
  réseau.
- Les interfaces dédiées sont reliées directement l’une à l’autre.
- Le contrôleur réseau principal est configuré et prêt avant la configuration du
  contrôleur secondaire.

> [!TIP]
> Il est recommandé d’utiliser la dernière interface réseau disponible sur chaque contrôleur
> réseau pour la HA. Par exemple, si `ens18` et `ens19` sont disponibles et que
> `ens18` est utilisée pour le trafic normal, utilisez `ens19` pour la liaison HA. N’utilisez jamais l’interface
> WAN pour la HA.

## Configurer le contrôleur réseau principal

1. Effectuez les étapes d’installation et de configuration réseau décrites dans
   [Installation d’un contrôleur réseau](/./advanced/networkcontrollerssetup/SettingUpServer.md).
2. Sur la page **Configurer le jeton (3/4)**, saisissez le jeton du contrôleur réseau.
3. Sélectionnez **Haute disponibilité**.
4. Définissez **Rôle** sur **Principal**.
5. Sous **Interface de haute disponibilité**, sélectionnez l’interface dédiée. Utilisez
   si possible la dernière interface réseau disponible.
6. Sélectionnez **Suivant** et attendez la fin de la vérification de la connexion.

![Configuration HA du contrôleur réseau principal](./screenshots/high-availability-primary.png ':size=700')

Laissez le contrôleur réseau principal en cours d’exécution avant de poursuivre avec le
contrôleur secondaire.

## Configurer le contrôleur réseau secondaire

1. Effectuez les étapes d’installation et de configuration réseau sur le deuxième
   contrôleur réseau.
2. Reliez son interface HA dédiée directement à l’interface HA dédiée du contrôleur principal.
3. Sur la page **Configurer le jeton (3/4)**, saisissez le même jeton de contrôleur réseau
   que celui utilisé par le contrôleur principal.
4. Sélectionnez **Haute disponibilité**.
5. Définissez **Rôle** sur **Secondaire**.
6. Sous **Interface de haute disponibilité**, sélectionnez l’interface reliée au
   contrôleur principal. Utilisez si possible la dernière interface réseau disponible.
7. Sélectionnez **Suivant**.

![Configuration HA du contrôleur réseau secondaire](./screenshots/high-availability-secondary.png ':size=700')

Pendant la configuration, le contrôleur secondaire configure temporairement son interface HA et
s’authentifie auprès du contrôleur principal. Lorsque le contrôleur principal est joignable et prêt, le
contrôleur secondaire confirme la connexion et passe en veille.

![Contrôleur réseau secondaire connecté au contrôleur principal](./screenshots/high-availability-secondary-ready.png ':size=700')

## Tester le basculement et le retour au rôle principal

Effectuez un test contrôlé une fois les deux contrôleurs réseau configurés :

1. Arrêtez le contrôleur réseau principal en laissant le câble HA
   connecté.
2. Vérifiez que le contrôleur secondaire réactive ses interfaces réseau habituelles et prend
   en charge le trafic.
3. Redémarrez le contrôleur réseau principal.
4. Vérifiez que le contrôleur principal est prêt et que le contrôleur secondaire repasse en veille.

Ne testez pas le basculement en débranchant uniquement le câble HA. Une liaison HA
défaillante peut entraîner l’activation du contrôleur secondaire alors que le contrôleur principal continue à gérer le trafic.

## Dépannage

Si le contrôleur secondaire ne parvient pas à se connecter au contrôleur principal pendant la configuration, vérifiez que :

- Les deux contrôleurs réseau utilisent le même jeton.
- Le contrôleur principal est configuré avec le rôle **Principal** et est en cours d’exécution.
- Les interfaces HA sélectionnées sont reliées directement l’une à l’autre.
- L’interface HA sélectionnée n’est pas l’interface WAN.
- Les interfaces sélectionnées sont connectées et disponibles pour le système d’exploitation.
