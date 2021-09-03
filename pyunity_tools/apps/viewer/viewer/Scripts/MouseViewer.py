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
