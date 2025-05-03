# Plex-Date-Added

I needed a way to remove a video from the "Recently Added in $LIBRARY" section of Plex. I found that while you could easily edit the meta-data of the file in the Plex interface, the "Date Added" field was not visible. Editing it via sqlite directly was possible, but annoying, so this uses the Plex API to do it.

## Usage:

```
python main.py -h
usage: main.py [-h] -H HOST -l LIBRARY -t TITLE [-u USERNAME] [-p PASSWORD] [-a AUTH_TOKEN] [-d DATE_ADDED]

options:
  -h, --help            show this help message and exit
  -H, --host HOST
  -l, --library LIBRARY
  -t, --title TITLE
  -u, --username USERNAME
  -p, --password PASSWORD
  -a, --auth-token AUTH_TOKEN
  -d, --date-added DATE_ADDED
```

### Authentication

To authenticate with Plex, you need to either specify your username and password, or an auth token. Getting an auth token is an easy way to make this process simple, and is detailed here: https://support.plex.tv/articles/204059436-finding-an-authentication-token-x-plex-token/

### SSL Verification

The hostname used must include a protocol (http:// or https://). If HTTPS is used, a valid SSL certificate must be used. If this is in a home-lab, you can use the plex.direct hostname like: https://12-34-56-78.123456789.plex.direct:32400



