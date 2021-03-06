# Nombre Creador: Ivan Alejandro Fernandez Gracia
# Universidad: Universidad de Santiago de Chile
# Mail: ivan.fernandez.g@usach.cl
# Objetivo: Ingresar parametros para calcular el
# torque de los actuadores de un robot delta

# Importar Librerias
import math


######################################################
##########  Cambio Unidades ##########################
######################################################
def dtr():
 valor = math.pi / 180.0  # Grados a Radianes
 return valor


def rtd():
 valor = 180.0 / math.pi  # Radianes a Grados
 return valor


def mmtm():
 valor = ((10.0) ** (-3))  # Milimetros a Metros
 return valor


def mtmm():
 valor = ((10.0) ** (3))  # Metros a Milimetros
 return valor


def kgm2tgrmm2():
 valor = ((10.0) ** (3 + 6))  # Kilogramo metro^2 a gramo mm^2
 return valor


######################################################
##########  Trigonometria ############################
######################################################
def sqrt3():
 valor = math.sqrt(3.0)
 return valor


def pi():
 valor = math.pi  # [rad]
 return valor


def sin120():
 valor = sqrt3() / 2.0
 return valor


def cos120():
 valor = -0.5
 return valor


def tan60():
 valor = sqrt3()
 return valor


def sin30():
 valor = 0.5
 return valor


def tan30():
 valor = 1.0 / sqrt3()
 return valor


def cos30():
 valor = (sqrt3()) / 2.0
 return valor


######################################################
##########  Dimensionamiento Geometrico Robot Delta ##
######################################################
def l2():
 valor = (880.0) * ((10.0) ** (-3))  # Longitud Antebrazo [m]
 return valor


def l1():
 valor = (620.0) * ((10.0) ** (-3))  # Longitud Brazo [m]
 return valor


def rb():
 valor = (50.0) * ((10.0) ** (-3))  # Radio plataforma movil[m]
 return valor


def ra():
 valor = (210.0) * ((10.0) ** (-3))  # Radio base fija [m]
 return valor


def e():
 valor = (2.0 * rb()) / (tan30())  # [m]
 return valor


def f():
 valor = (2.0 * ra()) / (tan30())  # [m]
 return valor


def hf():
 valor = math.sqrt(0.75 * (f() ** 2))  # [m]
 return valor


def he():
 valor = math.sqrt(0.75 * (e() ** 2))  # [m]
 return valor


######################################################
##########  Masas e Inercias #########################
######################################################
def m1():
 valor = (2213.0) * ((10.0) ** (-3))  # Masa Brazo [kg]
 return valor


def m_elbow():
 valor = (0.0) * ((10.0) ** (-3))  # Masa juntas [kg]
 return valor


def m2():
 valor = (1315.0 / 2.0) * ((10.0) ** (-3))  # Masa de una varilla del antebrazo [kg]
 return valor


def mp():
 valor = (510.0) * ((10.0) ** (-3))  # Masa plataforma movil [kg]
 return valor


def inercia_m():
 valor = (0.0) * ((10.0) ** (-3))  # Inercia actuadores [kg * m2]
 return valor


def gg():
 valor = (9.81)  # Gravedad [m/s2]
 return valor


def r_mass():
 valor = (0.5)  # Relacion de masas del antebrazo
 return valor


def com():
 valor = (l1()) * (((0.5 * (m1())) + (m_elbow()) + ((2) * (r_mass()) * (m2()))) /
				   ((1.0 * (m1())) + (m_elbow()) + ((2) * (r_mass()) * (m2()))))
 # Centro de masas brazo
 return valor


######################################################
##########  Restricciones Espacio de Trabajo #########
######################################################
# Restricciones limines de angulos de motores [grados]
def res_ang_min():
 valor = int(-90)
 # valor=int(-30)
 return valor


def res_ang_max():
 valor = ((res_ang_min()) * -1) + 1
 # valor=90
 return valor


# Restriccion angulos 2 y 3 de cada brazo [grados]
def theta2i_min():
 valor = 5
 return valor


def theta2i_max():
 valor = 180 - theta2i_min()
 return valor


def theta3i_min():
 valor = 45
 return valor


def theta3i_max():
 valor = 180 - theta3i_min()
 return valor


# Restricciones Singularidad Jacobiano
def err_jxx():
 valor = (6) * (10 ** (-1))
 return valor


def err_jinv():
 valor = (4) * (10 ** (-3))
 return valor


# Restriccion del fabricante (caja) [mm]
def px_max_ws():
 valor = 400
 return valor


def px_min_ws():
 valor = (-1) * px_max_ws()
 return valor


def py_max_ws():
 valor = 400
 return valor


def py_min_ws():
 valor = (-1) * py_max_ws()
 return valor


def pz_max_ws():
 valor = -300
 return valor


def pz_min_ws():
 valor = -750
 return valor
