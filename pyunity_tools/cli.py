import click
import os
import webbrowser
import glob
import platform
import subprocess
os.environ["PYUNITY_DEBUG_MODE"] = "0"

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])

def open_log(**kwargs):
    if platform.platform().startswith("Windows"):
        folder = os.path.join(os.getenv("appdata"), "PyUnity", "Logs")
    else:
        folder = os.path.join("/tmp", "pyunity", "logs")
    if kwargs["open"] is not None:
        if kwargs["open"] in ("latest", "newest"):
            file = os.path.join(folder, "latest.log")
        elif kwargs["open"] == "oldest":
            file = glob.glob(
                os.path.join(folder, "*.log"))[0]
        else:
            raise click.BadParameter("open must be one of latest, newest or oldest")
        if kwargs["verbose"]:
            click.echo(file)
        if os.path.isfile(file):
            try:
                os.startfile(file)
            except AttributeError:
                subprocess.call(["open", file])
    else:
        if kwargs["verbose"]:
            click.echo(folder)
        webbrowser.open(folder)

@click.group(context_settings=CONTEXT_SETTINGS)
def main():
    pass

@main.command()
@click.argument("open", required=False)
@click.option("-v", "--verbose", is_flag=True, help="click.echo additional info")
def logs(**kwargs):
    """
    Opens a log according to OPEN, if specified.
    Otherwise opens the system file browser with
    the folder containing PyUnity logs.

    OPEN can be one of latest, newest or oldest.

    """
    open_log(**kwargs)

if __name__ == "__main__":
    main()