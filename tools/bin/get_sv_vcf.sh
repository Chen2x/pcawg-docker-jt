local donor=$1

if [ ! -f $base_dir/data/$donor/brass.SV.vcf.gz ]; then
	$base_dir/bin/get_donor_SV.sh $donor
fi
