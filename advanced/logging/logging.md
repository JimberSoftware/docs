# LOGGING

You can find the log file locations for each platform below. 

The client/server log file gathers information regarding the startup of the SASE application on the installed platform, while the service log file gathers information regarding the connected service.

When there is an issue in the environment, it is interesting to create the `debug.log` file. That can be established by creating an empty file in the correct folder: %PROGRAMFILES%\Jimber\ (Windows) or /var/log/jimber/ (other OS). 


>[!Warning]
>The `debug.log` never contains logs. It will enable extra logging in the other log files.
<!-- If the debug.log file exists, debug information will be logged into the correct log files.  -->


##  Windows 
  - **Desktop:**
    - Client file: `%LocalAppData%\Jimber\client.log`
    - Service file: `%PROGRAMFILES%\Jimber\service.log`
    - Launcher file: `%PROGRAMFILES%\Jimber\launcher.log`
    - Debug file (Launcher, Client): `%PROGRAMFILES%\Jimber\debug.log`

    

  - **Server:**
    - Server file:  `%PROGRAMFILES%\Jimber\server.log`
    - Launcher file: `%PROGRAMFILES%\Jimber\launcher.log`
    - Debug file (Server, Launcher): `%PROGRAMFILES%\Jimber\debug.log`
    

---
## Linux
  - **Desktop:**
    - Client file: `~/.local/share/jimber/client.log`
    - Service file: `/var/log/jimber/service.log`
    - Launcher file: `/var/log/jimber/launcher.log`
    - Debug file (Launcher, Client):: `/var/log/jimber/debug.log`

  - **Server:**
    - Server file:  `/var/log/jimber/server.log`
    - Launcher file: `/var/log/jimber/launcher.log`
    - Debug file (Server, Launcher): `/var/log/jimber/debug.log`    
  

---
##  MacOS
  - **Desktop:**
    - Client file: `~/Library/Application Support/Jimber/client.log`
    - Service file: `/var/log/Jimber/service.log`
    - Launcher file: `/var/log/Jimber/launcher.log`
    - Debug file (Launcher, Client): `/var/log/Jimber/debug.log`
     
---
## Network Controller/NIAC/Synology/Raspberry Pi:

  - Server file:  `/var/log/jimber/server.log`
  - Launcher file: `/var/log/jimber/launcher.log`
  - Debug file (Server, Launcher): `/var/log/jimber/debug.log` 