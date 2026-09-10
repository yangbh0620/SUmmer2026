param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$Pattern = '*.tex',
    [switch]$Clean
)

$ErrorActionPreference = 'Stop'

$miktex = Join-Path $env:LOCALAPPDATA 'Programs\MiKTeX\miktex\bin\x64'
$strawberry = 'C:\Strawberry\perl\bin'
$env:Path = "$miktex;$strawberry;$env:Path"

if (-not (Test-Path (Join-Path $miktex 'latexmk.exe'))) {
    throw "latexmk.exe was not found under $miktex"
}
if (-not (Test-Path (Join-Path $strawberry 'perl.exe'))) {
    throw "perl.exe was not found under $strawberry"
}

$sources = Get-ChildItem -LiteralPath $Root -Recurse -File -Filter $Pattern |
    Where-Object {
        $_.FullName -notmatch '[\\/](shared|build_tools)[\\/]'
    } |
    Sort-Object FullName

if ($sources.Count -eq 0) {
    Write-Host "No LaTeX sources matched under $Root."
    exit 0
}

$failures = [System.Collections.Generic.List[string]]::new()

foreach ($source in $sources) {
    Write-Host "[LaTeX] $($source.FullName)"
    Push-Location $source.DirectoryName
    try {
        if ($Clean) {
            & latexmk -C $source.Name | Out-Host
        }
        & latexmk -pdf -interaction=nonstopmode -halt-on-error -file-line-error $source.Name | Out-Host
        if ($LASTEXITCODE -ne 0) {
            $failures.Add($source.FullName)
            continue
        }

        $pdf = [System.IO.Path]::ChangeExtension($source.FullName, '.pdf')
        if (-not (Test-Path -LiteralPath $pdf) -or (Get-Item -LiteralPath $pdf).Length -eq 0) {
            $failures.Add($source.FullName)
        }
    }
    finally {
        Pop-Location
    }
}

if ($failures.Count -gt 0) {
    Write-Error ("LaTeX build failures:`n" + ($failures -join "`n"))
    exit 1
}

Write-Host "Built $($sources.Count) LaTeX document(s) successfully."

