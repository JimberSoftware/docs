# ![](../images/icons/bar-chart-2-fill.png ':size=35') Insights


### Web Activity Insights

Web Activity Insights provides comprehensive visibility into your organization’s internet usage, application footprint, and web security enforcement. By aggregating web traffic data across your environment, this dashboard helps administrators and security teams monitor browsing trends, verify policy effectiveness, and identify potential security risks.

![web_activity_insights.png](./screenshots/web_activity_insights.png ":size=600")

##### Key Metrics Explained

- **Page Loads**

    Displays the total number of successful web page requests made across your monitored environment within the selected timeframe. Tracking page loads helps establish a baseline for normal network activity and identify unusual spikes in web traffic.

- **Blocked Requests**

    Shows the total number of web requests that were automatically prevented from loading based on your active security policies, content filters, or threat intelligence rules (such as malicious domains, phishing sites, or restricted categories). A high volume of blocked requests may indicate targeted attack attempts or users frequently trying to access unauthorized content.

- **Unique Apps**

    Indicates the total number of distinct web applications and cloud services accessed by your users. This metric helps you discover shadow IT, evaluate software adoption, and ensure that employees are using approved business tools.

- **Device Coverage**

    Represents the percentage or total number of managed devices actively reporting web traffic data compared to your total device fleet. High device coverage ensures complete visibility and confirms that your web protection policies are properly deployed and functioning across endpoints.



##### How to Use These Insights

- **Verify Security Enforcement:** Compare Blocked Requests against Page Loads to assess how actively your web filtering policies are protecting users.

- **Audit Shadow IT:** Regularly review Unique Apps to spot unapproved or high-risk cloud applications entering your network.

- **Identify Deployment Gaps:** Monitor Device Coverage to quickly detect endpoints that may be offline, misconfigured, or missing the required security agent.

>[!TIP]
>Insights can be filtered by selecting the **Today**, **7 days**, **30 days**, or **3 months** buttons.


### AI Activity Insights

AI Activity Insights provides comprehensive visibility into how artificial intelligence tools and generative AI platforms are being used across your organization. By monitoring AI-related traffic and user interactions, this dashboard helps administrators and security teams track AI adoption, prevent sensitive data leakage, and enforce acceptable use policies.

![ai_activity_insights.png](./screenshots/ai_activity_insights.png ":size=600")

##### Key Metrics Explained

- **AI Interactions (or Prompts / Requests)**

    Displays the total number of requests or interactions made with external AI platforms within the selected timeframe. Tracking this metric helps establish a baseline for organizational AI adoption and highlights sudden surges in usage.

- **Blocked AI Requests**

    Shows the total number of AI-related requests that were automatically prevented based on your active security and compliance policies (such as unauthorized AI tools, high-risk platforms, or restricted categories). A high number of blocked requests may indicate employees attempting to bypass governance rules or use unapproved generative AI services.

- **Unique AI Tools (or Apps)**

    Indicates the total number of distinct AI applications, chatbots, and AI-powered services accessed across your environment. This metric helps you identify "Shadow AI," evaluate which tools are most popular among teams, and ensure employees only use vetted, enterprise-approved AI solutions.

- **Active AI Users (or Device Coverage)**

    Represents the number or percentage of users or managed devices actively interacting with AI services compared to your total environment. Monitoring this metric helps you understand how widespread AI usage is across your workforce and verifies that your monitoring policies are effectively covering your endpoints.

##### How to Use These Insights

- Mitigate Data Leakage Risks: Monitor AI Interactions and Unique AI Tools to identify unvetted platforms where employees might inadvertently share confidential or proprietary company data.

- Enforce AI Governance: Compare Blocked AI Requests against total interactions to verify that your acceptable use policies are effectively blocking unauthorized AI services.

- Support Safe AI Adoption: Use insights on Unique AI Tools and Active AI Users to determine which AI tools teams actually need, helping you decide which solutions to officially license and secure.

>[!TIP]
>Insights can be filtered by selecting the **Today**, **7 days**, **30 days**, or **3 months** buttons.