from add_study_session import addStudySession
from get_session_history import getSessionHistory
from get_session_summary import get_session_summary
import os
import subprocess

selectedOptionNum = input("===== PYTHON STUDY TRACKER =====\n\n1. Add study session\n2. View study sessions\n3. View study summary\n4. Exit\n\nChoose an option:")

if selectedOptionNum == "1":
  addStudySession()
elif selectedOptionNum == "2":
  getSessionHistory()
elif selectedOptionNum == "3":
  get_session_summary()
elif selectedOptionNum == "4":
  command = "cls" if os.name == "nt" else "clear"
  subprocess.run(command, shell=True, check=False)
else:
  print("Invalid option. Please choose a valid option.")
