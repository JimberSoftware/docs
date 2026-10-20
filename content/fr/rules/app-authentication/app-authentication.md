File: rules/app-authentication/app-authentication.md

# Authentification des applications (SAML et OIDC)

L’authentification des applications permet à la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** d’agir en tant que fournisseur d’identité pour les applications internes et tierces. Les utilisateurs se connectent avec leur identité Jimber, tandis que les propriétaires des applications continuent d’utiliser l’intégration standard SAML 2.0 ou OpenID Connect (OIDC) proposée par leur application.

## Pourquoi utiliser l’authentification des applications ?

- **Une seule identité pour davantage d’applications :** les utilisateurs n’ont pas besoin d’un autre mot de passe propre à chaque application.
- **Contrôle d’accès centralisé :** accordez l’accès aux utilisateurs ou aux groupes et révoquez-le au même endroit lorsque les responsabilités changent.
- **Protection tenant compte des appareils :** exigez éventuellement un appareil approuvé exécutant l’agent Jimber avant d’autoriser l’authentification.
- **Intégration fondée sur des normes :** connectez des fournisseurs de services SAML et des parties utilisatrices OIDC sans protocole d’authentification propriétaire.
- **Exposition réduite des données :** ne transmettez que les attributs, les portées et les revendications nécessaires à une application.
- **Accès auditable :** consultez les connexions des utilisateurs et les événements de protocole depuis l’interface de supervision SASE.

> [!NOTE]
> L’authentification des applications contrôle les personnes autorisées à s’authentifier auprès d’une application. Si l’application est hébergée sur un réseau privé, configurez séparément le service requis et la politique de pare-feu.

## Avant de commencer

Rassemblez les valeurs d’intégration fournies par l’application :

- Pour SAML : l’ID d’entité du fournisseur de services, l’URL ACS (Assertion Consumer Service), l’URL de déconnexion unique facultative, le format NameID attendu et les attributs requis.
- Pour OIDC : l’URI de redirection, le type d’application, la méthode d’authentification au point de terminaison de jeton prise en charge, les portées demandées et l’URI de redirection après déconnexion facultative.

Assurez-vous que les utilisateurs qui vont se connecter disposent des données de profil requises, telles qu’une adresse e-mail, un prénom, un nom et un nom d’affichage.

Dans la plateforme SASE, accédez à **Sécurité > Authentification des applications**. Sélectionnez **Afficher les détails du fournisseur d’identité** pour obtenir les métadonnées SAML et l’URL de découverte OIDC. Privilégiez les métadonnées ou la découverte plutôt que la copie individuelle des points de terminaison, afin que les applications puissent découvrir les bons points de terminaison et les bonnes clés de signature.

## Créer une application

![create_authentication](./screenshots/create_authentication.png ":size=600")

1. Accédez à **Sécurité > Authentification des applications**.
2. Sélectionnez **Créer**.

    ![create_authentication](./screenshots/create_authentication2.png ":size=600")

3. Choisissez **SAML 2.0** ou **OpenID Connect (OIDC)**. Le protocole ne peut pas être modifié après la création de l’application.
4. Saisissez un nom de service reconnaissable (obligatoire), une brève description et l’URL de l’application.
5. Configurez les paramètres propres au protocole décrits ci-dessous.
6. Ajoutez au moins une attribution.
7. Sélectionnez **Enregistrer les modifications**.

>[!ATTENTION]
>L’URL de l’application est la destination ouverte depuis le panneau de sécurité. Elle n’est pas utilisée comme URL ACS SAML ni comme URI de redirection OIDC, sauf si la documentation de l’application précise explicitement qu’il s’agit de la même URL.

## Configurer une application SAML

#### Paramètres de base

Saisissez les valeurs fournies par le fournisseur de services :

- **ID d’entité SP :** identifiant unique du fournisseur de services (obligatoire).
- **URL ACS principale :** point de terminaison exact qui reçoit la réponse SAML (obligatoire).
- **URL de déconnexion unique SP :** point de terminaison facultatif pour les réponses de déconnexion initiées par le SP.
- **Source et format NameID :** valeur utilisateur et format d’identifiant attendus par le fournisseur de services. Un identifiant persistant constitue l’option la plus respectueuse de la vie privée lorsque l’application le prend en charge.

