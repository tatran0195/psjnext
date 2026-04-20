# Title:   dlg.get_combobox_option()
# Desc:    Get the string value of the being selected ComboBox option
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-get_combobox_option
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_combobox(name="ComboBox1",options=["item1","item2","item3","item4","item5","item6"],layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_combobox_sel(name="ComboBox1",option=2)
    print(dlg.get_combobox_option(name="ComboBox1",index=2))  # [hl]

if __name__=='__main__':
    main()
