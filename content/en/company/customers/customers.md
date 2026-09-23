# ![](../../images/menu/menu_customers.png ':size=25') Customers
> [!WARNING]
> This *Customers* section is exclusively available for **partners**. If you are an end customer, you will be directly redirected to the ***_<span style="color: darkblue;">Jimber SASE Platform</span>_*** configuration of your company.

In our platform, a **customer** refers to a company intending to use ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Integrators have the capability to manage these customers, ensuring seamless operations and service delivery.

For clarity, consider a scenario where a company named *`Astral Voyage`* wants to use ***_<span style="color: darkblue;">Jimber SASE Platform</span>_***. Then you must first create *`Astral Voyage`* as a customer on the platform before any further configurations or service provisions can occur.

![list_customers.png](./screenshots/list_customers.png ':size=800')

### Create Customer

To incorporate a new customer into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![create_customer.png](./screenshots/create_customer.png ':size=350')

- Following fields are required:
	
    - Name. 
    - Display name. Display name can contain letters and numbers.
    - Primary contact email.


- Options that need to be decided on:

    - Which plan: SASE or ViPN?
    - Toggle on ***Provision Cloud Controller*** when a network controller needs to be provisioned.

- Filling in the website will cause an icon to appear in front of the customer's name.

> [!WARNING]
> Name can only contain letters and numbers. No spaces, special characters, or symbols.
>
> You can however use these characters in the Display name field.




### Filter Customers

You can search the list of customers using the search box at the top of the page. This helps you quickly find and manage the customer you're looking for.


- Use the search box to enter keywords and filter the customer list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![filter_customer.png](./screenshots/filter_customer.png ':size=400' )

You can press the `+` button to add multiple filters.


> [!TIP]
> You can refresh the list of customers by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### Customer Details

Clicking on the corresponding strip of a customer opens a detailed view with additional information.

You get an overview of created assets, recent activity, and devices needing approval:

![overview_customer.png](./screenshots/overview_customer.png ':size=700')

> [!NOTE]
> A newly created customer has no assets to show yet.

If no cloudcontroller is started, you get a warning that you need to start one to enable SASE connectivity:

![warning_cloudcontroller.png](./screenshots/warning_cloudcontroller.png ':size=600')

![start_networkcontroller.png](./screenshots/start_networkcontroller.png ':size=600')

### Edit Customer
Customers can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit_customer.png](./screenshots/edit_customer.png ':size=350')

> [!CAUTION]
> You will be notified that changing the partner will remove all current security consultant roles.



### Delete Customer

Customers can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> All resources of the customer will be deleted when deleting a customer. This process is irreversible.

You will receive a warning before the customer is permanently deleted:

![delete_customer.png](./screenshots/delete_customer.png ':size=400') 

<!-- When `Provision Cloud Controller` is still toggled on, you will get a warning and be unable to delete the customer:

![provisioned_nc.png](./screenshots/provisioned_nc.png ':size=250') -->


