#!/usr/bin/env python
import argparse
from src.arguments.search import search_args
PARSER = argparse.ArgumentParser()
PARSER.add_argument("-s", "--search", help="enable debug mode",
                    action="store_true")

ARGV = PARSER.parse_args()


if __name__ == "__main__":
    search_args()