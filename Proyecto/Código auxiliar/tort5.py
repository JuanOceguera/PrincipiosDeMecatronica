#!/usr/bin/env python
#!/usr/bin/env python

import rospy
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
from math import pow, atan2, sqrt
import numpy as np
import time

x1 = 0;
y1 = 0;
theta1 = 0;
x2 = 0;
y2 = 0;
theta2 = 0;
x3 = 0;
y3 = 0;
theta3 = 0;
x4 = 0;
y4 = 0;
theta4 = 0;
x6 = 0;
y6 = 0;
theta6 = 0;

def poseCallback1(pose_message):
    global x1
    global y1
    global theta1
    
    x1 = pose_message.x
    y1 = pose_message.y
    theta1 = pose_message.theta

def poseCallback2(pose_message):
    global x2
    global y2
    global theta2
    
    x2 = pose_message.x
    y2 = pose_message.y
    theta2 = pose_message.theta

def poseCallback3(pose_message):
    global x3
    global y3
    global theta3
    
    x3 = pose_message.x
    y3 = pose_message.y
    theta3 = pose_message.theta

def poseCallback4(pose_message):
    global x4
    global y4
    global theta4
    
    x4 = pose_message.x
    y4 = pose_message.y
    theta4 = pose_message.theta

def poseCallback6(pose_message):
    global x6
    global y6
    global theta6
    
    x6 = pose_message.x
    y6 = pose_message.y
    theta6 = pose_message.theta


