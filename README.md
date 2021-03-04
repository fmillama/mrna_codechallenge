# mrna_codechallenge
Processing mRNA Sequences - Code Challenge 2021

- Download folder at https://github.com/fmillama/mrna_codechallenge/tree/master 
- Execute main.py on terminal to run processor. Python 3 is required.
- Terminal will demand inputs:
  - First: 
    - Select 1 for a local .txt file. Then, enter filepath. An invalid extension or a path not found in the local directory will raise an exception.
    - Select 2 for a string. Then, enter lines of text followed by a blank line to be processed as a string.
  - Second:
    - Select 1 to process all input and print a single list of genes or a single error message.
    - Select 2 to process all input and print each gene and error message in order until the end of file.
    - Select 3 to print the first gene or error message in the file. Then press enter to print each subsequent gene or error message.
- For Challenge 1 select string input, provide string and lastly select 1 to return a list of genes or a single error message.
- Possible error messages:
  - Characters that are not A, C, G or U will not be processed. Returns invalid character with line and column position.
  - Sequence length of valid characters must be divisible by 3. Returns an unfinished codon at the end of the file.
  - Final codon must match stop codons UAG, UGA or UAA. Returns an unfinished gene at the end of the file.
- The processor will print warnings regardless of mode:
  - Input between the a comment character '>' and the end of line will not be processed.
  - Comments are printed for clarity.
  - Reports on unfinished genes or codons once a comment line is reached. These elements will not be reset.
  - Reports on skipped single codon genes.
- Execute test_genchal.py to run tests.
