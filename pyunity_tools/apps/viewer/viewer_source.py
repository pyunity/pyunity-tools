from pyunity import *

class MouseViewer(Behaviour):
    rot = Vector3(30, -30, 0)
    start = Vector3.zero()
    other = ShowInInspector(GameObject)
    zoom = ShowInInspector(float, 2)
    minDist = ShowInInspector(float, 5, "Distance")

    def Start(self):
        mesh = self.other.GetComponent(MeshRenderer).mesh
        mag = mesh.max.abs().length
        self.distance = max(mag * self.zoom, mag + self.minDist)

        self.transform.localEulerAngles = self.rot
        direction = self.transform.rotation.RotateVector(Vector3.forward()) * self.distance
        self.transform.position = -direction

    def Update(self, dt):
        if Input.GetMouseDown(MouseCode.Left):
            self.start = Input.mousePosition
        if Input.GetMouse(MouseCode.Left):
            diff = Input.mousePosition - self.start
            self.rot += Vector3(diff.y / Screen.height * 60,
                                diff.x / Screen.width * 96,
                                0)
            self.rot = self.rot.replace(0, Mathf.Clamp(self.rot.x, -90, 90))
            self.transform.localEulerAngles = self.rot

            direction = self.transform.rotation.RotateVector(Vector3.forward()) * self.distance
            self.transform.position = -direction

            self.start = Input.mousePosition

class ColorChanger(Behaviour):
    renderer = ShowInInspector(MeshRenderer)
    def Start(self):
        self.renderer.mat = Material(RGB(255, 0, 0))

scene = SceneManager.AddScene("Scene")
scene.gameObjects[1].transform.position = Vector3(10, 20, -30)
scene.gameObjects[1].transform.LookAtPoint(Vector3(0, 0, 0))

obj = GameObject("Object")
renderer = obj.AddComponent(MeshRenderer)
renderer.mesh = Loader.Primitives.cube
changer = obj.AddComponent(ColorChanger)
changer.renderer = renderer
scene.mainCamera.AddComponent(MouseViewer).other = obj
scene.Add(obj)

SceneManager.LoadScene(scene)
Loader.GenerateProject("viewer")
