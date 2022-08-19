Use the python file to extract requirements from your SAD or SRS pdf files and put them as a dataframe in a csv file. 

How to run:
1. Install the requirement.txt using command pip install -r requirements.txt (Best Practice: Create a virtual environment before installing libraries)
2. Rename your SAD or SRS file to SAD.pdf or SRS.pdf and put in the same directory as the file extract_requirements.py
3. Run the python file extract_requirements.py using command python3 extract_requirements.py
4. requirement_list.csv will show up in the directory after running. (Example provided in the directory)


#To Do
1. Add variable input for files name
2. Add variable input for requirement initial

Note: For some reason the requirement SAD/SRS pdf file gets corrupted and can fail the file from running
