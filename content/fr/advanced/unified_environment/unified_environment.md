# Comment créer un environnement combiné pour plusieurs clients

## Qu’est-ce qu’un environnement unifié ?

Un environnement unifié dans la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** est une architecture dans laquelle les systèmes de plusieurs entreprises sont intégrés dans un seul environnement. Au lieu d’isoler les systèmes de chaque entreprise dans des environnements ou des locataires distincts, nous les réunissons au sein d’une seule instance SASE.

### Pourquoi choisir un environnement unifié ?

- **Rentabilité** : un seul environnement suffit pour plusieurs entreprises, ce qui réduit considérablement les frais d’infrastructure, de licences et d’exploitation.
- **Respect des exigences minimales** : Jimber SASE exige un minimum de 10 utilisateurs par environnement. En réunissant plusieurs entreprises dans un seul environnement, vous pouvez respecter efficacement cette exigence sans obliger les petites entreprises à maintenir des environnements distincts.
- **Gestion centralisée** : une seule instance SASE pour les petites entreprises simplifie l’administration, la supervision et les mises à jour.
- **Maintenance simplifiée** : avec moins d’environnements pour les petites entreprises, la maintenance continue et la gestion des politiques sont plus simples et prennent moins de temps.
- **Séparation claire et flexibilité** : même si les entreprises partagent un environnement unifié, des configurations, des politiques et des contrôles d’accès propres à chacune garantissent que chaque entreprise reste isolée et sécurisée au sein de l’environnement.

### Remarque

Pour les entreprises de plus de 10 utilisateurs, nous recommandons de créer un **environnement dédié** plutôt que de les inclure dans un environnement unifié. Cela permet d’éviter une complexité inutile et de gérer plus clairement les politiques et les configurations.



---

### Garder les choses organisées

Dans un environnement combiné, des conventions de nommage strictes et des mécanismes de séparation logique sont essentiels pour préserver la clarté et le contrôle. Voici comment nous procédons :

- **Groupes :** les ressources de chaque entreprise (utilisateurs, appareils, emplacements) sont affectées à des groupes distincts qui suivent une convention de nommage de type domaine (par exemple, `group.users.companya.be`, `group.devices.companyb.co.uk`).

- **Règles :** les règles de pare-feu, les politiques et les configurations de sécurité utilisent des noms de type domaine (par exemple, `rule.allow-http.companya.be`, `rule.allow-crm.companyb.co.uk`). Cela évite tout chevauchement ou toute application involontaire de politiques héritées.

- **Instances :** lorsque cela s’applique (par exemple, pour les passerelles virtuelles et les moteurs de politiques), des instances sont créées avec des identifiants uniques de type domaine (par exemple, `instance.gateway1.companya.be`, `instance.policyengine1.companyb.co.uk`).

---

## Intégration à un environnement unifié (Jimber SASE)

Dans un environnement combiné ou unifié, l’intégration de nouvelles entreprises et de leurs ressources suit un processus simplifié qui garantit la segmentation correcte de toutes les entités, tout en permettant leur gestion centralisée. Voici les étapes à suivre.

---

### Étape 1 — Ajouter les domaines des entreprises

La première étape consiste à enregistrer les domaines de chaque entreprise dans l’environnement SASE. Ces domaines définissent l’identité de chaque organisation au sein du système combiné.

**Exemples de domaines :**
- `companya.be`
- `companyb.co.uk`

Les domaines servent de référence principale à l’espace de noms des utilisateurs, des groupes, des ressources et des politiques.

![domains.png](/screenshots/domains.png ':size=600')

---

### Étape 2 — Ajouter les utilisateurs

Les utilisateurs sont ajoutés à partir de leurs adresses e-mail, qui les associent automatiquement au domaine ou à l’entreprise approprié.

Aucune autre étape d’intégration n’est nécessaire pour chaque utilisateur, au-delà de l’ajout de son adresse e-mail : son appartenance à un domaine est claire grâce à son adresse (par exemple, `alice@companya.be`, `bob@companyb.co.uk`).

![users.png](/screenshots/users.png ':size=600')

---

### Étape 3 — Affecter les utilisateurs à des groupes

