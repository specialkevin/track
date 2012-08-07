#track

A command-line tool to time and track how long a command takes to run. It will also send you a text message via Twilio upon completion or error.

## Installation

### Requirements

    pip install twilio

### Setup

Setup your twilio API access as environment variables. Replace the values with the corresponding values for your account.

    echo "export TWILIO_ACCOUNT_SID=ACXXXXXXXXXXXXXXXXX" >> ~/.bashrc
    echo "export TWILIO_AUTH_TOKEN=YYYYYYYYYYYYYYYYYY" >> ~/.bashrc

Setup the phone number provided by Twilio associated with your account.

    echo "export TWILIO_PHONE_NUMBER=+11234567890" >> ~/.bashrc

Setup the phone number you would like the SMS alert sent too. (Your phone number)

    echo "export TRACK_PHONE_NUMBER=+11234567890" >> ~/.bashrc

## Usage

    track "ping -c 50 google.com"

You must wrap your command in quotes for it to work and not complain about invalid number of arguments.
