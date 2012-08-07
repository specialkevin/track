#track

A command-line tool to time and track how long a command takes to run. It will also send you a text message via Twilio upon completion or error.

## Installation

### Requirements

twilio-python

## Usage

    track "ping -c 50 google.com"

You must wrap your command in quotes for it to work and not complain about invalid number of arguments.
