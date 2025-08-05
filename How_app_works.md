# COMP 170 SU25 Final Project – MyFriendsApp

## Description
This Python application allows you to manage contact records for friends. It uses object-oriented programming with custom classes (Friend, Person, Birthday), and supports creating, editing, deleting, and reporting on contacts.

## Features
1. Create new friend record (manual entry)
2. Search, edit, or delete friend records
3. Reports:
   - Alphabetical list
   - Upcoming birthdays
   - Mailing labels
4. Data saved to `friends_database.csv` automatically

## Files
- MyFriendsApp.py – Main application
- Friend.py – Inherits from Person
- Person.py – Stores personal and contact details
- Birthday.py – Handles date logic
- friends_database.csv – Sample data for testing

## Requirements
- Python 3.x
- No external libraries required

## How to Run
1. Open terminal or command line.
2. Navigate to the project folder.
3. Run the application:

   ```bash
   python MyFriendsApp.py
