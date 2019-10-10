"""
Выполнила: Крылова Александра Сергеевна
"""


import csv
from datetime import datetime
from datetime import timedelta
import argparse

PARSER = argparse.ArgumentParser(description='Data for the construction of candlestick charts.')
PARSER.add_argument('-f', '--file', type=str,
                    help='File containing exchange transactions in .csv format.')
PARSER.add_argument('--full_info', action='store_true',

                    help='a brief description of all the functions used')
ARGS = PARSER.parse_args()
if ARGS.full_info:
    print("\nFunction\n\n" +
          "1. ticker_value_interval(tikerlist, value_line, rang, interval)\n" +
          "Write data to the list\n\n2. csv_writer(interval_list, listname)\n" +
          "Write list to .csv file\n\n" +
          "3. interval_do(args_file, interval, tiker_list, listname)\nCreates a valid string\n\n")


def ticker_value_interval(tikerlist, value_line, rang, interval):
    """Write data to the list"""
    v_l = value_line[1]
    if not tikerlist:                                                        #if list is empty
        tikerlist.extend([value_line[0], value_line[3], v_l, v_l, v_l, v_l])
    if float(v_l) < float(tikerlist[4]):
        tikerlist[4] = v_l
    if float(v_l) > float(tikerlist[3]):
        tikerlist[3] = v_l
    tikerlist[5] = v_l
    tikerlist[1] = (rang - timedelta(minutes=interval)).strftime("%Y-%m-%d %H:%M:%S")
    return tikerlist


def csv_writer(interval_list, listname):
    """Write list to .csv file"""
    with open(listname + '.csv', 'w', newline='') as f_w:
        writer = csv.writer(f_w)
        for i in interval_list:
            writer.writerow(i)


def interval_do(args_file, interval, tiker_list, listn):
    """Creates a valid string"""
    with open(args_file, 'r') as file:
        sber_tiker = []
        aapl_tiker = []
        amzn_tiker = []
        t_d_d_t = '%Y-%m-%d %H:%M:%S.%f'
        reader = csv.reader(file)
        start = datetime.strptime('2019-01-30 07:00:00.000000', t_d_d_t)
        stop = datetime.strptime('2019-01-31 03:00:00.00000', t_d_d_t) + timedelta(minutes=interval)
        rang = datetime.strptime('2019-01-30 07:00:00.000000', t_d_d_t)
        for line in reader:
            time = datetime.strptime(line[3], t_d_d_t)
            if (time.strftime(t_d_d_t) >= start.strftime(t_d_d_t)
                    and (time.strftime(t_d_d_t) <= stop.strftime(t_d_d_t))):
                if time.strftime(t_d_d_t) < rang.strftime(t_d_d_t):=
                
                    if line[0] == 'SBER':
                        ticker_value_interval(sber_tiker, line, rang, interval)
                    if line[0] == 'AAPL':
                        ticker_value_interval(aapl_tiker, line, rang, interval)
                    if line[0] == 'AMZN':
                        ticker_value_interval(amzn_tiker, line, rang, interval)
                else:
                    if (rang - timedelta(minutes=interval)).strftime("%Y-%m-%d %H:%M:%S") \
                            in aapl_tiker:
                        tiker_list.append(aapl_tiker)
                    if (rang - timedelta(minutes=interval)).strftime("%Y-%m-%d %H:%M:%S") \
                            in sber_tiker:
                        tiker_list.append(sber_tiker)
                    if (rang - timedelta(minutes=interval)).strftime("%Y-%m-%d %H:%M:%S") \
                            in amzn_tiker:
                        tiker_list.append(amzn_tiker)
                    sber_tiker = []
                    aapl_tiker = []
                    amzn_tiker = []
                    rang = rang + timedelta(minutes=interval)
        csv_writer(tiker_list, listn)


if ARGS.file:
    OHLC5MIN = []
    OHLC30MIN = []
    OHLC240MIN = []
    interval_do(ARGS.file, 5, OHLC5MIN, 'ohlc_5min')
    interval_do(ARGS.file, 30, OHLC30MIN, 'ohlc_30min')
    interval_do(ARGS.file, 240, OHLC240MIN, 'ohlc_240min')
