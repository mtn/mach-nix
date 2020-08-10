import subprocess
import os

with open("package_list.txt") as f:
    packages = f.read().strip().split("\n")

with open("shell_template.nix") as f:
    shell_template = f.read()

    if os.path.isfile("shell.nix"):
        os.remove("shell.nix")

    for package in packages:
        shell = shell_template % package


        with open("shell.nix", "w") as sf:
            sf.write(shell)

        subprocess.Popen(["nix-build", "shell.nix"], shell=True)

    if os.path.isfile("shell.nix"):
        os.remove("shell.nix")
