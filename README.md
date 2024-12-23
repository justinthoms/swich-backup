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


