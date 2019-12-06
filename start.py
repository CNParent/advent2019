import lib.loadinput
import config
import year2019.t06p2 as task

year = 2019
day = 6

args = lib.loadinput.get(day, year, config.sessionValue)
print(task.run(args))