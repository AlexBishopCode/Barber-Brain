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

Click here[https://barber-brain-7aba89f189d5.herokuapp.com/] to view the live site 

![barber_title.png](https://github.com/AlexBishopCode/Barber-Brain/blob/main/assets/images/barber_title.png)


# Barber Brain

## Introduction

Barber Brain is a comprehensive loyalty management system designed specifically for barbershops. It helps manage client data, track visits, and award loyalty points to enhance customer engagement and retention. The system allows barbershops to offer personalized rewards, such as free shaves, to their most loyal clients, thus improving customer satisfaction and encouraging repeat visits.

![barber_flow_chart.pdf](https://github.com/AlexBishopCode/Barber-Brain/blob/main/assets/images/barber_flow_chart.png)

## Features

- **Client Management**: Store and manage client information.
- **Visit Tracking**: Track the number of visits each client makes.
- **Loyalty Points System**: Award and manage loyalty points.
- **Personalized Rewards**: Offer rewards like free shaves to loyal clients.

## Technologies Used

- **Python**: Core programming language.
- **Google Sheets API**: For managing and storing data.
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

![assets/images/barber_linter_screenshot.png]

# In-Line Command Code Testing

![assets/images/barber_testing_worksheet.png]
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