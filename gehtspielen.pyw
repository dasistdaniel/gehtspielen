import ctypes
import sched
import time
import os
import argparse

parser = argparse.ArgumentParser(description='gehtspielen - time based logout')
parser.add_argument('name', action="store")

dateiname = 'zeit.save'
intervall = 60 # Sekunden
maxtime = 5

def main():
    datum = time.strftime("%d.%m.%Y")
    print datum

    zeit = loadtime(dateiname,datum)
    print str(zeit)
    if zeit > maxtime:
        kill()
    
    s = sched.scheduler(time.time, time.sleep)
    s.enter(intervall, 1, do_something, (s,datum,zeit))
    s.run()
    
def do_something(sc,datum,alu):
    alu = alu + 1
    if alu > maxtime:
        kill()
    print "saving " + str(alu)
    savetime(dateiname, datum, alu)
    sc.enter(intervall, 1, do_something, (sc,datum,alu))

def loadtime(datei,datum):
    if os.path.isfile(datei):
        f = open(datei,'r')
        raw = f.read().split(',')
        print raw
        if datum == raw[0]:
            data = raw[1]
        else:
            data = 0
        f.close()
    else:
        data = 0
    return int(data)
    
def savetime(datei, datum, zeit):
    f = open(datei, 'w')
    f.write(datum + ',' + str(zeit))
    f.close()
    
def kill():
    #ctypes.windll.user32.ExitWindowsEx(0, 1)
    print "kill"

if __name__ == "__main__":
    main()




