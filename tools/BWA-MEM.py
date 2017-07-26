import subprocess
import os
import json
import sys

donor = "DO46792"
source = "ICGC"

function get_aligned_bams {
	local donor=$1
	local download_type=$2
	[[ "x$download_type" == "x" ]] && download_type='gnos'

	echo "Downloading aligned BAM files for $donor [$download_type]"
	if [ ! -f  $base_dir/data/$donor/normal.bam ]; then
		local donor_id_dir="$icgc_dir/$donor/ID"

		tumor_bam_file=$(ls $donor_id_dir/Aligned*tumour* | grep -v TopHat | grep -v STAR | head -n 1)
		normal_bam_file=$(ls $donor_id_dir/Aligned*Normal* | grep -v TopHat | grep -v STAR | head -n 1)
		if [ "$download_type" == 'gnos' ]; then
			tumor_sub=$(cut -f 2 "$tumor_bam_file")
			normal_sub=$(cut -f 2 "$normal_bam_file")
			$base_dir/bin/get_gnos_donor.sh $donor $tumor_sub $normal_sub
		else
			tumor_obj=$(cut -f 1 "$tumor_bam_file")
			normal_obj=$(cut -f 1 "$normal_bam_file")
			$base_dir/bin/get_icgc_donor.sh $donor $tumor_obj $normal_obj
		fi
	fi

	if [ $? == 0 ]; then
		echo "DONE Downloading aligned BAM files for $donor [$download_type]"
	else
		echo "ERROR Downloading aligned BAM files for $donor [$download_type]"
		exit -1
	fi
}

if source != "icgc" or source !="gnos":
    source = "icgc"




try:
    #get

    #dockstore tool launch --entry quay.io/pancancer/pcawg-bwa-mem-workflow:2.6.8_1.2 --json Dockstore.json
except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
        sys.exit(1)
