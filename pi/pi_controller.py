import requests
import time
import random
import click
from sense_hat import SenseHat
sense = SenseHat()


# Replace with your own function in Part 1
def get_direction():
    d_long = 0
    d_la = 0
    send_vel = False
    for event in sense.stick.get_events(): 
        c = event.direction
        if c =="left":
            click.echo('Left')
            send_vel = True
            d_long = -1
            d_la = 0
        elif c == "right":
            click.echo('Right')
            send_vel = True
            d_long = 1
            d_la = 0
        elif c =="up":
            click.echo('Up')
            send_vel = True
            d_long = 0
            d_la = 1
        elif c == "down":
            click.echo('Down')
            send_vel = True
            d_long = 0
            d_la = -1
        else:
            d_long = 0
            d_la = 0
            click.echo('Invalid input :(')
            send_vel = False
    return d_long, d_la, send_vel


if __name__ == "__main__":
    SERVER_URL = "http://127.0.0.1:5001/drone"
    while True:
        d_long, d_la, send_vel = get_direction()
        if send_vel:
            with requests.Session() as session:
                current_location = {'longitude': d_long,
                                    'latitude': d_la
                                    }
                resp = session.post(SERVER_URL, json=current_location)
