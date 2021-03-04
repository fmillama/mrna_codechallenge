import unittest
import io
import os
from genchal import genbuild
from genchal import genunf
from genchal import genproc

class TestGenChal(unittest.TestCase):

    def test_genbuild(self):
        mock1=genbuild('A','UA',['UCC']) #completes gene
        self.assertEqual(mock1,[['UCC','UAA'],'',[]])
        mock2=genbuild('U','UA',['UCC']) #completes codon
        self.assertEqual(mock2,[[],'',['UCC','UAU']])
        mock3=genbuild('U','U',['UCC']) #adds character
        self.assertEqual(mock3,[[],'UU',['UCC']])
        mock4=genbuild('A','UA',[]) #ignores single codon gene
        self.assertEqual(mock4,[[],'',[]])

    def test_genunf(self):
        mock1=genunf([],'') #passes empty arguments
        self.assertEqual(mock1,['',''])
        mock2=genunf(['UCC'],'') #unfinished gene warning
        self.assertEqual(mock2,['', "Gene: ['UCC']. "])
        mock3=genunf([],'U') #unfinished codon warning
        self.assertEqual(mock3,['Codon: U.', ''])
        mock4=genunf(['UCC'],'U')
        self.assertEqual(mock4,['Codon: U.', "Gene: ['UCC']. "])

    def test_genproc(self):
        mock1=[gen for gen in genproc(io.StringIO('ACg ACG UAAACG uAA UAACCCUAA'))] #executes without errors and ignores consecutive stop codon
        self.assertEqual(mock1,[['ACG', 'ACG', 'UAA'],['ACG', 'UAA'],['CCC', 'UAA']])
        mock2=[gen for gen in genproc(io.StringIO('ACG ACG UAA ACG'))] #yields one gene and invalid ending error
        self.assertEqual(mock2,[['ACG', 'ACG', 'UAA'], "Error: sequence must end in stop codon UAG, UGA or UAA. Process complete with unfinished elements. Gene: ['ACG']. "])
        mock3=[gen for gen in genproc(io.StringIO('ACG ACG UAA AC'))] #yields one gene and invalid length error
        self.assertEqual(mock3,[['ACG', 'ACG', 'UAA'], 'Error: sequence must have length divisible by 3. Process complete with unfinished elements. Codon: AC.'])
        mock4=[gen for gen in genproc(io.StringIO('ACG UAA ECG'))] #yields one gene and invalid letter error
        self.assertEqual(mock4,[['ACG', 'UAA'], 'Error: will ignore E found at line 1, column 7. Letters must be A, C, G or U.', 'Error: sequence must have length divisible by 3. Process complete with unfinished elements. Codon: CG.'])

if __name__=='__main__':
    unittest.main()


