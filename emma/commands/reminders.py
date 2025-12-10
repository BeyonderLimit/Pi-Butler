# commands/reminders.py
from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler()
scheduler.start()


def create(text):
    cal = parsedatetime.Calendar()
    time_struct, _ = cal.parse(text)
    run_time = datetime.datetime(*time_struct[:6])

    def alert():
        print("EMMA: Reminder triggered, sir.")

    scheduler.add_job(alert, 'date', run_date=run_time)
    return "Reminder set, sir."

