# Custom Configuration

To accommodate specific requirements or address compatibility issues with other software on your system, a custom configuration for the `Jimber SASE platform` may be necessary. This flexibility is especially useful during testing phases or when customizing the software to fit unique operational environments.

## Environment Variables

Our software's behavior can be tailored through specific environment variables:

```
JIMBER_PORT=13138
```

This alters the active listening ports of `Jimber SASE platform`. By setting this, you engage the specified port and the next three sequentially (8000, 8001, 8002, 8003), optimizing port management to suit your network configuration.

The environment variables can be found under Control Panel, System. Scroll down in the right pane and click on Advanced system settings.

![settings.png](/screenshots/settings.png ':size=500')

In the next window, choose Advanced system settings

![system_properties.png](/screenshots/system_properties.png ':size=300')

Then you can modify the variables.

![environment_variables.png](/screenshots/environment_variables.png ':size=500')


> [!WARNING]
> **Attention**! Be sure to consult Jimber when using the following environment variables. They can break your environment when not used correctly.

```
JIMBER_NOUPDATES=true
```

Activating this variable disables automatic software updates.

```
JIMBER_NOLAUNCHER=true
```

This enables starting the software without the launcher executable, offering a streamlined approach particularly useful in testing scenarios.
