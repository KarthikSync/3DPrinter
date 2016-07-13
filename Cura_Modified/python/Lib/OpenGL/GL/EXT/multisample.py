'''OpenGL extension EXT.multisample

This module customises the behaviour of the 
OpenGL.raw.GL.EXT.multisample to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/EXT/multisample.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.EXT.multisample import *
### END AUTOGENERATED SECTION