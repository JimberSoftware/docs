# Important Settings

## Firewall settings

To be able to use our SASE-platform following outgoing ports must be allowed on your firewall(s): 

- 51820 UDP 
- 51820 TCP
- 443 TCP

## The minimum specifications for on-prem Network Controller
 
 - **General**:
    - 25GB hard disk

 - **For every 50 users:**
    - 2 CPU
    - 4GB RAM


## Environment Variables

Our software's behavior can be tailored through specific environment variables:

```
JIMBER_PORT=13138
```

This alters the active listening ports of **_<span style="color: darkblue;">Jimber SASE Platform</span>_**. By setting this, you engage the specified port and the next three sequentially (8000, 8001, 8002, 8003), optimizing port management to suit your network configuration.

For more information, you can click [here](/./advanced/customconfiguration/customconfiguration).