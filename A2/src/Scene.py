## @file Scene.py
#  @title Scene
#  @author Michael Hammal
#  @brief This class creates a scene of shapes
#  @details This class creates a scene of shapes based on velocity and unbalanced force

from scipy.integrate import odeint


class Scene:

    ## @brief Constructor for Scene with five parameters
    #  @param s Shape
    #  @param Fx unbalanced force function in x direction
    #  @param Fy unbalanced force function in y direction
    #  @param vx initial velocity in x dir
    #  @param vy initial velocity in y dir
    def __init__(self, s, Fx, Fy, vx, vy):
        self.s = s
        self.Fx = Fx
        self.Fy = Fy
        self.vx = vx
        self.vy = vy

    ## @brief Getter method for the shape
    #  @return Shape
    def get_shape(self):
        return self.s

    ## @brief Getter method for the unbalanced forces functions
    #  @return the unbalanced forces functions
    def get_unbal_forces(self):
        return self.Fx, self.Fy

    ## @brief Getter method for the initial velocities
    #  @return the initial velocities
    def get_init_velo(self):
        return self.vx, self.vy

    ## @brief Setter method for the shape
    #  @param s new Shape
    def set_shape(self, new_s):
        self.s = new_s

    ## @brief Setter method for the unbalanced forces functions
    #  @param new_Fx new unbalanced force function in the x direction
    #  @param new_Fy new unbalanced force function in the y direction
    def set_unbal_forces(self, new_Fx, new_Fy):
        self.Fx = new_Fx
        self.Fy = new_Fy

    ## @brief Setter method for the initial velocities
    #  @param new_vx new initial velocity in the x direction
    #  @param new_vy new initial velocity in the y direction
    def set_init_velo(self, new_vx, new_vy):
        self.vx = new_vx
        self.vy = new_vy

    ## @brief Method to simulate the physics of a scene
    #  @details Method to simulate the physics of a scene where
    #  a shape moves through 2D space based on Newton's second law
    #  @return the function simulation
    #  @param t_final final time
    #  @param n_steps number of steps
    def sim(self, t_final, n_steps):
        t = [((i * t_final) / (n_steps - 1)) for i in range(n_steps)]
        return (t, odeint(self.__ode, [self.s.cm_x(), self.s.cm_y(), self.vx, self.vy], t))

    ## @brief Helper method to be used in the sim method
    #  @details Helper method to be used in the sim method based on Newton's second law
    #  @return sequence of four real numbers
    #  @param w sequence of four real numbers
    #  @param t time
    def __ode(self, w, t):
        return [w[2], w[3], (self.Fx(t) / self.s.mass()), (self.Fy(t) / self.s.mass())]
