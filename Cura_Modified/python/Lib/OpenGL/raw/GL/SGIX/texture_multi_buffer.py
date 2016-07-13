'''OpenGL extension SGIX.texture_multi_buffer

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_texture_multi_buffer'
_DEPRECATED = False
GL_TEXTURE_MULTI_BUFFER_HINT_SGIX = constant.Constant( 'GL_TEXTURE_MULTI_BUFFER_HINT_SGIX', 0x812E )


def glInitTextureMultiBufferSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )