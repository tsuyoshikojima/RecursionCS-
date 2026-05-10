import os

pid = os.fork()

if pid > 0:
    print("This is the parent process.")
    print("Parent PID : ", os.getpid())
    print("Child PID : ", pid)

elif pid == 0:
    print("This is the child  process.")
    print("Child PID : ", os.getpid())
    print("Parent PID : ", os.getppid())