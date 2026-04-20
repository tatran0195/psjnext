# Title:   dlg.set_radiobutton_state()
# Desc:    Set the state of the RadioButton to checked or unchecked
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_radiobutton_state
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,100,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_radiobutton(name="RadioButton2",text="Jupiter",checked=True,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_radiobutton_state(name="RadioButton2",checked=False)  # [hl]
    isChecked = dlg.isbutton_checked(name="RadioButton2")
    print(isChecked)

if __name__=='__main__':
    main()
