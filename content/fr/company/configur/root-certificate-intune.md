File: company/configur/root-certificate-intune.md

# Déployer le certificat racine Jimber sur macOS avec Microsoft Intune

Utilisez un profil de certificat approuvé Microsoft Intune pour installer le certificat d’autorité racine Jimber de votre entreprise sur les appareils macOS gérés. Vous éviterez ainsi d’installer et d’approuver manuellement le certificat sur chaque appareil.

## Avant de commencer

Vous devez disposer des autorisations nécessaires pour gérer votre entreprise dans Jimber SASE et créer des profils de configuration dans le centre d’administration Microsoft Intune.

1. Dans Jimber SASE, ouvrez **Entreprise**, puis **Configuration**.
2. Dans la carte **Isolation réseau**, sélectionnez **Télécharger le certificat**.
3. Vérifiez que le fichier téléchargé porte l’extension `.cer`. Le fichier contient uniquement le certificat public. Ne téléversez ni ne distribuez jamais de clé privée.

## Créer le profil de certificat approuvé

1. Dans le [centre d’administration Microsoft Intune](https://intune.microsoft.com), accédez à **Appareils** > **macOS** > **Configuration**.
2. Sélectionnez **Créer**, puis **Nouvelle stratégie**.
3. Pour **Plateforme**, sélectionnez **macOS**.
4. Pour **Type de profil**, sélectionnez **Modèles**.
5. Pour **Modèle**, sélectionnez **Certificat approuvé**.
6. Saisissez un nom et une description reconnaissables pour le profil.
7. Téléversez le certificat racine téléchargé depuis Jimber SASE. Intune accepte les fichiers `.cer`, `.crt` et `.der` contenant un certificat X.509 encodé en DER ou en Base64.
8. Attribuez le profil aux groupes d’appareils ou d’utilisateurs concernés.
9. Vérifiez le profil et sélectionnez **Créer**.

Intune installe le certificat dans le trousseau système de macOS en tant que racine approuvée sur les appareils concernés.

## Vérifier le déploiement

Ouvrez le profil dans Intune et consultez **État de l’appareil** et **État de l’utilisateur**. Résolvez les erreurs d’attribution ou d’installation avant la date d’expiration indiquée dans Jimber SASE.

Lorsque Jimber vous informe d’une expiration prochaine, planifiez le changement avant de sélectionner **Demander un nouveau certificat**. La confirmation de cette action remplace immédiatement le certificat. Téléchargez le nouveau certificat et mettez immédiatement à jour le profil Intune afin que les appareils gérés retrouvent ou conservent leur connectivité.
