Notes, TODOs, and gotchas:

 - If you `pip install -e flask_app/` from the `devops_for_python` directory without the trailing slash, you'll pull an unintended web package.
 - If you run flask from `devops_for_python` with `flask --app flask_app run` it will get confused by the collision between the local directory and the installed package.  To resolve, change into a different directory or install not in editable mode `pip install flask_app/` 
 
