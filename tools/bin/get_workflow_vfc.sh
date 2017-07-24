local donor=$1

if [ ! -f $base_dir/data/$donor/broad.oxoG.vcf.gz ]; then
	local donor_id_dir="$icgc_dir/$donor/ID"
         	$base_dir/bin/get_gnos_workflow_results.sh $donor
fi
