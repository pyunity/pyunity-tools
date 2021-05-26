@ECHO OFF

py prepare.py
py -m autopep8 -i -r --ignore E301,E302 pyunity_tools setup.py prepare.py cli.py
py setup.py bdist_wheel sdist
RMDIR /S /Q build\ pyunity_tools.egg-info\
IF NOT [%1] == [] (
git add .
git commit -m %1
git push
)
pip install --upgrade dist/pyunity_tools-0.1.0-py3-none-any.whl