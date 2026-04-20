# Title:   dlg.get_item_text()
# Desc:    Get text inside the component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-get_item_text
# ---
from pyjdg import *
def onGetButtonClicked(dlg):
    print(dlg.get_item_text(name="TextBox1"))  # [hl]

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_textbox(name="TextBox1",layout="Window")
    dlg.add_button(name="Button2",text="Get text",width=60,height=22,layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_command(name="Button2",callfunc=onGetButtonClicked)

if __name__=='__main__':
    main()
