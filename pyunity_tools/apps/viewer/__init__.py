import os
import click
from .. import current_dir

def main(file):
    if not os.path.isfile(file):
        raise click.BadParameter("File does not exist: " + repr(file))
    if not (file.endswith(".mesh") or file.endswith(".obj") or file.endswith(".stl")):
        raise click.BadParameter("File is not in a readable mesh format: " + repr(file))

    from pyunity import Loader, SceneManager, MeshRenderer
    funcs = {
        "mesh": Loader.LoadMesh,
        "obj": Loader.LoadObj,
        "stl": Loader.LoadStl
    }
    project = Loader.LoadProject(os.path.join(current_dir, "viewer", "viewer"))
    scene = SceneManager.GetSceneByIndex(project.firstScene)
    mesh = funcs[file.rsplit(".", 1)[-1]](file)
    scene.gameObjects[2].GetComponent(MeshRenderer).mesh = mesh
    SceneManager.LoadScene(scene)
