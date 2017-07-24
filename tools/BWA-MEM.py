import subprocess


print (subprocess.checkoutput(["run_workflow.sh", "BWA-MEM", donor, gnos_or_igcg]))
