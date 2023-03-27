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

# Load the Excel file into a variable
$global:InputFilePath = "C:\Users\andresfelipe.perez\Downloads\alm_hardware.xlsx"
$global:OutputFilePath = "C:\Users\andresfelipe.perez\Downloads\Minuta_computadores.xlsx"
# $inputFilePath = "C:\Users\Peter.Cadwell\Downloads\alm_hardware.xlsx"
# $outputFilePath = "C:\Users\Peter.Cadwell\Downloads\Minuta_computadores.xlsx"

$global:InputExcelApp = New-Object -ComObject Excel.Application
$global:InputWorkbook = $global:InputExcelApp.Workbooks.Open($inputFilePath)


function Clean_Controls {
    $textboxSearch.Text = ""
    $radioIngreso.Checked = $false
    $radioRetiro.Checked = $false
}

function Add_Non_Asurion_Device {
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
            [System.Windows.Forms.MessageBox]::Show([System.Text.RegularExpressions.Regex]::Unescape("Indique el n\u00FAmero serial del equipo"), "Error", "OK", "Error")
            return $true
        } elseif ([string]::IsNullOrWhiteSpace($textboxModel.Text)) {
            [System.Windows.Forms.MessageBox]::Show("Indique el modelo o referencia del equipo", "Error", "OK", "Error")
            return $true
        } elseif ([string]::IsNullOrWhiteSpace($textboxBearer.Text)) {
            [System.Windows.Forms.MessageBox]::Show([System.Text.RegularExpressions.Regex]::Unescape("Indique qui\u00E9n lleva el equipo"), "Error", "OK", "Error")
            return $true
        }
        return $false
    }
    # Create a form
    $form = New-Object System.Windows.Forms.Form
    $form.Text = ""
    $form.Size = New-Object System.Drawing.Size(400, 280)
    $form.StartPosition = "CenterScreen"
    $form.ControlBox = $false
    $form.MaximizeBox = $false
    $form.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle

    # Create labels and textboxes
    $labelSerial = New-Object System.Windows.Forms.Label
    $labelSerial.Location = New-Object System.Drawing.Point(20, 20)
    $labelSerial.Size = New-Object System.Drawing.Size(100, 20)
    $labelSerial.Text = [System.Text.RegularExpressions.Regex]::Unescape("N\u00FAmero serial:")
    $form.Controls.Add($labelSerial)

    $textboxSerial = New-Object System.Windows.Forms.TextBox
    $textboxSerial.Location = New-Object System.Drawing.Point(150, 20)
    $textboxSerial.Size = New-Object System.Drawing.Size(200, 20)
    $form.Controls.Add($textboxSerial)
    $textboxSerial.Text = $textboxSearch.Text

    $labelModel = New-Object System.Windows.Forms.Label
    $labelModel.Location = New-Object System.Drawing.Point(20, 60)
    $labelModel.Size = New-Object System.Drawing.Size(100, 20)
    $labelModel.Text = "Modelo:"
    $form.Controls.Add($labelModel)

    $textboxModel = New-Object System.Windows.Forms.TextBox
    $textboxModel.Location = New-Object System.Drawing.Point(150, 60)
    $textboxModel.Size = New-Object System.Drawing.Size(200, 20)
    $form.Controls.Add($textboxModel)

    $labelType = New-Object System.Windows.Forms.Label
    $labelType.Location = New-Object System.Drawing.Point(20, 100)
    $labelType.Size = New-Object System.Drawing.Size(120, 20)
    $labelType.Text = "Tipo de dispositivo:"
    $form.Controls.Add($labelType)

    $dropdownType = New-Object System.Windows.Forms.ComboBox
    $dropdownType.Location = New-Object System.Drawing.Point(150, 100)
    $dropdownType.Size = New-Object System.Drawing.Size(200, 20)
    $dropdownType.DropDownStyle = [System.Windows.Forms.ComboBoxStyle]::DropDownList
    $dropdownType.Items.Add("")
    $dropdownType.Items.Add("PC / Laptop")
    $dropdownType.Items.Add("Otro")
    $dropdownType.SelectedIndex = 0
    $form.Controls.Add($dropdownType)

    $labelBearer = New-Object System.Windows.Forms.Label
    $labelBearer.Location = New-Object System.Drawing.Point(20, 140)
    $labelBearer.Size = New-Object System.Drawing.Size(200, 20)
    $labelBearer.Text = "Nombre de quien lleva el equipo:"
    $form.Controls.Add($labelBearer)

    $textboxBearer = New-Object System.Windows.Forms.TextBox
    $textboxBearer.Location = New-Object System.Drawing.Point(220, 140)
    $textboxBearer.Size = New-Object System.Drawing.Size(130, 20)
    $form.Controls.Add($textboxBearer)

    $labelAdditional = New-Object System.Windows.Forms.Label
    $labelAdditional.Location = New-Object System.Drawing.Point(20, 180)
    $labelAdditional.Size = New-Object System.Drawing.Size(200, 20)
    $labelAdditional.Text = [System.Text.RegularExpressions.Regex]::Unescape("Informaci\u00F3n adicional:")
    $form.Controls.Add($labelAdditional)

    $textboxAdditional = New-Object System.Windows.Forms.TextBox
    $textboxAdditional.Location = New-Object System.Drawing.Point(220, 180)
    $textboxAdditional.Size = New-Object System.Drawing.Size(130, 20)
    $form.Controls.Add($textboxAdditional)

    # Create a button for bearer
    $buttonAddDevice = New-Object System.Windows.Forms.Button
    $buttonAddDevice.Location = New-Object System.Drawing.Point(90, 230)
    $buttonAddDevice.Size = New-Object System.Drawing.Size(200, 30)
    $buttonAddDevice.Text = "Registrar"
    $buttonAddDevice.Add_Click({
        if (-not (ValidateTextbox)){
            $newComputer = @()
            $newComputer += $textboxSerial.Text
            $newComputer += "N/A"
            $newComputer += "N/A"
            $newComputer += $textboxModel.Text
            if ((-not ($dropdownType.SelectedItem -eq ""))) {
                $newComputer += $dropdownType.SelectedItem
            } else {
                [System.Windows.Forms.MessageBox]::Show("Seleccione el tipo de dispositivo", "Error", "OK", "Error")
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
            $form.Close()
            $form.Dispose()
            Add_Record_To_File $newComputer
        }
    })
    $form.Controls.Add($buttonAddDevice)
    # Show the form
    $form.ShowDialog() | Out-Null
}

