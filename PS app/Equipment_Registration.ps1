Add-Type -AssemblyName System.Windows.Forms
Add-Type -AssemblyName System.Drawing


function Clean_Controls {
    $textboxSearch.Text = ""
    $radioIngreso.Checked = $false
    $radioRetiro.Checked = $false
}

function Add_Non_Asurion_Device ($outputFilePath) {
    $date = Get-Date
    $dateString = $date.ToString("yyyy-MM-dd HH:mm:ss")

    $tipoRegistro = ""

    if ($radioIngreso.Checked) {
        $tipoRegistro = "Ingreso"
    }
    elseif ($radioRetiro.Checked) {
        $tipoRegistro = "Retiro"
    }
    function ValidateTextbox {
        if ([string]::IsNullOrWhiteSpace($textboxSerial.Text)) {
            [System.Windows.Forms.MessageBox]::Show("Debe especificar el seríal del equipo", "Error", "OK", "Error")
            return $true
        } elseif ([string]::IsNullOrWhiteSpace($textboxModel.Text)) {
            [System.Windows.Forms.MessageBox]::Show("Debe especificar el modelo del equipo", "Error", "OK", "Error")
            return $true
        } elseif ([string]::IsNullOrWhiteSpace($textboxBearer.Text)) {
            [System.Windows.Forms.MessageBox]::Show("Debe especificar quien lleva el equipo", "Error", "OK", "Error")
            return $true
        }
        return $false
    }
    # Create a form
    $form = New-Object System.Windows.Forms.Form
    $form.Text = ""
    $form.Size = New-Object System.Drawing.Size(300, 220)
    $form.StartPosition = "CenterScreen"
    $form.ControlBox = $false
    $form.MaximizeBox = $false
    $form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle

    # Create labels and textboxes
    $labelSerial = New-Object System.Windows.Forms.Label
    $labelSerial.Location = New-Object System.Drawing.Point(10, 20)
    $labelSerial.Size = New-Object System.Drawing.Size(100, 20)
    $labelSerial.Text = "Numero serial:"
    $form.Controls.Add($labelSerial)

    $textboxSerial = New-Object System.Windows.Forms.TextBox
    $textboxSerial.Location = New-Object System.Drawing.Point(120, 20)
    $textboxSerial.Size = New-Object System.Drawing.Size(160, 20)
    $form.Controls.Add($textboxSerial)

    $labelModel = New-Object System.Windows.Forms.Label
    $labelModel.Location = New-Object System.Drawing.Point(10, 50)
    $labelModel.Size = New-Object System.Drawing.Size(100, 20)
    $labelModel.Text = "Modelo:"
    $form.Controls.Add($labelModel)

    $textboxModel = New-Object System.Windows.Forms.TextBox
    $textboxModel.Location = New-Object System.Drawing.Point(120, 50)
    $textboxModel.Size = New-Object System.Drawing.Size(160, 20)
    $form.Controls.Add($textboxModel)

    $labelType = New-Object System.Windows.Forms.Label
    $labelType.Location = New-Object System.Drawing.Point(10, 80)
    $labelType.Size = New-Object System.Drawing.Size(100, 20)
    $labelType.Text = "Tipo de dispositivo:"
    $form.Controls.Add($labelType)

    $dropdownType = New-Object System.Windows.Forms.ComboBox
    $dropdownType.Location = New-Object System.Drawing.Point(120, 80)
    $dropdownType.Size = New-Object System.Drawing.Size(160, 20)
    $dropdownType.Items.Add("Portátil")
    $dropdownType.Items.Add("Otro")
    $form.Controls.Add($dropdownType)

    $labelBearer = New-Object System.Windows.Forms.Label
    $labelBearer.Location = New-Object System.Drawing.Point(10, 110)
    $labelBearer.Size = New-Object System.Drawing.Size(100, 20)
    $labelBearer.Text = "Nombre de quien lleva el equipo:"
    $form.Controls.Add($labelBearer)

    $textboxBearer = New-Object System.Windows.Forms.TextBox
    $textboxBearer.Location = New-Object System.Drawing.Point(120, 110)
    $textboxBearer.Size = New-Object System.Drawing.Size(160, 20)
    $form.Controls.Add($textboxBearer)

    $labelAdditional = New-Object System.Windows.Forms.Label
    $labelAdditional.Location = New-Object System.Drawing.Point(10, 140)
    $labelAdditional.Size = New-Object System.Drawing.Size(100, 20)
    $labelAdditional.Text = "Informacion adicional:"
    $form.Controls.Add($labelAdditional)

    $textboxAdditional = New-Object System.Windows.Forms.TextBox
    $textboxAdditional.Location = New-Object System.Drawing.Point(120, 140)
    $textboxAdditional.Size = New-Object System.Drawing.Size(160, 20)
    $form.Controls.Add($textboxAdditional)

    # Create a button for bearer
    $buttonAddDevice = New-Object System.Windows.Forms.Button
    $buttonAddDevice.Location = New-Object System.Drawing.Point(10, 160)
    $buttonAddDevice.Size = New-Object System.Drawing.Size(200, 30)
    $buttonAddDevice.Text = "Registrar"
    $buttonAddDevice.Add_Click({
        if (-not (ValidateTextbox)){
            $newComputer = @()
            $newComputer += $textboxSerial.Text
            Write-Host "Serial asignado a newComp var $newComputer"
            $newComputer += "N/A"
            $newComputer += "N/A"
            $newComputer += $textboxModel.Text
            if (-not ($null -eq $dropdownType.SelectedItem)) {
                $newComputer += $dropdownType.SelectedItem
            } else {
                [System.Windows.Forms.MessageBox]::Show("Debe seleccionar el tipo dispositivo", "Error", "OK", "Error")
                return
            }
            $newComputer += $dateString
            $newComputer += $tipoRegistro
            $newComputer += $textboxBearer.Text
            $newComputer += [System.Environment]::UserName.ToUpper()
            if ($null -eq $dropdownType.SelectedItem) {
                $newComputer += "N/A"
            } else {
                $newComputer += $textboxAdditional.Text
            }
            Write-Host "newComp var antes de terminar evento $newComputer"
            $form.Close()
            $form.Dispose()
            Write-Host $newComputer.GetType().Name
            Add_Record_To_File $outputFilePath $newComputer
        }
    })
    $form.Controls.Add($buttonAddDevice)
    # Show the form
    $form.ShowDialog() | Out-Null
}

