import math
import pygame

from quaternion import Quaternion

from scene import Scene
from object3d import Object3d
from camera import Camera
from mesh import Mesh
from material import Material
from color import Color
from vector3 import Vector3

# declaration of the main function
def main():
    # pygame startup
    pygame.init()

    # Setting the screen resolution 
    res_x = 1024
    res_y = 768
   
    # Creation of the window where the project will run
    screen = pygame.display.set_mode((res_x, res_y))
     
    # Creation of the environment
    scene = Scene("Scene")
    scene.camera = Camera(False, res_x, res_y)

    #Distance of the camera by 3 units
    scene.camera.position -= Vector3(0, 0, 3)

    # Creation of the model, the tetrahedron, for the application    obj1 = Object3d("Tetraedro")
    obj1.scale = Vector3(1, 1, 1)
    obj1.position = Vector3(0, 0, 0)
    obj1.mesh = Mesh.create_tetra((1, 1, 1), 12, 12)
    obj1.material = Material(Color(1, 0, 0, 1), "tetraedro")
    scene.add_object(obj1)
    
    # Initialization of the variables used to move the object    
    x,y,z = 0, 0, 0

    pygame.mouse.set_visible(True)
    pygame.event.set_grab(False)

    #Loop until you detect the event that corresponds to the act of exiting the application    
    while True:
    #Initialization of the angle used to rotate the object in the application
        angle = 15
        for event in pygame.event.get():
        # Did the user click on the x in the window?
            if event.type == pygame.QUIT:
            # Application suspension           
                return
            
            elif event.type == pygame.KEYDOWN:  
            # Shortcut to close the window
                if event.key == pygame.K_ESCAPE:
                    return
                
                # Implementation of the object's rotation function around its "positive" Y axis
                if event.key == pygame.K_RIGHT:
                    axis = Vector3(0, 1, 0)
                    axis.normalize()
                    q = Quaternion.AngleAxis(axis, math.radians(angle))
                    obj1.rotation = q * obj1.rotation
                    scene.render(screen)
                    pygame.display.flip()

                # Implementation of the object's rotation function around its "negative" Y axis
                if event.key == pygame.K_LEFT:
                    axis = Vector3(0, -1, 0)
                    axis.normalize()
                    q = Quaternion.AngleAxis(axis, math.radians(angle))
                    obj1.rotation = q * obj1.rotation
                    scene.render(screen)
                    pygame.display.flip()

                # Implementation of the object's rotation function around its "positive" X axis
                if event.key == pygame.K_UP:
                    axis = Vector3(1, 0, 0)
                    axis.normalize()
                    q = Quaternion.AngleAxis(axis, math.radians(angle))
                    obj1.rotation = q * obj1.rotation
                    scene.render(screen)
                    pygame.display.flip()

                # Implementation of the object's rotation function around its "negative" X axis
                if event.key == pygame.K_DOWN:
                    axis = Vector3(-1, 0, 0)
                    axis.normalize()
                    q = Quaternion.AngleAxis(axis, math.radians(angle))
                    obj1.rotation = q * obj1.rotation
                    scene.render(screen)
                    pygame.display.flip()
                
                # Implementation of the object's rotation function around its "positive" Z axis
                if event.key == pygame.K_PAGEUP:
                    axis = Vector3(0, 0, 1)
                    axis.normalize()
                    q = Quaternion.AngleAxis(axis, math.radians(angle))
                    obj1.rotation = q * obj1.rotation
                    scene.render(screen)
                    pygame.display.flip()

                
                # Implementation of the object's rotation function around its "negative" Z axis
                if event.key == pygame.K_PAGEDOWN:
                    axis = Vector3(0, 0, -1)
                    axis.normalize()
                    q = Quaternion.AngleAxis(axis, math.radians(angle))
                    obj1.rotation = q * obj1.rotation
                    scene.render(screen)
                    pygame.display.flip()


                # Implementation of the upward movement function               
                if event.key == pygame.K_w:
                    y += 0.1
                    obj1.position = Vector3(x, y, z)
                    scene.render(screen)
                    pygame.display.flip()
                
                # Implementation of the function of moving the object down
                if event.key == pygame.K_s:
                    y -= 0.1
                    obj1.position = Vector3(x, y, z)
                    scene.render(screen)
                    pygame.display.flip()

                # Implementation of the function of moving the object to the right
                if event.key == pygame.K_d:
                    x += 0.1
                    obj1.position = Vector3(x, y, z)
                    scene.render(screen)
                    pygame.display.flip()
                
                # Implementation of the function of moving the object to the left
                if event.key == pygame.K_a:
                    x -= 0.1
                    obj1.position = Vector3(x, y, z)
                    scene.render(screen)
                    pygame.display.flip()

                # Implementation of the "move away" function of the object in relation to the camera
                if event.key == pygame.K_e: 
                #Treating the division by zero exception
                    if z < 1:
                        z += 0.1

                    obj1.position = Vector3(x, y, z)
                    scene.render(screen)
                    pygame.display.flip()
                
                # Implementation of the "approach" function of the object in relation to the camera
                if event.key == pygame.K_q:   
                    #Treating the division by zero exception
                    if z > -1:
                         z -= 0.1
                   
                    obj1.position = Vector3(x, y, z)

                    scene.render(screen)
                    pygame.display.flip()
        
                
        #Fill the screen with a dark blue
        screen.fill((0, 0, 20))

        # rendering of the object and "print" of the object on the user's screen        
        scene.render(screen)
        pygame.display.flip()

#main() initialization
main()
