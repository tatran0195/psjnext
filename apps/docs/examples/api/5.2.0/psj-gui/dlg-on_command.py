# Title:   dlg.on_command()
# Desc:    Bind a created def function to a component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-on_command
# ---
from pyjdg import *

def onApplyButtonClicked(dlg):
    Geometry.Part.Cube()
    print("--- Cube created! ---")

def main():
    dlg=JDGCreator(title="TechnoStar",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[80,0,50,0],orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label2",text="Click on Apply button!",layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_command(name="ButtonApply",callfunc=onApplyButtonClicked)  # [hl]

if __name__=='__main__':
    main()