class TurtleBot:

    def __init__(self):
        # Creates a node with name 'turtlebot_controller' and make sure it is a
        # unique node (using anonymous=True).
        rospy.init_node('turtlebot_controller', anonymous=True)

        # Publisher which will publish to the topic '/turtle5/cmd_vel'.
        self.velocity_publisher = rospy.Publisher('/turtle5/cmd_vel',
                                                  Twist, queue_size=10)

        # A subscriber to the topic '/turtle5/pose'. self.update_pose is called
        # when a message of type Pose is received.
        self.pose_subscriber = rospy.Subscriber('/turtle5/pose',
                                                Pose, self.update_pose)

        self.pose = Pose()
        self.rate = rospy.Rate(10)

    def update_pose(self, data):
        """Callback function which is called when a new message of type Pose is
        received by the subscriber."""
        self.pose = data
        self.pose.x = round(self.pose.x, 4)
        self.pose.y = round(self.pose.y, 4)

    def euclidean_distance(self, goal_pose):
        """Euclidean distance between current pose and the goal."""
        return sqrt(pow((goal_pose.x - self.pose.x), 2) +
                    pow((goal_pose.y - self.pose.y), 2))

    def linear_vel(self, goal_pose, constant=1.5):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * self.euclidean_distance(goal_pose)

    def steering_angle(self, goal_pose):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return atan2(goal_pose.y - self.pose.y, goal_pose.x - self.pose.x)

    def angular_vel(self, goal_pose, constant=6):
        """See video: https://www.youtube.com/watch?v=Qh15Nol5htM."""
        return constant * (self.steering_angle(goal_pose) - self.pose.theta)

    def calculaDistancia(self,x_1,y_1,x_2,y_2):
        return sqrt((x_2 - x_1)**2 + (y_2 - y_1)**2)
    
    def distanciaMinima(self,x,y): #Esta función no sirve para detectar tortugas en el semicirculo superior; sirve para hacer el test de la distancia mínima al final de cada trayectoria
        return min([self.calculaDistancia(x,y,x1,y1), self.calculaDistancia(x,y,x2,y2), self.calculaDistancia(x,y,x3,y3), self.calculaDistancia(x,y,x4,y4), self.calculaDistancia(x,y,x6,y6)])
    
    def proyeccion(self,x,y):
        return np.dot([x-self.pose.x,y-self.pose.y],[np.cos(self.pose.theta),np.sin(self.pose.theta)])
        
    def peligro(self,r1, r2): #El radio 1 es el radio de emergencia (regresa 1 si hay tortuga dentro del radio), el radio 2 es el radio para disminuir velocidad (regresa 2). En otro caso regresa 0.
        distancia = [];
        if self.proyeccion(x1,y1) > 0:
            distancia.append(self.calculaDistancia(self.pose.x,self.pose.y,x1,y1));
        if self.proyeccion(x2,y2) > 0:
            distancia.append(self.calculaDistancia(self.pose.x,self.pose.y,x2,y2));
        if self.proyeccion(x3,y3) > 0:
            distancia.append(self.calculaDistancia(self.pose.x,self.pose.y,x3,y3));
        if self.proyeccion(x4,y4) > 0:
            distancia.append(self.calculaDistancia(self.pose.x,self.pose.y,x4,y4));
        if self.proyeccion(x6,y6) > 0:
            distancia.append(self.calculaDistancia(self.pose.x,self.pose.y,x6,y6));
        if len(distancia) == 0:
            minD = r2+1;
        else:
            minD = min(distancia);
        if minD < r1:
            return 1;
        else:
            if minD < r2:
                return 2;
            else:
                return 0;

    def calculaTrayectoria(self,r): #ya si estamos en el peor escenario, qué trayectoria son posibles
        base = self.pose.theta;
        x = self.pose.x;
        y = self.pose.y;
        #Primer cuadrante
        tray1 = [];
        for i in range(7):
            tray1.append([x+r*np.cos(base+(i+1)*3.1416/16), y+r*np.cos(base+(i+1)*3.1416/16)]);
        #Segundo cuadrante
        tray2 = [];
        for i in range(7):
            tray2.append([x-r*np.cos(base+(i+1)*3.1416/16), y+r*np.cos(base+(i+1)*3.1416/16)]);
        #Tercer cuadrante
        tray3 = [];
        for i in range(7):
            tray3.append([x-r*np.cos(base+(i+1)*3.1416/16), y-r*np.cos(base+(i+1)*3.1416/16)]);
        #Cuarto cuadrante
        tray4 = [];
        for i in range(7):
            tray4.append([x+r*np.cos(base+(i+1)*3.1416/16), y-r*np.cos(base+(i+1)*3.1416/16)]);
        #Nos quedamos con los dos cuadrantes cuyas trayectorias tienen una proyección positiva con el ángulo al que nos dirijimos
        #trayF = [[-1,-1]];
        #if self.proyeccion(tray1[3][0],tray1[3][1]) >= -1000:
        #    trayF = np.concatenate((trayF, tray1));
        #if self.proyeccion(tray2[3][0],tray2[3][1]) >= -1000:
        #    trayF = np.concatenate((trayF, tray2));
        #if self.proyeccion(tray3[3][0],tray3[3][1]) >= -1000:
        #    trayF = np.concatenate((trayF, tray3));
        #if self.proyeccion(tray4[3][0],tray4[3][1]) >= -1000:
        #    trayF = np.concatenate((trayF, tray4));
        #if len(trayF) > 1:
        #    trayF = trayF.tolist()
        #trayF.pop(0)
        trayF = np.concatenate((tray1,tray2,tray3,tray4));
        return trayF
        
    def seleccionaTrayectoria(self,trayectorias): #De la lista de trayectorias generadas anteriormente, ¿cuál es la mejor? Si regresa un -1 lo mejor es esperar y recalcular
        res = [];
        mini = 1
        for i in trayectorias:
            aux = min([self.calculaDistancia(i[0],i[1],x1,y1),self.calculaDistancia(i[0],i[1],x2,y2),self.calculaDistancia(i[0],i[1],x3,y3),self.calculaDistancia(i[0],i[1],x4,y4),self.calculaDistancia(i[0],i[1],x6,y6)]);
            if aux > mini and i[0] > 1.5 and i[0] < 9.5 and i[1] > 1.5 and i[1] < 9.5 and abs(i[0]-self.pose.x)>0.5 and abs(i[1]-self.pose.y)>0.5:
                xmid = (i[0]+self.pose.x)/2;
                ymid = (i[1]+self.pose.y)/2;
                aux2 = min([self.calculaDistancia(xmid,ymid,x1,y1),self.calculaDistancia(xmid,ymid,x2,y2),self.calculaDistancia(xmid,ymid,x3,y3),self.calculaDistancia(xmid,ymid,x4,y4),self.calculaDistancia(xmid,ymid,x6,y6)]);
                if aux2 > 1:
                    mini = aux;
                    res = i;
        return res

    def move2goal(self, x, y, tol, pel): #Pel habilita/deshabilita la verificación de peligro
        """Moves the turtle to the goal."""
        goal_pose = Pose()

        # Get the input from the user.
        #goal_pose.x = float(input("Set your x goal: "))
        #goal_pose.y = float(input("Set your y goal: "))
        goal_pose.x = x;
        goal_pose.y = y;

        # Please, insert a number slightly greater than 0 (e.g. 0.01).
        #distance_tolerance = input("Set your tolerance: ")
        distance_tolerance = tol;

        vel_msg = Twist()

        while self.euclidean_distance(goal_pose) >= distance_tolerance:
            #Constante de velocidad linear
            K = 0.5;
            #Revisamos condiciones con respecto al resto de tortugas
            p = self.peligro(1, 2)
            if p == 2:
                K = K/2;
            else:
                if p == 1 and pel == 1:
                    vel_msg.linear.x = 0
                    vel_msg.angular.z = 0
                    self.velocity_publisher.publish(vel_msg)
                    return 0; #Si hay una tortuga en el círculo de emergencia, para la tortuga y rompe el ciclo para definir un nuevo rumbo
                    
            # Porportional controller.
            # https://en.wikipedia.org/wiki/Proportional_control

            # Linear velocity in the x-axis.
            aux = (self.pose.x < 1.5 or self.pose.y < 1.5 or self.pose.x > 9.5 or self.pose.y > 9.5);
            if aux and abs(self.steering_angle(goal_pose) - self.pose.theta) > 0.2:
                vel_msg.linear.x = self.linear_vel(goal_pose, 0.1)
            else:
                vel_msg.linear.x = self.linear_vel(goal_pose, K)
            vel_msg.linear.y = 0
            vel_msg.linear.z = 0

            # Angular velocity in the z-axis.
            vel_msg.angular.x = 0
            vel_msg.angular.y = 0
            vel_msg.angular.z = self.angular_vel(goal_pose)

            # Publishing our vel_msg
            self.velocity_publisher.publish(vel_msg)

            # Publish at the desired rate.
            self.rate.sleep()

        # Stopping our robot after the movement is over.
        vel_msg.linear.x = 0
        vel_msg.angular.z = 0
        self.velocity_publisher.publish(vel_msg)
        return 1

