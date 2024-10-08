
# Import external libraries for Google Sheets / authentication
import gspread
from google.oauth2.service_account import Credentials
import re

# Defines the scope for Google Sheets access
SCOPE = {
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
}

# Validate and initialize Google Sheets
CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('barber_brain')


def fetch_all_data():
    """
    Retrieves and stores all data from the 'staff', 'clients', and
    'visits' worksheets on Google Sheets.
    """
    global staff_members, client_data, visits_data, headers, visits
    # retreive worksheet data
    staff_members = SHEET.worksheet('staff').get_all_values()
    client_data = SHEET.worksheet('clients').get_all_values()
    visits_data = SHEET.worksheet('visits').get_all_values()
    visits = SHEET.worksheet('visits')

    # retrieve headers and the client data
    headers = client_data[0]
    client_data = client_data[1:]


fetch_all_data()


def print_title():
    """
    Prints the title header for the project.
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


def validate_input(prompt, validation_function, error_message):
    """
    Input validation functions.
    """
    while True:
        value = input(prompt).strip()
        if validation_function(value):
            return value
        print(error_message)


def is_valid_name(value):
    # re.match checks if the input matches pattern (left)
    # and bool() covernts into True or False
    return bool(re.match(r"^[A-Za-z\s]+$", value))


def is_valid_phone(value):
    return bool(re.match(r"^(?:\+44|0)\d{10}$", value))


def is_valid_email(value):
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', value))


def is_valid_pronouns(value):
    return bool(re.match(r"^[A-Za-z\s/]+/[A-Za-z\s/]+$", value))


def login():
    """
    Handles user login for staff. Prompts the user to enter a username
    and password and checks against credentials within the 'staff' Google
    worksheet.
    """
    while True:
        print("Barber Brain Staff Login")
        """
        [SOURCE CODE FOR strip() and lower() code
        https://stackoverflow.com/questions/54884992/python-apply-lower-strip-and-split-in-one-line
        """
        staff_username = input("Username: ").strip()
        staff_password = input("Password: ").strip()

        # Checking credentials against worksheet
        for row in staff_members[1:]:
            sheet_username = row[1]
            sheet_password = row[2]

            credentials_match = (
                (staff_username == sheet_username) and
                (staff_password == sheet_password)
            )
            if credentials_match:
                print("\nLogin successful!")
                return True

        print("\nInvalid username or password.")


def logout():
    """
    Exits the user's space and returns the user to the login function.
    """
    print("\nYou have been logged out.")
    return False


def search_client():
    """
    Searches for an existing client based on first name and second name
    credentials within the 'client' worksheet. If found, the client's
    details are displayed.
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
            second_name = input(
                "Enter the client's second name (or type 'exit' to quit): "
            ).strip().capitalize()

            if second_name.lower() == 'exit':
                print("Exiting the search.")
                return

            if not second_name:
                print("Please enter a surname.")
                continue

            break

        found = False
        # Search for client data matching names
        for row in client_data:
            first_name_match = (first_name == row[0].capitalize())
            second_name_match = (second_name == row[1].capitalize())

            if first_name_match and second_name_match:
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
                                "Would the client like to redeem 10 loyalty "
                                "points for a free shave? (yes/no): "
                            ).strip().lower()
                            while redeem not in ('yes', 'no'):
                                print("Please enter 'yes' or 'no'.")
                                redeem = input(
                                    "Would the client like to redeem 10 "
                                    "loyalty points for a free shave? "
                                    "(yes/no): "
                                ).strip().lower()
                            if redeem == 'yes':
                                new_points = loyalty_points - 10
                                # Updates the loyalty points
                                visits.update_cell(
                                    visits_data.index(visit_row) + 1, 3,
                                    new_points
                                )
                                print("*Points redeemed* Client has used 10 "
                                      "loyalty points for a free shave.")
                            else:
                                print("Loyalty points not redeemed.")
                        else:
                            print("This client is not eligible "
                                  "for a free shave yet.")
                        found = True
                        break
                break

        if not found:
            print("No details found for that name.")


