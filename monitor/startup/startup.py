import sys
import os

os.system("sudo service zookeeper start")
os.system("/srv/storm/bin/storm nimbus &")
os.system("/srv/storm/bin/storm supervisor &")
os.system("/srv/storm/bin/storm ui &")
os.system("Storm UI")

