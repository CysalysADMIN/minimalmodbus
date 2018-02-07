#!/usr/bin/env python
#
#   Copyright 2017  Gregory HERMANT
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#

"""

.. moduleauthor:: Gregory Hermant  <>

Driver for the Aeolos wind & solar hybrid controller for communication via the Modbus RTU protocol.

"""

import minimalmodbus
#minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

__author__  = "Gregory Hermant"
__license__ = "Apache License, Version 2.0"

class Aeolos(minimalmodbus.Instrument):
    """Instrument class for Aeolos wind and solar hybrid controller. 
    
    Communicates via Modbus RTU protocol (RS485), using the *MinimalModbus* Python module.    

    Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247

    Implemented with these function codes (in decimal):
        
    ===============================  ====================
    Description         	     	 Modbus function code
    ===============================  ====================
    Input status		       		2
    Input registers				3 
    ===============================  ====================
    """
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)
    
    ## Holding registers (Modbus function: 3)

    def get_status(self):
        """Return the wind controller status."""
        return self.read_register(259, 0, 3)

    def get_vbat(self):
        """Return the battery voltage."""
        return self.read_register(4096, 1, 3)

    def get_ibat(self):
        """Return the battery current."""
        return self.read_register(4097, 1, 3)

    def get_vsolar(self):
        """Return the solar voltage."""
        return self.read_register(4098, 1, 3)

    def get_isolar(self):
        """Return the solar current."""
        return self.read_register(4099, 1, 3)
		
    def get_vwind(self):
        """Return the wind voltage."""
        return self.read_register(4100, 1, 3)

    def get_iwind_before(self):
        """Return the wind current (before)."""
        return self.read_register(4101, 1, 3)

    def get_idumpload(self):
        """Return the dump load current."""
        return self.read_register(4102, 1, 3)
    
    def get_iwind_after(self):
        """Return the wind current (after)."""
        return self.read_register(4103, 1, 3)

    def get_inttemp(self):
        """Return the wind charger internal temperature."""
        return self.read_register(4104, 1, 3)

    def get_windtspeed(self):
        """Return the rotating speed of wind turbine."""
        return self.read_register(4111, 0, 3)

    def get_sumkw(self):
        """Return the kwh cumulated energy."""
        sumkw_l = self.read_register(4107, 0, 3) 
        sumkw_h = self.read_register(4108, 0, 3) 
        return (sumkw_h * 255) + sumkw_l  

    def get_sumw(self):
        """Return the wh cumulated energy."""
        sumw_l = self.read_register(4109, 0, 3) 
        sumw_h = self.read_register(4110, 0, 3) 
        return (sumw_h * 255) + sumw_l  

#   def get_braketype(self):
#       """Return the brake type of wind turbine."""
#       return self.read_register(7, 0, 3)   

#   def set_modbus_ad(self,modbus_ad):
	"""Set the modbus address of the Aeolos controller"""
	"""Register address: 0x1999 """
	self.write_registers(6553, modbus_ad, 0)

########################
## Testing the module ##
########################

if __name__ == '__main__':

    minimalmodbus._print_out('TESTING Aeolos Modbus Wind and Solar hybrid controller')
    
    # Assume Aeolos controller connected to /dev/ttyS1
    # Default Modbus @:1, serial port parameter: 19200,8,n,1
    a = Aeolos('/dev/ttyS1', 1)
    a.debug = True
    a.handle_local_echo = False
    
    minimalmodbus._print_out( 'Battery voltage {0}'.format(a.get_vbat()) )
    minimalmodbus._print_out( 'Solar voltage {0}'.format(a.get_vsolar()) )
    minimalmodbus._print_out( 'Solar current {0}'.format(a.get_isolar()) )
    minimalmodbus._print_out( 'Wind voltage {0}'.format(a.get_vwind()) )
    minimalmodbus._print_out( 'Wind current (before) {0}'.format(a.get_iwind_before()) )
    minimalmodbus._print_out( 'Wind current (after) {0}'.format(a.get_iwind_after()) )
    minimalmodbus._print_out( 'Rotating speed of wind turbine {0}'.format(a.get_windtspeed()) )
    minimalmodbus._print_out( 'Brake Type {0}'.format(a.get_braketype()) )

    minimalmodbus._print_out( 'DONE!' )

pass    
