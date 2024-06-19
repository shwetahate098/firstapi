import netaddr

def is_valid_subnet_mask(subnet):
    try:
        is_valid = netaddr.IPAddress(subnet).is_netmask()
        if is_valid:
            return True, None
        else:
            return False, "The Subnet is not valid"
    except netaddr.core.AddrFormatError:
        return False, "The Subnet is not valid"
    
print(is_valid_subnet_mask("255.255.255.265"))

# print(netaddr.IPAddress("255.255.255.2445").is_netmask())