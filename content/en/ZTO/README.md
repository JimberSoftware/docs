# ![](../images/menu/menu_security.png ':size=28') Zero Trust Outbound

Zero Trust Outbound (ZTO) controls internet access for user devices, servers, and NIACs. When ZTO is enabled, outbound internet traffic from these endpoints is blocked unless an enabled outbound policy allows it.

To make the initial setup easier, the platform can create a **Standard Internet** service and three outbound policies automatically. You can enable ZTO and create these defaults while creating a customer, or enable it later from the customer's configuration.

> [!IMPORTANT]
> Enabling ZTO changes the company from unrestricted endpoint internet access to policy-controlled access. Make sure the required outbound policies are enabled before users and devices need internet access.

> [!NOTE]
> Native-network internet access is controlled by its own outbound policies, independently of the ZTO setting. The automatic policies described on this page cover Users, Servers, and NIACs.

## What Is Created Automatically?

The first time ZTO is enabled, the platform creates:

- A **Standard Internet** service containing rules for common internet traffic, including HTTP, HTTPS, DNS, NTP, email, and ICMP.
- **Standard Internet - Users**, with `All Users` as its source.
- **Standard Internet - Servers**, with `All Servers` as its source.
- **Standard Internet - NIACs**, with `All NIACs` as its source.

All three policies are outbound policies. They use the **Standard Internet** service and have `Internet` as their destination.

![Standard Internet policies](./screenshots/standard-internet-policies.png ':size=1000')

## Enable ZTO When Creating a Customer

Use this option when ZTO should be active as soon as a new customer is created.

1. Open **Customers** and click **+ Create new**.
2. Enter the customer details.
3. Select a plan that includes the **Zero Trust Outbound** module.
4. Turn on **Enable ZTO**.
5. Click **Create**.

![Enable ZTO during customer creation](./screenshots/enable-zto-during-customer-creation.png ':size=420')

The platform enables ZTO and creates the Standard Internet service and all three default policies. The policies are enabled, so Users, Servers, and NIACs keep access to the standard internet services from the start.

> [!INFO]
> The **Enable ZTO** option is shown only when the selected plan includes the Zero Trust Outbound module. Selecting a plan without that module hides the option and leaves ZTO disabled.

## Enable ZTO for an Existing Customer

Use the company configuration when the customer already exists or ZTO was not enabled during customer creation.

1. Open the customer.
2. Go to **Company** > **Configuration**.
3. In the **Misc** section, turn on **Zero Trust Outbound**.
4. Confirm the Zero Trust Outbound warning.
5. Choose whether to keep **Allow internet** enabled:
    - **Enabled**: the three automatic policies are created and enabled.
    - **Disabled**: the policies are created but remain disabled. Internet access is blocked until an appropriate outbound policy is enabled.
6. Click **Apply**.

![Enable ZTO in company configuration](./screenshots/enable-zto-in-company-configuration.png ':size=1000')

The Standard Internet service and policies are created only the first time ZTO is enabled. Turning ZTO off and on again does not create duplicates or reset existing policies.

> [!TIP]
> If ZTO is enabled without **Allow internet**, review the policies immediately and enable only the access the customer requires.

## Review and Adjust Internet Access

Open **Security** > **Policies** after enabling ZTO. From there, you can:

- Enable or disable each Standard Internet policy.
- Edit a policy to narrow its sources.
- Edit the Standard Internet service to change the allowed ports and protocols.
- Create additional outbound services and policies for more specific access.

See [Policies](/./rules/firewall-policies/firewall-policies.md) for instructions on creating and managing policies.

## Expected Access

| ZTO setting | Matching enabled outbound policy | Result                                                |
| ----------- | -------------------------------- | ----------------------------------------------------- |
| Off         | Not required for endpoint ZTO    | Endpoint internet access is not restricted by ZTO.    |
| On          | Yes                              | Traffic covered by the policy and service is allowed. |
| On          | No                               | Outbound internet traffic is blocked.                 |

If a user, server, or NIAC loses internet access after ZTO is enabled, verify that:

- The relevant outbound policy is enabled.
- The policy source includes the affected entity.
- The policy uses a service containing the required protocol and port.
- The policy destination is `Internet`.
