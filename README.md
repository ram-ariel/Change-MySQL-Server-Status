# Change MySQL Server Status Tool  

This tool allows you to quickly change the status of the MySQL service on Windows with ease.  

## Features  
- Turn the MySQL service on/off with a simple executable file.  
- No need to open Command Prompt or remember service commands.  

---

## How to Use  

### 1. Download the Python Script  
- Download the `.py` file from this repository.  
- Replace `"MySQL80"` in the code with your MySQL service's name (as shown in Windows Services).  

### 2. Create an Executable File  
1. Open Command Prompt with **administrator privileges**.  
2. Run the following commands to install PyInstaller and generate the executable:  
   ```bash
   pip install pyinstaller
   pyinstaller --onefile --name "Change MySQL Server Status" path

  Replace `path` with the full path to the `.py` file.  

### 3. Locate the Executable  
- Navigate to the `dist` folder created by PyInstaller.  
- Move the `.exe` file to your desired location.  

### 4. Configure the Executable  
1. Right-click on the `.exe` file.  
2. Go to **Properties** → **Compatibility**.  
3. Check **Run this program as an administrator** and apply the changes.  

### 5. Run the Tool  
- Simply double-click the `.exe` file whenever you want to toggle the MySQL service **on/off**.  
