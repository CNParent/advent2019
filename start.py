import lib.loadinput
import config
import year2019.t12.p1 as task

year = 2019
day = 12

args = lib.loadinput.get(day, year, config.sessionValue)
print(task.run(args))