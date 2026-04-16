# Title:   dlg.set_checkbox_state()
# Desc:    Set the state of the CheckBox to checked or unchecked
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_checkbox_state
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_checkbox(name="CheckBox2",text="Jupiter",checked=True,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_checkbox_state(name="CheckBox2",checked=False)  # [hl]
    isChecked = dlg.isbutton_checked(name="CheckBox2")
    print(isChecked)

if __name__=='__main__':
    main()
