import subprocess


command =['python', 'reminder.py']
while True:
            # Execute the command
            result = subprocess.run(command)
            
            # Check the return code to determine if the process completed successfully
            if result.returncode == 0:
                print("Process completed successfully.")
                break  # Exit the loop if the process completed successfully
            else:
                print("Process exited with a non-zero return code:", result.returncode)

