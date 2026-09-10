param(
    [Parameter(Mandatory = $true)]
    [string]$PptxPath,
    [string]$PdfPath
)

$ErrorActionPreference = 'Stop'

$pptx = (Resolve-Path -LiteralPath $PptxPath).Path
if (-not $PdfPath) {
    $PdfPath = [System.IO.Path]::ChangeExtension($pptx, '.pdf')
}
$pdf = [System.IO.Path]::GetFullPath($PdfPath)

$outputDir = Split-Path -Parent $pdf
if (-not (Test-Path -LiteralPath $outputDir)) {
    New-Item -ItemType Directory -Force -Path $outputDir | Out-Null
}

$powerPoint = $null
$presentation = $null

try {
    $powerPoint = New-Object -ComObject PowerPoint.Application
    $presentation = $powerPoint.Presentations.Open($pptx, $true, $true, $false)

    # ppSaveAsPDF = 32
    $presentation.SaveAs($pdf, 32)
}
finally {
    if ($presentation) {
        $presentation.Close()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($presentation) | Out-Null
    }
    if ($powerPoint) {
        $powerPoint.Quit()
        [System.Runtime.InteropServices.Marshal]::ReleaseComObject($powerPoint) | Out-Null
    }
    [GC]::Collect()
    [GC]::WaitForPendingFinalizers()
}

if (-not (Test-Path -LiteralPath $pdf) -or (Get-Item -LiteralPath $pdf).Length -eq 0) {
    throw "PowerPoint did not create a valid PDF: $pdf"
}

Write-Host $pdf

