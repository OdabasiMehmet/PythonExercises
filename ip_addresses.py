# Implement a function that receives two IPv4 addresses, and returns the number of addresses between them (including the first one, excluding the last one).

# All inputs will be valid IPv4 addresses in the form of strings. The last address will always be greater than the first one.

# Examples

# With input "10.0.0.0", "10.0.0.50" => return 50
# With input "10.0.0.0", "10.0.1.0" => return 256
# With input "20.0.0.10", "20.0.1.0" => return
# 0-255.0-255.0-255.0-255

# 11111111.11111111.11111111.11111111

# 11 00 01 10

# 2^8 * 2^8 * 2^8 * 2^8
def find_ip(start, end) :
    
  start = list(map(int,start.split(".")))
  end = list(map(int,end.split("."))) 

  for i in range(3) :
    end[i+1] += (end[i] - start[i])*256
  return (end[3]-start[3])

print(find_ip("20.0.0.10", "20.0.1.0"))