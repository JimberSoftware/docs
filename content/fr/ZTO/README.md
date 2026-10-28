File: ZTO/README.md

# ![](../images/menu/menu_security.png ':size=28') Accès sortant Zero Trust

L’accès sortant Zero Trust (ZTO) contrôle l’accès à Internet des appareils utilisateurs, des serveurs et des NIAC. Lorsque ZTO est activé, le trafic Internet sortant de ces terminaux est bloqué, sauf si une politique sortante activée l’autorise.

Pour faciliter la configuration initiale, la plateforme peut créer automatiquement un service **Standard Internet** et trois politiques sortantes. Vous pouvez activer ZTO et créer ces paramètres par défaut lors de la création d’un client, ou l’activer ultérieurement depuis la configuration du client.

> [!IMPORTANT]
> L’activation de ZTO fait passer l’entreprise d’un accès Internet non restreint pour les terminaux à un accès contrôlé par des politiques. Assurez-vous que les politiques sortantes requises sont activées avant que les utilisateurs et les appareils aient besoin d’accéder à Internet.

> [!NOTE]
> L’accès Internet du réseau natif est contrôlé par ses propres politiques sortantes, indépendamment du paramètre ZTO. Les politiques automatiques décrites sur cette page couvrent les utilisateurs, les serveurs et les NIAC.

## Que crée la plateforme automatiquement ?

Lors de la première activation de ZTO, la plateforme crée :

- Un service **Standard Internet** contenant des règles pour le trafic Internet courant, notamment HTTP, HTTPS, DNS, NTP, la messagerie électronique et ICMP.
- **Standard Internet - Users**, avec `All Users` comme source.
- **Standard Internet - Servers**, avec `All Servers` comme source.
- **Standard Internet - NIACs**, avec `All NIACs` comme source.

Ces trois politiques sont des politiques sortantes. Elles utilisent le service **Standard Internet** et ont `Internet` pour destination.

![Politiques Standard Internet](./screenshots/standard-internet-policies.png ':size=1000')

## Activer ZTO lors de la création d’un client

Utilisez cette option lorsque ZTO doit être actif dès la création d’un nouveau client.

1. Ouvrez **Clients** et cliquez sur **+ Créer**.
2. Saisissez les informations du client.
3. Sélectionnez un forfait comprenant le module **Zero Trust Outbound**.
4. Activez **Activer ZTO**.
5. Cliquez sur **Créer**.

![Activer ZTO lors de la création d’un client](./screenshots/enable-zto-during-customer-creation.png ':size=420')

La plateforme active ZTO et crée le service Standard Internet ainsi que les trois politiques par défaut. Les politiques sont activées afin que les utilisateurs, les serveurs et les NIAC conservent dès le départ l’accès aux services Internet standard.

> [!INFO]
> L’option **Activer ZTO** s’affiche uniquement si le forfait sélectionné comprend le module Zero Trust Outbound. Si vous sélectionnez un forfait sans ce module, l’option est masquée et ZTO reste désactivé.

## Activer ZTO pour un client existant

Utilisez la configuration de l’entreprise lorsque le client existe déjà ou lorsque ZTO n’a pas été activé lors de sa création.

1. Ouvrez le client.
2. Accédez à **Entreprise** > **Configuration**.
3. Dans la section **Divers**, activez **Zero Trust Outbound**.
4. Confirmez l’avertissement Zero Trust Outbound.
5. Choisissez si vous souhaitez laisser **Autoriser Internet** activé :
    - **Activé** : les trois politiques automatiques sont créées et activées.
    - **Désactivé** : les politiques sont créées, mais restent désactivées. L’accès à Internet est bloqué jusqu’à ce qu’une politique sortante appropriée soit activée.
6. Cliquez sur **Appliquer**.

![Activer ZTO dans la configuration de l’entreprise](./screenshots/enable-zto-in-company-configuration.png ':size=1000')

Le service et les politiques Standard Internet ne sont créés que lors de la première activation de ZTO. Désactiver puis réactiver ZTO ne crée pas de doublons et ne réinitialise pas les politiques existantes.

> [!TIP]
> Si ZTO est activé sans **Autoriser Internet**, vérifiez immédiatement les politiques et n’activez que les accès requis par le client.

## Vérifier et ajuster l’accès à Internet

Après avoir activé ZTO, ouvrez **Sécurité** > **Politiques**. Vous pouvez alors :

- Activer ou désactiver chaque politique Standard Internet.
- Modifier une politique pour restreindre ses sources.
- Modifier le service Standard Internet pour changer les ports et les protocoles autorisés.
- Créer des services et des politiques sortants supplémentaires pour un accès plus ciblé.

Consultez [Politiques](/./rules/firewall-policies/firewall-policies.md) pour savoir comment créer et gérer des politiques.

## Accès attendu

| Paramètre ZTO | Politique sortante correspondante activée | Résultat                                                |
| ------------- | ----------------------------------------- | ------------------------------------------------------- |
| Désactivé     | Non requise pour ZTO des terminaux        | ZTO ne restreint pas l’accès Internet des terminaux.    |
| Activé        | Oui                                       | Le trafic couvert par la politique et le service est autorisé. |
| Activé        | Non                                       | Le trafic Internet sortant est bloqué.                  |

Si un utilisateur, un serveur ou un NIAC perd l’accès à Internet après l’activation de ZTO, vérifiez que :

- La politique sortante concernée est activée.
- La source de la politique inclut l’entité concernée.
- La politique utilise un service contenant le protocole et le port requis.
- La destination de la politique est `Internet`.
