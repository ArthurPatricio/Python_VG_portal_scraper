# Import
from scraper_incidents import scraper_incidents
from scraper_help_requests import scraper_help_requests
import pandas as pd

def run_scraper():

    df_incidents = scraper_incidents()
    df_help_requests = scraper_help_requests()

    writer = pd.ExcelWriter('VertiGIS_Tickets.xlsx', engine='xlsxwriter')

    df_incidents.to_excel(writer, sheet_name='incidents')
    df_help_requests.to_excel(writer, sheet_name='help_requests')

    writer.save()

if __name__ == "__main__":
    run_scraper()