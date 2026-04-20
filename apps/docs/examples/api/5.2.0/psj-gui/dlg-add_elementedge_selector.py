# Title:   dlg.add_elementedge_selector()
# Desc:    Add "Elem edge" to the selection list, allowing user to select element edges and store the selected element edges to the selection list
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_elementedge_selector
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Length in X",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label7",text="Length in Y",layout="Layout6")
    dlg.add_textbox(name="TextBox8",layout="Layout6")
    dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label10",text="Length in Z",layout="Layout9")
    dlg.add_textbox(name="TextBox11",layout="Layout9")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_elementedge_selector(text = "Element edge 1")  # [hl]
    dlg.generate_window()
    
if __name__=='__main__':
    main()
