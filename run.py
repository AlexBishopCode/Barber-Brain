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

def search_client():
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
        for index, row in enumerate(client_data):
            if first_name.lower() == row[0].lower() and second_name.lower() == row[1].lower():
                print("\nDetails found:")
                for i in range(len(headers)):
                    print(f"{headers[i]}: {row[i]}")
                found = True
        
        if not found:
            print("There are no deatils for that name.")
            break

def add_new_client():
    new_client = []
    print("Enter the new client's details: ")
    
    for header in headers:
        new_client.append(input(f"{header}: "))

    clients.append_row(new_client)
    print("New client created successfully.")

def navigation_menu():
    
    while True:
        print("\nBarber Brain")
        print("1. Search for an existing client")
        print("2. Add a new client")

        choice = input("Enter option (1/2): ").strip()

        if choice == '1':
            search_client()
        elif choice == '2':
            add_new_client()
        else:
            print("Invalid choice. Please enter 1 or 2.")

navigation_menu()