# coding: utf-8

# In[ ]:

# script to make a plot from a dataframe
# Fri Dec 9, 2016

# In[2]:

# import libraries: pandas, matplotlib.pyplot
import pandas
import matplotlib.pyplot as plt
# needed to allow calling a data filename for processing in terminal ie. chr18 vs. chr21
import sys
#this is needed to show the graph in this window
#commented out for to make a working .py file
#%matplotlib inline

#pulls in a text argument entered in terminal and feeds it to python
#Usage: gc_gene_plot_1.py myfile.txt
#filename = "myfile"
filename = sys.argv[1]
print("You are analyzing file:" + filename)

# import data using pandas
human_chr21 = pandas.read_csv(filename, sep="\t")
# calculate proportions and save as new columns in existing dataframe
human_chr21['gc_content'] = human_chr21['gc_bases']/ (human_chr21['win_end'] - human_chr21['win_start'])
human_chr21['gene_content'] = human_chr21['exon_bases'] / (human_chr21['win_end'] - human_chr21['win_start'])
# make a nice new plot
plt.plot(human_chr21['gc_content'],human_chr21['gene_content'], 'o')
plt.xlabel('Gene Content')
plt.ylabel('GC Content')
# save plot with name
plot_file_name = filename + '_plot.png'
plt.savefig(plot_file_name)

