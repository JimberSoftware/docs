

# ![](../../images/menu/menu_webfiltering.png ':size=28') Web Filtering

Web Filtering allows you to control and manage which websites a specific group can access on the network. You can block categories of content such as adult content, fake news, gambling, malware/adware, and social media.

Additionally, you can configure time-based restrictions, not only for specific hours of the day but also for certain days of the week. This allows you to tailor access more precisely, restricting content only during certain hours or on specific weekdays.

Traffic to blocked sites can be monitored, providing insights into which users attempted to access restricted content. You can further customize web filtering by using a blocklist to block specific sites or an allowlist to permit access to certain websites. All of these settings are configurable per group, so you can apply different rules based on the needs of each group within your network.

Web Filtering uses regularly updated lists per category to ensure that new threats and unwanted content are automatically detected and blocked as they emerge.

![Screenshot of the Web Filtering page](./screenshots/webfiltering.png ':size=800')

> [!WARNING]
> For web filtering rules to be effective, DNS Override must be enabled for the same group. Without it, filtering rules won’t be applied.

### Configuring Web Filtering

To set up web filtering for a group, follow these steps:

1. **Select a Group**: Start by selecting the group you want to configure filtering rules for.

> [!INFO] 
> If a user belongs to multiple groups with conflicting web filtering rules, blocking takes precedence over allowing. This means that if one group blocks a site and another allows it, the site will be blocked for that user.

2. **Block Categories**: Choose and block specific content categories (e.g., adult content, malware, gambling) to restrict access for the selected group. Use the corresponding toggle to enable or disable each category.

3. **Manage Websites**:
   - **Blocklist**: Add specific websites you want to block by entering their URLs into the blocklist.
   - **Allowlist**: Add trusted websites to the allowlist to ensure they remain accessible, even if they belong to a blocked category.
   - **Remove Websites**: To remove a website from either list, click the red trash bin icon next to the website name.

4. **Time-based Rules**: Set time-based rules to control access to certain sites during specific time slots. Click the clock icon to define when the restrictions should apply.

5. **Monitor Traffic**: You can also monitor traffic to the blocked or allowed websites to track usage patterns and ensure that the filtering rules are being followed. Use the corresponding toggle to enable or disable each category.

6. **Activate Changes**: Once you’ve made your changes, click the `➢ Submit rules` button to apply them and ensure the rules are active.

> [!WARNING] 
> Always double-check the rules before submitting to ensure the configuration is correct. If you make changes you don’t want to keep, use the `Clear changes` button to revert to the previously saved version.

> [!INFO]
> If there are any unsaved changes, a warning message will appear, so you won’t miss updating your settings.
>
>![Screenshot of the unsaved changes warning](../../images/notifications/unsaved_changes.png ':size=400')



