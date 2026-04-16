# Title:   dlg.add_vertex_selector()
# Desc:    Add "Vertex" to the selection list, allowing user to select vertexes and store the selected vertexes to the selection list
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_vertex_selector
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_vertex_selector()  # [hl]
    dlg.generate_window()

if __name__=='__main__':
    main()
