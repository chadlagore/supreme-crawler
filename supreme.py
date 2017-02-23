from difflib import SequenceMatcher
import os
import requests
import sys
import time
from time import gmtime, strftime

url = 'http://www.supremenewyork.com/shop'
thresh = 0.99 # Similarity

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


def get_time():
    return strftime("%Y-%m-%d %H:%M:%S", gmtime())


def get_cache():
    return requests.get(url).text


def wait_for_diff(cached, time_sleep):
    diff = 1

    while diff > thresh:
        # Sleep and check for updates.
        time.sleep(time_sleep)
        resp = requests.get(url)
        diff = similar(resp.text, cached)

        # Print some updates.
        print('/*------------------------------------------------*/')
        print('Checked {} at {}.'.format(url, get_time()))
        print('Noticed {} similarity.\n'.format(round(100*diff, 2)))

    print('Similarity dropped below 90%: {}. Check website now.'.format(diff))


def get_diff(a, b):
    for i,s in enumerate(difflib.ndiff(a, b)):
        if s[0]==' ': continue
        elif s[0]=='-':
            print(u'Delete "{}" from position {}'.format(s[-1],i))
        elif s[0]=='+':
            print(u'Add "{}" to position {}'.format(s[-1],i))


def finished():
    os.system('say "your program has finished"')


def main():
    print("Starting... ")

    time_sleep = 90 # Seconds

    if len(sys.argv) > 1:
        time_sleep = int(sys.argv[1])

    print(
        "Checking {} every {} seconds, control-c to kill.".format(
            url, time_sleep)
    )

    cached = get_cache()
    wait_for_diff(cached, time_sleep)
    finished()
    os.system('Rscript texter.R {}'.format(thresh))


if __name__ == '__main__':
    main()
