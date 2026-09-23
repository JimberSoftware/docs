# ![native_networks](../images/menu/menu_virtualinterfaces.png ':size=25') Virtual Interfaces

A virtual interface is a software-based, logical network connection that acts as a distinct endpoint without needing its own dedicated physical hardware port.

### Create Virtual Interface

![create_virtual_interface.png](./screenshots/create_virtual_interface.png ':size=800')


- **Interface**
    - Choose type of interface. For the moment you can only choose for IPSec.  
    - Choose a network controller (required).
    - Enter the local endpoint and remote endpoint (required).
- **Security**
    - Choose IKE settings. For the moment you can only choose for IKEv2.
    - Choose IKE proposal.
    - Choose authentication: Pre-Shared Key or Certificate-based.
    - Search ESP Proposals or enter a custom proposal (required).
- **Authentication**
    - If authentication is Pre-Shared Key:
        - Enter the Local ID and the remote ID.
        - Enter the pre-shared key (required).
    - If authentication is Certificate-based:
        - Enter the local ID.
        - Enter the remote ID (required).
        - Paste CA certificate (required).
        - Paste local certificate (required).
        - Paste private key (required).



### Filter Virtual Interfaces

You can search the list of interfaces using the search box at the top of the page. This helps you quickly find and manage the interface you're looking for.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`EQUALS`, `CONTAINS`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_interface.png](./screenshots/filter_interface.png ':size=500')

To add multiple filters you can press the filter icon ![](../../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

> [!TIP]
> You can refresh the list of interfaces by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### Virtual Interface Details

Clicking on the corresponding strip of the virtual interface opens a new window with two tabs.

The first tab shows the details of the virtual interface:

![details_interface.png](./screenshots/details_interface.png ':size=400')

The second tab opens a log file:

![virtual_interface_log.png](./screenshots/virtual_interface_log.png ':size=400')


### Edit Virtual Interface

A virtual interface can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in its row.

![update_virtual_interface.png](./screenshots/update_virtual_interface.png ':size=500')


All options are the same as when creating a virtual interface.

### Delete Virtual Interface

![delete_virtual_interface.png](./screenshots/delete_virtual_interface.png ':size=300')