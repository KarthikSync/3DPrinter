'''OpenGL extension SGIX.flush_raster

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_flush_raster'
_DEPRECATED = False

glFlushRasterSGIX = platform.createExtensionFunction( 
'glFlushRasterSGIX',dll=platform.GL,
extension=EXTENSION_NAME,
resultType=None, 
argTypes=(),
doc='glFlushRasterSGIX() -> None',
argNames=(),
deprecated=_DEPRECATED,
)


def glInitFlushRasterSGIX():
    '''Return boolean indicating whether this extension is available'''
    return extensions.hasGLExtension( EXTENSION_NAME )