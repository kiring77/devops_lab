import sys
import os
import subprocess
import json
import yaml

v = os.environ['VIRTUAL_ENV'].split('/')
site_packages = next(s for s in sys.path if 'site-packages' in s)
packages = subprocess.run(['pip', 'freeze'], stdout=subprocess.PIPE).stdout.decode('utf-8').split()
o = []
for i in packages:
    o += i.split('==')
n = {x: o[o.index(x) + 1] for x in o if o.index(x) % 2 == 0}

output = {
    'version': sys.version.split('\n')[0],
    'Virtual environment': v[-1],
    'Executable is located in': sys.executable,
    'PIP is located in': subprocess.check_output(['which', 'pip'],
                                                 universal_newlines=True).split('\n')[0],
    'PYTHONPATH contains': sys.path,
    'Installed packages': n,
    'Location of site-packages is': site_packages}

with open('output.json', 'w') as f:
    json.dump(output, f, indent=4)

with open('output.yaml', 'w') as f:
    yaml.dump(output, f, default_flow_style=False, indent=4)
