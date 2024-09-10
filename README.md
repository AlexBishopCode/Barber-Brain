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

#BARBER BRAIN

Table of Contents

##Introduction

The client is a barber who is currently looking for ways to boost customer retention, increase repeat business, and create personalized experiences to keep their clients coming back. The client sought a solution that not only enhances customer engagement but also rewards loyal clients with meaningful incentives. Recognizing this need, I developed Barber Brain to help the barbershop manage their client relationships more efficiently and drive business growth.

Barber Brain is a comprehensive loyalty management system specifically designed for barbershops to manage client data, track visits, and award loyalty points. This system empowers barbershops to build stronger relationships with their clients by offering personalized rewards, such as free shaves, to their most loyal customers. With Barber Brain, barbershops can enhance customer satisfaction, encourage repeat visits, and create a more engaging and tailored customer experience. Ultimately, this solution helps barbershop owners grow their business by fostering loyalty and improving the overall client experience.

#Features



#Technologies Used

Python - Core programming language
Google Sheets API - For managing and storing data
gspread - Python library for interacting with Google Sheets
Regular Expressions (re) - For input validation

#Installation

# Testing

#In-Line Command Code Testing

[barber_brain_test_table.pdf](https://github.com/AlexBishopCode/Barber-Brain/blob/main/barber_brain_test_table.pdf)

# Development

GITPOD - The online IDE was used for writing and testing the code in a cloud-based environment.
The GitHub repository was closed into github and the necessary dependencies and project settings were installed.

# Deployment

The project was deployed using Heroku. 

1. Account setup
A Heroku account was created and a new application was set up. 
The new Heroku environemt was configured to use python and nodejs.

2. Deployment process
The github repository was connected to Heroku, and afterwards automatic deployment was enabled. 

3. Configuration
The Pyton and Nosejs buildpacks were added to the configuration. 

4. Project pushed to Heroku
The final commited changes were added to the project.
The changes were pushed to the repository and Heroku detected the changes and automatically built and deployed the application.
The command-line interface (CLI) on Heroku was utilised to monitor the automatic deployments.

5. Post-Deployment Process.
The live application was tested within the Heroku CLI.
Any necessary adjustments were made and pushed to the repository and automatically deployed by Heroku.

6. Summary
By using Gitpod for development and Heroku for deployment, you streamlined your workflow from coding to deployment, leveraging Gitpod’s cloud-based IDE and Heroku’s seamless integration for deploying and managing your application.

#Usage


#Contributing


#License


#Contact