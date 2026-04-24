"""
The RNA complement module
"""
def to_rna(dna_strand:str) -> str:
    """
    This function determines the RNA complement of a given DNA sequence
    :param dna_strand(str)
    :return result(str)
    """
    rna_strang = {"G":"C", "C":"G", "T":"A", "A":"U"} 
    result = ""
    for nucleotide in dna_strand:
        if nucleotide in rna_strang:
            result += rna_strang.get(nucleotide)
    return result
