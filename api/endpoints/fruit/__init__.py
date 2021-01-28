from endpoints.classes import Resource

from .delete import DOC as delete_doc
from .delete import delete
from .get import DOC as get_doc
from .get import get
from .post import DOC as post_doc
from .post import post
from .put import DOC as put_doc
from .put import put

FRUIT = [
    Resource("GET", "/fruit", get, "Retrieve a fruit", "GET fruit", get_doc),
    Resource("PUT", "/fruit", put, "Update a fruit", "UPDATE fruit", put_doc),
    Resource("POST", "/fruit", post, "Create a fruit", "CREATE fruit", post_doc),
    Resource("DELETE", "/fruit", delete, "Delete a fruit", "DELETE fruit", delete_doc),
]
