# mrna_codechallenge
Processing mRNA Sequences - Code Challenge 2021

# mrna_codechallenge
Processing mRNA Sequences - Code Challenge 2021

Francesc Millà Martínez. Intern at Capgeimin's AD Center (valencia)
Two main files: genchal.py and test_genchal.py
Found in https://github.com/fmillama/mrna_codechallenge/master/

genchal.py
1. Defines four exception classes:
  InvalidArgument
  InvalidLetterError
  InvalidLengthError
  InvalidEndingError
2. Defines function "genargs(inp)":
  Determines whether input "inp" is a file at the directory with extension .txt and generates a text stream.
  Otherwise, determines whether input is a string and creates an in-memory text stream.
  Otherwise raises InvalidArgument error.
3. Defines generator function "genproc(inp)" to meet the Challenge 2 requirements. 
Once the generator with an argument is defined, each next() execution will yield a complete gene in the form of a list of strings, or else an error.
Execution terminates if next() yields an error:
  Calls genargs to generate text stream.
  Reads lines from text stream in a for loop with a line counter.
  Omits comment lines starting with '>'.
  Removes whitespace from lines and switches to uppercase.
  Reads columns from text stream lines in a for loop with a column counter.
  Checks whether each column matches letters A, C, G, U, otherwise raises InvalidLetterError.
  Adds columns to empty string "codon".
  Checks whether "codon" has reached length 3.
  If so, adds "codon" to empty list "codonlist", then checks whether "codon" is a stopcode UAG, UGA, UAA.
  If so, yields and resets "codonlist" and "codon". Otherwise it only resets "codon".
  When all lines have been read, checks whether "codon" and "codonlist" are unfinished. 
  If so, raises InvalidLengthError or InvalidEndingError respectively. 
  Otherwise prints 'Process successful' and terminates.
4. Defines function "genex(inp)" to meet the Challenge 1 requirements:
  Runs generator function "genproc" and creates a list comprehension with all genes yielded, this is, a list of lists of strings.
  Will not return a list if any of the four exceptions defined are raised.


test_genchal.py
1. Defines "test_genex(self)" unit test.
  Defines a set of mock data.
  Runs 5 assert methods to check whether "genchal.genex" provides edsired output.
  
