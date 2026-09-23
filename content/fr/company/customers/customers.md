# ![](../../images/menu/menu_customers.png ':size=25') Clients
> [!WARNING]
> Cette section *Clients* est exclusivement réservée aux **partenaires**. Si vous êtes un client final, vous serez directement redirigé vers la configuration ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_*** de votre entreprise.

Sur notre plateforme, un **client** désigne une entreprise qui souhaite utiliser la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Les intégrateurs peuvent gérer ces clients, garantissant ainsi le bon fonctionnement des opérations et la prestation des services.

Pour plus de clarté, prenons l’exemple d’une entreprise nommée *`Astral Voyage`* qui souhaite utiliser la ***_<span style="color: darkblue;">Plateforme Jimber SASE</span>_***. Vous devez d’abord créer *`Astral Voyage`* en tant que client sur la plateforme avant de pouvoir effectuer toute autre configuration ou fournir des services.

![list_customers.png](./screenshots/list_customers.png ':size=800')

### Créer un client

Pour ajouter un nouveau client à la plateforme, cliquez sur le bouton `+ Create new`, situé dans le coin supérieur droit de l’interface.

![create_customer.png](./screenshots/create_customer.png ':size=350')

- Les champs suivants sont obligatoires :
	
    - Nom. 
    - Nom d’affichage. Le nom d’affichage peut contenir des lettres et des chiffres.
    - Adresse e-mail du contact principal.


- Les options suivantes doivent être définies :

    - Quel forfait choisir : SASE ou ViPN ?
    - Activez ***Provision Cloud Controller*** lorsqu’un contrôleur réseau doit être provisionné.

- Le renseignement du site web fera apparaître une icône devant le nom du client.

> [!WARNING]
> Le nom ne peut contenir que des lettres et des chiffres. Les espaces, caractères spéciaux et symboles ne sont pas autorisés.
>
> Vous pouvez toutefois utiliser ces caractères dans le champ Nom d’affichage.




### Filtrer les clients

Vous pouvez rechercher un client dans la liste à l’aide du champ de recherche situé en haut de la page. Vous trouverez ainsi rapidement le client que vous cherchez et pourrez le gérer.

- Utilisez le champ de recherche pour saisir des mots-clés et filtrer la liste des clients.

À côté du champ de recherche se trouve une icône de filtre ![](../../images/icons/icon_filter.png ':size=20'). Cliquez dessus pour afficher des options de filtrage avancées permettant de définir des conditions supplémentaires selon les trois éléments suivants :

- **Propriété** : menu déroulant dans lequel vous choisissez le champ sur lequel effectuer le filtrage.
- **Type de correspondance** : menu déroulant qui vous permet de choisir comment faire correspondre la valeur (`equals`, `contains` ou `NOT`).
- **Valeur** : saisissez ou sélectionnez la valeur à faire correspondre, selon la propriété sélectionnée.

![filter_customer.png](./screenshots/filter_customer.png ':size=400' )

Vous pouvez appuyer sur le bouton `+` pour ajouter plusieurs filtres.


> [!TIP]
> Vous pouvez actualiser la liste des clients en appuyant sur l’icône d’actualisation ![](../../images/icons/icon_reload.png ':size=20') en haut de la page.

### Détails du client

Cliquez sur la ligne correspondant à un client pour ouvrir une vue détaillée contenant des informations supplémentaires.

Vous obtenez un aperçu des ressources créées, de l’activité récente et des appareils en attente d’approbation :

![overview_customer.png](./screenshots/overview_customer.png ':size=700')

> [!NOTE]
> Un client qui vient d’être créé n’a pas encore de ressources à afficher.

Si aucun contrôleur cloud n’est démarré, un avertissement vous indique que vous devez en démarrer un pour activer la connectivité SASE :

![warning_cloudcontroller.png](./screenshots/warning_cloudcontroller.png ':size=600')

![start_networkcontroller.png](./screenshots/start_networkcontroller.png ':size=600')

### Modifier un client
Vous pouvez modifier un client en cliquant sur l’icône de modification ![](../../images/icons/icon_edit.png ':size=20') de sa ligne.

![edit_customer.png](./screenshots/edit_customer.png ':size=350')

> [!CAUTION]
> Vous serez averti que le changement de partenaire supprimera tous les rôles de consultant en sécurité actuels.



### Supprimer un client

Vous pouvez supprimer un client en cliquant sur l’icône de suppression ![](../../images/icons/icon_delete.png ':size=20') de sa ligne.

> [!WARNING]
> Toutes les ressources du client seront supprimées lors de sa suppression. Cette opération est irréversible.

Un avertissement s’affichera avant la suppression définitive du client :

![delete_customer.png](./screenshots/delete_customer.png ':size=400') 

<!-- Lorsque `Provision Cloud Controller` est encore activé, un avertissement s’affiche et vous ne pourrez pas supprimer le client :

![provisioned_nc.png](./screenshots/provisioned_nc.png ':size=250') -->
