from common_function import get_all_sessions

def get_session_summary():
    sessions = get_all_sessions()
    total_sessions = len(sessions)
    total_minutes = sum(session['time'] for session in sessions)
    total_hours = total_minutes // 60
    total_minutes = total_minutes % 60

    average_time = total_minutes / total_sessions if total_sessions > 0 else 0
    average_hours = int(average_time) // 60
    average_minutes = int(average_time) % 60


    print(" ===== STUDY SUMMARY =====\n")
    print(f"Total study sessions: {total_sessions}")
    print(f"Total study time: {total_hours} hours {total_minutes} minutes")
    print(f"Average session: {average_hours} hours {average_minutes} minutes")

