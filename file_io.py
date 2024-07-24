import pathlib
import shutil

#Create a path object representing current working directory using pathlib
current_directory = pathlib.Path.cwd()

print("Current directory:", current_directory)


#New folder folder_week11; create it if it does not exist
folder_week11_path = current_directory / "folder_week11"
if not folder_week11_path.exists():
  folder_week11_path.mkdir()

#New text file week11.txt inside folder_week11
week11_file_path = folder_week11_path / "week11.txt"
week11_file_path.touch()

#Write text to week11.txt
text_write =  "Test: Writing to file."
with open(week11_file_path, 'w') as file:
  file.write(text_write)

#Print out file contents using read() to confirm text was written
with open(week11_file_path, 'r') as file:
  file_contents = file.read()
  print("Contents:", file_contents)

# New folder folder2_week11; create a new directory if it doesn't exist
folder2_week11_path = current_directory / "folder2_week11"
if not folder2_week11_path.exists():
  folder2_week11_path.mkdir()

# New text file week11_2.txt inside folder2_week11
week11_2_file_path = folder2_week11_path / "week11_2.txt"
week11_2_file_path.touch()

#Navigate back to folder_week11 directory
folder_week11_path = current_directory / "folder_week11"

#Print using rglob() from folder_week11
print("Text files from 'folder_week11' and its subdirectories:")
for file in folder_week11_path.rglob("*.txt"):
  print(file)