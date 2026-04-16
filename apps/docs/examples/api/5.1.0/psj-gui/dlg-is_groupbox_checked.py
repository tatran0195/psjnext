# Title:   dlg.is_groupbox_checked()
# Desc:    Check the state of a GroupBox's checkbox
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-is_groupbox_checked
# ---
from pyjdg import *
def on_group_checked(dlg,checked):
    if checked :
        print("checked")
    else:
        print("unchecked")
    print("get checked status==", str(dlg.is_groupbox_checked("GroupBox2")))  # [hl]
def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_groupbox(name="GroupBox2",text="GroupBox",layout="Window")
    dlg.set_groupbox_checked(name="GroupBox2",checked=False)
    dlg.add_button(name="Button3",text="Button",width=60,height=22,bk_color=15790320,layout="GroupBox2")
    dlg.generate_window()
    dlg.on_groupbox_checked("GroupBox2",on_group_checked)
if __name__=='__main__':
    main()
