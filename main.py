import ctypes
so = ctypes.cdll.LoadLibrary('./_golib.so')

hello = so.hello
hello.argtypes = [ctypes.c_char_p]
hello.restype = ctypes.c_void_p

free = so.free
free.argtypes = [ctypes.c_void_p]

ptr = hello('World'.encode('utf-8'))
out = ctypes.string_at(ptr)
free(ptr)

print(out.decode('utf-8'))