This code is used to quickly change the status of MySQL service on Windows. Follow these instructions:

1_ Download the .py file. Just replace "MySQL80" with your MySQL service's name

2_ Open the Command Prompt with administrator privileges and enter the following commands:

  pip install pyinstaller
  
  pyinstaller --onefile --name 'Change MySQL server status' {path}, replace {path} with the path to the .py file.
  
3_ Locate the "dist" folder and move the executable file to your desired location.

4_ Right-click on the file, go to Properties, then Compatibility, check 'Run as administrator,' and apply the changes.

Just doubleclick the .exe file when you want to turn MySQL service off/on.
That's it, enjoy!
