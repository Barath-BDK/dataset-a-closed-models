<#
.SYNOPSIS
  Creates the GitHub repository, the labels and one issue per package, and assigns the issues.

.DESCRIPTION
  Needs the GitHub CLI (gh) and a login:   gh auth login
  Fill assignments.csv (column github_username) first. Packages with an empty name get an issue without an assignee.

.EXAMPLE
  .\tools\create_github.ps1 -Repo "my-org/dataset-a-closed-models" -Visibility private
  .\tools\create_github.ps1 -Repo "my-org/dataset-a-closed-models" -SkipRepo     # repository exists: only labels and issues
  .\tools\create_github.ps1 -Repo "my-org/dataset-a-closed-models" -SkipRepo -InviteCollaborators
#>
param(
  [Parameter(Mandatory = $true)][string]$Repo,
  [ValidateSet("private", "public")][string]$Visibility = "private",
  [switch]$SkipRepo,
  [switch]$InviteCollaborators,
  [string]$Assignments = 'assignments.csv'
)
$ErrorActionPreference = "Stop"
Set-Location (Join-Path $PSScriptRoot "..")
if (-not (Get-Command gh -ErrorAction SilentlyContinue)) { throw "The GitHub CLI (gh) is not installed. Install it from https://cli.github.com/ and run: gh auth login" }
gh auth status | Out-Null

if (-not $SkipRepo) {
  if (-not (Test-Path .git)) { git init -b main | Out-Null; git add -A; git commit -m "Initial commit: dataset A (closed models) job" | Out-Null }
  gh repo create $Repo --$Visibility --source . --remote origin --push
}

# labels
$labels = @(
  @("model:chatgpt", "10a37f"), @("model:gemini", "4285f4"), @("model:claude", "d97757"),
  @("lang:python", "3572a5"), @("lang:c", "555555"), @("lang:cpp", "f34b7d"), @("lang:go", "00add8"),
  @("package", "0e8a16"), @("question", "d876e3")
)
foreach ($l in $labels) { gh label create $l[0] --color $l[1] --repo $Repo --force | Out-Null }

$rows = Import-Csv $Assignments
foreach ($r in $rows) {
  $pkg = $r.package
  $parts = $pkg.Split("_")
  $model = $parts[1]; $lang = $parts[2]
  $title = Get-Content "issues/$pkg.title.txt" -Raw
  $args = @("issue", "create", "--repo", $Repo, "--title", $title.Trim(), "--body-file", "issues/$pkg.md",
            "--label", "package,model:$model,lang:$lang")
  $user = $r.github_username.Trim()
  if ($user) {
    if ($InviteCollaborators) { gh api -X PUT "repos/$Repo/collaborators/$user" -f permission=push | Out-Null }
    $args += @("--assignee", $user)
  } else { Write-Warning "No GitHub user for ${pkg}: issue created without an assignee" }
  & gh @args
}
Write-Host "Done. Protect the main branch (Settings > Branches) so that it only accepts pull requests."


