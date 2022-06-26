from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from whatsappbot import checkup_patient

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(checkup_patient, 'interval', hours=1)

sched.start()