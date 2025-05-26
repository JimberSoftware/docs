# ![](../../images/menu/menu_customers.png ':size=25') Customers
> [!WARNING]
> This *`Customers`* section is exclusively available for **partners**. If you are an end customer, you will be directly redirected to the *`Jimber SASE Platform`* configuration of your company.

In our platform, a **customer** refers to a company intending to use `Jimber SASE Platform`. Integrators have the capability to manage these customers, ensuring seamless operations and service delivery.

For clarity, consider a scenario where a company named *`Astral Voyage`* wants to use `Jimber SASE Platform`. You must first create *`Astral Voyage`* as a customer on the platform before any further configurations or service provisions can occur.

![list_customers.png](./screenshots/list_customers.png ':size=800')

### Create Customers

To incorporate a new customer into the platform, click on the `+ Create new` button located at the upper right corner of the interface.

![create_customer.png](./screenshots/create_customer.png ':size=500')

Following fields should be provided:
	
  - Name
  - Display name
  - Primary contact email

> [!WARNING]
>  In the customer Name field spaces and special characters or symbols are not allowed. You can however use these characters in the Display name field.

Filling in the website will cause an icon to appear in front of the customer's name.

### Filter Customers

You can search the list of Customers using the search box at the top of the page. This helps you quickly find and manage the customer you're looking for.

- Use the search box to enter keywords and filter the customer list.

Next to the search box, there is a filter icon ![](../../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (e.g. `equals`, `contains`, etc.).
- **Value**: Enter or select the value to match, depending on the selected property.

You can press the `+` button to add multiple filters.

Once filters are applied:
- The results are updated to reflect your conditions.
- Active filters appear at the top of the page.
- You can remove filters individually by clicking the `X` next to each, or remove all at once by clicking the `Reset Filters` button.

> [!INFO]
> You can refresh the list of customers by pressing the refresh icon ![](../../images/icons/icon_reload.png ':size=20') at the top of the page.

### Customer Details

To view the details of a specific customer, select their row in the table (rather than using the action buttons at the end).
You get an overview of created assets:

![overview_customer.png](./screenshots/overview_customer.png ':size=800')

> [!NOTE]
> A newly created customer has no assets to show yet.

### Edit Customers
Customers can be edited by clicking on the edit icon ![](../../images/icons/icon_edit.png ':size=20') in their row.

![edit_customer.png](./screenshots/edit_customer.png ':size=500')

> [!WARNING]
> You will be notified that changing the partner will remove all current security consultant roles.



### Delete Customers

Customers can be deleted by clicking on the delete icon ![](../../images/icons/icon_delete.png ':size=20') in their row.

> [!WARNING]
> All resources of the customer will be deleted when deleting a customer. This process is irreversible.

You will receive a warning before the customer is permanently deleted:

![delete_customer.png](./screenshots/delete_customer.png ':size=500')

