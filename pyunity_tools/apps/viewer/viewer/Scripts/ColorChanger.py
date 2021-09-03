from pyunity import *

class ColorChanger(Behaviour):
    renderer = ShowInInspector(MeshRenderer)
    def Start(self):
        self.renderer.mat = Material(RGB(255, 0, 0))
