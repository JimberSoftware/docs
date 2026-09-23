# Déployer un contrôleur réseau dans Azure

Ce guide vous accompagne dans le déploiement d’un contrôleur réseau Jimber SASE sur Microsoft Azure.

## Prérequis

Procurez-vous les éléments suivants :

- Un abonnement Azure.
- Un fichier VHD de contrôleur réseau Jimber SASE

> [!Note]
> Les spécifications minimales du contrôleur réseau sont les suivantes :
> 
> - Disque dur de 25 Go
> - 2 CPU
> - 4 Go de RAM
> 
> **Tailles de machines virtuelles recommandées dans Azure :**
> - Standard_B2s (2 vCPU, 4 Go de RAM)
> - Standard_B2ms (2 vCPU, 8 Go de RAM)
> - Standard_D2s_v3 (2 vCPU, 8 Go de RAM)

## Télécharger le fichier VHD du contrôleur réseau

Avant de créer des ressources dans Azure, vous devez télécharger le fichier VHD du contrôleur réseau Jimber SASE.

1. Dans votre navigateur web, accédez à [https://sase.jimber.io/downloads](https://sase.jimber.io/downloads).

![download-vhd.png](./screenshots/download-vhd.png ':size=600')

2. Téléchargez le fichier VHD Azure du contrôleur réseau.

3. Enregistrez le fichier VHD à un emplacement de votre ordinateur local où vous pourrez facilement le retrouver pour le charger dans Azure au cours des étapes suivantes.

## Créer un groupe de ressources

Dans Azure, un groupe de ressources est un dossier logique qui regroupe toutes les ressources que vous créez, notamment les disques, les comptes de stockage, les machines virtuelles et les groupes de sécurité réseau. Si votre organisation limite la possibilité de gérer les groupes de ressources, contactez l’équipe d’administration Azure pour obtenir de l’aide.

Pour créer un groupe de ressources, procédez comme suit :

1. Connectez-vous à Azure avec un compte autorisé à créer un groupe de ressources.

2. Dans l’interface Azure, sélectionnez **Groupes de ressources** dans le menu des services Azure en haut de l’écran.

![resource_group.png](./screenshots/resource_group.png ':size=600')

3. Sélectionnez le bouton **+ Créer** en haut à gauche de l’écran Groupes de ressources.

![create_resource_group.png](./screenshots/create_resource_group.png ':size=600')

4. Renseignez les champs de l’écran Créer un groupe de ressources qui s’ouvre.

![resource_group_fields.png](./screenshots/resource_group_fields.png ':size=600')

5. Sélectionnez **Vérifier et créer**.

6. Vérifiez que les informations du groupe de ressources sont correctes, puis sélectionnez **Créer**.

## Créer un compte de stockage

Pour créer un compte de stockage, procédez comme suit :

1. Revenez à l’écran d’accueil Azure et sélectionnez **Comptes de stockage** dans le menu des services Azure en haut de l’écran.

2. Sélectionnez le bouton **+ Créer** en haut à gauche de l’écran Comptes de stockage qui s’ouvre.

3. Dans l’écran Créer un compte de stockage, renseignez les informations suivantes :

   - Pour **Groupe de ressources**, sélectionnez le menu déroulant, puis le groupe de ressources que vous avez créé lors de la procédure précédente.
   
   > [!Note]
   > Si votre groupe de ressources n’apparaît pas, vous pouvez le rechercher en saisissant son nom dans le champ Sélectionner un groupe existant en haut de la liste des groupes de ressources existants.

   - Le **Nom du compte de stockage**, qui doit comporter entre 3 et 24 caractères et ne contenir que des lettres minuscules et des chiffres.

   - (Facultatif) Indiquez l’**Emplacement** du compte de stockage, qui peut être différent de celui du groupe de ressources.

4. Sélectionnez **Vérifier et créer**.

5. Vérifiez que les informations de stockage sont correctes, puis sélectionnez **Créer**.

   Le compte de stockage est déployé et ajouté à la liste de l’écran Accueil, Comptes de stockage.

6. Sélectionnez votre nouveau compte de stockage dans la liste. Vous devez sélectionner le bouton **Actualiser**.

7. Dans la section Stockage des données du volet de navigation à gauche, sélectionnez **Conteneurs**. Le volet Conteneurs s’ouvre.

8. Sélectionnez **+ Conteneur** pour créer un conteneur de stockage dans le compte de stockage. Le panneau Nouveau conteneur s’ouvre à droite de l’écran.

9. Dans le panneau Nouveau conteneur, saisissez un **Nom** pour le nouveau conteneur, puis sélectionnez **Créer**.

   > [!Note]
   > Le nom du conteneur ne peut contenir que des lettres minuscules, des chiffres et des tirets. Il doit commencer par une lettre ou un chiffre. Chaque tiret doit être précédé et suivi d’un caractère autre qu’un tiret. Le nom doit également comporter entre 3 et 63 caractères.

10. Dans le panneau Conteneurs, repérez votre nouveau conteneur et sélectionnez son nom (et non la case à cocher située à sa gauche).

11. Dans le panneau qui s’ouvre, sélectionnez l’icône **Charger** en haut à gauche, puis sélectionnez l’image VHD du contrôleur réseau Jimber SASE pour la charger dans Azure.

## Créer un disque managé

Ensuite, créez un disque dans Azure.

Procédez comme suit :

1. Saisissez « disks » dans le champ de recherche en haut du portail Azure.

2. Sélectionnez **Disques** dans les résultats de recherche.

3. Sur la page Disques, sélectionnez le bouton **+ Créer** pour ajouter un nouveau disque.

![create-disk-1.png](./screenshots/create-disk-1.png ':size=600')

4. Sous **Détails du projet**, sélectionnez un groupe de ressources existant dans le menu déroulant.

5. Sous **Détails du disque**, renseignez les informations suivantes :

   - Le **Nom du disque**.

   - Pour **Région**, sélectionnez le même emplacement que celui de votre compte de stockage. Vous devez créer le disque dans le même emplacement que le compte de stockage dans lequel vous avez chargé votre fichier VHD.

6. Pour indiquer le type et les propriétés de la source du disque, procédez comme suit :

   - Dans le menu déroulant Type de source, sélectionnez **« Blob de stockage »**. D’autres commandes contextuelles s’affichent.

   - Dans le champ **Blob source**, utilisez le lien Parcourir pour sélectionner le fichier VHD. Sélectionnez le compte de stockage, puis le conteneur, puis le fichier VHD, et enfin **Sélectionner**.

![create-disk-select-blob1.png](./screenshots/create-disk-select-blob1.png ':size=600')

![create-disk-select-blob-2.png](./screenshots/create-disk-select-blob-2.png ':size=600')

![create-disk-select-blob-3.png](./screenshots/create-disk-select-blob-3.png ':size=600')

![create-disk-select-blob-4.png](./screenshots/create-disk-select-blob-4.png ':size=600')

   - Pour **Type de système d’exploitation**, sélectionnez **« Linux »**.

   - Vérifiez que la valeur de la commande Génération de machine virtuelle (qui s’est affichée lorsque vous avez sélectionné Linux à l’étape précédente) est **« Gen 1 »**.

7. Pour modifier la taille par défaut du disque (1 024 Gio), procédez comme suit :

   - Sélectionnez le lien **Modifier la taille**. La page Sélectionner une taille de disque s’ouvre.

   - Vérifiez que la valeur indiquée dans le menu déroulant Référence du disque est **« SSD Premium »**.

   - Sélectionnez une taille de disque dans la liste ou indiquez une taille personnalisée d’au moins **80 Gio**.

   - Sélectionnez **OK**

![create-disk-4.png](./screenshots/create-disk-4.png ':size=600')

8. Sélectionnez **Vérifier et créer**.

![create-disk-5.png](./screenshots/create-disk-5.png ':size=600')

9. Vérifiez que vos paramètres sont corrects et, si c’est le cas, sélectionnez **Créer**. Sinon, sélectionnez le bouton **Précédent** pour revenir en arrière et apporter les modifications nécessaires.

## Créer la machine virtuelle

Pour créer une machine virtuelle de contrôleur réseau dans Azure, procédez comme suit :

1. Revenez à la page Disques et sélectionnez votre disque. Un nouveau volet s’affiche avec l’option **+ Créer une machine virtuelle**.

![create-vm-1.png](./screenshots/create-vm-1.png ':size=600')

2. Sélectionnez **+ Créer une machine virtuelle**. Le panneau Créer une machine virtuelle s’affiche.

![create-vm-2.png](./screenshots/create-vm-2.png ':size=600')

3. Dans l’onglet **Informations de base**, saisissez un **Nom** pour votre machine virtuelle.

![create-vm-3.png](./screenshots/create-vm-3.png ':size=600')

4. Pour **Groupe de ressources**, sélectionnez **« Utiliser existant »**, puis sélectionnez votre groupe de ressources.

5. L’option **Emplacement** est désactivée, car elle est déterminée par l’emplacement du compte de stockage du disque.

6. Sélectionnez une taille. Pour plus d’informations, consultez la section Exigences d’installation. Sélectionnez la taille, puis le bouton **Sélectionner** en bas de la page.

7. Sélectionnez **Vérifier + créer**.

![create-vm-4.png](./screenshots/create-vm-4.png ':size=600')

8. Vérifiez les paramètres sur la page Récapitulatif, puis sélectionnez **Créer** pour appliquer vos modifications.

   Le déploiement commence. Pour suivre sa progression, sélectionnez l’icône en forme de cloche **Notifications** en haut à droite.

## Configurer les règles de port

Pour autoriser le trafic réseau vers le contrôleur réseau, configurez des règles de groupe de sécurité réseau (NSG) pour les ports 8080 et 38250.

1. Accédez à votre machine virtuelle dans le portail Azure, puis sélectionnez **Mise en réseau** dans le menu de navigation de gauche.

2. Sélectionnez le nom du **Groupe de sécurité réseau** associé à votre machine virtuelle.

3. Dans la section Paramètres, sélectionnez **Règles de sécurité entrantes**.

![add-port-rules-1.png](./screenshots/add-port-rules-1.png ':size=600')

4. Sélectionnez **+ Ajouter** pour créer une nouvelle règle entrante pour le port 8080 :

![add-port-rules-2.png](./screenshots/add-port-rules-2.png ':size=600')

   - **Source** : **« N’importe quelle »**
   - **Plages de ports sources** : **« * »**
   - **Destination** : **« N’importe quelle »**
   - **Plages de ports de destination** : **« 8080 »**
   - **Protocole** : **« TCP »**
   - **Action** : **« Autoriser »**
   - **Priorité** : saisissez un nombre unique (par exemple, **1000**)
   - **Nom** : saisissez un nom descriptif (par exemple, **« Allow-HTTP-8080 »**)

5. Sélectionnez **Ajouter** pour créer la règle.

6. Répétez les étapes 4 et 5 pour créer une deuxième règle pour le port 38250 avec les paramètres suivants :

   - **Plages de ports de destination** : **« 38250 »**
   - **Priorité** : saisissez un nombre différent (par exemple, **1010**)
   - **Nom** : saisissez un nom descriptif (par exemple, **« Allow-NetworkController-38250 »**)

7. Vérifiez que les deux règles apparaissent dans la liste Règles de sécurité entrantes avec l’état « Réussi ».

![add-port-rules-3.png](./screenshots/add-port-rules-3.png ':size=600')

## Installation du contrôleur réseau

Une fois la machine virtuelle déployée et les règles de port configurées, terminez l’installation du contrôleur réseau :

1. Récupérez l’adresse IP publique de votre machine virtuelle dans le portail Azure :

   - Accédez à votre machine virtuelle dans le portail Azure en recherchant son nom dans la barre de recherche en haut de l’écran ou en sélectionnant **Machines virtuelles** dans le menu des services Azure.

   - Sélectionnez votre machine virtuelle dans la liste pour ouvrir sa page Vue d’ensemble.

   - Sur la page Vue d’ensemble de la machine virtuelle, repérez le champ **Adresse IP publique** dans la section **Informations essentielles**. Il s’agit de l’adresse IP que vous utiliserez pour accéder à l’interface web du contrôleur réseau.

   - Copiez cette adresse IP pour l’utiliser lors des étapes suivantes.

2. Utilisez l’adresse IP affichée pour terminer l’installation du contrôleur réseau sur la Plateforme Jimber SASE en la renseignant dans le champ Adresse du point de terminaison.

   > [!Note]
   > Des instructions détaillées sur la création d’un contrôleur réseau sur site sont disponibles [ici](/./devices/networkcontrollers/networkcontrollers.md).

3. Dans votre navigateur web, accédez à `http://<your-vm-public-ip>:8080` pour ouvrir l’interface web du contrôleur réseau.

![nc-setup-1.png](./screenshots/nc-setup-1.png ':size=600')

4. Connectez-vous à l’interface web en utilisant `jimber` comme mot de passe.

![nc-setup-2.png](./screenshots/nc-setup-2.png ':size=600')

5. Définissez un nouveau mot de passe.

   > [!Warning]
   > Le nouveau mot de passe doit comporter au moins **16** caractères !

![nc-setup-3.png](./screenshots/nc-setup-3.png ':size=600')

6. Sélectionnez la configuration réseau appropriée, puis cliquez sur le bouton de test de connexion. Si le test réussit, vous pouvez passer à l’étape suivante.

   > [!Note]
   > En cas d’échec, vérifiez que le contrôleur réseau dispose d’une connexion Internet active et que la configuration de l’interface web est correcte. Vérifiez également que les règles de port (8080 et 38250) sont correctement configurées dans le groupe de sécurité réseau.

![nc-setup-4.png](./screenshots/nc-setup-4.png ':size=600')

7. Dans la Plateforme Jimber SASE, copiez le jeton du contrôleur réseau que vous venez de créer. Vous pouvez trouver ce jeton en modifiant le contrôleur réseau à l’aide du crayon jaune.

8. Collez ce jeton dans la configuration web du contrôleur réseau. Cliquez ensuite sur suivant.

9. Veuillez patienter pendant le test de la connexion.

![nc-setup-5.png](./screenshots/nc-setup-5.png ':size=600')

10. Une fois la connexion établie, un écran de confirmation s’affiche.

11. Vérifiez que votre contrôleur réseau est désormais en ligne sur la Plateforme Jimber SASE, dans la page Contrôleur réseau.
