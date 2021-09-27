from pyunity import *

class MouseViewer(Behaviour):
    rot = Vector3.zero()
    start = Vector3.zero()
    other = ShowInInspector(GameObject)
    def Update(self, dt):
        if Input.GetMouseDown(MouseCode.Left):
            self.start = Input.mousePosition
        if Input.GetMouse(MouseCode.Left):
            diff = Input.mousePosition - self.start
            self.rot += Vector3(diff.y / Screen.height * 60,
                                diff.x / Screen.width * 96,
                                0)
            self.rot.x = clamp(self.rot.x, -90, 90)
            self.transform.eulerAngles = self.rot

            direction = self.transform.rotation.RotateVector(Vector3.forward()) * 10
            self.transform.position = -direction

            self.start = Input.mousePosition

class ColorChanger(Behaviour):
    renderer = ShowInInspector(MeshRenderer)
    def Start(self):
        self.renderer.mat = Material(RGB(255, 0, 0))

scene = SceneManager.AddScene("Scene")
scene.mainCamera.transform.position = Vector3(0, 0, -10)
scene.mainCamera.gameObject.scene = scene

obj = GameObject("Object")
renderer = obj.AddComponent(MeshRenderer)
changer = obj.AddComponent(ColorChanger)
changer.renderer = renderer
scene.mainCamera.AddComponent(MouseViewer).other = obj
scene.Add(obj)

SceneManager.LoadScene(scene)
Loader.SaveAllScenes("viewer")