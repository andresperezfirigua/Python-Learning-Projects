# Set the path to the input and output Excel files
$inputFilePath = "C:\Users\andresfelipe.perez\Downloads\alm_hardware.xlsx"
$outputFilePath = "C:\Users\andresfelipe.perez\Downloads\Minuta_computadores.xlsx"

# Display a prompt to get the search value from the user
$searchValue = Read-Host "Ingrese equipo a buscar"

# Load the Excel file into a variable
$inputFile = New-Object -ComObject Excel.Application
$workbook = $inputFile.Workbooks.Open($inputFilePath)
$worksheet = $workbook.Sheets.Item(1)

# Get the last row of data in the worksheet
$lastRow = $worksheet.UsedRange.Rows.Count

# Loop through each row in the worksheet, starting from row 1
for ($i = 1; $i -le $lastRow; $i++) {
    # Check if the current row contains the search value
    if ($worksheet.Cells.Item($i, 1).Value2 -eq $searchValue  -or $worksheet.Cells.Item($i, 2).Value2 -eq $searchValue) {
        # If the search value is found, get the values in the row and copy them to the output worksheet
        $outputFile = New-Object -ComObject Excel.Application
        $outputWorkbook = $outputFile.Workbooks.Open($outputFilePath)
        $outputWorksheet = $outputWorkbook.Sheets.Item(1)

        # Get the last row of data in the output worksheet
        $outputLastRow = $outputWorksheet.UsedRange.Rows.Count

        # Copy the values from the input worksheet to the output worksheet
        for ($j = 1; $j -le $worksheet.UsedRange.Columns.Count; $j++) {
            $outputWorksheet.Cells.Item($outputLastRow + 1, $j).Value2 = $worksheet.Cells.Item($i, $j).Value2
        }

        # Save and close the output workbook
        $outputWorkbook.Save()
        $outputWorkbook.Close()

        # Exit the loop once the search value is found
        break
    }
}

# Close the input workbook and Excel application
$workbook.Close()
$inputFile.Quit()