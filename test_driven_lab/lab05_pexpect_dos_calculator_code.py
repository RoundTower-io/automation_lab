#
# A PExpect example that uses DOS to multiply 2 numbers.
#   1 - Pexpect spawns a DOS shell
#   2 - It waits for the DOS prompt ending in '>'
#   3 - It then sends 'set /a <number1>*<number2>' to DOS
#   4 - It looks for a response that is a single number
#   5 - We read the output line, strip off whitespace, and convert to int
#   6 - Finally, we return the integer
#
# Instructions: Write a new function that *adds* 2 numbers
#
import pexpect
from pexpect import popen_spawn

def dos_multiply(a, b):
    child = pexpect.popen_spawn.PopenSpawn('cmd', timeout=1)
    child.expect('D:.*>')
    child.sendline('set /a ' + str(a) + '*' + str(b))
    child.expect('\d+\r\n')
    return int(child.readline().strip())
