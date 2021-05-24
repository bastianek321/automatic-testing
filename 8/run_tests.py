from tests import stackoverflow_test, zalando_test
from datetime import datetime, date
# czasami pojawia sie taki blad, nie zawsze

# [21884:12608:0517/225453.130:ERROR:device_event_log_impl.cc(214)] [22:54:53.130] 
# USB: usb_device_handle_win.cc:1054 Failed to read descriptor from node connection: 
# Urz╣dzenie do│╣czone do komputera nie dzia│a. (0x1F)

start = datetime.now().time()
stackoverflow_test()
stack_duration = datetime.combine(date.min, datetime.now().time()) - datetime.combine(date.min, start)
start = datetime.now().time()
zalando_test()
zalando_duration = datetime.combine(date.min, datetime.now().time()) - datetime.combine(date.min, start)
print(stack_duration)
print(zalando_duration)