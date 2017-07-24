import subprocess

try:
    print (subprocess.checkoutput(["run_workflow.sh", task, donor, gnos_or_igcg]))
except Exception, e:
    with open('jt.log', 'w') as f: f.write(str(e))
        sys.exit(1)
