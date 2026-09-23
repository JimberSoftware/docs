# Plateforme SASE - Bonnes pratiques
## Introduction
Bienvenue dans le guide des bonnes pratiques de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Dans ce document, nous allons voir comment tirer le meilleur parti de notre produit en nous concentrant sur des aspects essentiels : la configuration des groupes, le choix des plages d’adresses IP appropriées et la gestion des autorisations des utilisateurs. Il est particulièrement important de vous familiariser dès maintenant avec ces fonctionnalités, car nous prévoyons de supprimer progressivement la prise en charge de plusieurs plages d’adresses IP. Ce guide a pour objectif de vous fournir tous les outils et les connaissances nécessaires pour que votre réseau soit non seulement performant, mais aussi sécurisé et prêt pour l’avenir.

## Application des règles
Lors de la configuration des règles dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, il est essentiel de privilégier la fonctionnalité plutôt que des groupes d’utilisateurs spécifiques. Cette approche met l’accent sur l’objectif ou l’action de la règle, ce qui rend la configuration de votre réseau plus intuitive et plus facile à gérer. Par exemple, au lieu de nommer un groupe en fonction d’un service ou du personnel, comme « Ventes », choisissez un nom qui reflète sa fonction. Vous pouvez, par exemple, utiliser « AutoriserServeurFichiers » pour accorder l’accès à un serveur de fichiers.

Pour illustrer ce principe, d’autres exemples de noms de groupes axés sur leur fonction pourraient inclure « ForcerPasserelleWan », pour acheminer tout le trafic via une passerelle WAN spécifique, ou « BloquerSitesDangereux » pour un groupe visant à renforcer la sécurité du réseau en limitant l’accès à des sites en ligne potentiellement dangereux. Autre exemple : « AutoriserConnexionServeurDistant », un groupe destiné aux utilisateurs qui ont besoin d’un accès à distance aux serveurs.

En adoptant cette convention de nommage fonctionnelle, vous créez une structure de règles claire et explicite. Cette méthode simplifie l’administration du réseau et permet d’identifier, de modifier et de comprendre rapidement le rôle et les autorisations de chaque groupe. Ainsi, à mesure que votre réseau se développe ou évolue, vous pouvez facilement adapter les accès et les autorisations sans avoir à remanier la structure des groupes.

<!-- ## Paramètres du pare-feu

Pour utiliser notre plateforme SASE, les ports sortants suivants doivent être autorisés sur votre ou vos pare-feu : 

- 51820 UDP
- 51820 TCP
- 443 TCP -->


## Groupes Azure
Lors de l’intégration de la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** à Azure Entra ID, il est important de comprendre le fonctionnement de la synchronisation des groupes. Par exemple, si vous avez un groupe nommé « AllowFileserver » dans Azure et que le groupe « Sales » en est membre, tous les membres de « Sales » seront automatiquement synchronisés avec le groupe « AllowFileserver » dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***.

Cela permet de refléter la structure de votre organisation dans les autorisations réseau en tirant parti des groupes imbriqués existants dans Azure. Cette intégration simplifie la gestion des accès, car les modifications apportées à l’appartenance aux groupes Azure sont automatiquement répercutées dans la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***, assurant ainsi cohérence et efficacité.


![entraid_example.png](/screenshots/entraid_example.png)
