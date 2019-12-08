import lib.loadinput
import config
import year2019.t08.p2 as task

year = 2019
day = 8

args = lib.loadinput.get(day, year, config.sessionValue)
print(task.run(args))