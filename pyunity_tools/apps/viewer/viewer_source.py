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
            diff = Vector2(diff.y / Screen.height * 180, diff.x / Screen.width * 360)
            self.transform.eulerAngles += Vector3(*diff, 0)
            self.start = new

class ColorChanger(Behaviour):
    renderer = ShowInInspector(MeshRenderer)
    def Start(self):
        self.renderer.mat = Material(RGB(255, 0, 0))

scene = SceneManager.AddScene("Scene")
scene.mainCamera.transform.position = Vector3(0, 0, -10)

obj = GameObject("Object")
renderer = obj.AddComponent(MeshRenderer)
changer = obj.AddComponent(ColorChanger)
changer.renderer = renderer
obj.AddComponent(MouseViewer)
scene.Add(obj)

Loader.SaveAllScenes("viewer")
SceneManager.LoadScene(scene)