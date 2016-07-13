'''OpenGL extension ARB.texture_mirrored_repeat

This module customises the behaviour of the 
OpenGL.raw.GL.ARB.texture_mirrored_repeat to provide a more 
Python-friendly API

Overview (from the spec)
	
	ARB_texture_mirrored_repeat extends the set of texture wrap modes to
	include a mode (GL_MIRRORED_REPEAT_ARB) that effectively uses a texture
	map twice as large at the original image in which the additional half,
	for each coordinate, of the new image is a mirror image of the original
	image.
	
	This new mode relaxes the need to generate images whose opposite edges
	match by using the original image to generate a matching "mirror image".

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/ARB/texture_mirrored_repeat.txt
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ARB.texture_mirrored_repeat import *
### END AUTOGENERATED SECTION