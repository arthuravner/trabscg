from OpenGL.GLUT import *
from OpenGL.GLU import * 
from OpenGL.GL import *
import math

def desenha():
    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glRotatef(2,1,3,0)
    desenhaEsfera()
    glutSwapBuffers()
 
def timer(i):
    glutPostRedisplay()
    glutTimerFunc(50,timer,1)

def getPonto(i, j):
    teta = ((i*math.pi)/nEsfera) - (math.pi/2)
    phi = j*2*math.pi/nRotacao

    x = r*math.cos(teta)*math.cos(phi)
    y = r*math.sin(teta)
    z = r*math.cos(teta)*math.sin(phi)
    return [x,y,z]

def desenhaEsfera():
    glBegin(GL_QUAD_STRIP)
    for i in range(0,nEsfera):
        glColor3fv(cores[i])
        for j in range(0, nRotacao):  
            glVertex3fv(getPonto(i,j))
            #glTexture2fv(g(i,j))
            glVertex3fv(getPonto(i+1,j))
            #glTexture2fv(g(i+1,j))
            glVertex3fv(getPonto(i,j+1))
            #glTexture2fv(g(i,0))
            glVertex3fv(getPonto(i+1,j+1))
            #glTexture2fv(g(i+1,0))            
    glEnd()

# PROGRAMA PRINCIPAL
cores = ( (1,0,0),(1,1,0),(0,1,0),(0,1,1),(0,0,1),(1,0,1),(0.5,1,1),(1,0,0.5) )

nEsfera = 8
nRotacao = 25
r = 2

glutInit(sys.argv)
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA | GLUT_DEPTH | GLUT_MULTISAMPLE)
glutInitWindowSize(800,600)
glutCreateWindow("ESFERA")
glutDisplayFunc(desenha)
glEnable(GL_MULTISAMPLE)
glEnable(GL_DEPTH_TEST)
glClearColor(0.,0.,0.,1.)
gluPerspective(45,800.0/600.0,0.1,50.0)
glTranslatef(0.0,0.0,-8)
glRotatef(45,1,1,1)
glutTimerFunc(50,timer,1)
glutMainLoop()