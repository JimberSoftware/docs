# ![](../images/menu/menu_dns.png ':size=25') Web Filtering

Use the *Web Filtering* page to apply filtering policies to a selected native network.

>[!ATTENTION]
>Web filtering will only be applied if Jimber DNS is used

You can control common content categories, social media platforms, AI tools, and custom domains through an allowlist or blocklist.

### Configure Web Filtering

![web-filtering.png](./screenshots/web-filtering.png ':size=700')


- Choose a *Native Network* from the dropdown at the top left of the page.
- Review the filtering cards on the page.
- For each category or service, enable the *Block* or *Monitor* toggle that matches your policy.

>[!Attention]
>Don't forget to click *Submit* at the top right of the page!


### Block and Monitor Modes

Each filtering item includes two toggle options:

- *Block* to prevent access.
- *Monitor* to observe traffic for that category or service.

Choose the setting that matches your policy for the selected network.

### Add a Domain to the Blocklist

![blocklist.png](./screenshots/blocklist.png ':size=500')

- Choose a *Native Network* from the dropdown at the top left of the page.
- In the *Blocklist* card, click the *+* button.
- Enter the domain when prompted by the interface.
- Click *Add* to save the entry.

>[!Attention]
>Don't forget to click *Submit* at the top right of the page!

If no custom domains have been added yet, the page shows *No domains on blocklist*:

![no_blocklist.png](./screenshots/no_blocklist.png ':size=500')


### Add a Domain to the Allowlist

![allowlist.png](./screenshots/allowlist.png ':size=500')

- Choose a *Native Network* from the dropdown at the top left of the page.
- In the *Allowlist* card, click the *+* button.
- Enter the domain when prompted by the interface.
- Click *Add* to save the entry.

>[!Attention]
>Don't forget to click *Submit* at the top right of the page!

If no custom domains have been added yet, the page shows *No domains on allowlist*:

![no_allowlist.png](./screenshots/no_allowlist.png ':size=500')

### Remark

If you click the little clock icon in the bottom right, a new window will appear where you can indicate on which days the blocklist or the allowlist apply:

![weekly_schedule.png](./screenshots/weekly_schedule.png ':size=500')

## Summary

Use *Web Filtering* to apply network-level content controls to devices connected through a native network, including unmanaged devices that do not run the *Jimber SASE Client*.
