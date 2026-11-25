from common_function import get_all_sessions


def getSessionHistory():
    print("===== STUDY HISTORY =====\n")

    sessions = get_all_sessions()

    if not sessions:
        print("No study sessions found.")
        return


    print(
        f"{'Date':<15}"
        f"{'Subject':<15}"
        f"{'Topic':<25}"
        f"{'Duration':>10}"
    )

    print("-" * 65)

    for session in sessions:
        print(
            f"{session['date']:<15}"
            f"{session['subject']:<15}"
            f"{session['topic']:<25}"
            f"{str(session['time']) + ' min':>10}"
        )
