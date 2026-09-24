# ![native_networks](../images/menu/menu_webfiltering.png ':size=25') Web Filtering

Use the _Web Filtering_ page to apply filtering policies to a selected native network.

> [!ATTENTION]
> Web filtering will only be applied if Jimber DNS is used

You can control common content categories, social media platforms, AI tools, and custom domains through an allowlist or blocklist.

### Configure Web Filtering

![web-filtering.png](./screenshots/web-filtering.png ':size=600')

- Choose a _Native Network_ from the dropdown at the top left of the page.
- Review the filtering cards on the page.
- For each category or service, enable the _Block_ or _Monitor_ toggle that matches your policy.

> [!Attention]
> Don't forget to click _Submit_ at the top right of the page!

### Block and Monitor Modes

Each filtering item includes two toggle options:

- _Block_ to prevent access.
- _Monitor_ to observe traffic for that category or service.

Choose the setting that matches your policy for the selected network.

### Add a Domain to the Blocklist

![blocklist.png](./screenshots/blocklist.png ':size=500')

- Choose a _Native Network_ from the dropdown at the top left of the page.
- In the _Blocklist_ card, click the _+_ button.
- Enter the domain when prompted by the interface.
- Click _Add_ to save the entry.

> [!Attention]
> Don't forget to click _Submit_ at the top right of the page!

If no custom domains have been added yet, the page shows _No domains on blocklist_:

![no_blocklist.png](./screenshots/no_blocklist.png ':size=500')

### Add a Domain to the Allowlist

![allowlist.png](./screenshots/allowlist.png ':size=500')

- Choose a _Native Network_ from the dropdown at the top left of the page.
- In the _Allowlist_ card, click the _+_ button.
- Enter the domain when prompted by the interface.
- Click _Add_ to save the entry.

> [!Attention]
> Don't forget to click _Submit_ at the top right of the page!

If no custom domains have been added yet, the page shows _No domains on allowlist_:

![no_allowlist.png](./screenshots/no_allowlist.png ':size=500')

### Remark

If you click the little clock icon in the bottom right, a new window will appear where you can indicate which days the blocklist or the allowlist applies to:

![weekly_schedule.png](./screenshots/weekly_schedule.png ':size=500')

## Summary

Use *Web Filtering* to apply network-level content controls to devices connected through a native network, including unmanaged devices that do not run the ***_<span style="color: darkblue;">Jimber SASE Client</span>_***.
