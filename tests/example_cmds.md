qmplot -I data/gwas_plink_result.tsv -T Test --dpi 72 -O test
qmplot -I data/gwas_plink_result.tsv -T Test --dpi 72 -O test --display

qmplot -I data/gwas_plink_result.tsv -T Test --dpi 72 -O test --outfiletype pdf
qmplot -I data/gwas_plink_result.tsv -T Test --dpi 72 -O test -M ID
qmplot -I data/gwas_plink_result.tsv -T Test --dpi 72 -O test -M ID --ld-block-size 500000
