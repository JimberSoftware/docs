# Intégration d’Active Directory

Dans cette section, vous découvrirez comment intégrer des utilisateurs et des groupes d’un Active Directory à la Plateforme Jimber SASE.

>[!WARNING]
>Pour activer l’intégration d’Active Directory, vous devez disposer d’au moins un contrôleur réseau sur site.

![no_on_premise.png](./screenshots/no_on_premise.png ':size=500')


Vous trouverez [ici](/./advanced/networkcontrollerssetup/SettingUpServer.md) la procédure de configuration d’un contrôleur réseau.



#### Dans Active Directory

Créez un nouvel utilisateur dans AD (par exemple **User1**) et ajoutez-le au groupe AD **Read-Only Domain Controllers** :

![user_in_rodc.png](./screenshots/user_in_rodc.png ':size=500')

> [!IMPORTANT]
> L’utilisateur en lecture seule, User1, permet à SASE de lire Active Directory depuis le contrôleur de domaine.

Définissez le groupe « Read-Only Domain Controllers » comme groupe principal de l’utilisateur.
- Sélectionnez les propriétés du groupe.

![properties_user.png](./screenshots/properties_user.png ':size=300')

  - Ouvrez l’onglet **Membre de**.
  - Sélectionnez le groupe **Read-Only Domain Controllers**.
  - Cliquez sur **Définir comme groupe principal**.

![primary_group.png](./screenshots/primary_group.png ':size=300')

Créez de nouveaux groupes de sécurité globaux, par exemple **JimberSASE_Sync** et **GeneralUsers** :

![new_groups.png](./screenshots/new_groups.png ':size=500')


Ajoutez l’utilisateur AD à synchroniser (par exemple Jack) au groupe GeneralUsers.

Ajoutez le groupe GeneralUsers au groupe JimberSASE_Sync.

![user_in_groups.png](./screenshots/user_in_groups.png ':size=500')


>[!IMPORTANT]
> Ajoutez au groupe GeneralUsers tout autre utilisateur ou groupe que vous souhaitez synchroniser avec la Plateforme SASE.


#### Dans la Plateforme SASE
 
Ouvrez la Plateforme Jimber SASE.


##### 1. Créez un groupe portant le même nom que dans Active Directory ; dans cet exemple, GeneralUsers.

![same_group.png](./screenshots/same_group.png ':size=500')

##### 2. Configurez le redirecteur DNS
   - Accédez à Entreprise > Intégrations
   - Le paramètre de configuration se trouve en haut de la page.
   - Ajoutez ici l’adresse IP d’isolation réseau du contrôleur de domaine.


   ![dnsforwarding.png](./screenshots/dnsforwarding.png ':size=600')

>[!NOTE]
> Le trafic des clients pour lesquels le remplacement DNS est activé est filtré par notre service DNS.
>
> Les requêtes spécifiques au domaine sont toujours résolues par le serveur indiqué dans ce champ.

##### 3. Synchronisation
- Accédez à Entreprise > Intégrations

![integrations.png](./screenshots/integrations.png ':size=600')
<!-- 

On the domain controller, open PowerShell and run these two commands: -->

- Dans le **champ Groupe SASE**, saisissez le nom distinctif du groupe (dans cet exemple : CN=JimberSASE_Sync,CN=Users,DC=domainname,DC=be).
- Dans le **champ Nom d’utilisateur**, saisissez le nom distinctif de l’utilisateur en lecture seule créé précédemment (dans cet exemple : CN=User1,CN=Users,DC=domainname,DC=be).
- Le **mot de passe** est celui de l’utilisateur (dans cet exemple, le mot de passe de User1).
- Choisissez le **contrôleur réseau** approprié.
- Cliquez sur le bouton **Appliquer** pour appliquer les valeurs saisies.

>[!TIP]
>Pour identifier les noms distinctifs appropriés, vous pouvez exécuter les commandes suivantes dans PowerShell :
>
>```bash
>   dsquery group -name JimberSASE_Sync
>```
>```bash
>   dsquery user -name user1
>```



##### 4. Groupe des contrôleurs de domaine

- Accédez à Entreprise > Groupes
- Créez un groupe **Domain Controllers**

![create_group_dc.png](./screenshots/create_group_dc.png ':size=500')

- Ajoutez le contrôleur de domaine à ce nouveau groupe :
    - Accédez à Entreprise > Appareils > Serveurs
    - Modifiez le contrôleur de domaine
    - Ajoutez le groupe **Domain Controllers** à la liste des groupes à l’aide de la liste déroulante.
    - Cliquez sur le bouton **Soumettre** pour appliquer les modifications.

![edit_server_dc.png](./screenshots/edit_server_dc.png ':size=600')

![update_dc.png](./screenshots/update_dc.png ':size=600')


##### 5. Ports

- Accédez à Sécurité > Services
- Cliquez sur le bouton`+ Create new` situé dans le coin supérieur droit de l’interface.
- Cliquez sur le bouton`Load template` en bas de la page.

![template_for_ad.png](./screenshots/template_for_ad.png ':size=600')

- Utilisez le modèle **Active Directory** existant :
  - Sélectionnez le modèle approprié.
  - Cliquez sur le bouton`Apply template` pour appliquer le modèle.


![choose_template.png](./screenshots/choose_template.png ':size=500')



##### 6. Politique basée sur un service

- Accédez à Sécurité > Politiques
- Choisissez `Create new` :


![create_policy_dc.png](./screenshots/create_policy_dc.png ':size=600')

Suivez ces étapes :
- Choisissez un nom pour la politique.
- Choisissez `Add Services` et sélectionnez le service approprié :

![choose_service.png](./screenshots/choose_service.png ':size=500')

- Choisissez `Add sources` et sélectionnez le groupe **Domain Controllers**

![choose_source.png](./screenshots/choose_source.png ':size=500')

  - Choisissez `Add Destinations`. Sélectionnez le contrôleur de domaine.

![choose_destination.png](./screenshots/choose_destination.png ':size=500')




>[!IMPORTANT]
> N’oubliez pas de cliquer sur le bouton`Save` après chaque étape.

>[!TIP]
> Pour trouver facilement les composants appropriés, vous pouvez utiliser la zone de recherche et/ou la liste déroulante des types
>
>![se_type_box.png](./screenshots/se_type_box.png ':size=400').





<!-- You can check whether the synchronization was successful at the users section. -->


Après avoir sélectionné les différents composants, cliquez sur le bouton `Submit` pour appliquer les modifications :

![result_attribute.png](./screenshots/result_attribute.png ':size=600')

Après avoir soumis la politique, vous devriez la trouver dans l’aperçu des `policies`.

![overview_att_policy.png](./screenshots/overview_att_policy.png ':size=800').
