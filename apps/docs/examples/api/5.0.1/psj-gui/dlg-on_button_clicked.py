# Title:   dlg.on_button_clicked()
# Desc:    Bind a created def function to a Button/RadioButton/CheckBox
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-on_button_clicked
# ---
from pyjdg import *

def on_button_clicked(dlg):
    JPT.Exec('CreateCube([0, 0, 0], [0.01, 0.01, 0.01], [10, 10, 10], "Cube_1", 5357649, 0:0)')
    print("--- Cube created! ---")

def on_checkbox_clicked(dlg):
    print("You clicked on Checkbox!")

def on_radio_buton_clicked(dlg):
    print("You clicked on Radio Button!")

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
    dlg.add_layout(name="Layout4",orientation=orientation.vertical,layout="GroupBox2")
    dlg.add_label(name="Label8",text="Click on Button!",text_halign="left",text_valign="top",layout="Layout4")
    dlg.add_button(name="Button5",text="Button",width=60,height=22,layout="Layout4")
    dlg.add_label(name="Label9",text="Click on Checkbox!",text_halign="left",text_valign="top",layout="Layout4")
    dlg.add_checkbox(name="CheckBox6",text="CheckBox",layout="Layout4")
    dlg.add_label(name="Label10",text="Click on Radio Button!",text_halign="left",text_valign="top",layout="Layout4")
    dlg.add_radiobutton(name="RadioButton7",text="RadioButton",layout="Layout4")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_button_clicked(name="Button5",callfunc=on_button_clicked)  # [hl:start]
    dlg.on_button_clicked(name="CheckBox6",callfunc=on_checkbox_clicked)
    dlg.on_button_clicked(name="RadioButton7",callfunc=on_radio_buton_clicked)  # [hl:end]

if __name__=='__main__':
    main()
