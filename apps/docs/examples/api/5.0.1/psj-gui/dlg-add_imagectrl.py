# Title:   dlg.add_imagectrl()
# Desc:    Add a frame to put an image to the creating dialog
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_imagectrl
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    image = JPT.GetProgramPath() + \
        r"SampleData\PSJ\PSJ-GUI\CreateBolt\CreatingBolt_Pics\M30.JPG"
    dlg.add_imagectrl(name="ImageCtrl",image_file=image,layout="Window")  # [hl]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