function Find_Computer($searchValue) {
    $foundItem = @()
    
    $worksheet = $global:InputWorkbook.Sheets.Item(1)
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
                    $foundItem += "No asignado"
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
    return $foundItem
}

function Add_Record_To_File ($foundItem) {
    $outputExcelApp = New-Object -ComObject Excel.Application
    $outputWorkbook = $outputExcelApp.Workbooks.Open($global:OutputFilePath)
    $outputWorksheet = $outputWorkbook.Sheets.Item(1)

    # Get the last row of data in the output worksheet
    $outputLastRow = $outputWorksheet.UsedRange.Rows.Count

    # Copy the values from the input worksheet to the output worksheet
    for ($j = 1; $j -le $foundItem.Length; $j++) {
        $outputWorksheet.Cells.Item($outputLastRow + 1, $j).Value2 = $foundItem[$j-1]
    }

    $outputWorkbook.Save()
    $outputWorkbook.Close()

    $outputExcelApp.Quit()

    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($outputExcelApp) | Out-Null
}

function Get_Different_Bearer ($foundItem) {
    function ValidateBearer {
        if ([string]::IsNullOrWhiteSpace($textboxBearer.Text)) {
            [System.Windows.Forms.MessageBox]::Show([System.Text.RegularExpressions.Regex]::Unescape("Indique qui\u00E9n lleva el equipo"), "Error", "OK", "Error")
            return $true
        }
        return $false
    }
    # Create a form
    $formBearer = New-Object System.Windows.Forms.Form
    $formBearer.Text = ""
    $formBearer.Size = New-Object System.Drawing.Size(237, 178)
    $formBearer.StartPosition = "CenterScreen"
    $formBearer.ControlBox = $false
    $formBearer.MaximizeBox = $false
    $formBearer.FormBorderStyle = [System.Windows.Forms.FormBorderStyle]::FixedSingle

    # Create a label and text box for bearer
    $labelBearer = New-Object System.Windows.Forms.Label
    $labelBearer.Location = New-Object System.Drawing.Point(19, 50)
    $labelBearer.Size = New-Object System.Drawing.Size(200, 20)
    $labelBearer.Text = [System.Text.RegularExpressions.Regex]::Unescape("Qui\u00E9n lleva el equipo?")
    $formBearer.Controls.Add($labelBearer)

    $textboxBearer = New-Object System.Windows.Forms.TextBox
    $textboxBearer.Location = New-Object System.Drawing.Point(19, 80)
    $textboxBearer.Size = New-Object System.Drawing.Size(200, 20)
    $formBearer.Controls.Add($textboxBearer)

    # Create a button for bearer
    $buttonBearer = New-Object System.Windows.Forms.Button
    $buttonBearer.Location = New-Object System.Drawing.Point(19, 110)
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
    if ([string]::IsNullOrWhiteSpace($textboxSearch.Text)) {
        [System.Windows.Forms.MessageBox]::Show("Ingrese un equipo para buscar", "Error", "OK", "Error")
        return
    }
    $searchToUpper = $textboxSearch.Text.ToUpper()
    $searchValue = $searchToUpper

    $foundItem = Find_Computer $searchValue

    if ($null -ne $foundItem){
        if (-not ($foundItem[2] -eq "No asignado")) {
            $bearer = $foundItem[7]
            $dialogResult = [System.Windows.Forms.MessageBox]::Show("Es $bearer quien tiene el equipo a registrar?", "Confirmation", "YesNoCancel", "Question")

            if ($dialogResult -eq "Yes") {
                Add_Record_To_File $foundItem
                # Display a message to the user indicating that the data was added successfully
                [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
                Clean_Controls
            }
            elseif ($dialogResult -eq "No") {
                $modifiedFoundItem = Get_Different_Bearer $foundItem

                Add_Record_To_File $modifiedFoundItem
                # Display a message to the user indicating that the data was added successfully
                [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
                Clean_Controls
            }
            elseif ($dialogResult -eq "Cancel") {
                Clean_Controls
            }
        } else {
            [System.Windows.Forms.MessageBox]::Show([System.Text.RegularExpressions.Regex]::Unescape("Este equipo a\u00FAn no est\u00E1 asignado en inventario"), "Error", "OK", "Error")
            $modifiedFoundItem = Get_Different_Bearer $foundItem

            Add_Record_To_File $modifiedFoundItem
            # Display a message to the user indicating that the data was added successfully
            [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
            Clean_Controls
        }
    } else {
        [System.Windows.Forms.MessageBox]::Show("El equipo no fue encontrado. Posibles razones:`n`n- Puede que no sea un PC o una laptop`n- Puede ser propiedad de Asurion pero en otro pais`n- Puede no ser propiedad de Asurion`n`n De clic en OK para registrarlo.", "Error", "OK", "Error")
        Add_Non_Asurion_Device
        # Display a message to the user indicating that the data was added successfully
        [System.Windows.Forms.MessageBox]::Show("Registro agregado exitosamente.", "", "OK", "Information")
        Clean_Controls
    }
}

# Event handler for FormClosing event
$handler_FormClosing = {
    # Save and close the output workbook
    $global:InputWorkbook.Save()
    $global:InputWorkbook.Close()

    # Quit Excel and release the object
    $global:InputExcelApp.Quit()
    
    [System.Runtime.Interopservices.Marshal]::ReleaseComObject($global:InputExcelApp) | Out-Null
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
$labelSearch.Location = New-Object System.Drawing.Point(25, 20)
$labelSearch.Size = New-Object System.Drawing.Size(200, 20)
$labelSearch.Text = "Ingrese el equipo a buscar:"
$form.Controls.Add($labelSearch)

$textboxSearch = New-Object System.Windows.Forms.TextBox
$textboxSearch.Location = New-Object System.Drawing.Point(25, 40)
$textboxSearch.Size = New-Object System.Drawing.Size(200, 20)
$form.Controls.Add($textboxSearch)

$radioIngreso = New-Object System.Windows.Forms.RadioButton
$radioIngreso.Location = New-Object System.Drawing.Point(25, 70)
$radioIngreso.Size = New-Object System.Drawing.Size(200, 30)
$radioIngreso.Text = "Ingreso de equipo"
$form.Controls.Add($radioIngreso)

$radioRetiro = New-Object System.Windows.Forms.RadioButton
$radioRetiro.Location = New-Object System.Drawing.Point(25, 100)
$radioRetiro.Size = New-Object System.Drawing.Size(200, 30)
$radioRetiro.Text = "Retiro de equipo"
$form.Controls.Add($radioRetiro)

# Create a button for Registrar equipo
$buttonRegistro = New-Object System.Windows.Forms.Button
$buttonRegistro.Location = New-Object System.Drawing.Point(25, 140)
$buttonRegistro.Size = New-Object System.Drawing.Size(200, 30)
$buttonRegistro.Text = "Registrar"
$form.add_FormClosing($handler_FormClosing)
$buttonRegistro.Add_Click({
        if ($radioIngreso.Checked -or $radioRetiro.Checked) {
            Record_Equipment
        }
        else {
            [System.Windows.Forms.MessageBox]::Show("Indique si el equipo ingresa o sale del piso", "Error", "OK", "Error")
        }
    })
$form.Controls.Add($buttonRegistro)

# Show the form
$form.ShowDialog() | Out-Null

Unregister-Event -SourceIdentifier FormClosing
[System.Runtime.Interopservices.Marshal]::ReleaseComObject($global:InputExcelApp) | Out-Null