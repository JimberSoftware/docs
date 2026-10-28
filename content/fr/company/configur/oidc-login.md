# Connexion OIDC

OpenID Connect (OIDC) permet aux utilisateurs de se connecter à la Plateforme Jimber SASE par l'intermédiaire d'un fournisseur d'identité externe, tel qu'Okta, Keycloak, Auth0 ou ZITADEL.

OIDC est une couche d'identité fondée sur OAuth 2.0. Dans cette intégration :

- La Plateforme Jimber SASE est la partie de confiance, parfois appelée fournisseur de services.
- Votre fournisseur d'identité authentifie l'utilisateur et applique ses propres politiques de sécurité.
- Le fournisseur d'identité renvoie à SASE des revendications d'identité signées.
- SASE associe la revendication d'e-mail vérifiée à un utilisateur existant dans l'entreprise sélectionnée et crée la session SASE.

La Plateforme SASE utilise le flux de code d'autorisation avec PKCE. Le mot de passe de l'utilisateur auprès du fournisseur d'identité est saisi uniquement chez ce fournisseur et n'est pas stocké par Jimber.

## Pourquoi la connexion OIDC est proposée

OIDC permet à une organisation d'utiliser sa plateforme d'identité existante comme point central d'authentification. Cette approche présente plusieurs avantages :

- **Une seule identité organisationnelle :** Les utilisateurs peuvent accéder à SASE avec le même compte que celui utilisé pour les autres applications de l'entreprise.
- **Contrôles de sécurité centralisés :** Le fournisseur d'identité peut imposer l'authentification multifacteur, l'accès conditionnel, des politiques de mot de passe et le verrouillage des comptes.
- **Gestion plus rapide du cycle de vie des comptes :** La désactivation d'un compte chez le fournisseur d'identité empêche les nouvelles connexions OIDC, sans avoir à gérer un autre mot de passe SASE.
- **Moins de mots de passe :** SASE n'a pas besoin d'un mot de passe distinct pour les utilisateurs qui s'authentifient par OIDC.
- **Intégration indépendante du fournisseur :** Tout fournisseur OIDC conforme aux normes peut être utilisé.

La connexion OIDC authentifie les utilisateurs, mais ne les provisionne pas. Créez ou synchronisez l'utilisateur dans SASE avant sa première connexion OIDC. L'utilisateur SASE et le compte du fournisseur d'identité doivent avoir la même adresse e-mail vérifiée.

## Prérequis

Avant de configurer OIDC, assurez-vous que :

- L'intégration OIDC est incluse dans le forfait SASE de l'entreprise.
- Vous avez l'autorisation de gérer la configuration SASE de l'entreprise.
- Vous pouvez créer une application web confidentielle auprès du fournisseur d'identité.
- Chaque utilisateur qui se connectera existe déjà dans l'entreprise SASE.
- Le fournisseur d'identité expose son émetteur et ses points de terminaison de découverte sur un HTTPS public.
- Le fournisseur d'identité renvoie une revendication `email` vérifiée.

Pendant la configuration et les tests d'OIDC, gardez au moins une méthode de connexion administrateur existante activée.

## 1. Créer l'application chez le fournisseur d'identité

Créez une application web confidentielle chez le fournisseur d'identité avec les paramètres suivants :

| Paramètre                    | Valeur                                             |
| ---------------------------- | -------------------------------------------------- |
| Type d'application           | Web                                                |
| Flux                         | Code d'autorisation avec PKCE (`S256`)            |
| URI de redirection           | `https://sase.jimber.io/api/v1/auth/oidc/callback` |
| Authentification du point de terminaison de jetons | `client_secret_post` |
| Portées                      | `openid profile email`                            |

L'URI de redirection est également affichée dans le formulaire du fournisseur SASE. Copiez-la exactement, y compris le schéma et le chemin.

Après avoir créé l'application, copiez son ID client et son secret client. Stockez le secret en lieu sûr, car il ne sera peut-être affiché qu'une seule fois.

> [!NOTE]
> Les consoles des fournisseurs utilisent des libellés différents pour l'authentification du point de terminaison de jetons. Par exemple, ZITADEL appelle simplement **Post** l'option `client_secret_post`.

## 2. Ajouter le fournisseur dans SASE

1. Ouvrez **Entreprise > Configuration**.
2. Dans **Authentification**, sélectionnez **Ajouter un fournisseur OIDC**.
3. Remplissez le formulaire du fournisseur.

