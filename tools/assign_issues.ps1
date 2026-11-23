# Assigns every issue to the person named in issues/titles.csv. Run it after they accepted the invitation (GitHub only lets collaborators be assigned).
#   .\tools\assign_issues.ps1 -Repo "Barath-BDK/dataset-a-closed-models"
param([Parameter(Mandatory = $true)][string]$Repo)
Set-Location (Join-Path $PSScriptRoot "..")
foreach ($x in (Import-Csv issues/titles.csv -Encoding UTF8)) {
  gh issue edit ([int]$x.number) --repo $Repo --add-assignee $x.assignee 2>$null | Out-Null
  if ($LASTEXITCODE -eq 0) { Write-Host "#$($x.number) -> $($x.assignee)" } else { Write-Host "#$($x.number): $($x.assignee) has not accepted the invitation yet" }
}
