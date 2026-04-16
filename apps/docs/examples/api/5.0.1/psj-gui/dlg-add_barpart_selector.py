# Title:   dlg.add_barpart_selector()
# Desc:    Add "Bar" to the selection list, allowing user to select bar parts and store the selected bar parts to the selection list
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_barpart_selector
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Mesh Count",layout="Layout1")
    dlg.add_textbox(name="TextBox3",layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_barpart_selector()  # [hl]
    dlg.generate_window()
    
if __name__=='__main__':
    main()
