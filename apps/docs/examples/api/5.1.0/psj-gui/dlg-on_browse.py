# Title:   dlg.on_browse()
# Desc:    Bind a created def function to a file/folder Browser component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-on_browse
# ---
from pyjdg import *

def on_browse_clicked(dlg,path_list):
    print(path_list[0])

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_browser(name="Browser2",mode="file",file_filter="All Files(*.*)",layout="Window")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_browse(name="Browser2",callfunc=on_browse_clicked)  # [hl]

if __name__=='__main__':
    main()
