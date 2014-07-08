# -*- coding: utf-8 -*-

## OpenKit Exporter
## Created by Peter Willemsen <peter@codebuffet.co>

from requests_oauthlib import OAuth1Session
import json

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    GREY = '\033[37m'

def intro():
    print """
                      Proudly build by%s
                        ███████████
                     █████████████████
                     █████████████████                      
                     ███           ███                      
                     ███           ███                      
                     █████████████████                      
                ███████████████████████████                
           █████████████████████████████████████            
           █████████████████████████████████████            
        ██████████████░░░░░█████░░░░░██████████████         
     █████████████████░░░░░█████░░░░░████████░░░██████      
     ██████████████░░░░░███████████░░░░░████████░░░███      
     ██████████████░░░░░███████████░░░░░████████░░░███      
  █████████████████░░░░░███████████░░░░░████████░░░░░░███   
  █████████████████░░░░░███████████░░░░░████████░░░░░░███   
  ████████████████████░░░░░█████░░░░░███████████░░░░░░███   
██████████████████████░░░░░█████░░░░░██████████████░░░░░░███
███████████████████████████████████████████████████░░░░░░███
███████████████████████████████████████████████████░░░░░░███
                                                            
                                                            
███████████████████████████████████████████████████░░░░░░███
███████████████████████████████████████████████████░░░░░░███
███████████████████████████████████████████████████░░░░░░███%s
""" % (bcolors.GREY, bcolors.ENDC)

    print """
Welcome to the Export tool for OpenKit!
This tool allows you to locally store all the data we can get from OpenKit, so you can keep it safe after the 1 december deadline.

After Gameeso is done, I (or we depending on how the community grows :)) will allow you to import that data again in Gameeso to continue your services.
Please follow the instructions along.

This tool functions like a insurance policy, to keep at least your data safe whenether or not I decide to continue with Gameeso.

With great love, Peter Willemsen.
More Info: http://gameeso.com/openkit-notes/
        """

def main():
    intro()
    server = input_default("Server", "http://api.openkit.io")
    app_key = input_default("Application Key", None)
    app_secret = input_default("Application Secret", None)

    import_from_server(server, app_key, app_secret)

def import_from_server(server, app_key, app_secret):
    print server, app_key, app_secret
    session = OAuth1Session(app_key,
                            client_secret=app_secret)

    output = {}

    def get(endpoint):
        return session.get("%s/%s" % (server, endpoint))

    leaderboards = json.loads(get("leaderboards?tag=v1").content)
    output['leaderboards'] = leaderboards
    for leaderboard in leaderboards:
        leaderboard['scores'] = json.loads(get("best_scores?leaderboard_id=%s&leaderboard_range=all_time&num_per_page=25&page_num=1" % leaderboard['id']).content)
    
    json_output = json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))

    file = open("my_data.json", "w")
    file.write(json_output)
    file.write("\n")
    file.close()

    print """
        Done! Please put the file my_data.json somewhere safe for later use!
    """


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