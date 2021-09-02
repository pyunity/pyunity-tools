from pyunity import *

class MouseViewer(Behaviour):
    def Start(self):
        self.start = None
    
    def Update(self, dt):
        if Input.GetMouseDown(MouseCode.Left):
            self.start = Input.mousePosition
        elif Input.GetMouse(MouseCode.Left):
            new = Input.mousePosition
            diff = new - self.start
            diff = Vector2(diff.y * Screen.height / 180, diff.x * Screen.width / 180)
            self.transform.eulerAngles += Vector3(*diff, 0)
            self.start = new

scene = SceneManager.AddScene("Scene")
scene.mainCamera.transform.position = Vector3(0, 0, -10)

obj = GameObject("Object")
renderer = obj.AddComponent(MeshRenderer)
renderer.mat = Material(RGB(255, 0, 0))
renderer.mesh = Mesh.cube(2)
obj.AddComponent(MouseViewer)
scene.Add(obj)

SceneManager.LoadScene(scene)