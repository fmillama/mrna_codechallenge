import io
import os

def genargs():
    """Creates a text stream whether it is from a path at the directory or a string, or else returns InvalidArgument"""
    inp=input('Insert local .txt pathfile or string: ')
    if os.path.isfile(inp) and inp.endswith('.txt'):
        return open(inp,'rt')
    else: #Invalid filepaths will be processed as strings and likely generate a LetterError
        return io.StringIO(inp)

def genbuild(char,codon,codonlist):
    yld=[]
    codon+=char
    if len(codon)==3:
        codonlist.append(codon)
        if codon in ['UAG','UGA','UAA']:
            if len(codonlist)==1:
                print(f'Warning: single codon gene {codon} ignored.')
            else:
                yld=codonlist
            codonlist=[]
        codon=''
    return [yld,codon,codonlist]

def genunf(codonlist, codon):
    '''Records unfinished genes and codons'''
    genstr,codstr='',''
    if codonlist:
        genstr+=f'Gene: {codonlist}. '
    if codon:
        codstr+=f'Codon: {codon}.'
    return [genstr,codstr]

def genproc(buf):
    """For Challenge 2 define generator function and run next() for each gene output"""
    codon,codonlist='',[] #Initializes codon and gene
    for lincount, lin in enumerate(buf,start=1): #Counts lines
        lin=lin.split('>') #Ignores comments from text stream
        seq=''.join(lin[0].split()).upper() #Removes whitespace and switches to uppercase
        for charcount, char in enumerate(seq,start=1): #Counts columns
            if char in ['A','C','G','U']:
                build=genbuild(char,codon,codonlist)
                codon,codonlist=build[1],build[2]
                if build[0]:
                    yield build[0]
            else: #Yields an error message if an invalid character is found
                yield f'Error: will ignore {char} found at line {lincount}, column {charcount}. Letters must be A, C, G or U.'
        if len(lin)>1:
            print(lin[1][:-1]) #Prints comment lines for clarity
            if codon or codonlist: #Reports on unfinished genes and codes
                warn=genunf(codonlist,codon)
                print('Warning: comment line reached but will not reset unfinished elements. '+warn[0]+warn[1])
    if codon or codonlist: #Yields an error message if process terminated with unfinished genes and codons
        warn=genunf(codonlist,codon)
        yield f'Error: end of stream reached with unfinished elements. '+warn[0]+warn[1]+'\nSequence must have length divisible by 3 and end in stop codon UAG, UGA or UAA.'
    return print('Process terminated')

def genex():
    """For Challenge 1: creates a list comprehension with all genes from text stream if no error is raised"""
    buf=genargs()
    generator=genproc(buf)
    for gene in generator:
        print(gene)
