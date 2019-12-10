import lib.loadinput
import config
import year2019.t09.p1 as task

year = 2019
day = 9

args = lib.loadinput.get(day, year, config.sessionValue)
print(task.run(args))