# Sortie Zero Trust

ZTO est un mode de sécurité dans lequel les connexions sortantes des agents sont restreintes par défaut, ce qui nécessite une règle de pare-feu explicite pour chaque connexion autorisée.

 Lorsque Zero Trust Outbound est activé, trois nouvelles politiques de pare-feu sont créées dans la **_<span style="color: darkblue;">Plateforme Jimber SASE</span>_** : 

 ![zto_policies.png](./images/zto_policies.png ':size=800') 

1. Internet standard - NIAC
2. Internet standard - Serveurs
3. Internet standard - Utilisateurs

Les trois politiques reposent sur le même principe : refuser tout le trafic sortant. Seul le trafic spécifiquement autorisé est permis.
Internet n’est utilisable que lorsque ces politiques sont activées. 

Vous trouverez [ici](/./rules/firewall-policies/firewall-policies.md) plus d’informations sur les politiques de pare-feu.



Dans les [services de pare-feu](/./rules/firewall-policies/firewall-policies.md), vous pouvez spécifier les ports et le protocole par lesquels le protocole communiquera.

![update_service_internet.png](./images/update_service_internet.png ':size=800') 

>[!WARNING]
>La modification ou la suppression de l’une de ces options peut entraîner une défaillance du service correspondant.
