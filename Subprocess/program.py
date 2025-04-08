import subprocess

p = subprocess.run(["python", "test.py"],
                   capture_output=True,
                   text=True,
                   input = "john",
                   check=True)
print("Program subprocess done.")
if p.returncode != 0:
  print("stdout: ", p.stdout)
  print("stderr: ", p.stderr)
