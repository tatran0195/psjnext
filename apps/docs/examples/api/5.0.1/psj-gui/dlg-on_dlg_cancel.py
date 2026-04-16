# Title:   dlg.on_dlg_cancel()
# Desc:    Execute a created function when Cancel button is clicked
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-on_dlg_cancel
# ---
from pyjdg import *

def on_button_Cancel_clicked(dlg):
    print("Cancel button is clicked")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True,include_apply=True)
    dlg.add_layout(name="Layout1",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Please click on Cancel button!",layout="Layout1")
    dlg.generate_window()
    dlg.on_dlg_cancel(callfunc=on_button_Cancel_clicked)  # [hl]

if __name__=='__main__':
    main()
