# Title:   dlg.set_item_text()
# Desc:    Set the text which will be shown inside the component
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-set_item_text
# ---
from pyjdg import *
def onSetButtonClicked(dlg):
    dlg.set_item_text(name="TextBox1",text="This is sample text")  # [hl]

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_textbox(name="TextBox1",layout="Window")
    dlg.add_button(name="Button2",text="Set text",width=60,height=22,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_command(name="Button2",callfunc=onSetButtonClicked)

if __name__=='__main__':
    main()
