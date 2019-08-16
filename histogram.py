#!/usr/bin/env python3


import pandas as pd
import matplotlib as plt
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import os,sys,argparse
import time

def file_process(filename):
    df1 = pd.read_csv(filename, sep=",", usecols = ['Protein', 'Drug'])
    df2 = df1.groupby(['Drug']).size().reset_index(name='count')
    df3 = df2.sort_values(by='count', ascending=False)
    return df3

def graph_image(df3): 
    my_plot = df3.plot.bar(stacked=False, colormap='Paired', figsize=(10,8), color=['antiquewhite'], width=(0.8), edgecolor='black')
    my_plot.set_xlabel("Drug", fontsize=16)
    my_plot.set_ylabel("Number of Target", fontsize=16)
    plt.title('Number of target per drug', fontsize=16)
    plt.savefig('foo.png')


def getArgs():
    parser = argparse.ArgumentParser('python')
    parser.add_argument('-infile', required=True)
    return parser.parse_args()

if __name__ == "__main__":
    args = getArgs()
    filename = file_process(args.infile)
    df3 = graph_image(filename)
    start = time.time()
    end = time.time()
    print ('time elapsed:' + str(end - start))


