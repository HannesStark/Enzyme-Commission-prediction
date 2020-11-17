import os

from Bio import SeqIO
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sn
sn.set_style('darkgrid')


fasta_path = 'data/nonRed_dataset.fasta'


identifiers = []
labels = []
sequences = []
solubility = []
for record in SeqIO.parse(fasta_path, "fasta"):
    identifiers.append(record.id)
    sequences.append(str(record.seq))
df = pd.DataFrame(list(zip(identifiers, sequences)),
                  columns=['identifier', 'seq'])
# df = df[df['solubility'] != 'U']
df['length'] = df['seq'].apply(lambda x: len(x))
print(df.describe())


## visualize class prevalences
#counts = df['label'].value_counts()
#counts = pd.DataFrame({'Localization': counts.index,
#                       "Number_Sequences": counts.array})
#counts['ordering'] = counts['Localization'].apply(lambda x: LOCALIZATION.index(x))
#counts = counts.sort_values(by=['ordering'])
#barplot = sn.barplot(x='Number_Sequences', y='Localization', data=counts, ci=None)
#barplot.set(xlabel='Number Sequences per Class', ylabel='')
#plt.show()
#
#print(df['label'].value_counts())

print('percentage of sequences larger than threshold AAs: {}'.format(100 * len(df[df['length'] > 1000]) / len(df)))
print(df[df['length'] > 6000])

cut_off = 1100
df[df['length'] < cut_off].hist(bins=50, ec='black')
plt.xlim((40, cut_off))  # there are only sequences longer than 40 in the datset
plt.title("Sequence lengths")
plt.xlabel("Sequence length")
plt.ylabel("Number sequences")
plt.show()

#cut_off = 1500
#axes = df[df['length'] < 1500].hist(by='label', ec='black', bins=30, color=color)
#for rows in axes:
#    for cell in rows:
#        cell.set_xlim((40, cut_off))  # there are only sequences longer than 40 in the datset
#        cell.tick_params(axis='x', which='both', labelbottom=False)
#plt.show()
