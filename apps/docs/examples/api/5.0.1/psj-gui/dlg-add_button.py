# Title:   dlg.add_button()
# Desc:    Add a Button to the creating dialog
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-add_button
# ---
from pyjdg import *

TechnoStarImage = JPT.GetProgramPath() + "SampleData/PSJ/PSJ-Utility/Utils/TechnoStar.ico"

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add_button(name="Button3",text="Button",width=60,height=22,layout="Layout2")  # [hl:start]
    dlg.add_button(name="Button4",text="Button",width=60,height=22,img=TechnoStarImage,
        location="left",layout="Layout2")
    dlg.add_button(name="Button5",text="Button",width=60,height=22,img=TechnoStarImage,
        location="right",layout="Layout2")
    dlg.add_button(name="Button6",text="Button",width=60,height=22,img=TechnoStarImage,
        location="top",layout="Layout2")  # [hl:end]
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()

if __name__=='__main__':
    main()
