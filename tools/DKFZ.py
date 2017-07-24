import subprocess


print (subprocess.checkoutput(["run_workflow.sh", "DKFZ", donor, gnos_or_igcg]))
