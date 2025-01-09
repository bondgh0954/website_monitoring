
# Website Monitoring Project

This project is a Python-based website monitoring tool that ensures the availability of your web application. It monitors the website hosted on a remote DigitalOcean server, running inside a Docker container, and takes automatic recovery actions if the application is down.

## Features

- Monitors website availability at specified intervals.
- Sends email notifications when the website is down.
- Automatically restarts the Docker container running the application.
- Optionally reboots the server if the issue persists (configurable).

## Requirements

- A server on DigitalOcean (or any other hosting platform).
- Docker installed and the application running inside a container.
- Python 3.x installed on the server.
- Necessary Python libraries:
  - `requests`
  - `smtplib`
  - `email`
- A Gmail account for sending email notifications.

## Setup

### 1. Prepare the Server

- Set up a server on DigitalOcean (or any hosting provider).
- Install Docker:
  ```bash
  sudo apt update
  sudo apt install docker.io

    Run your web application as a Docker container:

    docker run -d --name your_container_name -p 80:80 your_docker_image

2. Install Python and Dependencies

    Install Python 3.x:

sudo apt install python3 python3-pip

Install required libraries:

    pip install requests

3. Set Up Email Notifications

    Enable "Less Secure Apps" or generate an App Password in your Gmail account.
    Configure the script with your email credentials.

4. Deploy the Monitoring Script

    Clone this repository or download the script file.
    Update the configuration in monitor_and_restart.py:
        WEBSITE_URL: Replace with your website's URL.
        DOCKER_CONTAINER_NAME: Set to your container's name.
        EMAIL_SENDER, EMAIL_PASSWORD, and EMAIL_RECEIVER: Update with your email details.

5. Run the Script

Start the script to begin monitoring:

python3 monitor_and_restart.py

To keep the script running in the background, use tools like tmux, screen, or set it up as a systemd service.
How It Works

    The script checks the website's availability at regular intervals.
    If the website is down:
        Sends an email notification.
        Restarts the Docker container.
    If the issue persists after restarting the container:
        (Optional) Reboots the server.
    Logs the actions taken for future reference.

Configuration Options

    Monitoring Interval: Update CHECK_INTERVAL to change how often the website is checked.
    Email Notifications: Ensure the correct SMTP server and port are set for your email provider.
    Server Reboot: Enable or disable automatic server reboot by modifying REBOOT_SERVER.
