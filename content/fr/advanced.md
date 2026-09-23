# AVANCÉ

La section **Avancé** comprend des fonctionnalités et des intégrations puissantes pour les environnements complexes, notamment la prise en charge d’Active Directory, les clusters d’hyperviseurs, les installations de contrôleurs réseau et la journalisation étendue de la plateforme. Utilisez ces outils si vous travaillez dans un environnement d’entreprise ou si vous avez besoin d’une personnalisation et d’un contrôle approfondis.

---

- [Configuration personnalisée](./advanced/customconfiguration/customconfiguration)  
  Définissez des paramètres avancés et des remplacements pour adapter le comportement du réseau, les options de ***_<span style="color: darkblue;">Jimber SASE Client</span>_*** ou les paramètres propres aux services à votre environnement.

- [Active Directory](./advanced/activedirectory/activedirectory)  
  Intégrez Microsoft Active Directory pour synchroniser les utilisateurs et les groupes, et activer l’authentification afin de simplifier la gestion de l’entreprise.

- [Microsoft Entra ID](./advanced/entraid/entraid)  
  Connectez votre environnement à Microsoft Entra ID pour centraliser la gestion des identités et des accès dans le cloud sur l’ensemble de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

- [Installation sur un hyperviseur](./advanced/hypervisorinstallation/hypervisorinstallation.md)  
  Installez et configurez le ***_<span style="color: darkblue;">Jimber SASE Client</span>_*** sur votre hyperviseur pour activer l’accès chiffré et la segmentation des environnements virtualisés.

- [Installation des contrôleurs réseau](./advanced/networkcontrollerssetup/SettingUpServer.md)  
  Déployez et configurez des ***_<span style="color: darkblue;">Jimber SASE Controllers</span>_*** autonomes ou basés sur Docker pour segmenter et isoler les réseaux physiques.

- [Synology](./advanced/synology/synology.md)  
  Connectez et gérez en toute sécurité les systèmes NAS Synology via la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, avec notamment la réinitialisation d’usine et la configuration SSH facultatives.

- [Cluster Proxmox](./advanced/proxmox/proxmox)  
  Créez un cluster Proxmox à l’aide de liaisons chiffrées entre des hyperviseurs situés dans différents emplacements avec la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

- [Contrôleur réseau Docker](./advanced/dockernetworkcontroller/dockernetworkcontroller)  
  Configurez des ***_<span style="color: darkblue;">Jimber SASE Controllers</span>_*** conteneurisés pour le routage avancé et la segmentation. Recommandé aux utilisateurs expérimentés.

- [Journalisation](./advanced/logging/logging.md)  
  Repérez et activez la journalisation étendue pour le dépannage sur toutes les plateformes prises en charge. Activez `debug.log` pour obtenir des informations plus détaillées.

- [Jetons d’accès personnels](./advanced/personalaccesstokens/personalaccesstokens.md)  
  Générez et gérez des jetons d’accès personnels (PAT) depuis la page Paramètres pour vous authentifier en toute sécurité et tester des requêtes API dans l’interface `Swagger` à l’aide de votre identité utilisateur.
