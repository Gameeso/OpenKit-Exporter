## OpenKit Exporter
## Created by Peter Willemsen <peter@codebuffet.co>

def main():
    server = input_default("Server", "http://openkit.io")
    app_key = input_default("Application Key", None)
    app_secret = input_default("Application Secret", None)

    import_from_server(server, app_key, app_secret)

def import_from_server(server, app_key, app_secret):
    print server, app_key, app_secret


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'

def str_type_default(str):
    return '%s%s%s' % (bcolors.OKBLUE, str, bcolors.ENDC)

def input_default(message, default):
    if default == None:
        user_input = raw_input("%s: " % message)
    else:
        user_input = raw_input("%s [%s]: " % (message, str_type_default(default)))

    if not user_input:
        user_input = default

    return user_input

if __name__ == "__main__":
    main()