import time
import modbus_tk
import modbus_tk.defines as mdef
import modbus_tk.modbus
import modbus_tk.modbus_tcp

try:
  while 1:
    time.sleep(1)
    master = modbus_tk.modbus_tcp.TcpMaster('127.0.0.1', 502)
    master.set_timeout(3)
    temperature = master.execute(1, mdef.HOLDING_REGISTERS, 100, 1)
    print 'Current temperature is', temperature[0], 'C'
    
except Exception as e:
    print '================================================= error ======================================================='
    print e
finally:
    print '================================================= stop ========================================================'
