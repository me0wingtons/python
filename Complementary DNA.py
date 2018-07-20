def complementary(dna):
    result = ''
    for letter in range(len(dna)):
        if dna[letter] == 'A':
            result += 'T'
        if dna[letter] == 'T':
            result += 'A'
        if dna[letter] == 'C':
            result += 'G'
        if dna[letter] == 'G':
            result += 'C'
    return 'Complementary strand:' + ' ' + result

print('complementary() function with DNA string argument')

def mRNA_of(dna):
    result = ''
    for letter in range(len(dna)):
        if dna[letter] == 'A':
            result += 'U'
        if dna[letter] == 'T':
            result += 'A'
        if dna[letter] == 'C':
            result += 'G'
        if dna[letter] == 'G':
            result += 'C'
    return 'mRNA strand:' + ' ' + result

print('mRNA_of() function with DNA string argument')

def template_of(rna):
    result = ''
    for letter in range(len(rna)):
        if rna[letter] == 'A':
            result += 'T'
        if rna[letter] == 'U':
            result += 'A'
        if rna[letter] == 'C':
            result += 'G'
        if rna[letter] == 'G':
            result += 'C'
    return 'template strand:' + ' ' + result

print('template_of() function with RNA string argument')

def coding_of(rna):
    result = ''
    for letter in range(len(rna)):
        if rna[letter] == 'U':
            result += 'T'
        else:
            result += rna[letter]
    return 'coding strand:' + ' ' + result

print('coding_of() function with RNA string argument')

def count_sequence(seq, dna):
    if len(dna) < len(seq):
        return 0
    else:
        if dna[:len(seq)] == seq:
            return count_sequence(seq, dna[len(seq):]) + 1
        else:
            return count_sequence(seq, dna[1:])

print('count_sequence() function with sequence and DNA string arguments')

SEQ = str(input('Insert DNA/RNA sequence: '))
if 'U' in SEQ:
    print(template_of(SEQ))
    print(coding_of(SEQ))
else:
    print(complementary(SEQ))
    print(mRNA_of(SEQ))
