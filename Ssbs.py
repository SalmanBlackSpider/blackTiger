
import platform
b = platform.architecture()[0]
if b == '32bit':
    import SSB
elif b == '64bit':
    print("64bit Not Supported! Sorry")
