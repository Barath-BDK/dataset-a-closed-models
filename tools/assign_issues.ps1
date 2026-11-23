# Assigns the issues to the people in assignments_filled.csv. Run it after they accepted the invitation (GitHub only lets collaborators be assigned).
#   .\tools\assign_issues.ps1 -Repo "Barath-BDK/dataset-a-closed-models"
param([Parameter(Mandatory = $true)][string]$Repo, [string]$Assignments = "assignments_filled.csv")
Set-Location (Join-Path $PSScriptRoot "..")
$i = 0
foreach ($r in (Import-Csv $Assignments)) {
  $i++
  $u = $r.github_username.Trim()
  if ($u) { gh issue edit $i --repo $Repo --add-assignee $u | Out-Null; Write-Host "#$i -> $u" }
}
