import os
from subprocess import PIPE, run
print('installing')
command = "chmod -R u+w ./deps"
run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)


def download_model():
    path = './deps/Rerender_A_Video/models'
    if not os.path.exists(path):
        os.makedirs(path, exist_ok=True)
        command = f"wget -P {path} 'https://huggingface.co/PKUWilliamYang/Rerender/resolve/main/models/gmflow_sintel-0c07dcb3.pth'"
        run(command, stdout=PIPE, stderr=PIPE, universal_newlines=True, shell=True)


download_model()
