# ![native_networks](../images/menu/menu_wanloadbalance.png ':size=25') Équilibrage de charge WAN

Utilisez la page *Équilibrage de charge WAN* pour choisir les interfaces WAN utilisées en fonctionnement normal et celles réservées au basculement.

- Les *interfaces principales* sont les connexions WAN privilégiées pour les liaisons qui doivent acheminer le trafic en fonctionnement normal.
- Les *interfaces de basculement* sont les connexions WAN de secours utilisées lorsque la connectivité principale est indisponible.

![wan-load-balance.png](./screenshots/wan-load-balance.png ':size=800')

### Configurer l’équilibrage de charge WAN


- Ouvrez **Réseaux natifs**.
- Sélectionnez **Équilibrage de charge WAN**.
- Sélectionnez le **contrôleur réseau** approprié dans la liste déroulante en haut à gauche de la page.
- Dans la section *Interfaces principales*, cliquez sur **Ajouter des interfaces WAN**.

![add-wan-interface.png](./screenshots/add-wan-interface.png ':size=500')

- Sélectionnez une ou plusieurs interfaces WAN à l’aide des cases à cocher.
- Cliquez sur *Enregistrer*.
- Suivez la même procédure pour les **interfaces de basculement**.

>[!Attention]
> N’oubliez pas de cliquer sur *Soumettre* sur la page principale !

### Mettre à jour les interfaces WAN

La mise à jour des interfaces WAN s’effectue de la même manière que leur configuration :

- Ouvrez **Réseaux natifs**.
- Sélectionnez **Équilibrage de charge WAN**.
- Sélectionnez le **contrôleur réseau** approprié dans la liste déroulante en haut à gauche de la page.
- Modifiez les interfaces sélectionnées en ouvrant la fenêtre *Ajouter des interfaces WAN* dans l’une ou l’autre des sections.

>[!Attention]
> N’oubliez pas de cliquer sur *Enregistrer* dans la fenêtre actuelle et sur *Soumettre* sur la page principale !

<!-- 1. Return to *WAN Load Balance*.
2. Select the same *Network Controller*.
3. Open the *Add WAN Interfaces* window in either section.
4. Adjust the selected interfaces.
5. Click *Save*.
6. Click *Submit*. -->

### Supprimer des interfaces WAN

Pour supprimer une interface WAN :

- Ouvrez **Réseaux natifs**.
- Sélectionnez **Équilibrage de charge WAN**.
- Sélectionnez le **contrôleur réseau** approprié dans la liste déroulante en haut à gauche de la page.
- Ouvrez la fenêtre *Ajouter des interfaces WAN* dans l’une ou l’autre des sections.
- Cliquez sur le bouton *X* à côté du nom de l’interface.

![remove-wan-interface.png](./screenshots/remove-wan-interface.png ':size=500')

>[!Attention]
> N’oubliez pas de cliquer sur *Enregistrer* dans la fenêtre actuelle et sur *Soumettre* sur la page principale !


<!-- 1. Return to *WAN Load Balance*.
2. Select the same *Network Controller*.
3. Click the *X* button next to the interface name in the *Primary Interfaces* or *Failover Interfaces* section.
4. Click *Submit*. -->

> [!IMPORTANT]
> Au moins une interface principale est requise avant de pouvoir soumettre les modifications.

![one_primary_interface.png](./screenshots/one_primary_interface.png ':size=500')


> [!NOTE]
> Le WAN par défaut de votre contrôleur réseau est automatiquement sélectionné comme première interface WAN principale.
<!-- You can change it by clicking the edit icon in the *Primary Interfaces* section. -->

## Résumé

Utilisez *Équilibrage de charge WAN* pour améliorer la disponibilité et répartir le trafic sortant entre les interfaces WAN attribuées à un contrôleur réseau sur site.