function Find_Computer($inputFilePath, $searchValue) {
    $foundItem = @()
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

    # Loop through each row in the worksheet, starting from row 1
    for ($i = 1; $i -le $lastRow; $i++) {
        # Check if the current row contains the search value
        if ($worksheet.Cells.Item($i, 1).Value2 -eq $searchValue -or $worksheet.Cells.Item($i, 2).Value2 -eq $searchValue) {
            # If the search value is found, get the values in the row and copy them to the array
            for ($j = 1; $j -le $worksheet.UsedRange.Columns.Count; $j++) {
                if (($j -eq 3) -and ($worksheet.Cells.Item($i, 3).Value2 -eq "")) {
                    $foundItem += "Equipo no asignado"
                } else {
                    $cell = $worksheet.Cells.Item($i, $j).Value2
                    $foundItem += $cell
                }
            }

            # Add the current date/time to the next cell
            $foundItem += $dateString

            # Add the type of registration to the next cell
            $foundItem += $tipoRegistro

            # Add the name of the person that has the computer to the next cell
            $foundItem += $foundItem[2]

            # Add the person who verifies the registration to the next cell
            $foundItem += [System.Environment]::UserName.ToUpper()

            # Exit the loop once the search value is found
            break
        }
    }
    
    # Close the input workbook and Excel application
    $workbook.Close()
    $inputFile.Quit()
    return $foundItem
}

function Add_Record_To_File ($outputFilePath, $foundItem) {
    $outputFile = New-Object -ComObject Excel.Application
    $outputWorkbook = $outputFile.Workbooks.Open($outputFilePath)
    $outputWorksheet = $outputWorkbook.Sheets.Item(1)

    # Get the last row of data in the output worksheet
    $outputLastRow = $outputWorksheet.UsedRange.Rows.Count

    # Copy the values from the input worksheet to the output worksheet
    for ($j = 1; $j -le $foundItem.Length; $j++) {
        $outputWorksheet.Cells.Item($outputLastRow + 1, $j).Value2 = $foundItem[$j-1]
    }

    # Save and close the output workbook
    $outputWorkbook.Save()
    $outputWorkbook.Close()
    $outputFile.Quit()
}

