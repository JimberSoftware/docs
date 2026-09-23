# Comment créer un environnement combiné pour plusieurs clients

## Qu’est-ce qu’un environnement unifié ?

Un environnement unifié dans Jimber SASE est une configuration architecturale dans laquelle nous intégrons les systèmes de plusieurs entreprises dans un environnement unique. Au lieu d’isoler les systèmes de chaque entreprise dans des environnements ou des locataires distincts, nous les réunissons au sein d’une seule instance SASE.

### Pourquoi choisir un environnement unifié ?

- **Rentabilité** : un seul environnement suffit pour plusieurs entreprises, ce qui réduit considérablement les coûts liés à l’infrastructure, aux licences et aux opérations.
- **Respect des exigences minimales** : Jimber SASE exige un minimum de 10 utilisateurs par environnement. En réunissant plusieurs entreprises dans un seul environnement, vous pouvez satisfaire efficacement à cette exigence sans obliger les petites entreprises à gérer des environnements distincts.
- **Gestion centralisée** : une seule instance SASE pour les petites entreprises simplifie l’administration, la supervision et les mises à jour.
- **Maintenance simplifiée** : avec moins d’environnements pour les petites entreprises, la maintenance continue et la gestion des politiques sont plus faciles et prennent moins de temps.
- **Séparation claire et flexibilité** : même si les entreprises partagent l’environnement unifié, des configurations, des politiques et des contrôles d’accès spécifiques garantissent que chacune reste isolée et sécurisée au sein de la configuration.

### Remarque

Pour les entreprises comptant plus de 10 utilisateurs, nous conseillons de créer un **environnement dédié** plutôt que de les inclure dans un environnement unifié. Cela permet d’éviter toute complexité inutile et de mieux gérer les politiques et les configurations.



---

### Garder les choses organisées

Dans un environnement combiné, des conventions de nommage strictes et des mécanismes de séparation logique sont essentiels pour préserver la clarté et le contrôle. Voici comment nous procédons :

- **Groupes :** les ressources de chaque entreprise (utilisateurs, appareils, emplacements) sont affectées à des groupes distincts qui suivent une convention de nommage similaire à celle des domaines (par exemple, `group.users.companya.be`, `group.devices.companyb.co.uk`).

- **Règles :** les règles de pare-feu, les politiques et les configurations de sécurité utilisent des noms de type domaine (par exemple, `rule.allow-http.companya.be`, `rule.allow-crm.companyb.co.uk`). Cela garantit qu’il n’y a aucun chevauchement ni héritage de politique involontaire.

- **Instances :** lorsque cela s’applique (par exemple, pour les passerelles virtuelles ou les moteurs de politiques), les instances sont créées avec des identifiants uniques de type domaine (par exemple, `instance.gateway1.companya.be`, `instance.policyengine1.companyb.co.uk`).

---

## Intégration dans un environnement unifié (Jimber SASE)

Dans un environnement combiné ou unifié, l’intégration de nouvelles entreprises et de leurs ressources est un processus simplifié qui garantit que toutes les entités sont correctement segmentées tout en étant gérées de manière centralisée. Vous trouverez ci-dessous les étapes à suivre.

---

### Étape 1 — Ajouter les domaines des entreprises

La première étape consiste à enregistrer les domaines de chaque entreprise dans l’environnement SASE. Ces domaines définissent l’identité de chaque organisation au sein du système combiné.

**Exemples de domaines :**
- `companya.be`
- `companyb.co.uk`

Les domaines servent de références principales aux espaces de noms des utilisateurs, des groupes, des ressources et des politiques.

![domains.png](/screenshots/domains.png)

---

### Étape 2 — Ajouter les utilisateurs

Les utilisateurs sont ajoutés à partir de leurs adresses e-mail, qui les associent automatiquement au domaine et à l’entreprise correspondants.

Aucune autre étape d’intégration n’est nécessaire pour chaque utilisateur, hormis l’ajout de son adresse e-mail : son appartenance à un domaine est évidente à partir de son adresse (par exemple, `alice@companya.be`, `bob@companyb.co.uk`).

