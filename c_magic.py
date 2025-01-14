
from IPython.core.magic import Magics, magics_class, cell_magic
from IPython import get_ipython
import subprocess

@magics_class
class CMagic(Magics):
    @cell_magic
    def c(self, line, cell):
        # Save the C code to a temporary file
        with open('temp.c', 'w') as f:
            f.write(cell)

        # Compile the C code
        compile_command = f'gcc -o temp_executable temp.c'
        compile_result = subprocess.run(compile_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        if compile_result.returncode == 0:
            # If compilation is successful, execute the compiled code
            execute_command = './temp_executable'
            execute_result = subprocess.run(execute_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            print(execute_result.stdout)
            print(execute_result.stderr)
        else:
            # If compilation fails, print the error message
            print(compile_result.stderr)

# Register the magic command
ip = get_ipython()
ip.register_magics(CMagic)
