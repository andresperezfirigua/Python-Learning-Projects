Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing

# Create a form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Registro de equipos"
$form.Size = New-Object System.Drawing.Size(400, 600)
$form.StartPosition = "CenterScreen"

# Create a label and text box for search value
$labelSearch = New-Object System.Windows.Forms.Label
$labelSearch.Location = New-Object System.Drawing.Point(10, 20)
$labelSearch.Size = New-Object System.Drawing.Size(200, 20)
$labelSearch.Text = "Ingrese el equipo a buscar:"
$form.Controls.Add($labelSearch)

$textboxSearch = New-Object System.Windows.Forms.TextBox
$textboxSearch.Location = New-Object System.Drawing.Point(10, 40)
$textboxSearch.Size = New-Object System.Drawing.Size(200, 20)
$form.Controls.Add($textboxSearch)

# Create a button for Ingreso de equipo
$buttonIngreso = New-Object System.Windows.Forms.Button
$buttonIngreso.Location = New-Object System.Drawing.Point(10, 70)
$buttonIngreso.Size = New-Object System.Drawing.Size(200, 30)
$buttonIngreso.Text = "Ingreso de equipo"
$buttonIngreso.Add_Click({
    # Load the Excel file into a variable
    $inputFilePath = "C:\Users\andresfelipe.perez\Downloads\alm_hardware.xlsx"
    $outputFilePath = "C:\Users\andresfelipe.perez\Downloads\Minuta_computadores.xlsx"
    $searchToUpper = $textboxSearch.Text.ToUpper()
    $searchValue = $searchToUpper
    Write-Output $searchValue
    $inputFile = New-Object -ComObject Excel.Application
    $workbook = $inputFile.Workbooks.Open($inputFilePath)
    $worksheet = $workbook.Sheets.Item(1)
    $lastRow = $worksheet.UsedRange.Rows.Count
    $date = Get-Date
    $dateString = $date.ToString("yyyy-MM-dd HH:mm:ss")

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

            # Add the current date/time to the next cell
            $outputWorksheet.Cells.Item($outputLastRow + 1, $worksheet.UsedRange.Columns.Count + 1).Value2 = $dateString

            # Save and close the output workbook
            $outputWorkbook.Save()
            $outputWorkbook.Close()

            # Display a message to the user indicating that the data was added successfully
            [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "Success", "OK", "Information")
		
	    # Exit the loop once the search value is found
            break
        }
    }

    # Close the input workbook and Excel application
    $workbook.Close()
    $inputFile.Quit()
})
$form.Controls.Add($buttonIngreso)

# Show the form
$form.ShowDialog() | Out-Null