![users.png](/screenshots/users.png)

---

### Étape 3 — Affecter les utilisateurs à des groupes

Chaque utilisateur est placé dans des groupes propres à son entreprise. Ces groupes suivent la convention de nommage similaire à celle des domaines.

**Exemples :**
- `group.all-users.companya.be`
- `group.all-users.companyb.co.uk`

Vous pouvez créer des sous-groupes supplémentaires selon vos besoins, pour segmenter les utilisateurs par rôle ou par service (par exemple, `group.admins.companya.be`, `group.hr.companyb.co.uk`).

---

### Étape 4 — Intégrer les ressources de l’entreprise

Ajoutez les ressources propres à l’entreprise (serveurs, applications, partages de fichiers, etc.). Les ressources sont nommées selon la même convention de type domaine.

**Exemples :**
- `server.servera.companya.be`
- `app.sharepoint.companyb.co.uk`
- `db.db01.companya.be`

Cela facilite l’identification et la gestion des ressources propres à chaque entreprise.

![servers.png](/screenshots/servers.png)

---

### Étape 5 — Configurer l’accès au moyen d’une politique basée sur les services

Enfin, accordez l’accès en reliant les groupes créés (à l’étape 3) aux ressources correspondantes (à l’étape 4).

Pour ce faire, utilisez une politique basée sur les services, qui associe des attributs tels que l’appartenance à un groupe et les noms des ressources à des autorisations d’accès.

Les utilisateurs de chaque entreprise n’ont accès qu’aux ressources de leur entreprise, même si tout fonctionne au sein de la même plateforme SASE.

---

### Groupes de sécurité unifiés et fonctionnels

En plus des groupes propres à chaque entreprise, Jimber SASE permet de créer des groupes de sécurité unifiés et fonctionnels. Ces groupes offrent un moyen efficace d’appliquer des politiques de sécurité cohérentes à plusieurs entreprises au sein du même environnement combiné.

#### Que sont les groupes de sécurité unifiés et fonctionnels ?

Les groupes de sécurité unifiés et fonctionnels :
- couvrent plusieurs entreprises au sein de l’environnement combiné ;
- se concentrent sur des fonctions de sécurité communes plutôt que sur les limites entre entreprises ;
- permettent d’appliquer les politiques de manière centralisée et uniforme.

**Par exemple :**
- Un groupe tel que `group.webfiltering-enabled.all-companies` pourrait inclure `group.all-users.companya.be`, `group.all-users.companyb.co.uk` et d’autres groupes d’utilisateurs d’entreprises.

---

#### Fonctionnement

Application centralisée des politiques  
Vous pouvez associer des fonctionnalités de sécurité (telles que `policy.webfiltering.all-companies`, `policy.dns-protection.all-companies`) directement à ces groupes fonctionnels. Cela garantit l’application cohérente de la politique, quelle que soit l’entreprise.

**Appartenance flexible**  
Des groupes de différentes entreprises peuvent être ajoutés en tant que membres d’un groupe fonctionnel. Une seule politique peut ainsi couvrir de nombreuses entreprises sans qu’il soit nécessaire de dupliquer les configurations.

**Aucun risque supplémentaire**  
Même si ces groupes couvrent plusieurs entreprises :
- il n’y a aucun accès transversal involontaire aux ressources ou aux données ;
- les politiques appliquées servent uniquement à faire respecter les règles de sécurité et n’accordent pas l’accès aux ressources propres aux entreprises.

---

#### Exemple de cas d’utilisation

Imaginez que vous souhaitiez appliquer le filtrage web à toutes les entreprises que vous gérez.

1. Créez un groupe fonctionnel : `group.webfiltering-enabled.all-companies`
2. Ajoutez les groupes des entreprises :
   - `group.all-users.companya.be`
   - `group.all-users.companyb.co.uk`
   - `group.all-users.companyc.com`
3. Associez la politique : `policy.webfiltering.all-companies`

Tous les utilisateurs des différentes entreprises bénéficient alors d’une politique de protection web uniforme.
