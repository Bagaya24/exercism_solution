"""
The module of tranlating RNA sequences into protiens
"""
def proteins(strand:str) -> list:
    """
    The translater of RNA sequences into proteins
    param: strand(str)
    return: rna_list(list)
    """
    codons = ""
    rna_list = []
    for index, codon in enumerate(strand):
        if index % 3 == 0:
            codons += " "
        codons += codon
    codons = codons.split()

    for codon in codons:
        if codon == "AUG":
            rna_list.append("Methionine")
        elif codon in "UUU UUC":
            rna_list.append("Phenylalanine")
        elif codon in "UUA UUG":
            rna_list.append("Leucine")
        elif codon in "UCU UCC UCA UCG":
            rna_list.append("Serine")
        elif codon in "UAU UAC":
            rna_list.append("Tyrosine")
        elif codon in "UGU UGC":
            rna_list.append("Cysteine")
        elif codon == "UGG":
            rna_list.append("Tryptophan")
        elif codon in "UAA UAG UGA":
            break
        
    return rna_list
