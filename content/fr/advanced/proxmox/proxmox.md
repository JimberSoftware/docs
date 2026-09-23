# Création d’un cluster Proxmox via Jimber SASE

En combinant Jimber SASE et Proxmox, il est tout à fait possible de créer un cluster sur la connexion chiffrée. Ce cluster peut être étendu à plusieurs emplacements. Attention : vous avez besoin de connexions rapides pour que des fonctionnalités comme la haute disponibilité fonctionnent. Testez toujours l’ensemble de la configuration avant de l’appliquer dans des systèmes de production.

## Installer Jimber SASE
À l’aide de la CLI, installez le client Jimber sur tous les hyperviseurs que vous souhaitez ajouter à votre cluster. Dans cet exemple, nous utilisons 2 hyperviseurs :

- HVBruges, adresse IP NIAC 198.18.0.25
- HVGhent, adresse IP NIAC 198.18.0.26

## Définir les droits d’accès
Assurez-vous que les droits d’accès suivants sont activés pour permettre la communication entre les hyperviseurs :

| Service                        | Plage de ports   | Protocole |
|------------------------------- |----------------- |--------- |
| API/interface Web de Proxmox VE | 8006             | TCP      |
| SSH                            | 22               | TCP      |
| Corosync                       | 5404-5405        | UDP      |
| Système de fichiers du cluster PVE | 60000-60050      | TCP      |
| VNC                            | 5900-5999        | TCP      |
| SPICE                          | 3128             | TCP      |
| Moniteur Ceph                  | 6789             | TCP      |
| OSD Ceph                       | 6800-7300        | TCP      |
| Proxmox Backup Server          | 8007             | TCP      |
| Migration à chaud               | 8002-8003        | TCP      |

Vous pouvez créer un service avec ces ports et protocoles, ajouter les deux hyperviseurs à un groupe et autoriser le service du groupe vers les deux hyperviseurs. Vous pouvez tester la connectivité en ouvrant une session SSH d’un hyperviseur vers l’autre.

## Exemple de configuration

Nous créons d’abord le cluster sur la machine HVBruges
```
pvecm create jimberpvec --link0 address=198.18.0.25
```

Nous rejoignons ensuite le cluster depuis la machine HVGhent à l’aide de la commande add :
```
pvecm add proxmox-staging.jimber.io --link0 address=198.18.0.26
```

Lorsque certains protocoles ne sont pas autorisés, des paquets abandonnés apparaissent dans le journal d’activité. Ajustez la configuration des protocoles en conséquence.

## Dépannage
En cas de problème, vous pouvez retirer un HV du cluster d’un seul côté à l’aide des commandes suivantes :

```
systemctl stop pve-cluster
systemctl stop corosync
pmxcfs -l

rm /etc/pve/corosync.conf
rm /etc/corosync/*
killall pmxcfs

systemctl start pve-cluster

```