#Verifica que no haya puntos consecutivos con la misma coordenada en x o y (en ciertos casos provocan que giren y se salgan de control)
def arreglaPuntos(puntos):
    i = 0;
    a = len(puntos)-1;
    while i < a:
        if abs(puntos[i][0] - puntos[i+1][0]) < 0.5 or abs(puntos[i][1] - puntos[i+1][1]) < 0.5:
            if puntos[i][0] > 5:
                aux1 = -1;
            else:
                aux1 = 1;
            if puntos[i][1] > 5:
                aux2 = -1;
            else:
                aux2 = 1;
            puntos.insert(i+1, [(puntos[i][0] + puntos[i+1][0])*0.5+aux1, (puntos[i][1] + puntos[i+1][1])*0.5+aux2]);
            i = i + 2;
            a = a + 1;
        else:
            i = i + 1;

def recorrePuntos(puntos, eps):
    #Primero instanciamos nuestra tortuga (si no es la 1 debemos de cambiar el constructor)
    x = TurtleBot()
    #arreglaPuntos(puntos);
    print(puntos);
    #Ahora el loop general para ir a los puntos; la idea es que podamos agregar elementos a la lista puntos a la mitad del proceso si detectamos que la distancia con otra tortuga es muy corta
    pel = 1;
    while len(puntos) > 0:
        band = x.move2goal(puntos[0][0],puntos[0][1], eps, pel);
        pel = 1; #está activada la bandera de revisión de peligro. Solo se desactiva en caso de que se agregue un nuevo punto medio a la trayectoria
        if band == 0: #Significa que hay al menos una tortuga en posición peligrosa por lo tanto debemos de definir un punto medio en la trayectoria original
            tray = x.calculaTrayectoria(1.5);
            tray = x.seleccionaTrayectoria(tray);
            if len(tray) == 0: #No hay trayectoria deseable entonces esperamos a que se libere una
                time.sleep(1);
            else:
                puntos.insert(0, tray) #Insertamos el nuevo punto para alejarnos de la tortuga
                pel = 0;
        print(puntos);
        if abs(x.pose.x - puntos[0][0] < eps) and abs(x.pose.y - puntos[0][1] < eps) :
            puntos.pop(0);

if __name__ == '__main__':
    #Nos suscribimos para detectar la posición de las tortugas
    position_topic1 = "/turtle1/pose"
    pose_subscriber1 = rospy.Subscriber(position_topic1, Pose, poseCallback1)
    
    position_topic2 = "/turtle2/pose"
    pose_subscriber2 = rospy.Subscriber(position_topic2, Pose, poseCallback2)
    
    position_topic3 = "/turtle3/pose"
    pose_subscriber3 = rospy.Subscriber(position_topic3, Pose, poseCallback3)
    
    position_topic4 = "/turtle4/pose"
    pose_subscriber4 = rospy.Subscriber(position_topic4, Pose, poseCallback4)
    
    position_topic6 = "/turtle6/pose"
    pose_subscriber6 = rospy.Subscriber(position_topic6, Pose, poseCallback6)
   
    
    recorrePuntos([[10,10],[1,4],[3.5,7]],0.1)