Chaque utilisateur est placé dans des groupes propres à son entreprise. Ces groupes suivent la convention de nommage de type domaine.

**Exemples :**
- `group.all-users.companya.be`
- `group.all-users.companyb.co.uk`

Vous pouvez créer d’autres sous-groupes selon vos besoins pour segmenter les utilisateurs par rôle ou par service (par exemple, `group.admins.companya.be`, `group.hr.companyb.co.uk`).

---

### Étape 4 — Intégrer les ressources de l’entreprise

Ajoutez les ressources propres à l’entreprise (serveurs, applications, partages de fichiers, etc.). Les ressources sont nommées selon la même convention de type domaine.

**Exemples :**
- `server.servera.companya.be`
- `app.sharepoint.companyb.co.uk`
- `db.db01.companya.be`

Cela facilite l’identification et la gestion des ressources propres à chaque entreprise.

![servers.png](/screenshots/servers.png ':size=600')

---

### Étape 5 — Configurer l’accès au moyen d’une politique basée sur les services

Enfin, accordez l’accès en reliant les groupes créés à l’étape 3 aux ressources correspondantes de l’étape 4.

Cela se fait au moyen d’une politique basée sur les services, dans laquelle des attributs tels que l’appartenance à un groupe et les noms des ressources sont associés à des autorisations d’accès.

Les utilisateurs de chaque entreprise n’ont accès qu’aux ressources de leur entreprise, même si tout fonctionne au sein de la même plateforme SASE.

---

### Groupes de sécurité unifiés et fonctionnels

En plus des groupes propres à chaque entreprise, Jimber SASE permet de créer des groupes de sécurité unifiés et fonctionnels. Ces groupes constituent un moyen efficace d’appliquer des politiques de sécurité cohérentes à plusieurs entreprises au sein du même environnement combiné.

#### Que sont les groupes de sécurité unifiés et fonctionnels ?

Les groupes de sécurité unifiés et fonctionnels :
- couvrent plusieurs entreprises au sein de l’environnement combiné
- se concentrent sur des fonctions de sécurité communes plutôt que sur les limites entre les entreprises
- permettent d’appliquer les politiques de façon centralisée et uniforme

**Par exemple :**
- Un groupe tel que `group.webfiltering-enabled.all-companies` peut inclure `group.all-users.companya.be`, `group.all-users.companyb.co.uk` et d’autres groupes d’utilisateurs d’entreprise.

---

<!-- #### How They Work

Central policy application  
You can attach security features (such as `policy.webfiltering.all-companies`, `policy.dns-protection.all-companies`) directly to these functional groups. This ensures the policy is enforced consistently, no matter the company. -->
#### Fonctionnement comme application centralisée des politiques 
 
Vous pouvez associer directement des fonctionnalités de sécurité (telles que `policy.webfiltering.all-companies`, `policy.dns-protection.all-companies`) à ces groupes fonctionnels. Cela garantit une application cohérente de la politique, quelle que soit l’entreprise.


**Appartenance flexible**  
Les groupes de différentes entreprises peuvent être ajoutés en tant que membres d’un groupe fonctionnel. Cela permet à une seule politique de couvrir plusieurs entreprises sans dupliquer les configurations.

**Aucun risque supplémentaire**  
Même si ces groupes couvrent plusieurs entreprises :
- il n’y a aucun accès involontaire aux ressources ou aux données des autres entreprises
- les politiques appliquées ne servent qu’à mettre en œuvre des mesures de sécurité et n’accordent pas l’accès aux ressources propres à une entreprise

---

#### Exemple de cas d’utilisation

Imaginez que vous souhaitiez appliquer le filtrage web à toutes les entreprises que vous gérez.

1. Créez un groupe fonctionnel : `group.webfiltering-enabled.all-companies`
2. Ajoutez les groupes d’entreprises :
   - `group.all-users.companya.be`
   - `group.all-users.companyb.co.uk`
   - `group.all-users.companyc.com`
3. Associez la politique : `policy.webfiltering.all-companies`

Tous les utilisateurs des différentes entreprises bénéficient alors d’une politique uniforme de protection web.
