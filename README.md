# FÊNIX MODEL ROCKET SIMULATOR 🚀

![Fênix logotype](https://scontent.fplu1-1.fna.fbcdn.net/v/t1.6435-9/158499275_124854939643696_884025964079056168_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=e3f864&_nc_ohc=lOiVht85iucAX8OUZSa&_nc_ht=scontent.fplu1-1.fna&oh=00_AfAD0aDwQ5xpZectX7LwkavHNh4Q9nKiNUzxGW8aiksQZQ&oe=63B172A4)

<p align="center">
  <img alt="GitHub repo status" src="https://img.shields.io/badge/STATUS-IN%20DEVELOPMENT-brightgreen?style=for-the-badge">
  <a href="https://github.com/Rocket-Simulator/RocketSimulator/graphs/contributors">
    <img src="https://img.shields.io/github/contributors/Rocket-Simulator/RocketSimulator?style=for-the-badge" alt="Contributors">
  </a>  
  <a href="https://github.com/Rocket-Simulator/RocketSimulator/stargazers">
    <img alt="GitHub stars" src="https://img.shields.io/github/stars/Rocket-Simulator/RocketSimulator?style=for-the-badge">
  </a>
  <a href="https://github.com/Rocket-Simulator/RocketSimulator/network">
    <img alt="GitHub forks" src="https://img.shields.io/github/forks/Rocket-Simulator/RocketSimulator?style=for-the-badge">
  </a>
  <img alt="GitHub repo size" src="https://img.shields.io/github/repo-size/Rocket-Simulator/RocketSimulator?style=for-the-badge">
  <a href="https://github.com/Rocket-Simulator/     RocketSimulator/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/Rocket-Simulator/RocketSimulator?style=for-the-badge" >
  </a>
</p>


This program is a free and open access simulator for model rocketry. With this software, the user will be able to simulate their rocket as a rigid body,
obtaining important data about it, such as drag force, different drag coefficient types, the position of center of pression, trajectory expected, stress
data and so much more. By reading this document, you are going to be able to understand how to use this simulator, as well as what it calculates, what inputs
it needs and what outputs it returns.
Thus, this document is divided in the following topics, defined according to the folders and archives of the project:

+ Data
+ Utils
+ Physics
+ Aerodynamic
+ Propulsion
+ Recovery
+ Structure
+ Simulation
+ Accessing the Project

## Data 💾

The data folder contains some primordial information for the project, with files in JSON format. It is subdivided in folders with the type of data of the
following table:
| Folder      | Content                                                                                        |
| ----------- | ---------------------------------------------------------------------------------------------- |
| Cables      | Types of cables                                                                                |
| Materials   | Several materials for the model and its properties, such as aluminum, carbon fiber, etc.       |
| Parachutes  | Different kinds of parachute, depending on its geometry, with the info of its drag coefficient |
| Propellants | Three distinct propellant types with their tecnical features                                   |

![image](https://user-images.githubusercontent.com/119083049/205334940-a6ef751c-301f-4e05-b510-16c5f3a45f61.png)

*Example of data in 'materials' folder*

![image](https://user-images.githubusercontent.com/119083049/205336259-ce7237fa-ceeb-457c-a856-0b738c8cc93a.png)

*Example of data in 'propellants' folder*

## Utils 📝

In 'utils', we have important content simulation, like archives which contain classes for grouping related data, like parachute, nose type, rocket parts
data. We also have codes with fundamental constants needed and wind information for simulation.

![image](https://user-images.githubusercontent.com/119083049/205337747-80985d27-a945-499e-a02b-516676f5e25f.png)

*Parachute class code*

![image](https://user-images.githubusercontent.com/119083049/205337967-7099a96a-3698-4480-b9dd-23fade6ae09e.png)

*Wind direction class code*

## Physics ⚛️

<p align = "center">
  <img src= "https://user-images.githubusercontent.com/92520893/205438398-9d39c119-bc8a-4aa3-93d1-9287b9f822d9.jpeg">
</p>

Physics is a very important folder for the project, being responsible for bringing together most of the variables and functions that operate basic physics, or classical mechanics as it is commonly called. This section holds the programming that deals with the forces applied to the rocket, as well as vectors, which orient the forces and their direction, torque, coordinates, and more.

### forces

The folder that contains all the forces applied to the rocket through its trajectory, such as: drag, weight and wind force. All classes in this folder inherit from the **Vector** class, so they will all be treated as vectors, having their methods, as they should be.

*delta_time_simulation:*
<p>It contains the DeltaTimeSimulation class, which represents the state of the rocket at a given time. Its only use is to get this information
information in a practical way.</p>

### resultant_force

This file contains the ResultantForce class, responsible for receiving a list of forces and using them to calculate the resultant force at the indicated time "t". The list of forces MUST be ordered with the least dependent forces coming first, as changing the order can change the final result, with forces being calculated without having their dependent forces calculated properly. The change attenuates by decreasing *DELTA_TIME_SIMULATION*.

~~~python
class ResultantForce(Force):
    def __init__(self, forces: List[Force]):
        self.__forces = forces 
        # List of forces that MUST be ordered from most independent to least independent
        super().__init__(0, 0, 0, ApplicationPoint.CG)
~~~

Still within the class, we have the method that effectively performs the calculation of the resultant force, respecting all the peculiarities and dependencies of the other related forces.

~~~python
# Args: 'current_state: DeltaTimeSimulation' = Current state of the rocket.
def calculate(self, current_state: DeltaTimeSimulation):
        # Following the order of dependency of forces
        for force in self.__forces: 
            force.calculate(current_state)

        resultant_force = Vector(0, 0, 0)
        for force in self.__forces:
            resultant_force += force

        # Defines the resultant forces in each of the directions
        self.setX(resultant_force.x())
        self.setY(resultant_force.y())
        self.setZ(resultant_force.z())
~~~

### resultant_torque

This file contains the ResultantTorque class, responsible for receiving a list of torques and using them to calculate the resultant torque at the indicated time "t". The list of torques MUST be ordered with the least dependent torques coming first, as changing the order can change the final result, with torques being calculated without having their dependent torques calculated properly. The change attenuates by decreasing *DELTA_TIME_SIMULATION*.

~~~python
class ResultantTorque(Vector):
    def __init__(self, forces: List[Force], additional_torques=[]):
        self.__forces = forces
        self.__additional_torques = additional_torques
        # List of torques that MUST be ordered from most independent to least independent
        super().__init__(0, 0, 0)
~~~

Still within the class, we have the method that effectively performs the calculation of the resultant torque, respecting all the peculiarities and dependencies of the other related torques.

~~~python
# Args: 'current_state: DeltaTimeSimulation' = Current state of the rocket.
def calculate(self, current_state: DeltaTimeSimulation):
        # Following the order of dependency of forces
        for force in self.__forces:
            force.calculate(current_state)

        resultant_torque = Vector(0, 0, 0)
        for force in self.__forces:
            if force.application_point == ApplicationPoint.CG:
                continue
            
            lever = current_state.cg - current_state.cp
            torque = Vector.crossProduct(force, lever)
            resultant_torque += torque

        for torque in self.__additional_torques:
            torque.calculate(current_state)
            resultant_torque += torque

        # Defines the resultant torque in each of the directions
        self.setX(resultant_torque.x())
        self.setY(resultant_torque.y())
        self.setZ(resultant_torque.z())
~~~

### vector

The vector archive contains all the methods that deals with vector, like getting the scalar or cross product of two vectors, sum and subtraction of vectors, and the magnitude also.

Some examples of operations using the class **Vector**:

<img src="https://user-images.githubusercontent.com/92520893/205452599-0f47b5c9-0bb3-42b7-926a-bb99e8648efb.jpeg">

## Aerodynamic 💨

Aerodynamic deals with the result of the interaction of the air and a rigid body during the occurrence of a flow between them. It is, for obvious reasons,
indispensable for a model rocket project, once it influences hardly on its stability, apogee, trajectory and other parameters. Next, we describe briefly some of
the files restrained in this folder.

### 1. *Angular velocity* code

This file calculates the angular velocity of the model. Using the velocity of the rocket and its angle of attack, it multiplies the first by the sin() of the
second, which returns  the angular velocity.

![image](https://user-images.githubusercontent.com/119083049/205468607-17e3008e-7d16-4fde-8293-d3c7b9536fe9.png)

*Angular velocity calculus*

### 2. *CP of one body component* code

Through this code, we're able to estimate the center of pressure of each component of the rocket seperately. It receives the base area, the top area, the component
volume and its length to calculate this coordinate.

![image](https://user-images.githubusercontent.com/119083049/205468808-b5134961-dd94-41b4-981d-1963ac27862e.png)

*CP of one component function*

### 3. *Critical Reynolds number* code

Using the functions contained in this archive, the simulator is able to calculate the expected critical Reynolds number through the material roughness and the
rocket length. This parameter is important for us to understand the behavior of the model in an air flow.

### 4. *Fin drag* code

The code in this file considers that the air flow is perpendicular to the fin chord and, by this mean, calculates the fin drag in function of the mach number
of the rocket.

![image](https://user-images.githubusercontent.com/119083049/205469113-fa4a8cfe-8934-48d7-a106-fc84dbff6d8f.png)

*Fin drag code snippet*

### 5. *Lift effect* code

By manipulating the parameters of cilinder length, cilinder diameter, reference area and angle of attack, this code returns us the  normal force coefficient.

![image](https://user-images.githubusercontent.com/119083049/205469251-d7b28b2e-3586-4b26-8639-a42d9767ea3d.png)

*Lift effect code*

### 6. *Mach Number* code

A simple method to return the mach number, important for the calculations ahead, using the velocity of the rocket divided by the local sound velocity.

<img src="https://user-images.githubusercontent.com/92520893/205469116-3ea97332-1964-4c54-a941-74c268e58308.png">

### 7. *Nose Pressure Drag* code

If the transition batween the body of the rocket and the nose is smooth, the nose pressure drag coefficient is equal to zero. But if the transition has a conical shape, "bodynoseAngle" will be an argument used to calculate the pressure drag on the nose.

### 8. *Reynoulds Number* code

Reynolds number is used to determine the type of flow pattern as laminar or turbulent while flowing through a pipe, and it's calculated by the **reynolds_number** method. It's a simple file in the project, but very important.

<img src="https://user-images.githubusercontent.com/92520893/205469174-2e62b19e-66b9-4380-9916-ecaf6dd3eafa.png">

### 9. *Skin Friction* code

This file will return the drag coefficient according to the mach number, using the reynolds number, and will not be able to do so if the rocket is supersonic.

### 10. *Total Skin Friction Drag Coefficient* code

Finally, using the drag coefficient collected with the work of the two programs above, this method will return the total friction drag coefficient applied on the full body of the rocket.

<img src="https://user-images.githubusercontent.com/92520893/205469183-6f401e2e-0697-4efc-97fa-06917c96f901.png">

## Propulsion 🚀

## 1. Flow Area

The function in this file calculates the area of flow for the combustion products based on the volumetric load.

Inputs:

 d (num): internal diameter of the grain.
 Vl (num): volumetric loading fraction.

## 2. Burning Area

 The function of this file calculates the burning area of the propellent grain, that  is the product of pi and diameter squared.

Input: diamter

## 3. Burning Time

The burning time of the grain is the quocient of the external diameter of the grain minus the internal diameter of the grain by two times the grains´ burning rate.

Input: grains´external diamenter, grain's internal diameter and grains' burning rate

## 4. Chamber Pressure

By manipulating the parameters of the burning area of the propellant grain,  popellant's density, burn rate coefficient (determined by the propellant chosen), throat area, isentropic exponent (determined by the propellant chosen), molar gas constant, combustion temperature, pressure exponent (determined by the propellant chosen) it calculates the chamber pressure.

## 5. combustion chamber volume

 By manipulating the parameters of the combustion chamber diameter and combustion chamber lenght this function calculates the combustion chamber volume.

## 6. Combustion Temperature

  It calculates the temparature of the combustion of the grain.
  
  Inputs:
  temperature at the exit.
  isetropic exponent.
  Mach number of flow at the exit.

## 7. Flow speed

The function in this file calculates  the flow speed at the exit of the nozzle, by manipulating the parameters of isentropic exponent, combustion temperature of the proppelant, universal gas constant, effective molar mass of the products ,atmosferic pressure and pressure inside the chamber.

## 8. Nozzle Scape diameter

The  function in this file calculates the nozzle escape diameter by manipulating the parameters if medium throat diameter, isentropic exponent, gas escape pressure and chamber pressure.

## 9. Nozze Exit Area

 The function in this returns the nozzle exit area. This function require as input  the  diameter of nozzle's exit.

## 10. Nozzle throat area

 The function in this returns the nozzle throat area. This function require as input  the  diameter of the nozzle

## 11. Propellant Density

The function in this file calculates the propellant density by dividing the propellant mass by it's volume

## 12. Propellant volume

The function in this file calculates the propellant volume by manipulating the parameters of external diameter ,internal diameter ,segment's lenght, number of segments.

## 13. Throath diameter interval

 The function in this file calculates the throath diameter interval and has as input the  area of combustion products flow.

## 14. Volumetric Loading Fraction

The function in this file calculates the volumetric loading fraction by manipulating the parameters of propellant´s volume and the combustion chamber volume.

## Recovery 🪂

### 1. Weight Force

the weight force is the product of the mass and the gravity acceleration, as described by the second Newton's Law

Inputs:

+ **'mass'**
+**'gravity'**

the weight is a basic variable for other calculations

Outputs:

+ **'Weight_force'**

### 2. Velocity

the velocity on the vertical axis, based on the initial velocity when the parachute is deployed and for the acceleration resultant from the forces calculated.

Inputs:

+ **’velocity0’**
+**'time’**
+**’acceleration’**

Output:

+ **’velocity’**

Velocity calculation is independent from the trajectory made, an approximation made basically from the resultant of the forces and the time of falling

### 3. Time

the time is defined by the remaining time from the height where the parachute is ejectred until the rocket touches the ground

Inputs:

+ **'initial_vertical_position'**
+**'max_speed'**

Output:

+**'time'**

The time used here is also an aproximation, for this we use the maximum speed, that is based from the structure parameters for the speed when the rocket reachs the ground.

### 4. Max range

Max range is basically an calculation using the parameters from velocity and the time to make an aproximation for the maximum range of distance that the rocket can go when falling

Inputs:

+ **'velocity'**
+**'time'**

Outputs:

+ **'max_range'**

### 5. Acceleration

the acceleration that affects the rocket is described by the Second Newton's Law

Inputs:

+ **'Weight_force'**
+**'parachute_drag_force'**
+**'mass'**

Output:

+ **'acceleration'**

The acceleration is an calculation based on the resultant of the forces on the parachute, that is the Weight of the system against the drag force wich is calculated how it follows.

### 6. Nominal Diameter

Input:

+ **'transversal_section_area'**

Output:

+ **'nominal_Diameter'**

The nominal diameter is a aproximation made from the total area of the parachute, so it is basically the diameter of a parachute of the area speciffied but on circular shape (it independs from the actual parachute shape).

### 7. Mass Ratio

The inverted mass ratio plotted against the opening shock coefficient

Inputs:

+ **'air_density'**
+**'transversal_section_area'**
+**'mass'**

Output:

+ **'Rm'**

The mass ratio is used to calculate the opening shock as the variables from 8 to 11 that follows

### 8. Momentum

the momentum of the parachute has two states, one for the angle in horizontal, and one in vertical, for the present calculations we are going to use only the vertical momentum.

Inputs:

+ **'final_speed'**
+**'initial_speed'**
+**'g'**
+**'tfill'**

Output:

+ **'momentum'**

### 9. Normalized integral

The normalized integral is the aproximation made from the graphs of OSCalc that specify three different states, depending from de Inverted Mass Ratio.

Input:

+ **'Rm'**

Output:

+ **'If'**

As said previously, there are two different graphs we can make with different patterns when plotting the Inverted Mass Ratio against the Opening Shock, so depending from the Rm we are going to consider two different If.

![image](https://user-images.githubusercontent.com/98179873/205506324-a8d01c19-e7f1-43ee-bbd1-358a576f9d69.png)

### 10. Inflation time

the inflation time is a data that we can estimate from experimental results that bases on filling time.

Inputs:

+ **'stretch_speed'**
+**'tfill'**
+**'nominal_Diameter'**

Output:

+ **'inflation_time'**

The inflation time is a dimensional variable that is made from the filling time (tfill), based on stretch speed whose is the payload speed, details on the image:

![image](https://user-images.githubusercontent.com/98179873/205506288-f0ffaf26-4971-4e09-b96e-8f94a844139c.png)

### 11. General inflation time

the general inflation time is an arbitrary adimensional value based on inflation time

Inputs:

+ **'inflation_time'**
+**'nominal_diameter'**
+**'If'**
+'**transversal_section_area'**

Output:

+ **'general_Inflation_time'**

The same way of the inflation time, the general inflation time is calculated based on the other experimental data, but this is a non_dimensional variable.

### 12. Drag force

 the drag force is calculated with the use of many variables such as the drag coefficient, representing the flow of air by the parachute fibers.

Inputs:

+ **'air_density'**
+**'transversal_section_area'**
+**'drag_coefficient'**
+**'velocity'**

Output:

+ **'drag_force'**

The drag force uses the drag coefficient, wich is an experimental data, so in the code we are using general drag coefficient aproximations from research, the limitation of the code is the total of parachute data we could acomodate

![image](https://user-images.githubusercontent.com/98179873/205506155-6d12bb8e-86a7-464a-86c4-9b8285b83224.png)

### 13. Opening shock

the opening shock is the factor that determines the maximum force that affects the parachute

Inputs:

+ **'mass_ratio'**
+**'general_Inflation_time'**
+**'Integral'**

Output:

+ **'opening_shock

Based on the data and the calculations made until now the opening shock coefficient is a variable that our code ir assumed to get.

### 14. Maximum force

Maximum force is basically the maximum force that the system is going to be exposed during the flight
Inputs:

+ **'parachute_drag_force'**
+**'opening_shock'**

Output:

+ **'maximum_force'**

The maximum force is a simple multiplication of the opening shock coefficient for the parachute drag force, so that it is a algebraic variable

### 15. Cable tension

Returns the boleans based on the relation for the maximum force and the maximum cable tension supported

Inputs:

+ **'cable_number'**
+**'cable_area'**
+**'maximum_force'**
+**'safe_load'**

Output:

True or False

The code here has two parts, one that determines the cable tension that the recovery is making in each hope, and the second part compares this value to the resistance of the cables, returning True if it is suposed to break or false if it doesn´t.

![image](https://user-images.githubusercontent.com/98179873/205506181-5c6312a0-eda5-457c-9c64-7ea5b193af0f.png)

*The materials of cables supported by the actual code*

![image](https://user-images.githubusercontent.com/98179873/205506209-bf5b0d76-3997-4f03-b579-e12ce3406025.png)

*The code that tests the cables based on the maximum force*

## Structure 🧱

The Structure folder holds codes for the calculus of diverse tension and stress types, as well as of information got from the input dimensions of the
rocket and safety margin. Next, we will describe each code archive of this folder, its inputs and outputs.

### 1. *Parameter a* code

Inputs:

+ **'external_radius'**
+**'internal_radius'**
+**'vessel_maximum_pressure'**
+**'von_Mises_stress'**

Outputs:

+ **'parameter_a'**: the relation between motor external and internal radius.

This property of the motor can be calculated by different ways using different combinations of the inputs. Therefore, not all inputs are necessary.
The manners to calculate the 'parameter a' are shown below:

![image](https://user-images.githubusercontent.com/119083049/205346674-7cdf4c3e-b032-44c7-82db-42ae27ae9daf.png)

*Code for calculus of parameter a.*

### 2. *Thin walls check* code

Inputs:

+ **'external_radius'**
+**'internal_radius'**

Outputs:
+**'thickness'**: difference between external radius and internal radius

This technical feature will be important for some following calculus and is determined this way:

![image](https://user-images.githubusercontent.com/119083049/205354985-0f1eefdf-2225-4bfc-b759-3568199f8080.png)

### 3. *Circumferential tension* code

Inputs:

+ **'parameter_a'**: the relation between motor external and internal radius.
+ **'vessel_maximum_pressure'**: maximum pressure inside motor due to ignition of fuel grain.

Outputs:

+ **'circumferential_tension'**

This code calculates the circumferetial tension expected to act on motor thin walls.

### 4. *External radius* code

Inputs:

+ **'parameter_a'**
+ **'internal_radius'**

Outputs:

+ **'external_radius'**

As you might imagine, this code returns the external radius for the motor of the rocket.

### 5. *Longitudinal tension* code

Inputs:

+ **'parameter_a'**
+ **'vessel_maximum_pressure'**

Outputs:

+ **'longitudinal_tension'**: the longitudinal tension that will act on motor thin walls.

This parameter is important to know if the motor walls will resist the tension applied to it, and it is calculated with the following
expression:

$VMP / (2*(a - 1))$

*VMP: 'Vessel Maximum Pressure'*

### 6. *Radial tension* code

Inputs:

+ **'parameter_a'**
+ **'vessel_maximum_pressure'**

Outputs:

+ **0**: radial tension in motor considered to have thin walls is always zero.

With a thin walls motor, this function always returns 0.

### 7. *Von Mises stresss* code

Inputs:

+ **'parameter_a'**
+**'vessel_maximum_pressure'**
+**'safety_margin'**
+**'material'**: material used to build the motor

Output:

+ **'von_Mises_stress'**: von Mises stress calculated in it's own method

For this calculus, the safety margin is not a necessary input. Once the safety margin depends on Von Mises stress for being calculated, the
Von Mises Stress will be recalculated after obtaining the safety margin. Said that, this parameter is acquired this way:

![image](https://user-images.githubusercontent.com/119083049/205353417-75907c1f-12d4-4e3c-816e-9c52e512e312.png)

*Von Mises stress calculus*

### 8. *Safety margin* code

Inputs:

+ **'von_Mises_stress'**
+ **'material'**

Outputs:

+ safety_margin of the built motor

The safety margin is important to ensure that the motor will resist the Von Mises stress. It is calculated as in the next picture:

![image](https://user-images.githubusercontent.com/119083049/205365465-fa6fc29d-c934-4e6b-b135-8a4dd89e27c1.png)

*Safety margin calculus*

### 9. *Thickness* code

Inputs:

+ **'external_radius'**
+**'internal_radius'**

With all these methods, we're able to determine a lot of important things for simulation and for checking rocket properties.

## Simulation 🖥️

This folder is responsible for creating objects and abstract classes indispensable for the simulation and for making the simulations itself.
Its activities are accomplished by the codes that will be described next.

### 1. *Abstract ambient* code

This file creates a superclass for the other ambients needed. It receives a list of forces for the construction of the ambient.

### 2. *Airless earth ambient* code

It generates a subclass of AbstractAmbient which comprehends an environment of an airless earth and uses the *'physics'* codes.

![image](https://user-images.githubusercontent.com/119083049/205357761-2600c612-d2b9-4ef1-85f3-0ed59c2f1cc8.png)

*Airless earth code*

### 3. *Earth ambient* code

Just as the other classes, this is a subclass of AbstractAmbient. It is similar to the previous file, but this Earth has a 'little' difference:
it has atmosphere.

![image](https://user-images.githubusercontent.com/119083049/205398534-611817f8-7306-4d50-a9b7-56acd44dde18.png)

*Airfull Earth code*

### 4. *Simulation* code

This is the most extensive code of this folder and is responsible for the simulation itself. in the 'simulation' class, it coordinates the physics
simulation. This class has a lot of especial functions that will be briefly described in the ensuing table:

| Method                          | What it does                                                                             |
| ------------------------------- | ---------------------------------------------------------------------------------------- |
| setupForces()                   | adds the forces involved in the simulation                                               |
| tryEjection()                   | verifies periodically if the parachute must be ejected in that moment and tries to do so |
| __correctParachuteOrientation() | after ejection, it corrects rocket's orientation to (0,0,1)                              |
| simulate()                      | runs the simulation for a specified range time and using a defined time interval         |
| __applyResultantForce()         | applies the resultant force on the body                                                  |
| __applyResultantTorque()        | calculates and applies the resultant torque on the body                                  |

With this part of the code, we're able to simulate properly, as we wanted.

## Accessing the Project 🖿

[1] First, copy the link to the repository <https://github.com/Rocket-Simulator/RocketSimulator>.

[2] Next, right-click inside the folder you want to put, and select the Git Bash Here option.

[3] Inside the opened terminal, type git clone and then paste the copied link.

[4] Press Enter and in a few seconds you're done!

## References used in this project 📚

[1] Samuel Renan Costa Morais. Metodologia Para C ́alculo Estrutural de Motor de Foguete de Propelente S ́olido.
Belo Horizonte/MG, 2021.

[2] J. Barrowman. The practical calculation of the aerodynamic characteristics of slender finned vehicles. M.Sc.
thesis, The Catholic University of America, 1967.

[3] Sampo Niskanen. Openrocket technical documentation. Available at <https://openrocket.info/>
documentation.html (2021/11/10), 2013.

[4] Ma ́ıra Fernanda Oliveira de Miranda. DESENVOLVIMENTO DE UM SISTEMA DE RECUPERAC ̧AO ̃
PARA UM MINIFOGUETE, Uberlˆandia 2021.

[5] Gary Peek Jean Potvin. OSCALC: Opening Shock Calculator, julho 2006.
