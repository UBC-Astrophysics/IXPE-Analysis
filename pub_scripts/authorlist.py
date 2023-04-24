#!/usr/bin/python
# -*- coding: utf-8 -*-
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


finds=   [  '&',   'ü',   'ü',   'í',   'á',   'ò',   'à',   'à',  'č'   , '#',  '%', 'é']
replaces=[r'\&',r'\"u',r'\"u',r'\'i',r'\'a',r'\`o',r'\`a',r'\`a',r'\v{c}',r'\#',r'\%', r'\'e']

def unicode_to_latex(s):
    t=s
    for f,r in zip(finds,replaces):
        t=t.replace(f,r)
    
    return t

def uprint(s):
    print(unicode_to_latex(s))

def setuparrays():
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

def aalist():
    setuparrays()
    
# output the authors with affiliations footnoted
    namelist=[]
    for name,affil in zip(namearray,affilarray):
        namelist.append(r'%s \inst{\ref{in:%s}}' % (name,r'},\ref{in:'.join(affil)))
# output the affiliations        
    uprint(r'''%% list of authors
%% 
\author{%s}''' % '\n\\and '.join(namelist))
    

    affilarray=[]
    for ii,affil in enumerate(affillist):
        resdf=affilexcel[affilexcel['Affil']==affil]
        for index, row in resdf.iterrows():
            affilarray.append(r'%s \label{in:%s}' % (row['Affiliation'],affil))
    uprint(r'''
%% list of affiliations
    \institute{%s}''' % '\n\\and\n'.join(affilarray))

def apjlist():
    # create list of authors and ordered list of affiliations
    for index, row in authorexcel.iterrows():
        if pandas.isnull(row['Middle']):
            name=(' '.join([row['Firstname'],row['Lastname']]))
        else:
            name=(' '.join([row['Firstname'],row['Middle'],row['Lastname']]))
        if pandas.isnull(row['ORCID']):
            uprint(r'\author{%s}'%(name))
        else:
            uprint(r'\author[%s]{%s}'%(row['ORCID'],name))

        dumarray=[]
        for nameval in ['Affil1','Affil2','Affil3']:
            if pandas.notnull(row[nameval]):
                resdf=affilexcel[affilexcel['Affil']==row[nameval]]
                for index, rowa in resdf.iterrows():
                    uprint(r'\affiliation{%s}' % rowa['Affiliation'])


def naturelist():
    setuparrays()

# output the authors with affiliations footnoted
    namelist=[]
    for name,affil in zip(namearray,affilarray):
        footnotelist=[]
        for aa in affil:
            footnotelist.append(str(affillist.index(aa)+1))
        namelist.append('%s$^{%s}$' % (name,','.join(footnotelist)))
# output the affiliations        
    uprint(r'\author{%s}' % ',\n'.join(namelist))
    uprint(r'''
\begin{document}
\linenumbers

\maketitle

\begin{affiliations}''')
    for ii,affil in enumerate(affillist):
        resdf=affilexcel[affilexcel['Affil']==affil]
        for index, row in resdf.iterrows():
            uprint(r'\item %s' % row['Affiliation'])
    print(r'\end{affiliations}')

def mnlist():
    setuparrays()
    # output the authors with affiliations footnoted
    namelist=[]
    for name,affil in zip(namearray,affilarray):
        footnotelist=[]
        for aa in affil:
            footnotelist.append(str(affillist.index(aa)+1))
        namelist.append('%s$^{%s}$' % (name,','.join(footnotelist)))
# output the affiliations        
    uprint(r'''%% list of authors, use \newauthor to break lines
%% 
\author[Short Author List]{%s''' % ',\n'.join(namelist))
    print(r'''% list of affiliations
\\''')
    for ii,affil in enumerate(affillist):
        resdf=affilexcel[affilexcel['Affil']==affil]
        for index, row in resdf.iterrows():
            uprint(r'$^{%d}$ %s\\' % (ii+1,row['Affiliation']))
    print(r'}')

namearray=[]
affilarray=[]
affillist=[]
    
if len(argv)<2:
    print('python authorlist.py [-n/-aa/-mn/-apj] author.xlsx')
else:
    if (len(argv)<3):
        f=argv[1]
    else:
        f=argv[2]
    authorexcel=pandas.read_excel(f,sheet_name='Authors')
    affilexcel=pandas.read_excel(f,sheet_name='Affiliations')
    if len(argv)<3:
        naturelist()
    elif argv[1]=='-aa':
        aalist()
    elif argv[1]=='-mn':
        mnlist()
    elif argv[1]=='-apj':
        apjlist()
    else:
        naturelist()
