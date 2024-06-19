from flask import Flask, request, jsonify
import ipaddress
import netaddr
from netaddr import *
 
app = Flask(__name__)
 
class IPAddressValidator:
    def __init__(self, ip, subnet, gateway):
        self.ip = ip
        self.subnet = subnet
        self.gateway = gateway
 
    def validate_ip_address(self):
        try:
            ip_object = ipaddress.ip_address(self.ip)
            if IPAddress(self.ip).is_loopback() is True:
                return False, "This IP is reserved for loopback"
            elif IPAddress(self.ip).is_multicast() is True:
                return False, "This IP is reserved for Multicast"
            elif IPAddress(self.ip).is_netmask() is True:
                return False, "This IP is reserved for Netmask"
            elif IPAddress(self.ip).is_hostmask() is True:
                return False, "This IP is reserved for HostMask"
            elif IPAddress(self.ip).is_reserved() is True:
                return False, "This IP is reserved for Reserved"
            else:
                return True, None
        except ValueError as e:
            return False, "The IP address is not valid"
        
    def is_valid_subnet_mask(self):
        try:
            is_valid = netaddr.IPAddress(self.subnet).is_netmask()
            if is_valid:
                return True, None
            else:
                return False, "The Subnet is not valid"
        except netaddr.core.AddrFormatError:
            return False, "The Subnet is not valid"
 
   
    def validate_gateway(self):
        try:
            ipaddress.ip_address(self.gateway)
            return True, None
        except ValueError as e:
            return False, "The Gateway address is not valid"
 
 
    def validate(self):
        try:
            IP_SUBNET = self.ip + "/" + self.subnet
            ADDRESS = ipaddress.IPv4Interface(IP_SUBNET)
            #
            NETWORK_ADDRESS = ADDRESS.network        
            #
            IP_ADDRESS = ADDRESS.ip
            #
            BROADCAST_ADDRESS = NETWORK_ADDRESS.broadcast_address
            #
            NETWORK_ADDRESS = NETWORK_ADDRESS.network_address
       
           
            if self.gateway == str(IP_ADDRESS):
                return False,"Gateway is can not be same as IP address"
            elif str(IP_ADDRESS) == str(BROADCAST_ADDRESS):
                return False,"IP address can not be same as BROADCAST_ADDRESS "
            elif str(IP_ADDRESS) == str(NETWORK_ADDRESS):
                return False,"IP_ADDRESS can not be same as NETWORK_ADDRESS "
            elif self.gateway == str(NETWORK_ADDRESS):
                return False,"Gateway  can not be same as NETWORK_ADDRESS"
            elif self.gateway == str(BROADCAST_ADDRESS):
                return False,"Gateway can not be same as BROADCAST_ADDRESS"
            # elif ipaddress.IPv4Address(self.gateway) in ipaddress.IPv4Network(NETWORK_ADDRESS):
            # elif ipaddress.ip_address(self.gateway) not in ipaddress.IPv4Network(IP_SUBNET):
            #     return False, "Gateway is not in range of NETWORK_ADDRESS"
            elif ipaddress.ip_address(self.gateway) not in ipaddress.ip_network(ADDRESS.network):
                return False, "Gateway or IP address is out of range."
            else:
                return True, None
       
        except ValueError as e:
            return False, None
 
@app.route('/validate-ip', methods=['POST'])
def validate_ip():
    data = request.json
    ip = data.get('ip')
    subnet = data.get('subnet')
    gateway = data.get('gateway')
   
    validator = IPAddressValidator(ip, subnet, gateway)
  
    is_valid_ip, IP_error_msg = validator.validate_ip_address()
    is_valid_subnet, subnet_error_msg = validator.is_valid_subnet_mask()
    is_valid_gateway, gateway_error_msg = validator.validate_gateway()    
    result, result_error_msg= validator.validate()
    error_msgs = []
   
    if not is_valid_ip:
        error_msgs.append(IP_error_msg)
    if not is_valid_subnet:
        error_msgs.append(subnet_error_msg)
    if not is_valid_gateway:
        error_msgs.append(gateway_error_msg)
 
    if error_msgs:
        return jsonify({'success':False, 'message':error_msgs})
    elif result_error_msg:
        return jsonify({'success':False,'message' : result_error_msg})        
    else:
        return jsonify({'success':True,'message': True})
       
if __name__ == '__main__':
    app.run(debug=True)