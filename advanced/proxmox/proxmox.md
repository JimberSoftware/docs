# Creating a proxmox cluster over Network Isolation

Using Jimber Network Isolation in combination with Proxmox, it is perfectly possible to create a cluster of the encrypted connection. This cluster can be expanded over multiple locations, beware that you need fast connections if you want features like High Availability to work. Always test out the whole setup before applying in production systems.

## Install Jimber Network Isolation
Using CLI, install the Jimber client on all hypervisors you want to add to your cluster. For this example we are using 2 hypervisors:

- HVBruges, Network Isolation IP 198.18.0.25
- HVGhent, Network Isolation IP 198.18.0.26

## Setting the access rights
Be sure following access rights are enabled for communication between the hypervisors:

| Service                        | Port Range       | Protocol |
|------------------------------- |----------------- |--------- |
| Proxmox VE API/Web Interface   | 8006             | TCP      |
| SSH                            | 22               | TCP      |
| Corosync                       | 5404-5405        | UDP      |
| PVE Cluster File System        | 60000-60050      | TCP      |
| VNC                            | 5900-5999        | TCP      |
| SPICE                          | 3128             | TCP      |
| Ceph Monitor                   | 6789             | TCP      |
| Ceph OSDs                      | 6800-7300        | TCP      |
| Proxmox Backup Server          | 8007             | TCP      |
| Live Migration                 | 8002-8003        | TCP      |

You can create a service with these ports and protocols, add both of the hypervisors to a group and allow the service from the group to both of the hypervisors. You can test connectivity by opening an SSH session for one hypervisor to another.

## Example configuration

First we create the cluster on the HVBruges machine
```
pvecm create jimberpvec --link0 address=198.18.0.25
```

Next we join from the HVGhent machine using the add command:
```
pvecm add proxmox-staging.jimber.io --link0 address=198.18.0.26
```

When certain protocols are not allowed, dropped packets will appear in the activity log. Adjust the protocol configuration accordingly.

## Troubleshooting
If anything goes wrong, you can remove any of the HV's from the cluster one sided using following commands:

```
systemctl stop pve-cluster
systemctl stop corosync
pmxcfs -l

rm /etc/pve/corosync.conf
rm /etc/corosync/*
killall pmxcfs

systemctl start pve-cluster

```