#!/usr/bin/env python3
"""
Created by: Isaac Ip
Created on: Oct 2026
This module prints integers from 1000 to 2000.
"""


def main():
    # The main() function prints integers from 1000 to 2000, returns None.
    counter1 = 0
    counter2 = 0
    counter3 = 0
    counter4 = 0
    # input
    
    # process and output
    for counter1 in range(2):
        for counter2 in range(10):
            for counter3 in range(10):
                for counter4 in range(10):
                    if counter4 % 5 == 0:
                        print(f"\n")
                    print(f"{counter1}{counter2}{counter3}{counter4}")