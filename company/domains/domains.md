# ![](../../images/menu/menu_domains.png ':size=25') Domains

Domains play a crucial role in the configuration process of your `Jimber SASE Platform` settings. They provide the basis for setting up users and administrators, allowing efficient management of your network connections and changes.

> [!WARNING]
> Start by registering all domains your organization currently uses. This is a necessary first step before creating users and administrative accounts.

For example, to create a user like 'jef@jimber.test', you must first register the 'jimber.test' domain. This highlights the role of domains in setting up your network.

![domains.png](./screenshots/domains.png  ':size=800')

### Create Domains

To establish a new domain, simply click on the `+ Create new` button located at the upper right corner of the interface.

![create_new_domain.png](./screenshots/create_domain.png  ':size=500x200')

### Deleting Domains

Domains can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> A domain cannot be removed if there are users associated with it. Ensure to first disassociate all linked users from the domain under the `Users` section.

You will receive a warning before the domain is permanently deleted:

![delete-domain.png](./screenshots/delete_domain.png ':size=500')

A warning appears in the top right corner if not all users have been deleted:

![warning.png](./screenshots/warning.png)

