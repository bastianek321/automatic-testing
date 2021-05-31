import pytest as pt
import driver


class TestClass:
    
    def test_main_commands(self):
        tested = driver.Driver('Linux')
        assert tested.help() == driver.linux_commands 

    def test_system(self):
        with pt.raises(driver.DriverError):
            tested = driver.Driver('notlinux')
    
    def test_ls_command_description(self):
        tested = driver.Driver('Linux')
        assert driver.linux_commands['ls'] == tested.command_description('ls')


