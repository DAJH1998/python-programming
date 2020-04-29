import requests
import json

url = "https://covid-193.p.rapidapi.com/statistics"

headers = {
    'x-rapidapi-host': "covid-193.p.rapidapi.com",
    'x-rapidapi-key': "2ab7c9815dmshc54ce3e5affb5a7p117757jsn67407177f01b"
    }

response = requests.request("GET", url, headers=headers).json()

class CovidStats:
    #to see information
    def jprint(self, obj):
        text = json.dumps(obj, sort_keys=True, indent=4)
        print(text)

    def __init__(self):
        self.covid_stats = []
    
    def fetch_statistics(self):
        self.covid_stats = response["response"]
        
        return self.covid_stats

    def top_ten(self):
        cases_list = []
        for covid_cases in self.covid_stats:
            cases_list.append(covid_cases["cases"])
            sorted_list = sorted(cases_list, key=lambda k:k['total'],reverse=True)
        
        return sorted_list [0:9]

    def get_country_stats (self, country):
        for item in self.covid_stats:
            if item ["country"] == country:
                return item

    #def show_regional_stats(self):

    def test_unavailable (self):
        list_of_countries = []
        for items in self.covid_stats:
            if type(items ["tests"]["total"]) != int:
                list_of_countries.append (items["country"])
        
        return list_of_countries
    '''
    def stats_to_file(self, filename):
        for items in self.covid_stats:
            data_dump = {
                    "country":items["country"]
                    }
        with open (filename,"w") as dump_file:
            json.dump(data_dump, dump_file) 
    '''
c = CovidStats()

#c.jprint(response)
print(c.fetch_statistics())
print(c.top_ten())
print(c.get_country_stats('China'))
print(c.test_unavailable())
#c.stats_to_file('stats.json')
