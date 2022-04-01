import argparse
import sys
import os
parser = argparse.ArgumentParser(description="Live view of a program, instant reload of a program")
parser.add_argument("-run", required=True, help="Used as; APPNAME:RUNTYPE:STATE, required=True.")
args = parser.parse_args(sys.argv[1:])
#args.run => Gives the components based of the argparsers libary, via Namespace class
rn = []
appstr = ""
runtime = "0"
for i in args.run.split(":"):
    rn.append(i)
if len(rn) >> 2:
    print("[ERROR] You cannot pass more than three arguments to -run, please try again as: APPNAME:RUNTYPE:STATE")
    exit()

for i in range(len(rn)):
    #1 => get app
    #2 => detect runtype
    #3 => check if state is recogniseable.
    if i == 0:
        a = rn[i]
        with open(f"{a}.py", "r") as b:
            appstr = b.read()

    if i == 1:
        a = rn[i]
        if a == "live":
            runtime = a

    if i == 2:
        a = rn[i]
        if a == "full":
            continue
        else:
            print("[ERROR] State is not recognisable; did you mean full or vairous (Currently, only full allowed.)")
            exit()

exec(appstr)

while 1:
    appstr_save = appstr
    appstr = open(f"{rn[0]}.py", "r").read()
    if appstr != appstr_save:
        os.system("cls")
        exec(appstr)

