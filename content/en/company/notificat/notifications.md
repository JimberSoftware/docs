# ![](../../images/menu/menu_notifications.png ':size=25') Notifications

In this section, you can determine which people can receive which notifications.

- In the **_Company Notifications Settings_**, the notification settings can be set for anyone of the company.
- In the **_User Notifications Settings_**, the notification settings can be set for the **_logged-in_** user. 

### Company Notifications Settings

![company_not.png](./screenshots/company_notificat.png ':size=600')

In the email addresses field, you can enter the email addresses of the people who should receive the notifications.

- **Server Notification**  
    - Notifications include when a server is down for more than 3 minutes and when it comes back online.
- **NIAC Notifications**
    - Notifications include when a NIAC is down for more than 3 minutes and when it comes back online.
- **Network Controller Notifications**
    - Notifications include when a Network Controller is down for more than 3 minutes and when it comes back online.
- **Microsoft Entra ID Sync Notifications**
    - Notifications include when the platform fails to synchronize properly with Microsoft Entra ID.
- **Device Approval Notifications**
    - Notifications include when a user that belongs to a group who needs device approval tries to log in and is waiting for approval to connect.
- **EDR Notifications**
    - Notifications include when a malicious file or anomalous network activity is detected and SASE access is automatically disabled for a user.
- **Certificate Expiry Notifications**
    - Notifications remind administrators to request a new root certificate before the current certificate expires.

### User Notification Settings

![user_not.png](./screenshots/user_not.png ':size=600')

Here the email address is that of the **_logged-in_** user.
The available notifications are the same as above.

Each set of notifications can be turned on or off.

> [!IMPORTANT] 
> Always remember to click the **_Apply_** button to save your changes after editing any configuration setting. **You don't get a warning if not done**.