function Get_Different_Bearer ($foundItem) {
    function ValidateBearer {
        if ([string]::IsNullOrWhiteSpace($textboxBearer.Text)) {
            [System.Windows.Forms.MessageBox]::Show("Debe especificar quien lleva el equipo", "Error", "OK", "Error")
            return $true
        }
        return $false
    }
    # Create a form
    $formBearer = New-Object System.Windows.Forms.Form
    $formBearer.Text = ""
    $formBearer.Size = New-Object System.Drawing.Size(230, 120)
    $formBearer.StartPosition = "CenterScreen"
    $formBearer.ControlBox = $false
    $formBearer.MaximizeBox = $false
    $formBearer.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle

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
        if (-not (ValidateBearer)){
            $boxText = $textboxBearer.Text
            $cultureInfo = [System.Globalization.CultureInfo]::InvariantCulture
            $boxTextChanged = $cultureInfo.TextInfo.ToTitleCase($boxText.ToLower())
            $foundItem[7] = $boxTextChanged
            $formBearer.Close()
        }
    })
    $formBearer.Controls.Add($buttonBearer)
    # Show the form
    $formBearer.ShowDialog() | Out-Null
    $formBearer.Dispose()
    return $foundItem
}

function Record_Equipment {
    # Load the Excel file into a variable
    $inputFilePath = "C:\Users\andresfelipe.perez\Downloads\alm_hardware.xlsx"
    $outputFilePath = "C:\Users\andresfelipe.perez\Downloads\Minuta_computadores.xlsx"
    # $inputFilePath = "C:\Users\Peter.Cadwell\Downloads\alm_hardware.xlsx"
    # $outputFilePath = "C:\Users\Peter.Cadwell\Downloads\Minuta_computadores.xlsx"
    if ([string]::IsNullOrWhiteSpace($textboxSearch.Text)) {
        [System.Windows.Forms.MessageBox]::Show("Debe ingresar un equipo para buscar", "Error", "OK", "Error")
        return
    }
    $searchToUpper = $textboxSearch.Text.ToUpper()
    $searchValue = $searchToUpper

    $foundItem = Find_Computer $inputFilePath $searchValue

    if ($null -ne $foundItem){
        if (-not ($foundItem[2] -eq "Equipo no asignado")) {
            $bearer = $foundItem[7]
            $dialogResult = [System.Windows.Forms.MessageBox]::Show("Es $bearer quien tiene el equipo a registrar?", "Confirmation", "YesNoCancel", "Question")

            if ($dialogResult -eq "Yes") {
                Add_Record_To_File $outputFilePath $foundItem
                # Display a message to the user indicating that the data was added successfully
                [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
                Clean_Controls
            }
            elseif ($dialogResult -eq "No") {
                $modifiedFoundItem = Get_Different_Bearer $foundItem

                Add_Record_To_File $outputFilePath $modifiedFoundItem
                # Display a message to the user indicating that the data was added successfully
                [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
                Clean_Controls
            }
        } else {
            [System.Windows.Forms.MessageBox]::Show("Equipo no asignado en inventario", "Error", "OK", "Error")
            $modifiedFoundItem = Get_Different_Bearer $foundItem

            Add_Record_To_File $outputFilePath $modifiedFoundItem
            # Display a message to the user indicating that the data was added successfully
            [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
            Clean_Controls
        }
    } else {
        [System.Windows.Forms.MessageBox]::Show("El equipo no se encuentra en inventario", "Error", "OK", "Error")
        Add_Non_Asurion_Device $outputFilePath
        # Display a message to the user indicating that the data was added successfully
        [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
        Clean_Controls
    }
}

# Create a form
$form = New-Object System.Windows.Forms.Form
$form.Text = "Registration"
$form.Size = New-Object System.Drawing.Size(250, 225)
$form.StartPosition = "CenterScreen"
$form.MaximizeBox = $false
$form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle

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
            Record_Equipment
        }
        else {
            [System.Windows.Forms.MessageBox]::Show("Debe especificar si el equipo ingresa o sale del piso", "Error", "OK", "Error")
        }
    })
$form.Controls.Add($buttonRegistro)
# Show the form
$form.ShowDialog() | Out-Null