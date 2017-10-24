#toos to build your cron job

import getpass
from crontab import CronTab
import os



def cron_time():
    os.getcwd() #grabs current working directory path
    username = getpass.getuser() #grabs username to run cron under
    my_cron = CronTab( user=username)
    job = my_cron.new( command='python ' + os.getcwd() + "/" + '%s')
    job.minute.on('%s') % (minute)
    job.hour.on('%s') % (hour)

    my_cron.write()
