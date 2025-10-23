# Web Cinema Simulation

Web Cinema Simulation is a fully functional web application built with Python (Flask), HTML, CSS, JavaScript, and SQLite.
It simulates a small online cinema system, where users can view available movies, check details, and book tickets through an interactive and dynamic web interface.

The project demonstrates the integration of backend logic, database management, and frontend interactivity using Flask as the core framework.

## Project Structure

<img width="700" height="400" alt="Screenshot 2025-10-07 221040" src="https://github.com/user-attachments/assets/f2853c62-d0e4-44b6-ac70-a8cd3b3b9e56" />


## Core Features

### Movie List Interface

Displays all available movies with details such as title, description, ticket price, and poster image.
Users can easily scroll through the list to explore movies currently available.

![MovieListInterface](./Res_imgs/MovieListInterface.png)


### Ticket Booking System

Users can select a movie, enter the number of seats, and book tickets.
After booking, the system shows confirmation messages — first displaying the number of seats booked, then the total price paid.

![TicketBookingSystem](./Res_imgs/TicketBookingSystem.png) 

After pressing the “Book” button:

![TBSView1](./Res_imgs/TBSView1.png) 

![TBSView2](./Res_imgs/TBSView2.png)


### Database Integration

All data is stored in an SQLite database, including:

Movie details (title, description, image, price)

Available seats

Booked tickets

No external database tools (like DBeaver) are required — everything runs locally and automatically updates in real time.

![DatabaseIntegration](./Res_imgs/DatabaseIntegration.png)


### Dynamic Frontend

The frontend is built with HTML, CSS, and JavaScript, ensuring smooth interaction between user actions and backend logic.
Movie elements are dynamically generated from backend data and displayed with real-time updates.

![DynamicFrontend1](./Res_imgs/DynamicFrontend1.png) 

After clicking on the selected movie:

![DynamicFrontend2](./Res_imgs/DynamicFrontend2.png)


### Flask Backend

Flask handles:

Routing between pages

Serving dynamic content

Managing form submissions

Interacting with the SQLite database

### Final Web Application

![FinalWebApplication](./Res_imgs/FinalWebApplication.png)


## Learning Focus

This project was designed as a practical example to combine backend and frontend development into one coherent system.

You’ll find examples of:

Using Flask for backend web logic

Managing data via SQLite

Enhancing interactivity using JavaScript

Styling interfaces with CSS for a pleasant user experience

## Technologies Used

Python (Flask) – backend web framework

HTML5 / CSS3 / JavaScript – frontend development

SQLite – lightweight local database
