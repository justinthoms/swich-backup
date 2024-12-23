# Network Configuration Backup Script

This script automates the process of backing up network device configurations from switches (Cisco, Juniper, etc.), uploading them to Google Drive, and sending them to a Telegram channel. It supports SSH communication, Google Drive integration, and Telegram Bot API.

## Features
- **Backup Switch Configurations**: Retrieves running configurations from network devices via SSH.
- **Google Drive Integration**: Uploads configuration files to Google Drive with automatic folder creation.
- **Telegram Integration**: Sends configuration files to a Telegram channel using a bot.
- **Scheduled Backups**: Run backups automatically using the `schedule` library.

## Prerequisites

Before using the script, ensure you have the following installed:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Required Python libraries: 
  - `Flask`
  - `paramiko`
  - `requests`
  - `schedule`
  - `google-auth`
  - `google-api-python-client`
  - `flask_pymongo`
  - `pymongo`

  Install them using `pip`:
  ```bash
  pip install Flask paramiko requests schedule google-auth google-api-python-client flask_pymongo pymongo
  python3.X main.py



# Network Management Dashboard

This project is a web-based dashboard built with Flask that provides an interface to manage and back up network devices (switches). It connects to a MongoDB database to store information about network switches and allows the user to add, edit, delete, and back up configuration data.

## Features

- **Login System**: User authentication using Flask-Login.
- **Manage Network Devices**: Add, edit, and delete network switches from the MongoDB database.
- **Backup Switch Configuration**: Generate configuration backups for all switches stored in the database.
- **MongoDB Integration**: Uses MongoDB to store switch information and backup details.
- **User Session Management**: Session management with a timeout of 30 minutes.

## Prerequisites

Before setting up this project, ensure you have the following:

- **Python 3.x**: [Download Python](https://www.python.org/downloads/)
- Required Python libraries:
  - `Flask`
  - `Flask-PyMongo`
  - `Flask-Login`
  - `pymongo`
  - `boto3`

  Install the dependencies with `pip`:
  ```bash
  pip install Flask Flask-PyMongo Flask-Login pymongo
    python3.X main.py

