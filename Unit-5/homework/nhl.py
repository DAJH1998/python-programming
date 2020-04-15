import json
import requests

class NhlTeams:
    def __init__(self):
        response = requests.get('https://statsapi.web.nhl.com/api/v1/teams').json()
        self.nhl_stats = response['teams']

    def show_teams(self):
        print(json.dumps(self.nhl_stats[0], indent=2))

    def get_team_names(self):
        team_name = []
        for names in self.nhl_stats:
            team_name.append(names['name'])
        return (team_name)
    '''
    def win_count(self):
        wins = []
        for win in self.nhl_stats:
            wins.append(win['franchiseId'])
        return (wins)
    '''
    def conferences(self):
        return

    def get_oldest_team(self):
        sorted_list = sorted(self.nhl_stats, key = lambda k: k['firstYearOfPlay'])
        oldest_team = sorted_list[0]['name']
        print(f'Oldest Team is the {oldest_team}')

nhl = NhlTeams()

nhl.show_teams()
print(json.dumps(nhl.get_team_names(), indent = 2))
nhl.get_oldest_team()

