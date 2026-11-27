# Connexion automatique à Windows avec Microsoft Entra ID

Jimber SASE utilise le nom principal (UPN) de l’utilisateur Windows connecté et l’ID de l’appareil Entra pour vérifier si l’utilisateur peut se connecter à l’entreprise. L’administrateur configure l’entreprise et les groupes une seule fois. Chaque utilisateur doit **ouvrir Jimber SASE manuellement une fois après l’installation**.

## Configurer l’entreprise

1. Dans **Entreprise > Domaines**, enregistrez la partie de chaque UPN prévu qui suit le caractère `@`. Par exemple, enregistrez `example.com` pour `alex@example.com`. Jimber utilise le nom de connexion Windows, qui peut différer de l’alias de messagerie de l’utilisateur. [Domaines de l’entreprise](/company/domains/domains.md)
2. Dans le locataire Microsoft Entra de l’entreprise, créez une inscription d’application pour l’intégration. Accordez-lui les autorisations Microsoft Graph **Application** `Group.Read.All` et `User.Read.All` pour la synchronisation, ainsi que `Device.Read.All` pour la connexion automatique. Accordez le consentement administrateur à l’échelle du locataire. Notez l’ID de l’annuaire (locataire), l’ID de l’application (client) et la **valeur** du secret client, ainsi que sa date d’expiration. [Guide d’inscription d’une application Entra](/advanced/entraid/entraid.md)
3. Dans **Entreprise > Intégrations > Microsoft Entra ID**, saisissez ces trois identifiants et le **groupe SASE**. Dans Entra, placez les groupes à synchroniser dans ce groupe parent et ajoutez les utilisateurs aux groupes membres. Sélectionnez **Tester la synchronisation**, activez **Activer la synchronisation** et appliquez les paramètres. Ce test vérifie l’accès à l’annuaire. La vérification Windows ci-dessous teste l’accès à l’appareil pour un utilisateur admissible. Si la synchronisation Active Directory est déjà activée, les commandes Entra sont désactivées. Coordonnez tout changement de source d’annuaire avec votre administrateur. [Intégrations de l’entreprise](/company/integrations/integrations.md)
4. Dans **Entreprise > Configuration > Authentification**, activez **Microsoft** et enregistrez. Dans **Entreprise > Utilisateurs** et **Entreprise > Groupes**, vérifiez que l’UPN actuel de l’utilisateur est présent, que le compte est activé et que l’appartenance attendue aux groupes a été synchronisée.
5. Dans **Sécurité > Configuration de groupe**, modifiez l’un des groupes de l’utilisateur, activez **Connexion automatique** et enregistrez. Un utilisateur doit disposer d’au moins un groupe avec ce paramètre activé. [Configuration de groupe](/rules/groupconfiguration/groupconfiguration.md)

## Démarrer l’agent Windows

1. Connectez-vous à un appareil Windows **joint à Entra** en tant qu’utilisateur de l’entreprise concerné. Dans le locataire Entra de l’entreprise, le type de jonction de l’appareil doit être **Microsoft Entra joined** et cet UPN doit figurer parmi les utilisateurs enregistrés de l’appareil. Signal vérifie le type de confiance Graph `AzureAd`. La jonction hybride et l’inscription au lieu de travail ne satisfont pas à cette vérification.
2. Installez l’agent Windows. Dans le menu **Démarrer** de l’utilisateur connecté, **ouvrez Jimber SASE manuellement une fois**. Cela démarre l’icône dans la zone de notification de la session de cet utilisateur et crée sa clé d’appareil Jimber au premier lancement.
3. Si la clé d’appareil ne possède aucune session existante, l’icône dans la zone de notification ouvre la page de connexion Microsoft. Répondez aux demandes éventuelles, y compris l’authentification multifacteur, puis vérifiez l’icône Jimber dans la zone de notification. Si l’approbation de l’appareil est en attente, demandez à l’administrateur Jimber de l’approuver sous **Appareils > Appareils utilisateur**. Lorsque la clé dispose déjà d’une session et que les vérifications aboutissent, l’icône dans la zone de notification ignore la connexion dans le navigateur.

## Vérifier depuis le bureau de l’utilisateur concerné

