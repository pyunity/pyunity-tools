import os
import click
from pyunity import *
from .. import current_dir

def main(file):
    if not os.path.isfile(file):
        raise click.BadParameter("File does not exist: " + repr(file))
    if not file.endswith(".mesh"):
        raise click.BadParameter("File is not in PyUnity Mesh format: " + repr(file))
    
    project = Loader.LoadProject(os.path.join(current_dir, "viewer", "viewer"))
    scene = SceneManager.GetSceneByIndex(0)
    mesh = Loader.LoadMesh(file)
    scene.gameObjects[-1].GetComponent(MeshRenderer).mesh = mesh
    SceneManager.LoadScene(scene)
