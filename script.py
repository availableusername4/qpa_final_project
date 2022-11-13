from data.project_data import DNA_TO_RNA_DICT, RNA_TO_AA_DICT


def dna_to_rna(seq):
    new_seq = ''
    for base in seq:
        new_seq += DNA_TO_RNA_DICT[base]
    return new_seq


def rna_to_aa(seq):
    new_seq = ''
    number_of_codons = len(seq) // 3
    for codon_index in range(0, number_of_codons):
        codon = seq[codon_index * 3] + seq[codon_index*3 + 1] + seq[codon_index*3 + 2]
        new_seq += RNA_TO_AA_DICT[codon]
    return new_seq


print(rna_to_aa('AUUUGGCUACUAACAAUCUA'))
