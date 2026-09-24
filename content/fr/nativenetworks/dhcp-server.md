File: nativenetworks/dhcp-server.md

# ![native_networks](../images/menu/menu_dhcpserver.png ':size=25') Serveur DHCP

Utilisez la page *Serveur DHCP* pour configurer les paramètres DHCP et DNS d’un réseau natif.

Cette page vous permet de sélectionner un réseau natif, d’activer ou de désactiver DHCP, de définir la plage d’adresses IP pour les clients DHCP, de configurer la passerelle et de choisir entre les DNS *Jimber* et *Personnalisé*.

### Configurer le serveur DHCP

![dhcp-server.png](./screenshots/dhcp-server.png ':size=700')

- Choisissez un **Réseau natif** dans la liste déroulante en haut à gauche de la page.
- Dans la carte **Configuration DHCP** :
  - Activez la **Bascule principale DHCP** si vous souhaitez que les clients de ce réseau reçoivent automatiquement des adresses IP via DHCP.
  - Vérifiez le champ *Interface*. Ce champ est en lecture seule et affiche l’interface attribuée ainsi que son bloc CIDR.
- Configurez la **Plage** :
  - Saisissez l’adresse IP de début.
  - Saisissez l’adresse IP de fin.
- Saisissez l’**Adresse IP de la passerelle**.
- Configurez le DNS :
  - DNS Jimber : aucun autre paramètre n’est nécessaire.
  - DNS personnalisé :
    - Saisissez l’adresse IP du serveur DNS requis.
    - Pour ajouter un autre serveur DNS, cliquez sur `+ Add IP Address`.

![dhcp-server-custom-dns.png](./screenshots/dhcp-server-custom-dns.png ':size=500')

>[!ATTENTION]
>N’oubliez pas de cliquer sur `Submit` pour appliquer les modifications (bouton en haut à droite).


> [!TIP]
> Utilisez une plage d’adresses IP incluse dans le réseau sélectionné et qui ne chevauche pas les adresses réservées aux passerelles, aux serveurs ou à d’autres appareils ayant une adresse statique.

<!-- ### Configurer le DNS

Utilisez la carte *Configuration DNS* pour choisir comment le DNS doit être fourni aux clients DHCP.



#### Utiliser le DNS Jimber

1. Sélectionnez le *Réseau natif* requis.
2. Dans la carte *Configuration DNS*, choisissez *Jimber* dans la liste déroulante *Sélection DNS*.
3. Consultez le message affiché sur la page : *Modifiez le DNS en « Personnalisé » pour configurer les adresses IP*.
4. Cliquez sur *Submit*.

#### Utiliser des serveurs DNS personnalisés

![dhcp-server-custom-dns.png](./screenshots/dhcp-server-custom-dns.png ':size=500')

1. Sélectionnez le *Réseau natif* requis.
2. Dans la carte *Configuration DNS*, choisissez *Personnalisé* dans la liste déroulante *Sélection DNS*.
3. Dans la section *Adresses IP*, saisissez l’adresse IP du serveur DNS requis.
4. Pour ajouter un autre serveur DNS, cliquez sur *+ Add IP Address*.
5. Pour supprimer un serveur DNS, cliquez sur l’icône de suppression à côté de l’adresse IP.
6. Cliquez sur *Submit*. -->

### Effacer ou soumettre les modifications

En haut à droite de la page se trouvent deux boutons d’action :

- Utilisez **Effacer les modifications** pour annuler vos modifications.
- **Soumettre** enregistre la configuration actuelle.

### Désactiver DHCP

Lorsque vous essayez de désactiver DHCP pour l’un des réseaux natifs, un avertissement s’affiche :

![disabling_DHCP.png](./screenshots/disabling_DHCP.png ':size=400')

Pour désactiver effectivement DHCP, saisissez le nom du réseau natif et cliquez sur le bouton `Disable`.

## Résumé

Utilisez la page *Serveur DHCP* pour configurer l’attribution des adresses IP et les paramètres DNS des appareils connectés à un réseau natif.
