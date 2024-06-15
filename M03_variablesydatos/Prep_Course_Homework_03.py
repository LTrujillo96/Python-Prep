#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla

# In[7]:

x=5
print(x)


# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

print(type(8.5))



# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:

print(type(x))



# 4) Crear una variable que contenga tu nombre

# In[2]:

mi_nombre = "Luis"


# 5) Crear una variable que contenga un número complejo

# In[3]:

num1= 4 + 4j  



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:


print(type(num1))


# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


numPi = 3.1415


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

q = "True" #es un string
w = True  #es un boolean



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

print(type(q))
print(type(w))



# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:


o = 7 + 7.6


# 11) Realizar una operación de suma de números complejos

# In[2]:

a = 4 + 3j
b = 3 + 4j
print(a+b)



# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:


c = a + 7j
print(c)


# 13) Realizar una operación de multiplicación

# In[5]:

print(5*5)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

print(2**8)


# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

t = 27 / 4
print(t)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

t = 27//4
print(t)



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

t = 27 % 4
print(t)



# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:


4*6+3


# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:

alfa1= "Hola"
alfa2= " Carnalito"
print(alfa1+alfa2)



# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:


"2" == 2 


# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:

int("2") == 2



# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


#por que el 3,8 es un str 


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

g = 3 
g -= 1
print(g)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:

1<<2
#La expresión resultado = 1 << 2 efectúa un desplazamiento de bits hacia la izquierda y guarda el resultado en la variable resultado. Lo que produce el número 4 como salida. 
#es un sistema numerico que solo usa el 0 y el 1 no como el sistema numerico que estamos acostumbrados a usar que va del 0 al 9.



# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:

2 + "2" #no se puede efectuar la operacion por que uno es un entero y el otro es un string 
#si los dos fueran del mismo tipo arrojaria 4 al ser 2 + 2 ambos enteros o 22 siendo los dos strings




# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

var1= "Mi novia tiene "
var2= 28
var3= "pero actua como una niña de "
var4= 4
var5= " años"
print(var1+str(var2)+var5+" "+var3+str(var4)+var5)

