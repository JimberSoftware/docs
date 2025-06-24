# How to create a combined environment for multiple customers

## What is a unified environment?

A unified environment in Jimber SASE is an architectural setup where we integrate the systems of multiple companies into a single environment. Instead of isolating each company’s systems in separate environments or tenants, we bring them together under one SASE instance.

### Why choose a unified environment?

- **Cost efficiency**: You only need one environment for multiple companies, significantly reducing infrastructure, licensing, and operational overhead.
- **Meets minimum requirements**: Jimber SASE requires a minimum of 10 users per environment. By unifying companies into one environment, you can efficiently meet this requirement without forcing small companies to maintain separate environments.
- **Centralized management**: A single SASE instance for small companies simplifies administration, monitoring, and updates.
- **Simplified maintenance**: With fewer environments for small companies, ongoing maintenance and policy management are easier and less time-consuming.
- **Clear separation with flexibility**: Even though companies share the unified environment, unique configurations, policies, and access controls ensure that each company remains isolated and secure within the setup.

### Remark

For companies with more than 10 users, we advise creating a **dedicated environment** rather than including them in a unified environment. This helps avoid unnecessary complexity and ensures cleaner management of policies and configurations.



---

### Keeping things organized

In a combined environment, strict naming conventions and logical separation mechanisms are essential to maintain clarity and control. Here’s how we achieve that:

- **Groups:** Each company’s assets (users, devices, locations) are assigned to distinct groups that follow a domain-like naming standard (e.g., `group.users.companya.be`, `group.devices.companyb.co.uk`).

- **Rules:** Firewall rules, policies, and security configurations use domain-style names (e.g., `rule.allow-http.companya.be`, `rule.allow-crm.companyb.co.uk`). This ensures there’s no overlap or unintended policy inheritance.

- **Instances:** Wherever applicable (e.g., virtual gateways, policy engines), instances are created with unique domain-style identifiers (e.g., `instance.gateway1.companya.be`, `instance.policyengine1.companyb.co.uk`).

---

## Onboarding into a Unified Environment (Jimber SASE)

In a combined or unified environment, onboarding new companies and their assets is a streamlined process that ensures all entities are properly segmented while being managed centrally. Below is the step-by-step flow.

---

### Step 1 — Add Company Domains

The first step is to register the domains of each company into the SASE environment. These domains define the identity of each organization within the combined system.

**Example domains:**
- `companya.be`
- `companyb.co.uk`

Domains act as the primary namespace reference for users, groups, resources, and policies.

---

### Step 2 — Add Users

Users are added based on their email addresses, which automatically tie them to the appropriate domain/company.

No additional onboarding steps are required per user beyond adding their email — their domain affiliation is clear from the email (e.g., `alice@companya.be`, `bob@companyb.co.uk`).

---

### Step 3 — Assign Users to Groups

Each user is placed into company-specific groups. These groups follow the domain-like naming convention.

**Examples:**
- `group.all-users.companya.be`
- `group.all-users.companyb.co.uk`

You can create additional sub-groups as needed for role-based or department-based segmentation (e.g., `group.admins.companya.be`, `group.hr.companyb.co.uk`).

---

### Step 4 — Onboard Company Resources

Add the resources (servers, applications, file shares, etc.) specific to the company. Resources are named using the same domain-style pattern.

**Examples:**
- `server.servera.companya.be`
- `app.sharepoint.companyb.co.uk`
- `db.db01.companya.be`

This makes it easy to identify and manage company-specific assets.

---

### Step 5 — Configure Access via Attribute Service

Finally, grant access by linking the created groups (from Step 3) to the corresponding resources (from Step 4).

This is done through the Attribute Service function, where attributes such as group membership and resource names are mapped to access permissions.

Each company’s users only have access to their company’s resources, even though everything operates within the same SASE platform.

---

### Unified, Functional Security Groups

In addition to company-specific groups, Jimber SASE supports the creation of unified, functional security groups. These groups provide a powerful way to apply consistent security policies across multiple companies within the same combined environment.

#### What are Unified, Functional Security Groups?

Unified, functional security groups:
- Span multiple companies in the combined environment
- Focus on shared security functions rather than company boundaries
- Allow policies to be applied centrally and uniformly

For example:
- A group like `group.webfiltering-enabled.all-companies` could include `group.all-users.companya.be`, `group.all-users.companyb.co.uk`, and other company user groups.

---

#### How They Work

Central policy application  
You can attach security features (such as `policy.webfiltering.all-companies`, `policy.dns-protection.all-companies`) directly to these functional groups. This ensures the policy is enforced consistently, no matter the company.

Flexible membership  
Groups from different companies can be added as members of a functional group. This allows a single policy to cover many companies without duplicating configurations.

No added risk  
Even though these groups span multiple companies:
- There is no unintended cross-access to resources or data
- Policies applied are security enforcements only, not permissions to access company-specific resources

---

#### Example Use Case

Imagine you want to enforce web filtering across all your managed companies.

1. Create a functional group: `group.webfiltering-enabled.all-companies`
2. Add company groups:
   - `group.all-users.companya.be`
   - `group.all-users.companyb.co.uk`
   - `group.all-users.companyc.com`
3. Attach the policy: `policy.webfiltering.all-companies`

Now, all users across companies benefit from a uniform web protection policy.
