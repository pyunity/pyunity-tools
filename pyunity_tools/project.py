from pyunity import Loader, SceneManager
import os
import click

def create_blank(name, path="."):
    folder = os.path.join(path, name, "")
    if not os.path.isdir(path):
        raise click.BadParameter("The specified directory does not exist.")
    if os.path.isdir(folder) and os.listdir(folder):
        raise click.BadParameter("The specified directory is not empty.")
    SceneManager.AddScene("Main Scene")
    Loader.SaveAllScenes(name, folder)
    if path == ".":
        folder = name
    click.echo("Created project at " + folder)
