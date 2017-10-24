#toos to build your cron job

import getpass
from crontab import CronTab
import os



def cron_time():
    minute = input( 'what minute on the hour do you want this to run?(pick 1-60): ' )
    hour = input( 'what hour would you like this to run(pick from 1-24)?: ' )
    os.getcwd() #grabs current working directory path
    username = getpass.getuser() #grabs username to run cron under
    my_cron = CronTab( user=username)
    job = my_cron.new( command='python ' + os.getcwd() + "/" + '%s')
    job.minute.on('%s') % (minute)
    job.hour.on('%s') % (hour)

    my_cron.write()