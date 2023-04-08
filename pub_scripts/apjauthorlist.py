#
#
# process the author XLSX file to latex in this case appropriate for Astrophysical Journal
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
            name=(' '.join([row['Firstname'],row['Lastname']]))
        else:
            name=(' '.join([row['Firstname'],row['Middle'],row['Lastname']]))
        if pandas.isnull(row['ORCID']):
            print(r'\author{%s}'%(name))
        else:
            print(r'\author[%s]{%s}'%(row['ORCID'],name))

        dumarray=[]
        for nameval in ['Affil1','Affil2','Affil3']:
            if pandas.notnull(row[nameval]):
                resdf=affilexcel[affilexcel['Affil']==row[nameval]]
                for index, rowa in resdf.iterrows():
                    print(r'\affiliation{%s}' % rowa['Affiliation'])
