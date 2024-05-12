from diagrams import Diagram
from diagrams.programming.flowchart import Action
from diagrams.digitalocean.storage import Folder


with Diagram("Go project structure", show=False, direction="TB"):
    Folder("pkg") >> [Folder("controlle"),
                  Folder("config"),
                  Folder("models"),
                  Folder("routes"),
                  Folder("utils")]
    Folder("cmd") >> [Folder("main"),
                  Folder("cmd")]
