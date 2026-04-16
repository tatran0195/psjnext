# Title:   dlg.on_textbox_input()
# Desc:    Bind a created function to a textbox component when its text is changed
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-on_textbox_input
# ---
from pyjdg import *
def on_input(dlg):
    text=dlg.get_item_text("TextBox2")
    if text=="1":
        return False
    else :
        print("Hello")
        return True
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_textbox(name="TextBox2",layout="Window")
    dlg.generate_window()
    dlg.on_textbox_input("TextBox2",on_input,True)  # [hl]
if __name__=='__main__':
    main()
