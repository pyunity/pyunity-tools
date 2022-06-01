import random
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

class Hover(Behaviour):
    renderer = ShowInInspector(MeshRenderer)
    rb = ShowInInspector(Rigidbody)

    def Start(self):
        self.on = False
        self.rb.gravity = False

        mesh = self.renderer.mesh
        self.points = [
            Vector3(mesh.min.x, mesh.min.y, mesh.min.x),
            Vector3(mesh.min.x, mesh.min.y, mesh.max.x),
            Vector3(mesh.max.x, mesh.min.y, mesh.min.x),
            Vector3(mesh.max.x, mesh.min.y, mesh.max.x),
        ]
        self.rb.mass = 35 * Mathf.Sqrt((mesh.max.x - mesh.min.x) ** 2 + (mesh.max.z - mesh.min.z) ** 2)

    def Update(self, dt):
        if self.on:
            for point in self.points:
                worldspace = self.transform.rotation.RotateVector(point) + self.transform.position
                self.rb.AddForce(Vector3(0, 5 ** (2-worldspace.y), 0), point)

        if Input.GetKeyDown(KeyCode.Space):
            if self.on:
                self.rb.gravity = False
                self.rb.force = Vector3.zero()
                self.rb.torque = Vector3.zero()
                self.rb.velocity = Vector3.zero()
                self.rb.rotVel = Vector3.zero()
                self.transform.position = Vector3.zero()
            else:
                self.rb.gravity = True
            self.on = not self.on

scene = SceneManager.AddScene("Scene")
scene.gameObjects[1].transform.position = Vector3(10, 20, -30)
scene.gameObjects[1].transform.LookAtPoint(Vector3(0, 0, 0))

obj = GameObject("Object")
renderer = obj.AddComponent(MeshRenderer)
renderer.mesh = Loader.Primitives.cube
changer = obj.AddComponent(ColorChanger)
changer.renderer = renderer
scene.mainCamera.AddComponent(MouseViewer).other = obj
rb = obj.AddComponent(Rigidbody)
hover = obj.AddComponent(Hover)
hover.renderer = renderer
hover.rb = rb
scene.Add(obj)

canvasObj = GameObject("Canvas")
canvas = canvasObj.AddComponent(Canvas)
scene.mainCamera.canvas = canvas
scene.Add(canvasObj)

label = GameObject("Label", canvasObj)
text = label.AddComponent(Text)
text.text = "Press Space to start/stop hover"
text.font = FontLoader.LoadFont("Arial", 24)
text.centeredY = TextAlign.Top
text.color = RGB(0, 0, 0)
rectTransform = label.AddComponent(RectTransform)
rectTransform.offset.min = Vector2(10, 10)
rectTransform.offset.max = Vector2(400, 50)
scene.Add(label)

SceneManager.LoadScene(scene)
Loader.GenerateProject("viewer")
