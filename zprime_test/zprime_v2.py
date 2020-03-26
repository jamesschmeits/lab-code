"""Program for determining Zprime from a csv data file."""
# import sys
import csv
from statistics import stdev
import os
import time


def zprime_calc(positive_list, negative_list):
    """Calculate Zprime"""
    ave_pos = sum(positive_list) / len(positive_list)
    ave_neg = sum(negative_list) / len(negative_list)
    stdev_pos = stdev(positive_list)
    stdev_neg = stdev(negative_list)
    zprime = 1 - 3 * (stdev_pos + stdev_neg) / abs(ave_pos - ave_neg)
    return zprime


def main():
    """Main program will watch for new files
    and then pass them to csv_work, getting back
    zprime values to write to a new file."""
    path_to_watch = '.'
    before = dict([(f, None) for f in os.listdir(path_to_watch)])
    while 1:
        time.sleep(5)
        after = dict([(f, None) for f in os.listdir(path_to_watch)])
        added = [f for f in after if f not in before]
        if added:
            zprime_num = str(csv_work(added))
            print(added, zprime_num)
            with open(
                'zprime_log.txt',
                mode='wt',
                encoding='utf-8'
            ) as output_file:
                output_file.write(zprime_num)
                # want to add the file name
                # want to append it instead of making a new file
        before = after


def csv_work(data_file):
    """Main program for opening and closing files,
    extracting data and calling zprime"""
    with open(data_file[0], newline='') as data_handle:
        data_reader = csv.reader(data_handle)
        data = []
        # make a single list of all the data fields
        for one_line in list(data_reader):
            data.extend(one_line)
    with open('template.csv', newline='') as template_handle:
        template_reader = csv.reader(template_handle)
        template = []
        # make a single list of all the temple fields
        for one_line in list(template_reader):
            template.extend(one_line)
    # pair the template fields to the data fields
    paired_list = list(zip(template, data))
    # populate lists with positive and negative data
    positive_list = []
    negative_list = []
    for identity, value in paired_list:
        if identity == 'positive':
            positive_list.append(float(value))
        elif identity == 'negative':
            negative_list.append(float(value))
    zprime = zprime_calc(positive_list, negative_list)
    return zprime


if __name__ == "__main__":
    main()
