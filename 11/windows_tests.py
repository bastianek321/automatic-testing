import pytest as pt
import driver

class TestClass:

    def test_main_commands(self):
        tested = driver.Driver('Windows')
        assert tested.help() == driver.windows_commands

    def test_system(self):
        with pt.raises(driver.DriverError):
            tested = driver.Driver('notwindows')
    
    def test_find_command_description(self):
        tested = driver.Driver('Windows')
        assert driver.windows_commands['find'] == tested.command_description('find')
        