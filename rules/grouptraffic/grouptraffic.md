# Group Traffic

The **Group Traffic** feature controls how different groups can communicate with each other across your network setup. On the *`Jimber SASE Platform`*, a **group** is a flexible concept — it can represent users, servers, or devices connected via a Network Isolation Access Client (NIAC).

![group_traffic_start.png](/group_traffic_start.png ':size=800')

Because groups can be applied to various types of endpoints, this feature gives you precise control over traffic flow between these segments. For example, you might:

- Allow a group of **developers (users)** to access a group containing **staging servers**
- Permit **NIAC-connected devices** to communicate with a group of **infrastructure services**
- Enable internal communication between all devices within a **specific department**

To configure group communication, define:

- A **source group** (initiating communication)
- A **destination group** (receiving communication)
- A **start port** and **end port** to define the allowed port range  
  If you don’t specify a range, it will default to **1–65535**, allowing all ports.

For example, to grant the **"Developers"** group access to your **"Servers"**, you would set **"Developers"** as the source group and **"Servers"** as the destination group.

![group_traffic.png](/group_traffic.png ':size=800')

If you want members within the same group to communicate with each other, select the same group as both source and destination.

![group_traffic_intern.png](/group_traffic_intern.png ':size=800')

After defining your rules, click `Submit Rules` to apply them. Additionally, you can **download all group traffic rules** as a **.csv file** by pressing the download button located next to the Submit Rules button.


If there are any unsaved changes, a warning message will appear, so you won’t miss updating your settings.

![unsaved_changes.png](/unsaved_changes.png ':size=500x175')

> [!WARNING]  
> Group Traffic should be used carefully. For more targeted control over specific services, consider using **Allow Custom Ports**, which offers a more secure and detailed approach.
