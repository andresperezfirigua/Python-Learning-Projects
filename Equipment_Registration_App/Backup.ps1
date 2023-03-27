Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing
# Hide the console window
Add-Type -Name Window -Namespace ConsoleApp -MemberDefinition '
[DllImport("Kernel32.dll")]
public static extern IntPtr GetConsoleWindow();

[DllImport("user32.dll")]
public static extern bool ShowWindow(IntPtr hWnd, int nCmdShow);

public static void Hide()
{
    IntPtr hWnd = GetConsoleWindow();
    if (hWnd != IntPtr.Zero)
    {
        // 0 = Hide the window
        ShowWindow(hWnd, 0);
    }
}'
[ConsoleApp.Window]::Hide()

function AddRecord {
    # Load the Excel file into a variable
    # $inputFilePath = "C:\Users\andresfelipe.perez\Downloads\alm_hardware.xlsx"
    # $outputFilePath = "C:\Users\andresfelipe.perez\Downloads\Minuta_computadores.xlsx"
    $inputFilePath = "C:\Users\Peter.Cadwell\Downloads\alm_hardware.xlsx"
    $outputFilePath = "C:\Users\Peter.Cadwell\Downloads\Minuta_computadores.xlsx"
    if ([string]::IsNullOrWhiteSpace($textboxSearch.Text)) {
        [System.Windows.Forms.MessageBox]::Show("Debe ingresar un equipo para buscar", "Error", "OK", "Error")
        return
    }
    $searchToUpper = $textboxSearch.Text.ToUpper()
    $searchValue = $searchToUpper


    $inputFile = New-Object -ComObject Excel.Application
    $workbook = $inputFile.Workbooks.Open($inputFilePath)
    $worksheet = $workbook.Sheets.Item(1)
    $lastRow = $worksheet.UsedRange.Rows.Count

    $date = Get-Date
    $dateString = $date.ToString("yyyy-MM-dd HH:mm:ss")

    $tipoRegistro = ""

    if ($radioIngreso.Checked) {
        $tipoRegistro = "Ingreso"
    }
    elseif ($radioRetiro.Checked) {
        $tipoRegistro = "Retiro"
    }

    $isFound = $false

    # Loop through each row in the worksheet, starting from row 1
    for ($i = 1; $i -le $lastRow; $i++) {
        # Check if the current row contains the search value
        if ($worksheet.Cells.Item($i, 1).Value2 -eq $searchValue -or $worksheet.Cells.Item($i, 2).Value2 -eq $searchValue) {
            # If the search value is found, get the values in the row and copy them to the output worksheet
            $isFound = $true
            $bearer = $worksheet.Cells.Item($i, 3).Value2

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

            # Add the type of registration to the next cell
            $outputWorksheet.Cells.Item($outputLastRow + 1, $worksheet.UsedRange.Columns.Count + 2).Value2 = $tipoRegistro

            # Add the person who verifies the registration to the next cell
            $outputWorksheet.Cells.Item($outputLastRow + 1, $worksheet.UsedRange.Columns.Count + 4).Value2 = [System.Environment]::UserName

            $dialogResult = [System.Windows.Forms.MessageBox]::Show("Es $bearer quien tiene el equipo a registrar?", "Confirmation", "YesNo", "Question")

            if ($dialogResult -eq "Yes") {
                # Add the name of the person that has the computer to the next cell
                $outputWorksheet.Cells.Item($outputLastRow + 1, $worksheet.UsedRange.Columns.Count + 3).Value2 = $bearer

                # Save and close the output workbook
                $outputWorkbook.Save()
                $outputWorkbook.Close()

                # Display a message to the user indicating that the data was added successfully
                [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
		
                # Exit the loop once the search value is found
                break
            }
            elseif ($dialogResult -eq "No") {
                # Add the name of the person that has the computer to the next cell

                # Create a form
                $formBearer = New-Object System.Windows.Forms.Form
                $formBearer.Text = ""
                $formBearer.Size = New-Object System.Drawing.Size(280, 150)
                $formBearer.StartPosition = "CenterScreen"

                # Create a label and text box for bearer
                $labelBearer = New-Object System.Windows.Forms.Label
                $labelBearer.Location = New-Object System.Drawing.Point(10, 20)
                $labelBearer.Size = New-Object System.Drawing.Size(200, 20)
                $labelBearer.Text = "Quien lleva el equipo?"
                $formBearer.Controls.Add($labelBearer)

                $textboxBearer = New-Object System.Windows.Forms.TextBox
                $textboxBearer.Location = New-Object System.Drawing.Point(10, 40)
                $textboxBearer.Size = New-Object System.Drawing.Size(200, 20)
                $formBearer.Controls.Add($textboxBearer)


                # Create a button for bearer
                $buttonBearer = New-Object System.Windows.Forms.Button
                $buttonBearer.Location = New-Object System.Drawing.Point(10, 70)
                $buttonBearer.Size = New-Object System.Drawing.Size(200, 30)
                $buttonBearer.Text = "OK"
                $buttonBearer.Add_Click({
                        $outputWorksheet.Cells.Item($outputLastRow + 1, $worksheet.UsedRange.Columns.Count + 3).Value2 = $textboxBearer.Text
                        $formBearer.Close()
                    })
                $formBearer.Controls.Add($buttonBearer)

                # Show the form
                $formBearer.ShowDialog() | Out-Null
                $formBearer.Dispose()

                # Save and close the output workbook
                $outputWorkbook.Save()
                $outputWorkbook.Close()

                # Display a message to the user indicating that the data was added successfully
                [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")

                # Exit the loop once the search value is found
                break
            }
        }
    }

    # Close the input workbook and Excel application
    $workbook.Close()
    $inputFile.Quit()

    if ($isFound -eq $false) {
        # Display a message to the user indicating that the computer was not found
        [System.Windows.Forms.MessageBox]::Show("No se encontro el equipo", "Error", "OK", "Error")
    }
}

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

$radioIngreso = New-Object System.Windows.Forms.RadioButton
$radioIngreso.Location = New-Object System.Drawing.Point(10, 70)
$radioIngreso.Size = New-Object System.Drawing.Size(200, 30)
$radioIngreso.Text = "Ingreso de equipo"
$form.Controls.Add($radioIngreso)

$radioRetiro = New-Object System.Windows.Forms.RadioButton
$radioRetiro.Location = New-Object System.Drawing.Point(10, 100)
$radioRetiro.Size = New-Object System.Drawing.Size(200, 30)
$radioRetiro.Text = "Retiro de equipo"
$form.Controls.Add($radioRetiro)

# Create a button for Registrar equipo
$buttonRegistro = New-Object System.Windows.Forms.Button
$buttonRegistro.Location = New-Object System.Drawing.Point(10, 140)
$buttonRegistro.Size = New-Object System.Drawing.Size(200, 30)
$buttonRegistro.Text = "Registrar"
$buttonRegistro.Add_Click({
        if ($radioIngreso.Checked -or $radioRetiro.Checked) {
            AddRecord
        }
        else {
            [System.Windows.Forms.MessageBox]::Show("Debe especificar si el equipo ingresa o sale del piso", "Error", "OK", "Error")
        }
    })
$form.Controls.Add($buttonRegistro)

# Show the form
$form.ShowDialog() | Out-Null