File: advanced/unified_environment/unified_environment.md

# Comment créer un environnement combiné pour plusieurs clients

## Qu’est-ce qu’un environnement unifié ?

Un environnement unifié dans Jimber SASE est une configuration architecturale dans laquelle nous intégrons les systèmes de plusieurs entreprises dans un environnement unique. Au lieu d’isoler les systèmes de chaque entreprise dans des environnements ou des locataires distincts, nous les regroupons dans une seule instance SASE.

### Pourquoi choisir un environnement unifié ?

- **Rentabilité** : un seul environnement suffit pour plusieurs entreprises, ce qui réduit considérablement les frais liés à l’infrastructure, aux licences et aux opérations.
- **Respect des exigences minimales** : Jimber SASE exige un minimum de 10 utilisateurs par environnement. En regroupant les entreprises dans un seul environnement, vous pouvez satisfaire efficacement à cette exigence sans obliger les petites entreprises à gérer des environnements distincts.
- **Gestion centralisée** : une seule instance SASE pour les petites entreprises simplifie l’administration, la supervision et les mises à jour.
- **Maintenance simplifiée** : avec moins d’environnements pour les petites entreprises, la maintenance continue et la gestion des politiques sont plus faciles et prennent moins de temps.
- **Séparation claire et flexibilité** : même si les entreprises partagent l’environnement unifié, des configurations, des politiques et des contrôles d’accès propres à chacune garantissent que chaque entreprise reste isolée et protégée au sein de la configuration.

### Remarque

Pour les entreprises de plus de 10 utilisateurs, nous conseillons de créer un **environnement dédié** plutôt que de les inclure dans un environnement unifié. Cela permet d’éviter une complexité inutile et de gérer plus clairement les politiques et les configurations.



---

### Garder les choses organisées

Dans un environnement combiné, des conventions de nommage strictes et des mécanismes de séparation logique sont essentiels pour maintenir la clarté et le contrôle. Voici comment nous procédons :

- **Groupes :** les ressources de chaque entreprise (utilisateurs, appareils, emplacements) sont affectées à des groupes distincts qui respectent une convention de nommage de type domaine (par exemple, `group.users.companya.be`, `group.devices.companyb.co.uk`).

- **Règles :** les règles de pare-feu, les politiques et les configurations de sécurité utilisent des noms de type domaine (par exemple, `rule.allow-http.companya.be`, `rule.allow-crm.companyb.co.uk`). Cela évite tout chevauchement ou toute héritage de politique involontaire.

- **Instances :** le cas échéant (par exemple, pour les passerelles virtuelles ou les moteurs de politiques), les instances sont créées avec des identifiants uniques de type domaine (par exemple, `instance.gateway1.companya.be`, `instance.policyengine1.companyb.co.uk`).

---

## Intégration dans un environnement unifié (Jimber SASE)

Dans un environnement combiné ou unifié, l’intégration de nouvelles entreprises et de leurs ressources est un processus simplifié qui garantit que toutes les entités sont correctement segmentées tout en étant gérées de manière centralisée. Voici les étapes à suivre.

---

### Étape 1 — Ajouter les domaines des entreprises

La première étape consiste à enregistrer les domaines de chaque entreprise dans l’environnement SASE. Ces domaines définissent l’identité de chaque organisation au sein du système combiné.

**Exemples de domaines :**
- `companya.be`
- `companyb.co.uk`

Les domaines servent d’espace de noms de référence principal pour les utilisateurs, les groupes, les ressources et les politiques.

![domains.png](/screenshots/domains.png ':size=600')

---

### Étape 2 — Ajouter les utilisateurs

Les utilisateurs sont ajoutés en fonction de leur adresse e-mail, qui les associe automatiquement au domaine et à l’entreprise appropriés.

Aucune autre étape d’intégration n’est nécessaire pour chaque utilisateur, au-delà de l’ajout de son adresse e-mail : son appartenance à un domaine est évidente à partir de son adresse (par exemple, `alice@companya.be`, `bob@companyb.co.uk`).

![users.png](/screenshots/users.png ':size=600')

---

### Étape 3 — Affecter les utilisateurs à des groupes

Chaque utilisateur est placé dans des groupes propres à son entreprise. Ces groupes respectent la convention de nommage de type domaine.

**Exemples :**
- `group.all-users.companya.be`
- `group.all-users.companyb.co.uk`

Vous pouvez créer des sous-groupes supplémentaires selon vos besoins, pour segmenter les utilisateurs par rôle ou par département (par exemple, `group.admins.companya.be`, `group.hr.companyb.co.uk`).

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

Enfin, accordez l’accès en reliant les groupes créés (à l’étape 3) aux ressources correspondantes (à l’étape 4).

Cela se fait au moyen d’une politique basée sur les services, dans laquelle des attributs tels que l’appartenance à un groupe et les noms des ressources sont associés à des autorisations d’accès.

Les utilisateurs de chaque entreprise n’accèdent qu’aux ressources de leur entreprise, même si tout fonctionne au sein de la même plateforme SASE.

---

### Groupes de sécurité unifiés et fonctionnels

En plus des groupes propres à chaque entreprise, Jimber SASE permet de créer des groupes de sécurité unifiés et fonctionnels. Ces groupes offrent un moyen efficace d’appliquer des politiques de sécurité cohérentes à plusieurs entreprises au sein du même environnement combiné.

#### Que sont les groupes de sécurité unifiés et fonctionnels ?

Les groupes de sécurité unifiés et fonctionnels :
- Regroupent plusieurs entreprises dans l’environnement combiné
- Se concentrent sur des fonctions de sécurité communes plutôt que sur les limites entre entreprises
- Permettent d’appliquer les politiques de manière centralisée et uniforme

**Par exemple :**
- Un groupe comme `group.webfiltering-enabled.all-companies` pourrait inclure `group.all-users.companya.be`, `group.all-users.companyb.co.uk` et les groupes d’utilisateurs d’autres entreprises.

---

<!-- #### How They Work

Central policy application  
You can attach security features (such as `policy.webfiltering.all-companies`, `policy.dns-protection.all-companies`) directly to these functional groups. This ensures the policy is enforced consistently, no matter the company. -->
#### Fonctionnement en tant qu’application de politiques centralisée 
 
Vous pouvez associer des fonctionnalités de sécurité (telles que `policy.webfiltering.all-companies`, `policy.dns-protection.all-companies`) directement à ces groupes fonctionnels. Cela garantit l’application uniforme de la politique, quelle que soit l’entreprise.


**Appartenance flexible**  
Des groupes de différentes entreprises peuvent être ajoutés comme membres d’un groupe fonctionnel. Ainsi, une seule politique peut couvrir de nombreuses entreprises sans qu’il soit nécessaire de dupliquer les configurations.

**Aucun risque supplémentaire**  
Même si ces groupes regroupent plusieurs entreprises :
- Il n’y a aucun accès croisé involontaire aux ressources ou aux données
- Les politiques appliquées concernent uniquement les mesures de sécurité et n’accordent pas l’accès aux ressources propres à une entreprise

---

#### Exemple de cas d’utilisation

Imaginez que vous vouliez appliquer le filtrage web à toutes les entreprises que vous gérez.

1. Créez un groupe fonctionnel : `group.webfiltering-enabled.all-companies`
2. Ajoutez les groupes des entreprises :
   - `group.all-users.companya.be`
   - `group.all-users.companyb.co.uk`
   - `group.all-users.companyc.com`
3. Associez la politique : `policy.webfiltering.all-companies`

Tous les utilisateurs des différentes entreprises bénéficient alors d’une politique de protection web uniforme.
