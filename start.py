import lib.loadinput
import config
import year2019.t07p2 as task

year = 2019
day = 7

args = lib.loadinput.get(day, year, config.sessionValue)
print(task.run(args))