#### Accès à l’application

Ici, vous pouvez choisir d’afficher une vignette de lancement dans votre panneau de sécurité et de refuser les connexions sans appareil inscrit et approuvé.

#### Sécurité SAML

Les assertions SAML sont signées avec RSA-SHA256. Laissez l’option **Signer l’assertion** activée, sauf si le fournisseur de services exige explicitement que la réponse complète soit signée à la place. Activez la signature des demandes d’authentification ou le chiffrement des assertions uniquement si le fournisseur de services les prend en charge, et fournissez le certificat correspondant du fournisseur de services.

#### Points de terminaison ACS supplémentaires

Utilisez **Points de terminaison ACS supplémentaires** uniquement pour des points de terminaison de basculement, régionaux ou de connectivité privée documentés. SASE n’accepte que les points de terminaison enregistrés.

#### Attributs

Dans l’onglet **Attributs**, associez chaque attribut requis par le fournisseur de services au champ utilisateur Jimber approprié. Évitez d’envoyer des attributs dont l’application n’a pas besoin.

 ![attributes](./screenshots/attributes.png ":size=600")

> [!TIP]
> Lorsque cela est possible, importez les métadonnées SAML SASE dans le fournisseur de services. Les métadonnées contiennent l’ID d’entité, le point de terminaison de connexion, le point de terminaison de déconnexion et le certificat de signature.

## Configurer une application OIDC

#### Options

Choisissez les paramètres client correspondant à l’application :

- **Client public :** navigateur, application mobile, application de bureau ou autre logiciel incapable de conserver un secret en toute sécurité. L’authentification au point de terminaison de jeton est **Aucune — PKCE uniquement**.
- **Client confidentiel :** logiciel côté serveur capable de protéger un secret client. Sélectionnez la méthode d’authentification au point de terminaison de jeton documentée par l’application.
- **Type d’application :** sélectionnez web ou native selon l’environnement d’exécution du client.
- **Identifiant de sujet :** utilisez le sujet par paire recommandé, sauf si l’application a un besoin documenté d’un autre identifiant.
- **URI de redirection :** enregistrez chaque rappel à l’identique. Les caractères génériques ne sont pas acceptés.
- **URI de redirection après déconnexion :** destinations exactes facultatives pouvant être utilisées après la déconnexion.
- **Durée de vie des jetons et jetons d’actualisation :** choisissez une courte durée de vie pour les jetons d’accès et n’activez les jetons d’actualisation que si l’application a besoin d’un accès prolongé.

![Paramètres d’application OIDC dans Jimber SASE](./screenshots/oidc-settings.png ':size=800')

Après l’enregistrement, copiez l’ID client généré dans l’application. Le secret d’un client confidentiel n’est affiché qu’au moment de sa création ou de sa régénération. **Copiez-le immédiatement** et stockez-le dans le gestionnaire de secrets de l’application.

> [!IMPORTANT]
> Les clients publics doivent utiliser le flux Authorization Code avec PKCE. Utilisez la méthode de défi de code `S256` et ne placez jamais de secret client dans le code d’une application de navigateur ou installée.

#### Sélectionner les portées et les revendications

La portée _**openid**_ est toujours activée. N’activez que les données supplémentaires nécessaires à l’application :

- _**profile**_ fournit _*name*_, _*given_name*_, _*family_name*_ et _*preferred_username*_.
- _**email**_ fournit _email_ et *email_verified*.
- _**groups**_ fournit les *appartenances aux groupes de l’annuaire*.
- <b>offline_access</b> est activé lorsque les jetons d’actualisation sont autorisés.

Vérifiez la source de chaque revendication. L’ID utilisateur immuable est toujours utilisé pour `sub`. Les autres revendications peuvent être associées aux valeurs correspondantes du profil utilisateur.

![Portées OIDC et associations de revendications dans Jimber SASE](./screenshots/scopes-and-claims.png ':size=800')

## Attribuer les accès et appliquer la protection des appareils

Ouvrez **Attributions**, sélectionnez **Ajouter des attributions**, puis choisissez les utilisateurs ou les groupes autorisés à se connecter. Un utilisateur doit être couvert par une attribution pour que SASE autorise l’accès à l’application.

