# coding=gb2312
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def Draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 1, 0, 1) #angle,x,y,z。其中，angle代表角度，控制转速；x,y,z代表旋转的轴
    glutWireTeapot(0.5)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("旋转吧茶壶")
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
glutMainLoop()