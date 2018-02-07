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

Driver for the ADAM-4117 ADC, for communication via the Modbus RTU protocol.

"""

import minimalmodbus
#minimalmodbus.CLOSE_PORT_AFTER_EACH_CALL = True

__author__  = "Gregory Hermant"
__license__ = "Apache License, Version 2.0"


class Adam_4117(minimalmodbus.Instrument):
    """Instrument class for ADAM-4117 ADC module. 
    
    Communicates via Modbus RTU protocol (RS485), using the *MinimalModbus* Python module.    

    Args:
        * portname (str): port name
        * slaveaddress (int): slave address in the range 1 to 247

    Implemented with these function codes (in decimal):
        
    ===============================  ====================
    Description         	     Modbus function code
    ===============================  ====================
    Input status		        2
    Holding registers			4 
    ===============================  ====================

    """
    
    def __init__(self, portname, slaveaddress):
        minimalmodbus.Instrument.__init__(self, portname, slaveaddress)

    ## Binary inputs (Modbus function: 2)

    def get_burnout_ch0(self):
    	"""Return burnout channel 0."""
    	return self.read_bit(0, 2) == 1

    def get_burnout_ch1(self):
    	"""Return burnout channel 1."""
    	return self.read_bit(1, 2) == 1

    def get_burnout_ch2(self):
    	"""Return burnout channel 2."""
    	return self.read_bit(2, 2) == 1

    def get_burnout_ch3(self):
    	"""Return burnout channel 3."""
    	return self.read_bit(3, 2) == 1

    def get_burnout_ch4(self):
    	"""Return burnout channel 4."""
    	return self.read_bit(4, 2) == 1

    def get_burnout_ch5(self):
    	"""Return burnout channel 5."""
    	return self.read_bit(5, 2) == 1

    def get_burnout_ch6(self):
    	"""Return burnout channel 6."""
    	return self.read_bit(6, 2) == 1

    def get_burnout_ch7(self):
    	"""Return burnout channel 7."""
    	return self.read_bit(7, 2) == 1

    ## Holding registers (Modbus function: 4)
    ## Current value

    def get_cvalue_ch0(self, signed):
        """Return the current value of channel0."""
        return self.read_register(0, 0, 4, signed)

    def get_cvalue_ch1(self, signed):
        """Return the current value of channel1."""
        return self.read_register(1, 0, 4, signed)

    def get_cvalue_ch2(self, signed):
        """Return the current value of channel2."""
        return self.read_register(2, 0, 4, signed)

    def get_cvalue_ch3(self, signed):
        """Return the current value of channel3."""
        return self.read_register(3, 0, 4, signed)

    def get_cvalue_ch4(self, signed):
        """Return the current value of channel4."""
        return self.read_register(4, 0, 4, signed)

    def get_cvalue_ch5(self, signed):
        """Return the current value of channel5."""
        return self.read_register(5, 0, 4, signed)

    def get_cvalue_ch6(self, signed):
        """Return the current value of channel6."""
        return self.read_register(6, 0, 4, signed)

    def get_cvalue_ch7(self, signed):
        """Return the current value of channel7."""
        return self.read_register(7, 0, 4, signed)   

    ### Set Type code
    def set_typecode_ch0(self, typecode):
        """Set type code of channel0."""
        return self.write_register(200, typecode)

    def set_typecode_ch1(self, typecode):
        """Set type code of channel1."""
        return self.write_register(201, typecode)

    def set_typecode_ch2(self, typecode):
        """Set type code of channel2."""
        return self.write_register(202, typecode)

    def set_typecode_ch3(self, typecode):
        """Set type code of channel3."""
        return self.write_register(203, typecode)

    def set_typecode_ch4(self, typecode):
        """Set type code of channel4."""
        return self.write_register(204, typecode)

    def set_typecode_ch5(self, typecode):
        """Set type code of channel5."""
        return self.write_register(205, typecode)

    def set_typecode_ch6(self, typecode):
        """Set type code of channel6."""
        return self.write_register(206, typecode)

    def set_typecode_ch7(self, typecode):
        """Set type code of channel7."""
        return self.write_register(207, typecode)   

    # Get Type Code
    def get_typecode_ch0(self):
        """Return the type code of channel0."""
        return self.read_register(200, 0, 4)

    def get_typecode_ch1(self):
        """Return the type code of channel1."""
        return self.read_register(201, 0, 4)

    def get_typecode_ch2(self):
        """Return the type code of channel2."""
        return self.read_register(202, 0, 4)

    def get_typecode_ch3(self):
        """Return the type code of channel3."""
        return self.read_register(203, 0, 4)

    def get_typecode_ch4(self):
        """Return the type code of channel4."""
        return self.read_register(204, 0, 4)

    def get_typecode_ch5(self):
        """Return the type code of channel5."""
        return self.read_register(205, 0, 4)

    def get_typecode_ch6(self):
        """Return the type code of channel6."""
        return self.read_register(206, 0, 4)

    def get_typecode_ch7(self):
        """Return the type code of channel7."""
        return self.read_register(207, 0, 4)   

    ### Module name 1
    def get_module_name1(self):
        """Return the module name 1."""
        return self.read_register(210, 0, 4)

    ### Module name 2
    def get_module_name2(self):
        """Return the module name 2."""
        return self.read_register(211, 0, 4)

    def get_version1(self):
        """Return version 1."""
        return self.read_register(212, 0, 4)

    def get_version2(self):
        """Return version 2."""
        return self.read_register(213, 0, 4)

    def get_ch_status(self, channel):
        """Return channel enable/disable status."""
        mask = 1 << channel
	status = self.read_register(214, 0, 4) and mask
	return (status >> channel) 

    def set_ch_status(self, channel):
        """Enable channel."""
        mask = 1 << channel
	reg = self.read_register(214, 0, 4)
	value = reg and mask
	self.write_register(214, value)

########################
## Testing the module ##
########################

if __name__ == '__main__':

    minimalmodbus._print_out('TESTING ADAM4117 MODBUS MODULE')
    
# Assume ADAM4117 controller connected to /dev/ttyO1
# Default Modbus @:1, serial port parameter: 9600,8,n,1

    a = Apm303('/dev/ttymxc1', 1)
    a.debug = True
    a.handle_local_echo = False
    
    minimalmodbus._print_out( 'Burn-out channel 0 {0}'.format(a.get_burnout_ch0()) )
    minimalmodbus._print_out( 'Burn-out channel 1 {0}'.format(a.get_burnout_ch1()) )
    minimalmodbus._print_out( 'Burn-out channel 2 {0}'.format(a.get_burnout_ch2()) )
    minimalmodbus._print_out( 'Burn-out channel 3 {0}'.format(a.get_burnout_ch3()) )
    minimalmodbus._print_out( 'Burn-out channel 4 {0}'.format(a.get_burnout_ch4()) )
    minimalmodbus._print_out( 'Burn-out channel 5 {0}'.format(a.get_burnout_ch5()) )
    minimalmodbus._print_out( 'Burn-out channel 6 {0}'.format(a.get_burnout_ch6()) )
    minimalmodbus._print_out( 'Burn-out channel 7 {0}'.format(a.get_burnout_ch7()) )

    minimalmodbus._print_out( 'Current value channel 0: {0}'.format(a.get_icur_ch0()) )
    minimalmodbus._print_out( 'Current value channel 1: {0}'.format(a.get_icur_ch1()) )
    minimalmodbus._print_out( 'Current value channel 2: {0}'.format(a.get_icur_ch2()) )
    minimalmodbus._print_out( 'Current value channel 3: {0}'.format(a.get_icur_ch3()) )
    minimalmodbus._print_out( 'Current value channel 4: {0}'.format(a.get_icur_ch4()) )
    minimalmodbus._print_out( 'Current value channel 5: {0}'.format(a.get_icur_ch5()) )
    minimalmodbus._print_out( 'Current value channel 6: {0}'.format(a.get_icur_ch6()) )
    minimalmodbus._print_out( 'Current value channel 7: {0}'.format(a.get_icur_ch7()) )

    minimalmodbus._print_out( 'Type Code channel 0: {0}'.format(a.get_typecode_ch0()) )
    minimalmodbus._print_out( 'Type Code channel 1: {0}'.format(a.get_typecode_ch1()) )
    minimalmodbus._print_out( 'Type Code channel 2: {0}'.format(a.get_typecode_ch2()) )
    minimalmodbus._print_out( 'Type Code channel 3: {0}'.format(a.get_typecode_ch3()) )
    minimalmodbus._print_out( 'Type Code channel 4: {0}'.format(a.get_typecode_ch4()) )
    minimalmodbus._print_out( 'Type Code channel 5: {0}'.format(a.get_typecode_ch5()) )
    minimalmodbus._print_out( 'Type Code channel 6: {0}'.format(a.get_typecode_ch6()) )
    minimalmodbus._print_out( 'Type Code channel 7: {0}'.format(a.get_typecode_ch7()) )

    minimalmodbus._print_out( 'Module Name 1: {}'.format(a.get_module_name1()) )
    minimalmodbus._print_out( 'Module Name 2: {}'.format(a.get_module_name2()) )

    minimalmodbus._print_out( 'Version 1: {}'.format(a.get_version1()) )
    minimalmodbus._print_out( 'Version 2: {}'.format(a.get_version2()) )

    minimalmodbus._print_out( 'Channel enable/disable register: {}'.format(a.get_ch_status()) )

    minimalmodbus._print_out( 'DONE!' )

pass    