Ouvrez une fenêtre PowerShell standard dans la même session Windows que celle de l’icône dans la zone de notification. Exécutez :

```powershell
whoami /upn
dsregcmd /status | Select-String '^\s*(AzureAdJoined|DomainJoined|WorkplaceJoined|DeviceId|TenantId|DeviceAuthStatus|AzureAdPrt)\s*:'
```

Vérifiez l’UPN complet et son suffixe, les ID du locataire et de l’appareil, ainsi que `AzureAdJoined : YES`. `DeviceAuthStatus : SUCCESS` signifie qu’Entra reconnaît un appareil activé. `AzureAdPrt : YES` signifie que cette session Windows possède un jeton d’actualisation principal Entra. Si `whoami /upn` échoue, l’icône dans la zone de notification vérifie également les champs du compte dans `dsregcmd /status`. Le diagnostic affiche la valeur qu’il sélectionne. [Documentation de référence de Microsoft sur dsregcmd](https://learn.microsoft.com/en-us/entra/identity/devices/troubleshoot-device-dsregcmd)

Pour vérifier le service Jimber de production et afficher un résumé à communiquer au support, exécutez :

```powershell
& ([scriptblock]::Create((irm https://debug.jimber.io/win-entra)))
```

Le diagnostic envoie une requête `POST https://sase.jimber.io/api/v1/autologin` contenant l’UPN Windows (`email`), le `deviceId` Entra et le `publicKey` Jimber. Une clé vide permet tout de même de vérifier l’admissibilité. Cette vérification ne connecte pas l’utilisateur et n’inscrit pas l’appareil. Copiez la sortie du terminal dans votre demande d’assistance Jimber. Elle comprend les identifiants du compte et de l’appareil, l’heure UTC, la requête réelle ou un aperçu local, ainsi que la réponse du serveur. [Diagnostics Windows](https://debug.jimber.io/windows)

| Résultat                                         | Mesure à prendre                                                                                                                                                                                                                   |
| ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Aperçu local uniquement                       | Consultez le résultat local. Exécutez l’outil en tant qu’utilisateur Windows concerné et vérifiez la jonction de l’appareil, l’UPN et l’ID de l’appareil.                                                                          |
| Entreprise introuvable ou non configurée       | Comparez le suffixe de l’UPN actuel avec **Entreprise > Domaines** et vérifiez les paramètres d’intégration Entra de l’entreprise.                                                                                                  |
| Aucun groupe activé pour la connexion automatique | Le domaine a été associé, mais Signal a ignoré Graph. Vérifiez l’UPN synchronisé, l’appartenance au groupe et le paramètre **Connexion automatique**. Un utilisateur non synchronisé produit le même résultat.                    |
| Échec de la requête d’appareil ou privilèges insuffisants | Ouvrez **Supervision > Activité**. Dans **Activité récente**, faites correspondre **Connexion automatique de l’utilisateur** à l’heure du rapport et à l’UPN. Vérifiez le locataire configuré, l’ID de l’application, la valeur et la date d’expiration du secret, ainsi que le consentement administrateur pour les autorisations d’application Graph. |
| Appareil ou utilisateur enregistré refusé      | Recherchez l’ID de l’appareil indiqué dans le locataire associé. Vérifiez le type de jonction et l’UPN actuel de l’utilisateur enregistré.                                                                                           |
| Vérifications Graph réussies                   | Signal a lu l’appareil et trouvé une correspondance avec un utilisateur enregistré. Si l’icône dans la zone de notification ne parvient toujours pas à se connecter, vérifiez sa connexion dans le navigateur, la clé d’appareil de l’utilisateur Windows et l’état d’approbation de l’appareil. |

Après un changement d’UPN, connectez-vous à Windows à l’aide de **Autre utilisateur** et du nouvel UPN complet. Comparez **UPN de l’icône** dans la sortie avec l’utilisateur de l’entreprise synchronisé. **E-mail lors de la jonction** peut encore afficher l’adresse d’origine. [Conseils de Microsoft sur le changement d’UPN](https://learn.microsoft.com/en-us/entra/identity/hybrid/connect/howto-troubleshoot-upn-changes#managed-devices-issues)
