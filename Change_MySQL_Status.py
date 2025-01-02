import subprocess
command_start_server = 'net start MySQL80'
command_stop_server = 'net stop MySQL80'

def change_mysql_status():
    try:
        result = subprocess.run('sc query MySQL80', capture_output=True, text=True, shell=True)
        if 'RUNNING' in result.stdout:
            subprocess.run(command_stop_server, shell=True)
            print('The server is turned off')
        else:
            subprocess.run(command_start_server, shell=True)
            print('The server is turned on')
    except subprocess.CalledProcessError as e:
        print('Execution error')

change_mysql_status()