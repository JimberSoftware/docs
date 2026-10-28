# ![](../../images/menu/menu_packetinspection.png ':size=25') Accès effectif

### Exemple 1 : politique correspondante

Après avoir installé plusieurs politiques de pare-feu, il est recommandé d’inspecter les accès résultant des politiques de pare-feu actives, car le routage, la disponibilité des points de terminaison, le mode sécurisé et l’état du contrôleur peuvent encore affecter la connexion réelle.

![effective_access.png](./screenshots/effective_access.png ':size=700')

1. Sélectionnez l’entité à inspecter (utilisateurs, groupes, serveurs ou appareils)
 
 ![select_entity.png](./screenshots/select_entity.png ':size=400')
   
2. Choisissez le sens : sortant, entrant
3. Vous pouvez également sélectionner une destination, un protocole (TCP, UDP ou ICMP) et un port
4. Cliquez sur `Inspect access` pour afficher les résultats

 ![results_effective_access.png](./screenshots/results_effective_access.png ':size=600')

>[!TIP]
>Vous pouvez vérifier la politique qui affecte l’entité choisie en cliquant sur `View policy` à la fin de sa ligne. 

### Exemple 2 : aucune politique correspondante

   ![no_match.png](./screenshots/no_match.png ':size=600')
