# ![](../images/menu/menu_monitoring.png ':size=25') Monitoring

>[!ATTENTION]
>Depending on the installed options, you can see a different menu, with more or less items.

![monitoring.png](./screenshots/monitoring.png ":size=200")

### Activity

Here you find an overview of all activity on the network. Options are `create`, `update`, and `delete`.

![recent_activity.png](./screenshots/recent_activity.png ":size=700")

##### Details of an activity

Clicking on the corresponding strip of a activity opens a window with the activity information.

![activity_details.png](./screenshots/activity_details.png ":size=400")

##### Sorting the Activity list

You can sort the list alphabetically by any listed field: type, created at, actor. 

##### Filter the Activity list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the activity list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![act_monitoring_filter.png](./screenshots/act_monitoring_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_act.png ':size=700')

> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.


### Packet Inspection

Packet inspection is the process of examining data packets as they travel across a network to determine their contents. This allows devices like firewalls to detect and block threats like malware, identify specific applications, or manage traffic flow more effectively. 

![packet_inspection.png](./screenshots/packet_inspection.png ":size=700")

>[!ATTENTION]
>For the moment, you can only monitor *_dropped_* packets. 


##### Sorting the Packet Inspection list

You can sort the list alphabetically by any listed field: timestamp, action, source, source type, destination, destination type, protocol. 

##### Filter the Packet Inspection list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the packet inspection list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![pi_monitoring_filter.png](./screenshots/pi_monitoring_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_pi.png ':size=700')


> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.



### Web Filter Monitoring

Web Filter Monitoring is the continuous observation and analysis of a Domain Name System to ensure domain name resolution is reliable, fast, and secure. This process checks that DNS consistently translates domain names into IP addresses without delays, errors, or malicious changes, which is crucial for maintaining website availability and security. 

![dns_monitoring.png](./screenshots/dns_monitoring.png ":size=700")

##### Sorting the Web Filter Monitoring list

You can sort the list alphabetically by any listed field: hostname, device type, type, action, content category, address, timestamp.

##### Filter the Web Filter Monitoring list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the web filter monitoring list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![dns_monitoring_filter.png](./screenshots/dns_monitoring_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_DNS.png ':size=700')


> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.


## EDR

<!-- tabs:start -->

### **Malicious Files**

Detected malicious files are to be find in this section. You can see date and time of the detection, on which device it is detected, the involved user and filename, the level of severity and the action taken. 

  ![malicious_file.png](./screenshots/malicious_file.png ":size=700")

>[!NOTE]
>A file can be added to the whitelist by clicking on the plus sign at the end of its row.

##### Details of a malicious file

Clicking on the corresponding strip of a malicious file opens a detailed view with additional information. 

![malicious_file_details.png](./screenshots/malicious_file_details.png ":size=500")

##### Sorting the Malicious Files list

You can sort the list alphabetically by any listed field: timestamp, device, user, security level, filename, action taken.

##### Filter the Malicious Files list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the malicious files list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![malicious_file_filter.png](./screenshots/malicious_file_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_malfiles.png ':size=600')


> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.

### **File Anomalies**

File anomalies are unexpected changes or behaviors in file systems, often detected by security tools as signs of malware (like ransomware encrypting files), data corruption, or policy violations, involving sudden large-scale creations/deletions/modifications, access issues (permission changes), or structural oddities within executable files (PE files).

![file_anomalies.png](./screenshots/file_anomalies.png ":size=700")

##### Details of a file anomaly

Clicking on the corresponding strip of a file anomaly opens a detailed view with additional information. 

![file_anomalies_details.png](./screenshots/file_anomalies_details.png ":size=500")

##### Sorting the File Anomalies list

You can sort the list alphabetically by any listed field: timestamp, device, user, security level, anomaly type, process, action taken.

##### Filter the File Anomalies list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the file anomalies list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![file_anomaly_filter.png](./screenshots/file_anomaly_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_anomalies.png ':size=600')


> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.

  

### **Network Anomalies**

Network anomaly detection identifies unusual patterns in network traffic, going beyond known threats (signatures) to spot new attacks (zero-days), policy violations, or performance issues by establishing a baseline of normal behavior and flagging significant deviations.

![network_anomalies.png](./screenshots/network_anomalies.png ":size=700")

##### Details of a network anomaly

Clicking on the corresponding strip of a network anomaly opens a detailed view with additional information. 

![nw_anomalies_details.png](./screenshots/nw_anomalies_details.png ":size=500")

##### Sorting the Network Anomalies list

You can sort the list alphabetically by any listed field: timestamp, device, user, security level, anomaly type, source, destination, action taken.

##### Filter the Network Anomalies list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the network anomalies list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![nw_anomaly_filter.png](./screenshots/nw_anomaly_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_nw_anomalies.png ':size=600')


> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.





### **Unsigned Binaries**

The detection of unsigned binaries is a crucial security practice used to identify potential malware or unauthorized software within a system. Binaries (executable files, DLLs, etc.) should ideally be digitally signed by a trusted publisher using a certificate to verify their origin and ensure they haven't been tampered with. Unsigned or improperly signed binaries are often used by adversaries to evade security measures. 

![unsigned_binaries.png](./screenshots/unsigned_binaries.png ":size=700")

##### Details of a unsigned binary

Clicking on the corresponding strip of a network anomaly opens a detailed view with additional information. 

![binary_details.png](./screenshots/binary_details.png ":size=500")

##### Sorting the Unsigned Binaries list

You can sort the list alphabetically by any listed field: timestamp, device, user, security level, filename, action taken.

##### Filter the Unsigned Binaries list

You can search the list using the search box at the top of the page. 

Use the search box to enter keywords and filter the unsigned binary list.

Next to the search box, there is a filter icon ![](../images/icons/icon_filter.png ':size=20'). When clicked, it reveals advanced filtering options where you can define additional conditions based on the following three elements:

- **Property**: A dropdown menu where you choose the field to filter on.
- **Match type**: A dropdown that allows you to select how to match the value (`equals`, `contains`, or `NOT`).
- **Value**: Enter or select the value to match, depending on the selected property.

![unsigned_binary_filter.pn](./screenshots/unsigned_binary_filter.png ':size=500')

To add multiple filters you can press the filter icon ![](../images/icons/icon_filter.png ':size=20') again and then press the `+` button.

Active filters appear at the top of the page:

![active_filters.png](./screenshots/active_filters_unsigned_binary.png ':size=600')


> [!TIP]
> You can refresh the list by pressing the refresh icon ![](../images/icons/icon_reload.png ':size=20') at the top of the page.

<!-- tabs:end -->