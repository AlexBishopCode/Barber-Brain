import gspread
from google.oauth2.service_account import Credentials
import re

SCOPE = {
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
}

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('barber_brain')

staff_members = SHEET.worksheet('staff').get_all_values()
clients = SHEET.worksheet('clients')
client_data = clients.get_all_values()
visits = SHEET.worksheet('visits')
visits_data = visits.get_all_values()

headers = client_data[0]
client_data = client_data[1:]

def print_title():
    title = """
    ##################################################################
    #                                                                #
    #                          BARBER BRAIN                          #
    #                         Loyalty System                         #
    #                                                                #
    ##################################################################
    """
    print(title)

def check_input_valid(input_value, validation_type):
    
    patterns = {
        'phone': r"^(?:\+44|0)\d{10}$",
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    }
    return re.match(patterns[validation_type], input_value) is not None

def login():
    while True:
        print("Barber Brain Staff Login")

        staff_username = input("Username: ").strip()
        staff_password = input("Password: ").strip()

        for row in staff_members_data[1:]:
            sheet_username = row[1]
            sheet_password = row[2]

            if staff_username == sheet_username and staff_password == sheet_password:
                print("\nLogin successful!")
                return True
        
        print ("\nInvalid username or password.")

def logout():
    print("\nYou have been logged out.")
    return False

def main():
    print_title()

    while True:
        if login():
            while True:
                if not navigation_menu():
                    break
        else:
            print("Login failed. Exiting program.")
            break

def search_client():
    while True:
        first_name = input("Enter the clients first name (or type exit to quit): ").strip().capitalize()

        if first_name.lower() == 'exit':
            print("Exiting the search.")
            break

        second_name = input("Enter the client's second name (or type 'exit' to quit): ").strip().capitalize()

        if second_name.lower() == 'exit':
            print("Exiting the search.")
            break

        found = False
        for row in client_data:
            if first_name == row[0].capitalize() and second_name == row[1].capitalize():
                client_id = row[2]
                print("\nDetails found:")
                for i in range(len(headers)):
                    print(f"{headers[i]}: {row[i]}")

                for visit_row in visits_data[1:]:
                    if visit_row[0] == client_id:
                        total_visits = int(visit_row[1])
                        loyalty_points = int(visit_row[2])

                        print(f"Number of visits: {total_visits}")
                        print(f"Loyalty Points: {loyalty_points}")

                        if loyalty_points >= 10:
                            print("This client is eligible for a free shave!")
                            redeem = input(
                                "Would the client like to redeem 10 loyalty points for a free shave? (yes/no): "
                                ).strip().lower()
                            if redeem == 'yes':
                                new_points = loyalty_points - 10
                                visits.update_cell(visits_data.index(visit_row) + 1, 3, new_points)
                                print("*Points redeemed* Client has used 10 loyalty points for a free shave.")
                            else:
                                print("Loyalty points not redeemed.")
                        else:
                            print("This client is not eligible for a free shave yet.")
                        
                        found = True
                        break
                break

        if not found:
            print("No details found for that name.")
            break

def add_new_client():
    new_client = []
    print("Enter the new client's details: ")

    global client_data, headers
    client_data = clients.get_all_values()
    headers = client_data[0]
    client_data = client_data[1:]

    if client_data:
        current_client_ids = [int(row[2]) for row in client_data if row[2].isdigit()]
        new_client_id = max(current_client_ids) + 1 if current_client_ids else 1
    else:
        new_client_id = 1

    
    for header in headers: 
        if header.lower() == 'phone number':
            while True:
                phone_number = input(f"Enter {header}: ")
                if check_input_valid(phone_number, 'phone'):
                    new_client.append(phone_number)
                    break
                else:
                    print("Invalid phone number. Must start with +44 or 0 followed by 10 digits.")
        elif header.lower() == 'email address':
            while True:
                email = input(f"Enter {header}: ")
                if check_input_valid(email, 'email'):
                    new_client.append(email)
                    break
                else:
                    print("Invalid email address. Please enter a valid email address.")
        elif header.lower() != 'client id':
            value = input(f"Enter {header}: ")
            new_client.append(value)

    new_client.insert(2, new_client_id)

    friend_referral = input("Was the client referred by a friend? (yes/no): ").strip().lower()
    starting_loyalty_points = 10 if friend_referral == 'yes' else 0

    clients.append_row(new_client)
    print("New client created. Client ID:", new_client_id)

    visits.append_row([new_client_id, 0, starting_loyalty_points])
    print(f"Added client ID {new_client_id} to visits sheet (0 visits - {starting_loyalty_points} loyalty points).")

def log_client_visit():
    client_id = input("Enter the client's ID to log a visit: ")

    global visits_data
    visits_data = visits.get_all_values()
    client_found = False

    for i, row in enumerate(visits_data[1:], start=2):
        if row[0] == client_id:
            current_visits = int(row[1])
            new_visits = current_visits + 1
            visits.update_cell(i, 2, new_visits)

            current_points = int(row[2])
            new_points = current_points + 1
            visits.update_cell(i, 3, new_points) 

            print(f"Client visits updated to {new_visits}.")
            print(f"Loyalty points updated to {new_points}.")

            if new_points >= 10:
                print("The client has earned a free shave!")
                redeem = input(
                    "Would the client like to redeem 10 loyalty points for a free shave? (yes/no): "
                    ).strip().lower()
                if redeem == 'yes':
                    new_points -= 10
                    visits.update_cell(i, 3, new_points)
                    print(
                        "*Points redeemed* The client has used 10 loyalty points for a free shave."
                        )
                else:
                    print("Loyalty points not redeemed.")

            client_found = True
            break

    if not client_found:
        print("Client ID could not be found.")

def navigation_menu():
    
    while True:
        print("\nBarber Brain")
        print("1. Search for an existing client")
        print("2. Add a new client")
        print("3. Log a client visit") 
        print("4. Logout")

        choice = input("Enter option (1/2/3/4): ").strip()

        if choice == '1':
            search_client()
        elif choice == '2':
            add_new_client()
        elif choice == '3':
            log_client_visit()
        elif choice == '4':
            return logout()
        else:
            print("Invalid choice. Enter option (1/2/3/4).")

if __name__ == "__main__":
    main()