def add_new_client():
    """
    Adds a new client to the system, asking for various details to be
    inputted. If the client is referred by a friend, they are awarded
    10 loyalty points.
    """
    new_client = []
    print("Enter the new client's details: ")

    global client_data, headers
    fetch_all_data()

    # Determine value of next client ID
    if client_data:
        current_client_ids = [
            int(row[2]) for row in client_data if row[2].isdigit()
        ]
        new_client_id = max(current_client_ids) + 1 if current_client_ids else 1
    else:
        new_client_id = 1

    # Retrieve client details from headers and validate accordingly
    for header in headers:
        if header.lower() in ['first name', 'surname']:
            new_client.append(
                validate_input(
                    f"Enter {header}: ",
                    is_valid_name,
                    f"{header} must only contain letters and spaces."
                )
            )
        elif header.lower() == 'pronouns':
            new_client.append(
                validate_input(
                    f"Enter {header}: ",
                    is_valid_pronouns,
                    "Pronouns must include a slash and contain letters, "
                    "spaces, or slashes."
                )
            )
        elif header.lower() == 'phone number':
            new_client.append(
                validate_input(
                    f"Enter {header}: ",
                    is_valid_phone,
                    "Invalid no. Must start with +44 / 0 followed by 10 digits"
                )
            )
        elif header.lower() == 'email address':
            new_client.append(
                validate_input(
                    f"Enter {header}: ",
                    is_valid_email,
                    "Invalid email address. Enter a valid email address."
                )
            )
        elif header.lower() != 'client id':
            new_client.append(
                validate_input(
                    f"Enter {header}: ",
                    is_valid_name,
                    f"{header} must only contain letters and spaces."
                )
            )

    # Insert the new client ID
    new_client.insert(2, new_client_id)

    # Check if the client was referred by a friend
    friend_referral = input(
        "Was the client referred by a friend? (yes/no): "
    ).strip().lower()

    while friend_referral not in ('yes', 'no'):
        print("Please enter 'yes' or 'no'.")
        friend_referral = input(
            "Was the client referred by a friend? (yes/no): "
        ).strip().lower()

    starting_loyalty_points = 10 if friend_referral == 'yes' else 0

    # Add new client to 'clients' worksheet
    clients = SHEET.worksheet('clients')
    visits = SHEET.worksheet('visits')
    clients.append_row(new_client)
    print("New client created. Client ID:", new_client_id)

    # Add the client to the 'visits' sheet also
    visits.append_row([new_client_id, 0, starting_loyalty_points])
    print(
        f"Added client ID {new_client_id} to visits sheet "
        f"(0 visits - {starting_loyalty_points} loyalty points)."
    )


def log_client_visit():
    """
    Logs a client's visit and updates their visit count and loyalty points.
    """
    global visits
    client_id = input("Enter the client's ID to log a visit: ")

    fetch_all_data()
    client_found = False

    """
    [Source Material for enumerate research] =
    https://docs.python.org/3/library/functions.html#enumerate
    and https://www.youtube.com/watch?v=nI-jkrJxlz0)
    """
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
                    "Would the client like to redeem 10 loyalty points for a "
                    "free shave? (yes/no): "
                ).strip().lower()
                while redeem not in ('yes', 'no'):
                    print("Please enter 'yes' or 'no'.")
                    redeem = input(
                        "Would the client like to redeem "
                        "10 loyalty points for a "
                        "free shave? (yes/no): "
                    ).strip().lower()
                if redeem == 'yes':
                    new_points -= 10
                    visits.update_cell(i, 3, new_points)
                    print("*Points redeemed* The client has used 10 loyalty "
                          "points for a free shave.")
                else:
                    print("Loyalty points not redeemed.")

            client_found = True
            break

    if not client_found:
        print("Client ID could not be found.")


def navigation_menu():
    """
    Displays the navigation menu and handles user choices.
    """
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
    Runs the application. Prints title, presents login, and handles the
    navigation elements within the system's menu.
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


# [SOURCE CODE = https://stackoverflow.com/questions/1954700/
# whats-the-point-of-a-main-function-and-or-name-main-check-in-pytho]
if __name__ == "__main__":
    main()
