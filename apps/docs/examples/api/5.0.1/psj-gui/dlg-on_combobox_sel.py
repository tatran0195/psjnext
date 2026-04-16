# Title:   dlg.on_combobox_sel()
# Desc:    Run a created function after a ComboBox item is selected
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-on_combobox_sel
# ---
from pyjdg import *

def on_combobox_select(dlg):
    print("Index of selected combobox: {}"
        .format(dlg.get_combobox_sel(name="ComboBox1")))

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_layout(name="Layout1",margin=[0,0,100,0],
        orientation=orientation.horizontal,layout="Window")
    dlg.add_combobox(name="ComboBox1",
        options=["item1","item2","item3","item4","item5"],
        width=70,layout="Layout1")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonApply",text="Apply",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_combobox_sel(name="ComboBox1",callfunc=on_combobox_select)  # [hl]

if __name__=='__main__':
    main()
