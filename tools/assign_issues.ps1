# Assigns every issue to the person named in issues/titles.csv. Only people who accepted the invitation can be assigned; the others are listed.
#   .\tools\assign_issues.ps1 -Repo "Barath-BDK/dataset-a-closed-models"
param([Parameter(Mandatory = $true)][string]$Repo)
Set-Location (Join-Path $PSScriptRoot "..")
$collab = @(gh api "repos/$Repo/collaborators" --paginate --jq ".[].login") | ForEach-Object { $_.ToLower() }
foreach ($x in (Import-Csv issues/titles.csv -Encoding UTF8)) {
  if ($collab -contains $x.assignee.ToLower()) {
    gh issue edit ([int]$x.number) --repo $Repo --add-assignee $x.assignee | Out-Null
    Write-Host "#$($x.number) -> $($x.assignee)"
  } else { Write-Host "#$($x.number): $($x.assignee) has not accepted the invitation yet" }
}
