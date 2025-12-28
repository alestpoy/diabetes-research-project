#!/usr/bin/env python3
"""
Script to analyze association between GeneX variant and Metformin response.
Reads data/patient_data.csv and calculates response rates for each subgroup.
"""

import csv
import os

def main():
    # Path to data file (relative to repository root)
    data_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'patient_data.csv')
    
    # Counters
    variant_true_total = 0
    variant_true_positive = 0
    variant_false_total = 0
    variant_false_positive = 0
    
    with open(data_path, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            geneX_variant = row['geneX_variant'].strip().upper()
            metformin_response = row['metformin_response'].strip().lower()
            
            if geneX_variant == 'TRUE':
                variant_true_total += 1
                if metformin_response == 'positive':
                    variant_true_positive += 1
            elif geneX_variant == 'FALSE':
                variant_false_total += 1
                if metformin_response == 'positive':
                    variant_false_positive += 1
            else:
                print(f"Warning: unknown geneX_variant value: {geneX_variant}")
    
    # Calculate proportions
    if variant_true_total > 0:
        prop_true = variant_true_positive / variant_true_total * 100.0
    else:
        prop_true = 0.0
    
    if variant_false_total > 0:
        prop_false = variant_false_positive / variant_false_total * 100.0
    else:
        prop_false = 0.0
    
    # Print results
    print(f"Response rate with GeneX variant: {prop_true:.1f}% ({variant_true_positive}/{variant_true_total})")
    print(f"Response rate without GeneX variant: {prop_false:.1f}% ({variant_false_positive}/{variant_false_total})")

if __name__ == '__main__':
    main()