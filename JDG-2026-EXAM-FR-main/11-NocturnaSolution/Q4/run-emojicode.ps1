#!/usr/bin/env pwsh
param(
    [Parameter(Mandatory=$true, Position=0)]
    [string]$File
)

$ErrorActionPreference = "Stop"

if (-not (Test-Path $File)) {
    Write-Error "File not found: $File"
    exit 1
}

$FileName = Split-Path $File -Leaf
$BaseName = [System.IO.Path]::GetFileNameWithoutExtension($FileName)

Write-Host "Compiling and running $FileName..." -ForegroundColor Green
$OriginalLocation = Get-Location

# Change to emojicode-container directory and run
$ScriptDir = Split-Path -Parent $PSCommandPath
$ContainerDir = Join-Path $ScriptDir "emojicode-container"
Set-Location $ContainerDir

docker-compose run --rm emojicode bash -c "emojicodec $FileName && ./$BaseName"

Set-Location $OriginalLocation
