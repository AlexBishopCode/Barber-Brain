![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **May 14, 2024**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!

#### Click [here](https://barber-brain-7aba89f189d5.herokuapp.com/) to view the live site.
#### (Utilise username 'jbloggs1' password '121212', client 'joe' 'bloggs' and client ID '1' as an example. Explore the google spreadsheet screenshots below to test the functions)

# Barber Brain

![Title Banner Screengrab](assets/images/barber_title.png)

## Introduction

Barber Brain is a comprehensive loyalty management system designed specifically for barbershops. It helps manage client data, track visits, and award loyalty points to enhance customer engagement and retention. The system allows barbershops to offer personalized rewards, such as free shaves, to their most loyal clients, thus improving customer satisfaction and encouraging repeat visits.

### The Client

The client operates a barbershop in a busy city center and seeks a loyalty system to enhance customer engagement and boost repeat business. The new system should efficiently manage the existing loyalty scheme, where clients earn a free shave after ten visits. It must be accessible to all staff, providing them with clients' loyalty and personal information to improve the customer experience.

### User Stories

1. As a staff member, I want to be able to easily access the system and to easily type the clients name in and discover their details in as fewer clicks as possible.
2. As the barber shop owner, I want to see how many times clients are visiting to understand how much repeat trade is occuring.
3. As the barber shop owner, I want to be able to add login details for new staff members.
3. As a staff member I want the system to provide clear details about each client as a prompt without me having to remmeber.


### System Data Flow Chart

The flow chart visually illustrates the sequence of steps and decisions a user experiences, along with the data paths involved. The chart maps out how users interact with the system and how data moves through different stages of the process.

![Code Flow Chart Screengrab](assets/images/barber_flow_chart.png)

## Features

### Existing Features

#### TITLE

- **Client Management**: Store and manage client information.
- **Visit Tracking**: Track the number of visits each client makes.
- **Loyalty Points System**: Award and manage loyalty points.
- **Personalized Rewards**: Offer rewards like free shaves to loyal clients.

#### Title banner
- A graphic banner is present at the top of the system to frame the application and provide structure and visual appeal, improving user experience.

![Title Banner Screengrab](assets/images/barber_title)

#### login section
- A secure login page where staff members enter their username and password to access the system.

![Login Screengrab](assets/images/barber_login.png)

#### Navigation menu 
- A menu that lets staff navigate between searching for clients, adding new clients, logging visits, and logging out.

![Title Banner Screengrab](assets/images/

#### Search for a client feature
- A search feature where staff can look up clients by first and last name to view their loyalty details and personal information.
- Displays the client's personal information, such as name, pronouns, phone number, and email, along with their visit count and loyalty points.

![Title Banner Screengrab](assets/images/

#### Add a new client feature
- A form for adding new clients, allowing staff to enter details like name, contact info, and whether they were referred by a friend.

![Title Banner Screengrab](assets/images/

#### Log a client visit feature
- An option to record a client's visit, which updates their visit count and loyalty points and checks if they qualify for a free shave.

![Title Banner Screengrab](assets/images/

#### Loyalty points management feature
- Manages client loyalty points, including a prompt to redeem points for a free shave if they have earned enough.

![Title Banner Screengrab](assets/images/

#### Error Handling and Validation: 
- Error messages and checks to make sure all entered information, like emails and phone numbers, is correct.

![Title Banner Screengrab](assets/images/

#### Logout feature
- A straightforward button for staff to log out of the system securely.

#### Future Features
- A feature where the managers log in details allows them to add a new member of staff onto the system.
- A feature where staff are able to change their own password for the page.
- A feature where the password is able to be hidden throughout the entire process.
- A feature where customers are also able to log onto the system to see how many loyalty points they have.
- A feature where an automatic email or text message is sent to the client once they have reached 10 loyalty points.

## Technologies Used

- **Python**: The core programming language used.
- **Google Sheets API**: For managing and storing data on spreadsheets.
- **gspread**: Python library for interacting with Google Sheets.
- **Regular Expressions (re)**: For input validation.

## Installation

To install and run the Barber Brain application, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/YourUsername/Barber-Brain.git
   cd Barber-Brain

## Testing

# Linter 

![Linter Validation Screengrab](assets/images/barber_linter_screenshot.png)

# In-Line Command Code Testing

![Testing Worksheet Screengrab](assets/images/barber_testing_worksheet.png)
## Development

- GITPOD - The online IDE was used for writing and testing the code in a cloud-based environment.
- The GitHub repository was closed into github and the necessary dependencies and project settings were installed.

## Deployment

The project was deployed using Heroku. 

1. Account setup
- A Heroku account was created and a new application was set up. 
- The new Heroku environemt was configured to use python and nodejs.

2. Deployment process
- The github repository was connected to Heroku, and - afterwards automatic deployment was enabled. 

3. Configuration
The Pyton and Nosejs buildpacks were added to the configuration. 

4. Project pushed to Heroku
- The final commited changes were added to the project.
- The changes were pushed to the repository and Heroku detected the changes and automatically built and deployed the application.
- The command-line interface (CLI) on Heroku was utilised to monitor the automatic deployments.

5. Post-Deployment Process.
- The live application was tested within the Heroku CLI.
- Any necessary adjustments were made and pushed to the repository and automatically deployed by Heroku.

6. Summary
- By using Gitpod for development and Heroku for deployment, you streamlined your workflow from coding to deployment, leveraging Gitpod’s cloud-based IDE and Heroku’s seamless integration for deploying and managing your application.

#Usage


#Contributing


#License


#Contact
For any questions or further information, please contact Alex at helloalexbishop@gmail.com


## Index – Table of Contents
* [User Experience (UX)](#user-experience-ux) 
* [Features](#features)
* [Design](#design)
* [Technologies Used](#technologies-used)
* [Testing](#testing)
* [Deployment](#deployment)
* [Credits](#credits)