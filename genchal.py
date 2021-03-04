import io
import os

class InvalidArgument(Exception):
    pass

def genargs():
    print('Code Challenge: mRNA Sequence Processor')
    inp=''
    mode=''
    buf=1
    while inp not in['1','2']:
        inp=input('Enter 1 or 2 to select input type:\n1. Local .txt file\n2. String\n')
    if inp=='1':
        buf=input('Insert local .txt pathfile: ')
        if not os.path.isfile(buf) or not buf.endswith('.txt'):
            raise InvalidArgument('Invalid extension or file not found at local directory.')
        buf=open(buf,'rt',buffering=1)
    else:
        print('Insert lines of text followed by a blank line to be processed as a string.')
        multiline=''
        while buf:
            buf=input()
            multiline+=buf+'\n'
        buf=io.StringIO(multiline)
    while mode not in ['1','2','3']:
        mode=input('Enter 1, 2 or 3 to select processor mode:\n1. Print full gene list or terminate process with an error message.\n2. Print all genes and error messages until the end of file.\n3. Print one gene or error message at a time.\n')
    return [mode,buf]


def genbuild(char,codon,codonlist):
    """Constructs codons and genes"""
    yld=[]
    codon+=char #Adds character to codon
    if len(codon)==3:
        codonlist.append(codon) #Adds complete codon to gene
        if codon in ['UAG','UGA','UAA']: #hecks whether if complete codon is a stop codon
            if len(codonlist)==1: #Ignores single codon genes and issues a warning
                print(f'Warning: single codon gene {codon} ignored.')
            else:
                yld=codonlist #Stores complete gene to yield in "genproc"
            codonlist=[] #Resets gene
        codon='' #Resets codon
    return [yld,codon,codonlist]

def genunf(codonlist, codon):
    '''Records unfinished genes and codons'''
    genstr,codstr='',''
    if codonlist: #Checks unfinished gene
        genstr+=f'Gene: {codonlist}. '
    if codon: #Checks unfinished codon
        codstr+=f'Codon: {codon}.'
    return [codstr,genstr]

def genproc(buf):
    """Defines generator function. Command next() will iterate through each gene and error."""
    print("Warning: any text between comment character '>' and end of line will not be processed.")
    codon,codonlist='',[] #Initializes codon and gene
    for lincount, lin in enumerate(buf,start=1): #Counts lines
        lin=lin.split('>') #Ignores comments from text stream
        seq=''.join(lin[0].split()).upper() #Removes whitespace and switches to uppercase
        for charcount, char in enumerate(seq,start=1): #Counts columns
            if char in ['A','C','G','U']:
                build=genbuild(char,codon,codonlist) #Constructs codons and genes
                codon,codonlist=build[1],build[2]
                if build[0]:
                    yield build[0] #Yields complete gene
            else: #Yields an error message if an invalid character is found
                yield f'Error: will ignore {char} found at line {lincount}, column {charcount}. Letters must be A, C, G or U.'
        if len(lin)>1:
            print(lin[1][:-1]) #Prints comment lines for clarity
            if codon or codonlist: #Reports on unfinished genes and codes
                warn=genunf(codonlist,codon)
                print('Warning: comment line reached but will not reset unfinished elements. '+warn[1]+warn[0])
    warn=genunf(codonlist,codon)
    if warn[0]:
        yield 'Error: sequence must have length divisible by 3. Process complete with unfinished elements. '+warn[0]
    if warn[1]:
        yield 'Error: sequence must end in stop codon UAG, UGA or UAA. Process complete with unfinished elements. '+warn[1]
    return print('Process terminated')

def genex():
    """Prints genes and errors yielded from "genproc" iterator as well as warnings"""
    source=genargs()
    generator=genproc(source[1])
    result=[]
    for gene in generator:
        if source[0]=='1':
            if "Error" in gene:
                return print(gene)
            result.append(gene)
        else:
            print(gene)
            if source[0]=='3':
                inp=input('\nPress enter to return next gene or error message: ')
    if source[0]=='1':
        print('\nOutput:\n')
        print(result)