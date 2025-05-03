#!/usr/bin/env python3

import argparse
import os
import sys

from plexapi.myplex import MyPlexAccount
from plexapi.server import PlexServer

# Example:
# python main.py -a $PLEX_TOKEN -H "https://12-34-56-78.123456789.plex.direct:32400" -l Movies -t "Comedy Central Roast of Pamela Anderson"
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--host",required=True)
parser.add_argument("-l", "--library",required=True)
parser.add_argument("-t", "--title",required=True)
parser.add_argument("-u", "--username")
parser.add_argument("-p", "--password")
parser.add_argument("-a", "--auth-token")
parser.add_argument("-d", "--date-added", default="2020-01-01 00:00:00")
args = parser.parse_args()

if args.auth_token is not None:
	plex = PlexServer(args.host, args.auth_token)
elif args.username is not None and args.password is not None:
	account = MyPlexAccount(args.username, args.password)
	plex = account.resource(args.host).connect()
else:
	print("You must specify a user/pass or auth token")
	exit(1)

library = plex.library.section("Movies")
video = library.get(title="Comedy Central Roast of Pamela Anderson")

updates = {"addedAt.value": args.date_added}

video.edit(**updates)
