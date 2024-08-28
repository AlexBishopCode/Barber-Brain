import gspread
from google.oauth2.service_account import Credentials

SCOPE = {
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
}

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('barber_brain')

clients = SHEET.worksheet('clients')

client_data = clients.get_all_values()

headers = client_data[0]
client_data = client_data[1:]

while True:
    first_name = input("Enter the clients first name (or type exit to quit): ")

    if first_name.lower() == 'exit':
        print("Exiting the search.")
        break

    second_name = input("Enter the client's second name (or type 'exit' to quit): ")

    if second_name.lower() == 'exit':
        print("Exiting the search.")
        break

    found = False
    for row in client_data:
        if first_name.lower() == row[0].lower() and second_name.lower() == row[1].lower():
            print("\nDetails found:")
            for i in range(len(headers)):
                print(f"{headers[i]}: {row[i]}")
            found = True
    
    if not found:
        print("There are no deatils for that name.")