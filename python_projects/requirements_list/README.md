**Requirements Extraction Program**

This program is created to extract software requirements from PDF files to a csv for traceability purposes 

How to run:
1. Install the requirement.txt using command pip install -r requirements.txt (Best Practice: Create a virtual environment before installing libraries)
2. Rename your SAD or SRS file to SAD.pdf or SRS.pdf and put in the same directory as the file extract_requirements.py
3. Run the python file extract_requirements.py using command python3 extract_requirements.py
4. requirement_list.csv will show up in the directory after running.


#To Do
1. Add variable input for files name
2. Add variable input for requirement initial

Note: For some reason the requirement SAD/SRS pdf file gets corrupted and can fail the file from running. Testing only done for 1 page documents. Will update after more pages are tested. I will soon update an example SAD and SRS for testing along with a sample result.

Limitation: Currently it can only extract requirements that are labeled with an ID e.g: ABCDSRS001 or ABCDSAD001