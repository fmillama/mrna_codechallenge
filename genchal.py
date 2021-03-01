import io
import os

class InvalidArgument(Exception):
    """Raised when input is not .txt file or string"""
    pass

class InvalidLetterError(Exception):
    """Raised when string characters are not A, C, G or U"""
    pass

class InvalidLengthError(Exception):
    """Raised when number of letters is not a multiple of 3"""
    pass

class InvalidEndingError(Exception):
    """Raised when string does not end in a stop codon"""
    pass

def genargs(inp):
    """Creates a text stream whether it is from a path at the directory or a string, or else returns InvalidArgument"""
    if os.path.isfile(inp) and inp.endswith('.txt'):
        return open(inp,'rt')
    elif isinstance(inp,str): #Invalid filepaths will be processed as strings and likely generate a LetterError
        return io.StringIO(inp)
    else:
        raise InvalidArgument('Input must be .txt file at directory or string')

def genproc(inp):
    """For Challenge 2 define generator function and run next() for each gene output"""
    buf=genargs(inp)
    letters=['A','C','G','U']
    stopcodon=['UAG','UGA','UAA']
    codon='' #Initializes the codon
    codonlist=[] #Initializes the list of codons
    for lincount, lin in enumerate(buf,start=1): #Counts lines
        lin=lin.split('>')[0] #Ignores comments from text stream
        lin=''.join(lin.split()).upper() #Removes whitespace and switches to uppercase
        for charcount, char in enumerate(lin,start=1): #Counts columns
            if char not in letters:
                raise InvalidLetterError('Letters must be A, C, G or U.\nFound {0} at line {1}, column {2}'.format(char,lincount,charcount))
            codon+=char
            if len(codon)==3:
                codonlist.append(codon) #Records a complete codon when length reaches 3
                if codon in stopcodon:
                    if len(codonlist)>1: #Ignores consecutive stop codons
                        yield codonlist #Records a complete gene when a stop codon is found
                    codonlist=[] #Reinitializes the list of codons
                codon='' #Reinitializes the codon
    if codon:
        raise InvalidLengthError('Number of letters must be a multiple of 3.\nProcess complete with unfinished codon: '+codon)
    if codonlist:
        raise InvalidEndingError('Sequence must end in stop codons UAG, UGA or UAA.\nProcess complete with unfinished gene: {}'.format(codonlist))
    return print('Process successful')

def genex(st):
    """For Challenge 1: creates a list comprehension with all genes from text stream if no error is raised"""
    return [gene for gene in genproc(st)]
