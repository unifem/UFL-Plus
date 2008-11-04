"""A collection of utility algorithms for handling UFL files."""

from __future__ import absolute_import

__authors__ = "Martin Sandve Alnes"
__date__ = "2008-03-14 -- 2008-11-04"

from ..output import ufl_error, ufl_info
from ..form import Form
from ..function import Function
from .checks import validate_form

#--- Utilities to deal with form files ---

infostring = """An exception occured during evaluation of form file.
To find the location of the error, a temporary script
'%s' has been created and will now be executed:"""

def load_forms(filename):
    # Read form file
    code = "from ufl import *\n"
    code += "\n".join(file(filename).readlines())
    namespace = {}
    try:
        exec(code, namespace)
    except:
        tmpname = "ufl_analyse_tmp_form"
        tmpfile = tmpname + ".py"
        f = file(tmpfile, "w")
        f.write(code)
        f.close()
        ufl_info(infostring % tmpfile)
        m = __import__(tmpname)
        ufl_error("Aborting load_forms.")
    
    # Extract Form objects, and Function objects to get their names
    forms = []
    function_names = []
    for k,v in namespace.iteritems():
        if isinstance(v, Form):
            forms.append((k,v))
        elif isinstance(v, Function):
            function_names.append((v,k))
    
    # Analyse validity of forms
    for k,v in forms:
        errors = validate_form(v)
        if errors:
            msg = "Found errors in form '%s':\n%s" % (k, errors)
            raise RuntimeError, msg
    
    return forms#, function_names # TODO: Return function_names?
