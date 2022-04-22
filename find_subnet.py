# Write a program that finds subnet address for a host with a given IP address
def network_id(ipaddress) :
  ex = ipaddress.split("/")
  ip = ex[0]
  cidr = int(ex[1])
  list_ip = list(map(int,ip.split(".")))
  octet = cidr // 8
  kalan = cidr % 8
  list_ip[octet] = 2**(8-kalan)  * (list_ip[octet] // 2**(8-kalan))
  for i in range(octet+1,4) :
    list_ip[i] = 0
  
  return ".".join(list(map(str,list_ip)))


ip = "200.10.5.68/12"
print(network_id(ip))