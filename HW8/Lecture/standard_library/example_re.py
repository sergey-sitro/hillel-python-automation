import re
# https://docs.python.org/3/library/re.html

example_str = "some random example string"
print(re.search(r"^some.*string$", example_str))
print(re.search(r"^other.*string$", example_str))


print(re.findall(r"om", example_str))
print(re.findall(r"test", example_str))

print(re.split(r"\s", example_str, 1))

print(re.sub(r"example", "test", example_str))
print(re.sub(r"\s", "-", example_str))
print(re.sub(r"\s", "-", example_str, 1))

log = 'Jun  3 14:39:05.941: %SW_MATM-4-MACFLAP_NOTIF: Host f03a.b216.7ad7 in vlan 10 is flapping between port Gi0/5 and port Gi0/15'
match = re.search(r'Host (\S+) in vlan (\d+) .* port (\S+) and port (\S+)', log)
print(match.group())
print(match.groups())
print(match.group(0))
print(match.group(1))
print(match.group(1, 3))

match = re.search(r'Host (?P<mac>\S+) in vlan (?P<vlan>\d+) .* port (?P<int1>\S+) and port (?P<int2>\S+)', log)
print(match.group('mac'))
print(match.group('int2'))
print(match.groupdict())

line = '100     aab1.a1a1.a5d3    FastEthernet0/1'
match = re.search(r'(\d+)\s+(\w+)?', line)
print(match.groups())

line = '100     '
match = re.search(r'(\d+)\s+(\w+)?', line)
print(match.groups())


line = '  10     aab1.a1a1.a5d3    FastEthernet0/1  '
match = re.search(r'(?P<val>\d+)\s+([0-9a-f.]+)\s+(\S+)', line)
print(match.span())
print(line[match.start():match.end()])
print(match.span("val"))


regex = re.compile(r'(?P<val>\d+)\s+([0-9a-f.]+)\s+(\S+)')
match = regex.search(line)
print(match.group())


###

log_file = """
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/16 and port Gi0/24
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/19
%SW_MATM-4-MACFLAP_NOTIF: Host 01e2.4c18.0156 in vlan 10 is flapping between port Gi0/24 and port Gi0/16
"""

regex = (r'Host \S+ '
         r'in vlan (\d+) '
         r'is flapping between port '
         r'(\S+) and port (\S+)')

ports = set()

for line in log_file.split("\n"):
    match = re.search(regex, line)
    if match:
        vlan = match.group(1)
        ports.add(match.group(2))
        ports.add(match.group(3))
print(ports)



###


output = '''
R1#show ip interface brief
Interface             IP-Address      OK? Method Status           Protocol
FastEthernet0/0       15.0.15.1       YES manual up               up
FastEthernet0/1       10.0.12.1       YES manual up               up
FastEthernet0/2       10.0.13.1       YES manual up               up
FastEthernet0/3       unassigned      YES unset  up               up
Loopback0             10.1.1.1        YES manual up               up
Loopback100           100.0.0.1       YES manual up               up
'''


result = re.finditer(r'(\S+) +([\d.]+) +\w+ +\w+ +(up|down|administratively down) +(up|down)', output)
groups = []
for m in result:
    print(m)
    groups.append(m.groups())
print(groups)



###


mac_address_table = """
          Mac Address Table
-------------------------------------------

Vlan    Mac Address       Type        Ports
----    -----------       --------    -----
 100    a1b2.ac10.7000    DYNAMIC     Gi0/1
 200    a0d4.cb20.7000    DYNAMIC     Gi0/2
 300    acb4.cd30.7000    DYNAMIC     Gi0/3
 100    a2bb.ec40.7000    DYNAMIC     Gi0/4
 500    aa4b.c550.7000    DYNAMIC     Gi0/5
 200    a1bb.1c60.7000    DYNAMIC     Gi0/6
 300    aa0b.cc70.7000    DYNAMIC     Gi0/7
"""

print(re.findall(r'(\d+) +(\S+) +\w+ +(\S+)', mac_address_table))


###


example_text = """
In lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit. In voluptate velit esse cillum dolore eu fugiat nulla pariatur.
Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
"""
print(example_text.count("in"))

regex = re.compile(r"\b(in)\b", re.IGNORECASE)
print(len(regex.findall(example_text)))



###



sentence = 'I need need to learn regex regex from scratch!'
print(re.sub(r'\b(\w+)( \1\b)+', r'\1', sentence))
