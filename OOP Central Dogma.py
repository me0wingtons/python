###############
# CODON TABLE #
###############

bases = 'UCAG'
codons = [a + b + c for a in bases for b in bases for c in bases]
amino_acids = 'FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG'
codon_table = dict(zip(codons, amino_acids))

################################################################################


class NucleicAcid:
    def __init__(self, code):
        self.code = code
        
    def complementary(self):
        com = ''
        for base in self.code:
            if base == 'A':
                com += 'T'
            elif base == 'T':
                com += 'A'
            elif base == 'C':
                com += 'G'
            elif base == 'G':
                com += 'C'
        return com


class DNA(NucleicAcid):
    def __init__(self, code):
        super().__init__(code)

    def replicate(self):
        return DNA(self.code)

    def transcription(self):
        com = self.complementary()
        txn = ''
        for base in com:
            if base == 'T':
                txn += 'U'
            else:
                txn += base
        return mRNA(txn)

    
class mRNA(NucleicAcid):
    def __init__(self, code):
        super().__init__(code)

    def translation(self):
        peptide_code = ''
        for i in range(0, len(self.code), 3):
            codon = self.code[i:i+3]
            aa = codon_table[codon]
            if aa != '*':
                peptide_code += aa
            else:
                break
        return Peptide(peptide_code)


class Peptide:
    def __init__(self, code):
        self.code = code


promoter = DNA('TATA')
