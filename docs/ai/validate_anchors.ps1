$content = [IO.File]::ReadAllText('interview/index.html')
$hrefs = [regex]::Matches($content, 'href="#([^"]+)"') | ForEach-Object { $_.Groups[1].Value } | Select-Object -Unique
$ids = [regex]::Matches($content, 'id="([^"]+)"') | ForEach-Object { $_.Groups[1].Value }

$missing = @()
foreach ($h in $hrefs) {
    if ($ids -notcontains $h) {
        $missing += $h
    }
}

if ($missing.Count -eq 0) {
    Write-Output "ALL_SIDEBAR_LINKS_PERFECT"
} else {
    Write-Output ("Missing targets: " + ($missing -join ", "))
}
