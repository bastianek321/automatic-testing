from linux_tests import TestClass as test_linux_class
from windows_tests import TestClass as test_windows_class

linux = test_linux_class()
windows = test_windows_class()

linux.test_ls_command_description()
linux.test_main_commands()
linux.test_system()
windows.test_find_command_description()
windows.test_main_commands()
windows.test_system()