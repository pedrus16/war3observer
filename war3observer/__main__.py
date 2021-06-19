import argparse
import json
import os

from war3observer import __version__, Server

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument('--version',
    action='version',
    version='war3observer %s' % __version__)
  parser.add_argument('--config',
    default='./war3observer.config.json',
    help='the path to a config file to use')
  parser.add_argument('-v', '--verbose',
    default=argparse.SUPPRESS,
    type=int,
    const=10,
    nargs='?',
    dest='loggingLevel',
    metavar='LOGGINGLEVEL',
    help='the logging level to use')
  parser.add_argument('--host',
    default=argparse.SUPPRESS,
    help='the address the server will listen on')
  parser.add_argument('--port',
    default=argparse.SUPPRESS,
    help='the port the server will listen on')
  parser.add_argument('--client-settings',
    default=argparse.SUPPRESS,
    type=json.loads,
    dest='clientSettings',
    help='options sent to the client (json)')

  args = parser.parse_args()

  path = args.config

  if os.path.isfile(path):
    with open(path, 'r') as json_file:
      config = json.load(json_file)
  else:
    config = {}

  args = vars(args)
  config = {**config, **args}

  server = Server(config)
  server.serve()

if __name__ == '__main__':
  main()
