# ![native_networks](../images/menu/menu_nativenetworks.png ':size=25') Équilibrage de charge WAN

Utilisez la page *Équilibrage de charge WAN* pour choisir les interfaces WAN utilisées en fonctionnement normal et celles réservées au basculement.

- Les *Interfaces WAN principales* sont les connexions WAN privilégiées pour les liens qui doivent acheminer le trafic en fonctionnement normal.
- Les *Interfaces WAN de basculement* sont des connexions WAN de secours utilisées lorsque la connectivité principale est indisponible.

![wan-load-balance.png](./screenshots/wan-load-balance.png ':size=900')

### Configurer l’équilibrage de charge WAN


- Ouvrez **Réseaux natifs**.
- Sélectionnez **Équilibrage de charge WAN**.
- Sélectionnez le **contrôleur réseau** approprié dans la liste déroulante en haut à gauche de la page.
- Dans la section *Interfaces WAN principales*, cliquez sur **Ajouter des interfaces WAN**.

![add-wan-interface.png](./screenshots/add-wan-interface.png ':size=600')

- Sélectionnez une ou plusieurs interfaces WAN à l’aide des cases à cocher.
- Cliquez sur *Enregistrer*.
- Suivez la même procédure pour les **Interfaces WAN de basculement**

>[!Attention]
> N’oubliez pas de cliquer sur *Soumettre* sur la page principale !

### Mettre à jour les interfaces WAN

La mise à jour des interfaces WAN s’effectue de la même manière que leur configuration : 

- Ouvrez **Réseaux natifs**.
- Sélectionnez **Équilibrage de charge WAN**.
- Sélectionnez le **contrôleur réseau** approprié dans la liste déroulante en haut à gauche de la page.
- Modifiez les interfaces sélectionnées en ouvrant la fenêtre *Ajouter des interfaces WAN* dans l’une ou l’autre section.

>[!Attention]
> N’oubliez pas de cliquer sur *Enregistrer* dans la fenêtre actuelle, puis sur *Soumettre* sur la page principale !

<!-- 1. Retournez à *Équilibrage de charge WAN*.
2. Sélectionnez le même *contrôleur réseau*.
3. Ouvrez la fenêtre *Ajouter des interfaces WAN* dans l’une ou l’autre section.
4. Modifiez les interfaces sélectionnées.
5. Cliquez sur *Enregistrer*.
6. Cliquez sur *Soumettre*. -->

### Supprimer des interfaces WAN

Pour supprimer une interface WAN 

- Ouvrez **Réseaux natifs**.
- Sélectionnez **Équilibrage de charge WAN**.
- Sélectionnez le **contrôleur réseau** approprié dans la liste déroulante en haut à gauche de la page.
- Ouvrez la fenêtre *Ajouter des interfaces WAN* dans l’une ou l’autre section.
- Cliquez sur le bouton *X* à côté du nom de l’interface.

![remove-wan-interface.png](./screenshots/remove-wan-interface.png ':size=600')

>[!Attention]
> N’oubliez pas de cliquer sur *Enregistrer* dans la fenêtre actuelle, puis sur *Soumettre* sur la page principale !


<!-- 1. Retournez à *Équilibrage de charge WAN*.
2. Sélectionnez le même *contrôleur réseau*.
3. Cliquez sur le bouton *X* à côté du nom de l’interface dans la section *Interfaces WAN principales* ou *Interfaces WAN de basculement*.
4. Cliquez sur *Soumettre*. -->

> [!IMPORTANT]
> Au moins une interface principale est requise avant de pouvoir soumettre les modifications.

![one_primary_interface.png](./screenshots/one_primary_interface.png ':size=600')


> [!NOTE]
> Le WAN par défaut de votre contrôleur réseau est automatiquement sélectionné comme première interface WAN principale. 
<!-- Vous pouvez le modifier en cliquant sur l’icône de modification dans la section *Interfaces WAN principales*. -->

## Résumé

Utilisez *Équilibrage de charge WAN* pour améliorer la disponibilité et répartir le trafic sortant entre les interfaces WAN attribuées à un contrôleur réseau sur site.
