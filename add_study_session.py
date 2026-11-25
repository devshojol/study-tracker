import json
from datetime import datetime
from common_function import get_all_sessions, create_or_update_session


def addStudySession():
    subject = input("Enter Subject: ")
    topic = input("Enter Topic: ")
    time = input("Enter Time Spent (in minutes): ")

    new_session = {
        "subject": subject.strip(),
        "topic": topic.strip(),
        "time": int(time.strip()),
        "date": datetime.now().strftime("%Y-%m-%d")
    }

    sessions = get_all_sessions()

    sessions.append(new_session)

    create_or_update_session(sessions)

    print("Study session added successfully!")
    return new_session
