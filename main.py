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
    BOLD = '\033[1m'

def intro():
    print """
                      Proudly built by%s
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
This tool allows you to locally store all the data we can get from OpenKit, so you can keep it safe after the 1 December deadline.

After Gameeso is done, I (or we depending on how the community grows :)) will allow you to import that data again in Gameeso to continue your services.
Please follow along with the instructions.

This tool functions like a insurance policy, to at least keep your data safe whenether or not I decide to continue with Gameeso.

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
    output['users'] = []
    
    def fetch_leaderboard_page(leaderboard, page_num):
        if not 'scores' in leaderboard:
            leaderboard['scores'] = []
        
        content = json.loads(get("best_scores?leaderboard_id=%s&leaderboard_range=all_time&num_per_page=25&page_num=%s" % (leaderboard['id'], page_num)).content)
        for score in content:
            # Merge leaderboard data from scores
            inner_leaderboard = score['leaderboard']
            user = score['user']
            
            leaderboard.update(inner_leaderboard)
            
            possible_user = next((item for item in output['users'] if item['id'] == user['id']), None)
            if possible_user == None:
                output['users'].append(user)
                print str_type_progress("\t\tUser found, id: %s%s%s" % (bcolors.BOLD, user['id'], bcolors.ENDC))
            
            score.pop('leaderboard', None)
            score.pop('user', None)
            
        leaderboard['scores'].extend(content)

        return content
    
    for leaderboard in leaderboards:
        page_num = 1
        
        print str_type_progress("Fetching leaderboard id: %s%s%s" % (bcolors.BOLD, leaderboard['id'], bcolors.ENDC))
        
        result = None
        while result != []:
            print str_type_progress("\tFetching leaderboard page %s%s%s" % (bcolors.BOLD, page_num, bcolors.ENDC))
            result = fetch_leaderboard_page(leaderboard, page_num)
            page_num = page_num + 1
        
        print str_type_progress("No more pages left for leaderboard id: %s%s%s" % (bcolors.BOLD, leaderboard['id'], bcolors.ENDC))
    
    json_output = json.dumps(output, sort_keys=True, indent=4, separators=(',', ': '))

    file = open("my_data.json", "w")
    file.write(json_output)
    file.write("\n")
    file.close()

    print """
        Done! Please put the file my_data.json somewhere safe for later use!
        I worked on this tool in my free time and made it freely available, if this tool helped you, please consider a donation: http://gameeso.com/#donation
    """

def str_type_progress(str):
    return str

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
