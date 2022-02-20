#Import
from get_html_v2 import get_html
import pandas as pd


def scraper_incidents():

    class_instance = get_html()
    html = class_instance.get_html_incidents()

    # Get tr tags with data-entity = incident
    titletags = html.find_all('tr', attrs={'data-entity':'incident'})


    # Empty Lists
    titles_lst = []
    ticket_numbers_lst = []
    ticket_status_lst = []
    severity_lst = []
    account_lst = []
    custom_id_lst = []
    created_on_lst = []

    for i in range(len(titletags)):
        titles = titletags[i].attrs['data-name']
        titles_lst.append(titles) 

        ticket_numbers = html.find_all('tr', attrs={'data-entity':'incident'})[i]
        ticket_numbers = ticket_numbers.find_all('td',attrs={'data-attribute':'ticketnumber'})
        ticket_numbers = ticket_numbers[0].attrs['aria-label']
        ticket_numbers_lst.append(ticket_numbers)

        ticket_status = html.find_all('tr', attrs={'data-entity':'incident'})[i]
        ticket_status = ticket_status.find_all('td',attrs={'data-attribute':'statuscode'})
        ticket_status = ticket_status[0].attrs['aria-label']
        ticket_status_lst.append(ticket_status)

        severity = html.find_all('tr', attrs={'data-entity':'incident'})[i]
        severity = severity.find_all('td',attrs={'data-attribute':'severitycode'})
        severity = severity[0].attrs['aria-label']
        severity_lst.append(severity)

        created_on = html.find_all('tr', attrs={'data-entity':'incident'})[i]
        created_on = created_on.find_all('td',attrs={'data-attribute':'createdon'})
        created_on = created_on[0].attrs['aria-label']
        created_on_lst.append(created_on)

        account = html.find_all('tr', attrs={'data-entity':'incident'})[i]
        account = account.find_all('td',attrs={'data-th':'Account'})
        account = account[0].attrs['aria-label']
        account_lst.append(account)

        custom_id = html.find_all('tr', attrs={'data-entity':'incident'})[i]
        custom_id = custom_id.find_all('td',attrs={'data-th':'Custom Ticket-ID'})
        custom_id = custom_id[0].attrs['aria-label'] 
        custom_id_lst.append(custom_id)


        df_incidents = pd.DataFrame(list(
        zip(ticket_numbers_lst, custom_id_lst, ticket_status_lst, titles_lst, created_on_lst, severity_lst, account_lst)), 
        columns=['Number', 'Custom Ticket-ID', 'Status Reason', 'Title','Created On', 'Severity', 'Account'])

        # Order df_incidents per ticket Severity
        df_incidents = df_incidents.sort_values('Severity')

        # Filter df_incidents for Burns' tickets
        df_incidents = df_incidents.query('Account == "Burns & McDonnell Engineering Company, Inc" ')

    return df_incidents

if __name__ == "__main__":
    scraper_incidents()