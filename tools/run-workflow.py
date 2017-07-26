import subprocess

task = 'BWA-Mem'
donor = "DO46792"
source = "ICGC"

try:
    print (subprocess.checkoutput(["run_workflow.sh", task, donor, source]))
except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
        sys.exit(1)
