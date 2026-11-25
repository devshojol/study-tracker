from add_study_session import addStudySession
from get_session_history import getSessionHistory
selectedOptionNum = input("===== PYTHON STUDY TRACKER =====\n\n1. Add study session\n2. View study sessions\n3. View study summary\n4. Exit\n\nChoose an option:")

if selectedOptionNum == "1":
  addStudySession()
elif selectedOptionNum == "2":
  getSessionHistory()
elif selectedOptionNum == "3":
  pass
elif selectedOptionNum == "4":
  pass
else:
  print("Invalid option. Please choose a valid option.")
