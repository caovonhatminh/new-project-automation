param(
    [string]$TaskName = "NewProject_Automation_Full_1AM",
    [string]$RunAt = "01:00",
    [switch]$DryRun,
    [switch]$Uninstall
)

$ErrorActionPreference = "Stop"

$projectRoot = Split-Path -Parent $MyInvocation.MyCommand.Path
$pythonExe = Join-Path $projectRoot ".venv\Scripts\python.exe"
$logDir = Join-Path $projectRoot "artifacts\scheduled"
$logFile = Join-Path $logDir "daily_automation.log"
$currentUser = "$env:USERDOMAIN\$env:USERNAME"

if (-not (Test-Path $pythonExe)) {
    throw "Cannot find Python in venv: $pythonExe"
}

if ($Uninstall) {
    if (Get-ScheduledTask -TaskName $TaskName -ErrorAction SilentlyContinue) {
        Unregister-ScheduledTask -TaskName $TaskName -Confirm:$false
        Write-Host "Removed scheduled task: $TaskName"
    }
    else {
        Write-Host "Scheduled task not found: $TaskName"
    }
    return
}

if (-not (Test-Path $logDir)) {
    New-Item -ItemType Directory -Path $logDir -Force | Out-Null
}

# Run full automation suites and append logs each day.
$cmd = "cd /d `"$projectRoot`" && `"$pythonExe`" -m pytest tests api_tests e2e_tests >> `"$logFile`" 2>&1"

if ($DryRun) {
    Write-Host "Dry run only. No changes applied."
    Write-Host "TaskName : $TaskName"
    Write-Host "RunAt    : $RunAt"
    Write-Host "User     : $currentUser"
    Write-Host "Command  : cmd.exe /c $cmd"
    return
}

$action = New-ScheduledTaskAction -Execute "cmd.exe" -Argument "/c $cmd" -WorkingDirectory $projectRoot
$trigger = New-ScheduledTaskTrigger -Daily -At ([datetime]::ParseExact($RunAt, "HH:mm", $null))
$settings = New-ScheduledTaskSettingsSet -StartWhenAvailable -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -MultipleInstances IgnoreNew

Register-ScheduledTask `
    -TaskName $TaskName `
    -Action $action `
    -Trigger $trigger `
    -Settings $settings `
    -User $currentUser `
    -Description "Run full automation tests daily at $RunAt from $projectRoot" `
    -Force | Out-Null

Write-Host "Scheduled task created/updated: $TaskName"
Write-Host "Runs daily at $RunAt"
Write-Host "Log file: $logFile"
Write-Host "Run now (manual): Start-ScheduledTask -TaskName `"$TaskName`""
