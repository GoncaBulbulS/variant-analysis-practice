# variant-analysis-practice
Practice workflow for variant filtering, annotation, and interpretation using VCF-style data.

## Goal
To demonstrate basic steps used in variant analysis, including quality filtering, population frequency filtering, and clinical database review.

## Planned Workflow
1. Start with VCF-style variant data
2. Filter low-quality variants
3. Prioritize rare variants
4. Review known clinical significance using resources such as ClinVar
5. Summarize candidate variants for interpretation

## Skills Demonstrated
- Variant filtering logic
- VCF interpretation
- Population frequency reasoning
- Clinical genomics terminology
- Reproducible analysis with Python

## Example Variant Filtering

From the sample dataset:

- Removed low-quality variants (quality < 30)
- Removed common variants (frequency > 0.01)
- Prioritized rare, high-quality variants

### Resulting Candidates
- BRCA1 variant (rare, high quality)
- CFTR variant (very rare, high quality)

These would be further evaluated using databases such as ClinVar and population resources.
