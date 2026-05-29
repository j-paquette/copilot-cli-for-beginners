# Review all Python files in the book app
Get-ChildItem samples/book-app-project/*.py | ForEach-Object {
    $relativePath = "samples/book-app-project/$($_.Name)";
    Write-Host "Reviewing $relativePath...";
    copilot --allow-all -p "Quick code quality review of @$relativePath - critical issues only"
}