import telnetlib
import getpass

def get_ip(f):
 ip = f.readline()
 return ip
def connect(ip):
 telnet = telnetlib.Telnet(ip)
 print telnet.read_until(":")
 telnet.write("tom\r")
 print telnet.read_until("Password:")
 telnet.write("rkhknp\r")
 telnet.read_until(">",2)
 i = 1
 try:
   print tn.read_until("""#""",0.5)
 except Exception:
   i = 0
 if i == 0:
  telnet.write("enable\r")
  telnet.read_until("Password:")
  telnet.write("Meg@Pup$\r")
 telnet.read_until("""#""")
 telnet.read_until("""#""")
 telnet.write("config terminal\r")
 telnet.read_until("(config)")
 telnet.write("logging 195.20.96.8 facility local1 level informational")
 telnet.read_until("""#""")
 telnet.write("exit/r")
 telnet.read_until("""#""")
 telnet.write("write/r")
 telnet.read_until("[Y/N]:")
 telnet.write("yes")
 telnet.close()
f = open('/home/tom/testplace/ip_db.txt', 'r')
ip = "10.110.67.13"
while ip <> "End":
 ip = get_ip(f)
 print ip
 connect(ip)