![Ajouter un fournisseur OIDC dans la Plateforme Jimber SASE](./screenshots/oidc-provider-form.png ':size=360')

Utilisez les valeurs suivantes :

- **Nom du fournisseur :** Le nom affiché sur la page de connexion de l'entreprise, par exemple `Company SSO`.
- **URL de l'émetteur :** La valeur exacte de l'émetteur figurant dans le document de découverte du fournisseur.
- **URL de découverte :** Généralement `<issuer>/.well-known/openid-configuration`. SASE génère automatiquement cette URL et permet de la modifier pour les fournisseurs qui publient leurs métadonnées ailleurs.
- **ID client :** L'ID client de l'application créée chez le fournisseur d'identité.
- **Secret client :** Le secret client de l'application.
- **Portées :** Utilisez `openid profile email`, sauf si le fournisseur exige des portées supplémentaires.
- **Revendication d'e-mail :** Utilisez `email`, sauf si le fournisseur expose l'adresse vérifiée de l'utilisateur sous un autre nom de revendication.

Sélectionnez **Ajouter un fournisseur** pour enregistrer la configuration.

## 3. Tester le flux de connexion

1. Ouvrez l'URL de connexion propre à l'entreprise dans une fenêtre de navigation privée :

    ```text
    https://sase.jimber.io/login/<company-name>
    ```

2. Sélectionnez le fournisseur OIDC configuré.

![Sélectionner le fournisseur OIDC sur la page de connexion de l'entreprise](./screenshots/oidc-login-screen.jpg ':size=480')

3. Authentifiez-vous auprès du fournisseur d'identité.
4. Vérifiez que le navigateur revient au tableau de bord SASE.

Le bouton du fournisseur affiche le nom configuré pour celui-ci. Une entreprise peut configurer plusieurs fournisseurs OIDC lorsque différents groupes d'utilisateurs s'authentifient auprès de systèmes d'identité différents.

## Comment SASE associe un utilisateur

Après que le fournisseur d'identité a renvoyé la réponse d'autorisation, SASE valide l'état, le nonce, le vérificateur PKCE, la signature du jeton, l'émetteur et le sujet. SASE lit ensuite la revendication d'e-mail configurée.

Lors de la première connexion d'un utilisateur par l'intermédiaire d'un fournisseur :

- La revendication doit contenir une adresse e-mail.
- Le fournisseur doit marquer la revendication standard `email` comme vérifiée.
- L'adresse vérifiée doit correspondre à un utilisateur existant dans la même entreprise SASE.

Après une association réussie, SASE lie le sujet du fournisseur à cet utilisateur. Les connexions suivantes utilisent ce lien vers le sujet propre au fournisseur, tout en préservant la séparation entre les entreprises.

## Dépannage

Si SASE affiche **Échec de la connexion OIDC**, vérifiez les points suivants :

- L'URL de l'émetteur correspond exactement à la valeur `issuer` du document de découverte.
- L'URL de découverte est accessible via un HTTPS public.
- L'URI de redirection configurée chez le fournisseur d'identité correspond exactement à celle affichée par SASE.
- L'ID client et le secret client sont à jour.
- Le fournisseur d'identité accepte `client_secret_post` sur son point de terminaison de jetons.
- Le flux de code d'autorisation et PKCE `S256` sont activés.
- Les portées demandées incluent `openid` et le fournisseur renvoie la revendication d'e-mail configurée.
- Le fournisseur renvoie `email_verified: true` lors d'une première association.
- Un utilisateur SASE ayant la même adresse e-mail existe dans l'entreprise sélectionnée et est activé.

Les administrateurs peuvent consulter **Supervision > Activité** pour repérer une entrée d'échec de connexion OIDC. Si le problème persiste, copiez les informations de débogage SASE et joignez-les à une demande d'assistance. N'incluez jamais le secret client dans des captures d'écran, des tickets ou des journaux.

## Mettre à jour ou supprimer un fournisseur

Utilisez **Modifier** à côté du fournisseur pour changer son nom d'affichage, ses points de terminaison, ses identifiants, ses portées ou sa revendication d'e-mail. Lors de la rotation du secret client, mettez à jour le fournisseur d'identité et SASE, puis effectuez un autre test de connexion dans une fenêtre de navigation privée.

Avant de désactiver ou de supprimer un fournisseur, vérifiez qu'une autre méthode de connexion reste disponible. Cela évite que les administrateurs perdent l'accès à l'entreprise.
