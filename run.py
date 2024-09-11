import gspread
from google.oauth2.service_account import Credentials
import re

# Defines the scope for Google Sheets access
SCOPE = {
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
}

# Validate and initialise the Google sheets client
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('barber_brain')


def fetch_all_data():
    """
    Retrieves and stores all data from the 'staff', 'clients', and 'visits' worksheets on Google sheets.
    """
    global staff_members, client_data, visits_data, headers, visits
    staff_members = SHEET.worksheet('staff').get_all_values()
    client_data = SHEET.worksheet('clients').get_all_values()
    visits_data = SHEET.worksheet('visits').get_all_values()
    visits = SHEET.worksheet('visits')

    headers = client_data[0]
    client_data = client_data[1:]


fetch_all_data()


def print_title():
    """
    Prints the title header for the project
    """
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
    """
    Validates input data for phone numbers and emails
    """

    patterns = {
        'phone': r"^(?:\+44|0)\d{10}$",
        'email': r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    }
    return re.match(patterns[validation_type], input_value) is not None


def login():
    """
    Handles user login for staff
    Prompts the user to enter a username and login and checks
    against credentials within the 'staff' google worksheet.
    """
    while True:
        print("Barber Brain Staff Login")

        staff_username = input("Username: ").strip()
        staff_password = input("Password: ").strip()

        for row in staff_members[1:]:
            sheet_username = row[1]
            sheet_password = row[2]

            if (staff_username, staff_password) == (sheet_username, sheet_password):
                print("\nLogin successful!")
                return True
        print("\nInvalid username or password.")


def logout():
    """
    Exits the users space and returns the user to the login function
    """
    print("\nYou have been logged out.")
    return False


def search_client():
    """
    Function which searches for an existing client based on first name and second name
    credentials within the 'client' worksheet.

    If found, the clients detailed are displayed.
    """
    while True:
        first_name = (
            input("Enter the client's first name (or type 'exit' to quit): ")
            .strip().capitalize()
            )

        if first_name.lower() == 'exit':
            print("Exiting the search.")
            return

        if not first_name:
            print("Please enter a first name.")
            continue

        while True:
            second_name = input("Enter the client's second name (or type 'exit' to quit):").strip().capitalize()

            if second_name.lower() == 'exit':
                print("Exiting the search.")
                return

            if not second_name:
                print("Please enter a surname.")
                continue

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
                            while redeem not in ('yes', 'no'):
                                print("Please enter 'yes' or 'no'.")
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


def add_new_client():
    """
    Function that adds a new client to the system, asking
    for various details to be inputted. If the client is referred 
    by a friend they are awarded 10 loyalty points.
    """
    new_client = []
    print("Enter the new client's details: ")

    global client_data, headers
    fetch_all_data()

    if client_data:
        current_client_ids = [int(row[2]) for row in client_data if row[2].isdigit()]
        new_client_id = max(current_client_ids) + 1 if current_client_ids else 1
    else:
        new_client_id = 1

    for header in headers:
        if header.lower() == 'first name' or header.lower() == 'surname':
            while True:
                value = input(f"Enter {header}: ").strip()
                if value:
                    new_client.append(value.capitalize())
                    break
                else:
                    print(f"{header} cannot be empty.")
        elif header.lower() == 'phone number':
            while True:
                phone_number = input(f"Enter {header}: ").strip()
                if phone_number and check_input_valid(phone_number, 'phone'):
                    new_client.append(phone_number)
                    break
                else:
                    print("Invalid phone number. Must start with +44 or 0 followed by 10 digits.")
        elif header.lower() == 'email address':
            while True:
                email = input(f"Enter {header}: ").strip()
                if email and check_input_valid(email, 'email'):
                    new_client.append(email)
                    break
                else:
                    print("Invalid email address. Please enter a valid email address.")
        elif header.lower() != 'client id':
            while True:
                value = input(f"Enter {header}: ").strip()
                if value:
                    new_client.append(value)
                    break
                else:
                    print(f"{header} cannot be empty.")

    new_client.insert(2, new_client_id)

    friend_referral = input("Was the client referred by a friend? (yes/no): ").strip().lower()
    while friend_referral not in ('yes', 'no'):
        print("Please enter 'yes' or 'no'.")
        friend_referral = input("Was the client referred by a friend? (yes/no): ").strip().lower()

    starting_loyalty_points = 10 if friend_referral == 'yes' else 0

    clients = SHEET.worksheet('clients')
    visits = SHEET.worksheet('visits')

    clients.append_row(new_client)
    print("New client created. Client ID:", new_client_id)

    visits.append_row([new_client_id, 0, starting_loyalty_points])
    print(f"Added client ID {new_client_id} to visits sheet (0 visits - {starting_loyalty_points} loyalty points).")


def log_client_visit():
    global visits
    client_id = input("Enter the client's ID to log a visit: ")

    fetch_all_data()
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
                while redeem not in ('yes', 'no'):
                    print("Please enter 'yes' or 'no'.")
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


def main():
    """
    Function which runs the application.

    Prints title, presents login and handles the navigation elements within the systems menu.
    """
    print_title()

    while True:
        if login():
            while True:
                if not navigation_menu():
                    break
        else:
            print("Login failed. Exiting program.")
            break



if __name__ == "__main__":
    main()