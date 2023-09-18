from CircleT import CircleT
from TriangleT import TriangleT
from BodyT import BodyT
from Scene import Scene
from Plot import plot
import pytest
import pytest_cov

# Class to test CircleT module
class TestCircleT:
    # setup circles
    def setup_method(self, method):
        self.circle1 = CircleT(1, 2, 5, 6)
        self.circle2 = CircleT(-1, -2, 5, 6)

    # teardown circles
    def teardown_method(self,method):
        self.circle1 = None
        self.circle2 = None
    
    # Test cm_x()
    def test_cm_x(self):
        assert self.circle1.cm_x() == 1

    def test_cm_x2(self):
        assert self.circle2.cm_x() == -1

    # Test cm_y()
    def test_cm_y(self):
        assert self.circle1.cm_y() == 2

    def test_cm_y2(self):
        assert self.circle2.cm_y() == -2

    # Test mass()
    def test_mass(self):
        assert self.circle1.mass() == 6

    # Test negative mass
    def test_mass2(self):
        with pytest.raises(ValueError):
            circle3 = CircleT(1, 2, 5, -6)
    
    # Test negative radius
    def test_radius(self):
        with pytest.raises(ValueError):
            circle3 = CircleT(1, 2, -5, 6)

    # Test m_inert()
    def test_m_inert(self):
        assert self.circle1.m_inert() == 75
#-------------------------------------------------------------
# Class to test TriangleT module
class TestTriangleT:
    # setup triangles
    def setup_method(self, method):
        self.triangle1 = TriangleT(1, 2, 5, 6)
        self.triangle2 = TriangleT(-1, -2, 5, 6)

    # teardown triangles
    def teardown_method(self,method):
        self.triangle1 = None
        self.triangle2 = None
    
    # Test cm_x()
    def test_cm_x(self):
        assert self.triangle1.cm_x() == 1

    def test_cm_x2(self):
        assert self.triangle2.cm_x() == -1

    # Test cm_y()
    def test_cm_y(self):
        assert self.triangle1.cm_y() == 2

    def test_cm_y2(self):
        assert self.triangle2.cm_y() == -2

    # Test mass()
    def test_mass(self):
        assert self.triangle1.mass() == 6

    # Test negative mass
    def test_mass2(self):
        with pytest.raises(ValueError):
            triangle3 = TriangleT(1, 2, 5, -6)
    
    # Test negative side length
    def test_radius(self):
        with pytest.raises(ValueError):
            triangle3 = TriangleT(1, 2, -5, 6)

    # Test m_inert()
    def test_m_inert(self):
        assert self.triangle1.m_inert() == 12.5
#-------------------------------------------------------------
# Class to test BodyT module
class TestBodyT:
    # setup body
    def setup_method(self, method):
        self.body1 = BodyT([1,2,3,4],[1,2,3,4],[1,2,3,4])

    # teardown body
    def teardown_method(self,method):
        self.body1 = None
    
    # Test cm_x()
    def test_cm_x(self):
        assert self.body1.cm_x() == 3

    # Test cm_y()
    def test_cm_y(self):
        assert self.body1.cm_y() == 3

    # Test mass()
    def test_mass(self):
        assert self.body1.mass() == 10

    # Test negative mass
    def test_mass2(self):
        with pytest.raises(ValueError):
            body2 = BodyT([-1,-2,-3,-4],[-1,-2,-3,-4],[1,-2,3,4])
    
    # Test unequal sequences
    def test_unequal_sequences(self):
        with pytest.raises(ValueError):
            circle3 = BodyT([-1,-2,-3,-4],[-1,-2,-3,-4],[1,2,3,4,5])

    # Test m_inert()
    def test_m_inert(self):
        assert self.body1.m_inert() == 20.0

#-------------------------------------------------------------
# Class to test Plot module
class TestPlot:
    def test_plot(self):
        g = 9.81  # accel due to gravity (m/s^2)
        m = 1  # mass (kg)
        def Fx(t):
                return 5 if t < 5 else 0
        def Fy(t):
            return -g * m if t < 3 else g * m
        c = CircleT(1.0, 10.0, 0.5, 1.0)
        S = Scene(c, Fx, Fy, 0, 0)
        t, wsol = S.sim(10, 100)
        #plot(wsol, t)

#-------------------------------------------------------------
# Class to test Scene module
class TestScene:
    # setup scene
    def setup_method(self, method):
        self.shape = CircleT(12, 22, 32, 42)
        self.vx = 2
        self.vy = 4
        self.scene = Scene(self.shape, self.Fx, self.Fy, self.vx, self.vy)

    # teardown scene
    def teardown_method(self, method):
        self.shape = None
        self.vx = None
        self.vy = None 

    def Fx(self, t):
        return 5 if t < 5 else 0

    def Fy(self, t):
        g = 9.81  # accel due to gravity (m/s^2)
        m = 100  # mass 
        return -g * m if t < 3 else g * m

    def test_get_shape(self):
        assert self.shape == self.scene.get_shape()

    def test_set_shape(self):
        self.scene.set_shape(TriangleT(12, 22, 32, 42))
        assert not (self.scene.get_shape() == self.shape)

    def test_get_init_velo(self):
        assert (self.scene.get_init_velo()) == (self.vx, self.vy)

    def test_set_init_velo(self):
        self.scene.set_init_velo(5, 6)
        assert not (self.scene.get_init_velo()) == (self.vx, self.vy)

    def test_sim(self):
        t, wsol = self.scene.sim(5, 5)
        calculate_wsol = [[12.0, 22.0, 2.0, 4.0], [14.6, 8.8, 2.2, -25.2], 
        [17.4, -40.9, 2.3, -54.3], [20.3, -113.9, 2.5, -48.5], [23.5, -156.3, 2.6, -19.3]]
        answer = []
        for i in range(5):
            for j in range(4):
                answer.append((abs(calculate_wsol[i][j] - wsol[i][j])) / (abs(wsol[i][j])))
        assert max(answer) < 0.05             


