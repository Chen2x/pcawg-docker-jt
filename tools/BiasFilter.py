import subprocess


print (subprocess.checkoutput(["run_workflow.sh", "BiasFilter", donor, gnos_or_igcg]))
