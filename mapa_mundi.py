from OpenGL.GLUT import *
from OpenGL.GLU import * 
from OpenGL.GL import *
import math
import png

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    desenhaEsfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def getPonto(i, j):
    teta = ((i*math.pi)/nEsfera) - (math.pi/r)
    phi = j*r*math.pi/nRotacao

    x = r*math.cos(teta)*math.cos(phi)
    y = r*math.sin(teta)
    z = r*math.cos(teta)*math.sin(phi)
    return [x,y,z]

def desenhaEsfera():
    glBegin(GL_QUAD_STRIP)
    for i in range(0,nEsfera):
        #glColor3fv(cores[i])
        for j in range(0, nRotacao):              
            glTexCoord2f(i/nEsfera, j/nRotacao)
            glVertex3fv(getPonto(i,j))
            glTexCoord2f((i+1)/nEsfera, j/nRotacao)
            glVertex3fv(getPonto(i+1,j))
            glTexCoord2f(i/nEsfera, (j+1)/nRotacao)
            glVertex3fv(getPonto(i,j+1))
            glTexCoord2f((i+1)/nEsfera, (j+1)/nRotacao)
            glVertex3fv(getPonto(i+1,j+1))
                   
    glEnd()

def LoadTextures():
    global texture
    texture = glGenTextures(1)

    glBindTexture(GL_TEXTURE_2D, texture)
    reader = png.Reader(filename='mapa.png')
    w, h, pixels, metadata = reader.read_flat()
    if(metadata['alpha']):
        modo = GL_RGBA
    else:
        modo = GL_RGB
    glPixelStorei(GL_UNPACK_ALIGNMENT,1)
    glTexImage2D(GL_TEXTURE_2D, 0, modo, w, h, 0, modo, GL_UNSIGNED_BYTE, pixels.tolist())
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_CLAMP)
#    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_CLAMP)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexEnvf(GL_TEXTURE_ENV, GL_TEXTURE_ENV_MODE, GL_DECAL)




# PROGRAMA PRINCIPAL
#cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

nEsfera = 25 #i
nRotacao = 25 #j
r = 2

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("Mapa Mundi")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)

glClearDepth(1.0)
glDepthFunc(GL_LESS)   
glEnable(GL_DEPTH_TEST)     
glShadeModel(GL_SMOOTH)   
glMatrixMode(GL_PROJECTION)

gluPerspective(45,800.0/600.0,0.1,50.0)

glMatrixMode(GL_MODELVIEW)

glTranslatef(0.0,0.0,-8)
glRotatef(1,1,1,1)
glutTimerFunc(50,timer,1)
LoadTextures()
glEnable(GL_TEXTURE_2D)
glutMainLoop()