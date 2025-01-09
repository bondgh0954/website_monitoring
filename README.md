
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
- Necessary Python libraries:
  - `requests`
  - `smtplib`
  - `pramiko`
- A Gmail account for sending email notifications.

## Setup

### 1. Prepare the Server

- Set up a server on DigitalOcean (or any hosting provider).
- Install Docker:
  ```bash
  sudo apt update
  sudo apt install docker.io

    Run nginx as a Docker container:

    docker run -d -p 80:80 nginx

2. Install Python and Dependencies

Install required libraries:

    pip install requests







