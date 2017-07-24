local donor=$1

if [ ! -f $base_dir/data/$donor/consensus.vcf ]; then
	local donor_id_dir="$icgc_dir/$donor/ID"
  
	consensus_vcf_sub=$(cut -f 2 $donor_id_dir/SSM*consensus*snv_mnv*)
	$base_dir/bin/get_gnos_vcf.sh $consensus_vcf_sub $base_dir/data/$donor/consensus.vcf.gz
              cp  $base_dir/data/$donor/consensus.vcf.gz $base_dir/data/$donor/consensus.vcf.gz.tmp
              gunzip  $base_dir/data/$donor/consensus.vcf.gz
              mv  $base_dir/data/$donor/consensus.vcf.gz.tmp  $base_dir/data/$donor/consensus.vcf.gz
	grep -v "LOWSUPPORT\|OXOG" $base_dir/data/$donor/consensus.vcf | sed 's/bPcr\|bSeq//g' > $base_dir/data/$donor/consensus.filter.vcf
fi
