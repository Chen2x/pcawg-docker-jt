local donor=$1
echo "Downloading un-aligned BAM files for $donor"

if [ ! -f $base_dir/data/$donor/normal_unaligned_bams ]; then 
         	$base_dir/bin/get_unaligned_bams.sh $donor
fi

if [ $? == 0 ]; then
	echo "DONE Downloading un-aligned BAM files for $donor"
else
	echo "ERROR Downloading un-aligned BAM files for $donor"
	exit -1
fi
