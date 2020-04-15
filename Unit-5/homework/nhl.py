import json
import requests

class NhlTeams:
    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
        self.nhl_stats = response['teams']

    def get_team_names(self):
        team_name = []
        for names in self.nhl_stats:
            team_name.append(names['name'])
        return (team_name)

    def win_count(self):
        wins = []
        for win in self.nhl_stats:
            wins.append(win['franchiseId'])
        return (wins)
    
    def conferences(self):
        return

    def get_oldest_team(self):
        return

nhl = NhlTeams()

print(json.dumps(nhl.get_team_names(), indent = 2))
print(json.dumps(nhl.win_count(), indent = 2))
