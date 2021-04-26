class DriverError(Exception):
    pass

class Driver:

    def __init__(self, system_name='Windows'):
        self.system_name = system_name
        if system_name=='Linux':
            self.commands = linux_commands
        elif system_name == 'Windows':
            self.commands = windows_commands
        else:
            print('Driver not recognised')
            raise DriverError()
            
            
    def help(self):
        for key in self.commands:
            print(key)
            for option in self.commands[key]:
                print(option, self.commands[key][option])
            print('\n')
        return linux_commands if self.system_name == 'Linux' else windows_commands

    def command_description(self, command):
        for option in self.commands[command]:
            print(option)
        return self.commands[command]


linux_commands = {
    'ls':{
        '-l': 'shows detailed information',
        '-a': 'shows all files including hidden ones',
        '-s': 'shows file size'
    },
    'cat': {
        '-n': 'numbers each line',
        '-T': 'shows tabulation sign as ^T'
    },
    'rmdir': {
        '-p': 'removes parent directory if they are empty',
        '-v': 'shows information about every removed directory'
    },
    'chmod': {
        '-R': 'sets same rights in subfolders',
        '-v': 'prints what rights have been assigned to each file' 
    },
    'rm': {
        '-i': 'prompt before deleting each file',
        '-r': 'recursively removing directory and its contents'
    }
}

windows_commands = {
    'ipconfig': {
        '/all': 'display full configuration information',
        '/flushdns': 'purge the DNS resolver cache'
    },
    'find': {
        '[pathname]': 'a drive/file(s) to search (wildcards accepted)',
        '/V': 'display all lines NOT containing the specified string',
        '/C': 'count the number of lines containing the string'
    },
    'shutdown': {
        '/i': 'displays the GUI (has to be the first option)',
        '/l': 'logs out',
        '/r': 'shutdown and restart'
    },
    'winget': {
        'install': 'install the specified application',
        'show': 'display details for the specified application'
    },
    'tracert': {
        '-d': 'do not resolve addresses to hostnames',
        '-h <max_hops>': 'maximum number of hops to search for target(default=30)'
    }
}
