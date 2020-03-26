"""Program for determining Zprime from a csv data file."""
import sys
import csv
from statistics import stdev


def zprime_calc(positive_list, negative_list):
    """Calculate Zprime"""
    ave_pos = sum(positive_list) / len(positive_list)
    ave_neg = sum(negative_list) / len(negative_list)
    stdev_pos = stdev(positive_list)
    stdev_neg = stdev(negative_list)
    zprime = 1 - 3 * (stdev_pos + stdev_neg) / abs(ave_pos - ave_neg)
    return zprime


def main(data_file, template_file, out_file):
    """Main program for opening and closing files,
    extracting data and calling zprime"""
    with open(data_file, newline='') as data_handle:
        data_reader = csv.reader(data_handle)
        data = []
        # make a single list of all the data fields
        for one_line in list(data_reader):
            data.extend(one_line)
    with open(template_file, newline='') as template_handle:
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
    print("Zprime = " + str(zprime))

    # with open(out_file, mode='wt', encoding='utf-8') as output_file:
    #     outfile_writer = csv.writer(output_file)
    #     outfile_writer.writerows(paired_list)

if __name__ == "__main__":
    data_file = sys.argv[1]
    template_file = sys.argv[2]
    dot = data_file.find('.')
    out_file = data_file[:dot] + "_zprime" + data_file[dot:]
    main(data_file, template_file, out_file)
