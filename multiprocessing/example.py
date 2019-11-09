from sys import argv
from multiprocessing import Pool
from time import sleep

sleep_timeout = 2
pool_size = 4

def greet(word):
    print(f"{word} - Sleeping for {sleep_timeout} seconds...")
    sleep(sleep_timeout)
    print(f"{word} - Finished processing")

if __name__ == "__main__":

    words = argv[1:]

    with Pool(processes=pool_size) as p:
        p.map(greet, words)

    print("Finished processing everything")
