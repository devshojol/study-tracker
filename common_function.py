import json


def get_all_sessions(filepath="session.json"):
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        return []

def create_or_update_session(session_data, filepath="session.json"):

  with open(filepath, "w", encoding="utf-8") as file:
      json.dump(session_data, file, indent=4)
