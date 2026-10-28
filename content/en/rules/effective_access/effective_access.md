# ![](../../images/menu/menu_packetinspection.png ':size=25') Effective Access

### Example 1: matching policy

After installing several firewall policies, it is good practice to inspect the access produced by active firewall policies, because routing, endpoint availability, secure mode, and controller state can still affect the real connection.

![effective_access.png](./screenshots/effective_access.png ':size=700')

1. Select the entity to inspect (users, groups, servers, or devices)
 
 ![select_entity.png](./screenshots/select_entity.png ':size=400')
   
2. Choose direction: outgoing, incoming
3. Optionally, you can also select a destination, a protocol (TCP, UDP, or ICMP ), and a port
4. Click `Inspect access` to see the results

 ![results_effective_access.png](./screenshots/results_effective_access.png ':size=600')

>[!TIP]
>You can check the policy which effects the chosen entity by clicking `View policy` at the end of its row. 

### Example 2: no matching policy

   ![no_match.png](./screenshots/no_match.png ':size=600')
