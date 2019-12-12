import lib.loadinput
import config
import year2019.t11.p1 as task

year = 2019
day = 11

args = lib.loadinput.get(day, year, config.sessionValue)
print(task.run(args))