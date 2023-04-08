#
#
# process the author XLSX file to latex in this case appropriate for Nature
#
# 1) To create the author XLSX file, use the Tier 2 author list, and move the Tier one authors to the top and add additional authors where appropriate
# 2) Be sure to add the affilliations of the additional authors to the affiliation sheet as well.
#
#
#
import pandas
import numpy as np
from sys import argv
from sys import argv
if len(argv)<2:
    print('python authorlist.py author.xlsx')
else:
    authorexcel=pandas.read_excel(argv[1],sheet_name='Authors')
    affilexcel=pandas.read_excel(argv[1],sheet_name='Affiliations')

    namearray=[]
    affilarray=[]
    affillist=[]
# create list of authors and ordered list of affiliations
    for index, row in authorexcel.iterrows():
        if pandas.isnull(row['Middle']):
            namearray.append(' '.join([row['Firstname'],row['Lastname']]))
        else:
            namearray.append(' '.join([row['Firstname'],row['Middle'],row['Lastname']]))
        dumarray=[]
        for nameval in ['Affil1','Affil2','Affil3']:
            if pandas.notnull(row[nameval]):
                dumarray.append(row[nameval])
                if not (row[nameval] in affillist): 
                    affillist.append(row[nameval])        
        affilarray.append(dumarray)

# output the authors with affiliations footnoted
    namelist=[]
    for name,affil in zip(namearray,affilarray):
        footnotelist=[]
        for aa in affil:
            footnotelist.append(str(affillist.index(aa)+1))
        namelist.append('%s$^{%s}$' % (name,','.join(footnotelist)))
# output the affiliations        
    print(r'\author{%s}' % ',\n'.join(namelist))
    print(r'''
\begin{document}
\linenumbers

\maketitle

\begin{affiliations}''')
    for ii,affil in enumerate(affillist):
        resdf=affilexcel[affilexcel['Affil']==affil]
        for index, row in resdf.iterrows():
            print(r'\item %s' % row['Affiliation'])
    print(r'\end{affiliations}')