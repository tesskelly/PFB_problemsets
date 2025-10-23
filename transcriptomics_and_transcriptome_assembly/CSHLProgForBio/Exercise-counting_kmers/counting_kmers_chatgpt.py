#!/usr/bin/env python
import sys
import argparse
from collections import defaultdict, Counter
import math

def read_fastq(filename):
    with open(filename, 'r') as f:
        while True:
            header = f.readline().strip()
            if not header:
                break
            seq = f.readline().strip()
            f.readline()  # +
            f.readline()  # quality
            yield seq

def shannon_entropy(seq):
    counts = Counter(seq)
    total = len(seq)
    entropy = 0
    for base, count in counts.items():
        p = count / total
        entropy -= p * math.log2(p)
    return entropy

def count_kmers(fastq_file, k):
    kmer_counts = defaultdict(int)
    for seq in read_fastq(fastq_file):
        for i in range(len(seq) - k + 1):
            kmer = seq[i:i + k]
            kmer_counts[kmer] += 1
    return kmer_counts

def assemble_contigs(kmer_counts, k, min_entropy=1.0, max_contigs=0, min_contig_length=50):
    kmers = dict(kmer_counts)
    contigs = []
    used = set()

    while kmers:
        seed = max(kmers.items(), key=lambda x: x[1])[0]
        entropy = shannon_entropy(seed)
        if entropy < min_entropy:
            del kmers[seed]
            continue

        contig = seed
        used.add(seed)

        # Extend to the right
        extended = True
        while extended:
            extended = False
            suffix = contig[-(k - 1):]
            extensions = [mer for mer in kmers if mer.startswith(suffix) and mer not in used]
            if extensions:
                next_mer = max(extensions, key=lambda m: kmers[m])
                contig += next_mer[-1]
                used.add(next_mer)
                extended = True

        # Extend to the left
        extended = True
        while extended:
            extended = False
            prefix = contig[:k - 1]
            extensions = [mer for mer in kmers if mer.endswith(prefix) and mer not in used]
            if extensions:
                next_mer = max(extensions, key=lambda m: kmers[m])
                contig = next_mer[0] + contig
                used.add(next_mer)
                extended = True

        del kmers[seed]
        if len(contig) >= min_contig_length:
            contigs.append(contig)
        if max_contigs and len(contigs) >= max_contigs:
            break

    return contigs

def main():
    parser = argparse.ArgumentParser(description="Count kmers and assemble contigs from a FASTQ file")
    parser.add_argument("fastq_file", help="Input FASTQ file")
    parser.add_argument("k", type=int, help="kmer size")
    parser.add_argument("--top", type=int, default=0, help="Show only top N kmers by count")
    parser.add_argument("--min-entropy", type=float, default=0.0, help="Minimum entropy for kmer seeds")
    parser.add_argument("--min-contig-length", type=int, default=50, help="Minimum contig length to keep")
    parser.add_argument("--max-contigs", type=int, default=0, help="Stop after this many contigs (0 = no limit)")
    parser.add_argument("--min-count", type=int, default=1, help="Ignore kmers with counts below this threshold")
    args = parser.parse_args()

    print(f"Counting {args.k}-mers from {args.fastq_file}...")
    kmer_counts = count_kmers(args.fastq_file, args.k)

    # Filter by count threshold
    kmer_counts = {kmer: count for kmer, count in kmer_counts.items() if count >= args.min_count}

    # Sort by count and optionally show top N
    sorted_kmers = sorted(kmer_counts.items(), key=lambda x: x[1], reverse=True)
    if args.top > 0:
        print("kmer\tcount\tentropy")
        for kmer, count in sorted_kmers[:args.top]:
            print(f"{kmer}\t{count}\t{shannon_entropy(kmer):.3f}")

    print("\nAssembling contigs...")
    contigs = assemble_contigs(kmer_counts, args.k, min_entropy=args.min_entropy,
                               max_contigs=args.max_contigs, min_contig_length=args.min_contig_length)

    print("\n### Assembled Contigs ###")
    for i, contig in enumerate(contigs, 1):
        print(f">contig_{i}\n{contig}\n")

if __name__ == "__main__":
    main()

#gives weird answer, I think his is wrong. Need to work on it more. 



