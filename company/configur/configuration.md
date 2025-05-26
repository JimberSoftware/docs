# ![](../../images/menu/menu_configuration.png ':size=25') Configuration

The **Configuration** section lets you manage essential settings for your company and how user devices interact with your network. It is divided into two main areas:


### Company Settings

These settings define general information about your company within the `Jimber SASE Platform`.

![Company Configuration](./screenshots/config_company.png ':size=700')

- **Primary contact email**: Enter a contact email address that can be used for support or administrative purposes.
- **Website URL**: Specify your company’s website.  
  >[!INFO] 
  > The platform will automatically try to extract the company logo from this URL and display it in the user interface.
- **Display name**: This is the company name as it will appear throughout the platform for users and administrators.


### Network Isolation <!--Jimber SASE Licence--> Settings

These settings control how user devices are managed and isolated in your environment.

![Network Isolation Configuration](./screenshots/config_ni.png ':size=700')

- **IP range**: Define the internal IP range used for isolated network segments.
- **Native Devices enabled**: Toggle this option to allow or block native devices from accessing the platform.
- **User devices expiry time**: Set how many days a user device remains active before it expires.  
  > [!INFO] 
  > The default is **30 days**.
- **Device limit enabled**: Enable this toggle to restrict the number of devices a user can register.
- **Amount of devices allowed per user**: Specify the maximum number of devices per user.  
  > [!INFO] 
  > The default value is **3 devices**.


> [!NOTE]  
> Always remember to click the `Apply` button to save your changes after editing any configuration setting.