![Utilisateur attribué dans Jimber SASE](./screenshots/assignments.png ':size=800')

Les options de l’application proposent également deux contrôles d’accès :

- **Afficher dans le panneau de sécurité :** affiche une vignette de lancement aux utilisateurs auxquels l’application est attribuée.
- **Exiger l’agent Jimber :** refuse la connexion si l’utilisateur n’utilise pas un appareil inscrit et approuvé. Utilisez cette option lorsque l’accès à l’application doit dépendre de la confiance accordée à l’appareil.

## Tester la connexion

Après avoir enregistré l’application, sélectionnez **Démarrer le test de connexion**. Terminez le flux d’authentification de l’application et vérifiez les points suivants :

- Les réponses SAML arrivent au point de terminaison ACS enregistré, ou l’autorisation OIDC revient à l’URI de redirection exacte.
- L’application reconnaît l’identifiant utilisateur attendu.
- Les attributs ou revendications requis contiennent les valeurs de profil attendues.
- Les clients OIDC publics échangent le code d’autorisation avec le vérificateur PKCE d’origine et sans secret client.

>[!NOTE]
>Le test confirme le bon fonctionnement de l’échange d’identité. L’application reste responsable de la création de sa session locale et de l’application de ses propres règles d’autorisation.

## Superviser les connexions

Sélectionnez **Afficher l’activité de connexion** depuis une application, ou accédez à **Supervision > Authentification des applications**.

- **Activité de connexion** affiche les tentatives de connexion des utilisateurs par heure, application, protocole et utilisateur.

![Activité de connexion OIDC dans Jimber SASE](./screenshots/sign-in-activity.png ':size=800')


- **Événements d’authentification** affiche les événements de protocole SAML ou OIDC individuels et les échecs qui permettent de diagnostiquer une tentative.

![Événements d’authentification OIDC dans Jimber SASE](./screenshots/authentication.png ':size=800')

- **Détails**

Cliquer sur la bande correspondante d’une ligne ouvre une vue détaillée contenant des informations supplémentaires :


![Détails](./screenshots/details.png ':size=600')


## Dépannage

| Symptôme                                           | Éléments à vérifier                                                                                                           |
| -------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| L’utilisateur ne dispose d’aucune attribution     | Attribuez l’utilisateur directement ou par l’intermédiaire d’un groupe dans le même contexte d’entreprise.                    |
| L’application signale une incompatibilité de redirection ou d’ACS | Copiez l’URL enregistrée à l’identique, y compris le schéma, l’hôte, le chemin, le port et la barre oblique finale.           |
| Un rappel OIDC ne contient pas de code d’autorisation | Vérifiez l’échec d’autorisation sous **Événements d’authentification**, l’attribution du client, l’URI de redirection et les paramètres PKCE. |
| Un client OIDC public demande un secret client     | Configurez-le en tant que client public et utilisez Authorization Code avec PKCE au lieu d’un secret.                        |
| Une revendication ou un attribut SAML est vide     | Activez la portée ou l’association d’attributs requise et vérifiez que la source sélectionnée existe dans le profil de l’utilisateur. |
| La connexion est refusée car un agent est requis   | Utilisez un appareil inscrit et approuvé exécutant l’agent Jimber, ou désactivez cette exigence si la confiance de l’appareil n’est pas nécessaire. |

## Recommandations de sécurité

- Utilisez des URL HTTPS pour les rappels, les points de terminaison ACS et de déconnexion, ainsi que les URL des applications en production.
- Privilégiez les métadonnées SAML et la découverte OIDC afin que les points de terminaison et les clés de signature restent à jour.
- Utilisez des sujets OIDC par paire et des identifiants SAML persistants lorsque ces options sont prises en charge.
- Utilisez PKCE avec `S256`, en particulier pour les clients publics.
- Stockez les secrets des clients confidentiels dans un gestionnaire de secrets côté serveur et renouvelez-les s’ils sont exposés.
- Accordez l’accès au moyen de l’attribution à l’utilisateur ou au groupe la plus restreinte possible.
- Ne transmettez que les attributs, les portées et les revendications nécessaires à l’application.
- Consultez les **Événements d’authentification** après des modifications de configuration et lors de l’analyse des échecs de connexion.
