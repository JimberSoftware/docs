File: advanced/mapnetworkdrives/mapnetworkdrives.md

# Mapper des lecteurs réseau à la connexion

Le mappage de lecteurs réseau via SMB (partage de fichiers Windows) est un peu délicat avec la mise en réseau ZTNA. Il est important de savoir que Windows n’ajoute un lecteur réseau que si celui-ci est accessible au moment de son montage. La méthode la plus simple consiste à utiliser la fonctionnalité de script de Network Isolation.

![scripts.jpg](/scripts.jpg)


Voici un exemple de script permettant de monter un lecteur réseau :


```powershell
$officePath = "\\office"
#add more paths here

$timestamp = Get-Date -Format "yyyyMMdd_HHmmss"
$folderPath = "$env:USERPROFILE\jimber_script_logs"

Start-Transcript -Path (Join-Path -Path $folderPath -ChildPath "connected-script-transcript-$timestamp.txt")
$outputFile = Join-Path -Path $folderPath -ChildPath "connected-script-logging-$timestamp.txt"

$defaultSharePath = "\\server.isolated" # Replace with the server hostname or IP address

net use O: /del /yes



$targetIP = "198.18.0.50" # Replace with the IP address you're expecting
$hostname = "server.isolated" # Replace with the hostname you want to resolve

do {
    # Resolve the DNS name
    $resolvedIP = (Resolve-DnsName $hostname).IPAddress

    # Check if the resolved IP is not the target IP
    if ($resolvedIP -ne $targetIP) {
        Write-Host "Resolved IP ($resolvedIP) does not match target IP ($targetIP). Retrying..."
        Start-Sleep -Seconds 5 # Wait for 5 seconds before retrying
    }

} until ($resolvedIP -eq $targetIP)

Write-Host "Resolved IP matches target IP. Continuing..."

do {
    # Attempt to ping the target IP
    $pingResult = Test-Connection -ComputerName $targetIP -Count 1 -Quiet

    if (-not $pingResult) {
        Write-Host "Ping to $targetIP failed. Retrying..."  | Out-File -FilePath $outputFile -Append
        Start-Sleep -Seconds 5 # Wait for 5 seconds before retrying
    }

} until ($pingResult)

Write-Host "Ping to $targetIP successful. Continuing..."  | Out-File -FilePath $outputFile -Append

$driveMappingJson = '[{
    "Path": "\\' + $defaultSharePath + '' + $officePath + '",
    "DriveLetter": "O",
    "Label": "Office"
}]' #you can extend with more shares here

$driveMappingConfig = $driveMappingJson | ConvertFrom-Json

foreach ($drive in $driveMappingConfig) {
    try {
        $exists = Get-PSDrive -Name $drive.DriveLetter -ErrorAction SilentlyContinue
        $connected = $exists -ne $null

        if (-not $connected) {
            Write-Output "Mapping network drive $($drive.Path)" | Out-File -FilePath $outputFile -Append
            New-PSDrive -Name $drive.DriveLetter -PSProvider FileSystem -Root $drive.Path -Persist -Scope Global -ErrorAction SilentlyContinue | Out-File -FilePath $outputFile -Append
        }
        else {
            Write-Output "Drive '$($drive.DriveLetter):\' '$($drive.Path)' already exists with a connection." | Out-File -FilePath $outputFile -Append
        }
    }
    catch {
        Write-Error "Error mapping drive $($drive.DriveLetter): $($_.Exception.Message)" | Out-File -FilePath $outputFile -Append
    }
}

net use | Out-File -FilePath $outputFile -Append
Stop-Transcript
```

ou téléchargez le script [ici](https://docs.jimber.io/advanced/mapnetworkdrives/mapnetworkdrives.ps1)
