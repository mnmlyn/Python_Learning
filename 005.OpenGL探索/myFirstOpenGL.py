# coding=gb2312
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def Draw():
    glClear(GL_COLOR_BUFFER_BIT)
    glRotatef(0.1, 1, 0, 1) #angle,x,y,z�����У�angle����Ƕȣ�����ת�٣�x,y,z������ת����
    glutWireTeapot(0.5)
    glFlush()

glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGBA)
glutInitWindowSize(400, 400)
glutCreateWindow("��ת�ɲ��")
glutDisplayFunc(Draw)
glutIdleFunc(Draw)
glutMainLoop()