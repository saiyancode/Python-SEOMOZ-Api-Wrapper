from mozscape import Mozscape
from creds import client
import pandas as pd

class grab_da():

    def __init__(self, domain):
        mozMetrics = client.urlMetrics(domain)
        df = pd.DataFrame(mozMetrics)
        df.to_csv('results.csv', index=False)
        self.da = mozMetrics['pda']

    def authority(self):
        return self.da

#Example function: Pass list of domains to export to results.csv

for i in domains:
    grab_da(i)

#Example function return DA only

for i in domains:
    result = grab_da(i)
    da = result.authority()
    # Do what you like with the da value now

