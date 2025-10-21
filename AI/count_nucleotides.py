#!/usr/bin/env python3
# Take a multi-FASTA Python_08.fasta file from user input and calculate the nucleotide composition for each sequence. 
# Use a datastructure to keep count. Print out each sequence name and its composition in this format seqName\tA_count\tT_count\tG_count\tC_count

#!/usr/bin/env python3

import sys

def count_nts(seq):
    """Count A, T, G, C in the sequence (case‑insensitive). Returns dict with keys 'A','T','G','C'."""
    counts = {'A':0, 'T':0, 'G':0, 'C':0}
    for ch in seq.upper():
        if ch in counts:
            counts[ch] += 1
    return counts

def parse_fasta(fp):
    """Generator: yields (header_name, sequence_string) for each record in FASTA file."""
    name = None
    seq_lines = []
    for line in fp:
        line = line.rstrip('\n')
        if not line:
            continue
        if line.startswith('>'):
            if name is not None:
                yield name, ''.join(seq_lines)
            # new record
            # take name as the first token after '>'
            name = line[1:].split()[0]
            seq_lines = []
        else:
            seq_lines.append(line)
    # yield last
    if name is not None:
        yield name, ''.join(seq_lines)

def main(fasta_path):
    # open the file (or URL)  
    if fasta_path.startswith(('http://', 'https://')):
        import urllib.request
        with urllib.request.urlopen(fasta_path) as response:
            # decode to text lines
            for name, seq in parse_fasta((line.decode('utf‑8') for line in response)):
                counts = count_nts(seq)
                print(f"{name}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")
    else:
        with open(fasta_path, 'r') as fp:
            for name, seq in parse_fasta(fp):
                counts = count_nts(seq)
                print(f"{name}\t{counts['A']}\t{counts['T']}\t{counts['G']}\t{counts['C']}")

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} <fasta_file_or_url>", file=sys.stderr)
        sys.exit(1)
    fasta_path = sys.argv[1]
    main(fasta_path)
