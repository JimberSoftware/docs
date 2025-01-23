# Services

Within our platform, a "Service" refers to a digital service that is accessible by a user. These services can encompass a variety of applications and resources, including websites/web portals, remote desktops, and internal CRMs (Customer Relationship Management systems). 

Once a service is attributed to a group and a destination, the service entries will appear in the "Security Panel" of the user.
The Security Panel can be reached by clicking on the Jimber Network Isolation icon in the taskbar:

![security_panel.png](/security_panel.png ':size=300')

A security panel with multiple services can look like this:

![security_panel_overview.png](/security_panel_overview.png ':size=800')


## Create Service

To create a service into the platform, click on the `Create new` button

![create_new.png](/create_new.png)

prominently located at the upper right corner of the interface.


![create_service.png](/create_service.png ':size=800')


You can choose a name for the service. Next step is creating a new service entry by clicking on 'Create new service entry'.

<!-- ![create_new_entry.png](/create_new_entry.png ':size=900x') -->

You can create your service by entering a description, selecting what it should do and the URL or Path the service will need to complete the action. 

<!-- ![create_access_rules.png](/create_access_rules.png ':size=900x') -->

To add an access rule, write a description, define start and end ports and choose the protocol through which the service will communicate.

> [!WARNING]
> Don't forget to submit the service, by clicking on the `Submit service` button ![submit_service.png](/submit_service.png ':size=100') prominently located at the upper right corner of the interface.

In any case, you will receive a warning if the service was not submitted:

![unsaved_changes.png](/unsaved_changes.png ':size=400')


After creating the service you can switch to [Attribute Services](/./rules/attribute_services/attribute_services.md) to specify the details of the service.


## Edit Service
Services can be edited by clicking on the yellow pencil icon next to their name 
![icon_edit.png](/icon_edit.png ':size=35').

The same window appears as when creating a service. You can separately modify or delete service inputs or access rules.


## Delete Service

Services can be removed by clicking on the red trash bin icon next to their name 
![icon_delete.png](/icon_delete.png ':size=35').

 You will receive a warning before the service is permanently deleted:
 
![deleting_service.png](/deleting_service.png ':size=500x150')

