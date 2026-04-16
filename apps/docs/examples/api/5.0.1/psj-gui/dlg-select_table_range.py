# Title:   dlg.select_table_range()
# Desc:    Select a specific range by position in the Table
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-gui/dlg-select_table_range
# ---
from pyjdg import *

def on_click_select(dlg):
    left=int(dlg.get_item_text(name="TextBox5"))
    top=int(dlg.get_item_text(name="TextBox7"))
    right=int(dlg.get_item_text(name="TextBox9"))
    bottom=int(dlg.get_item_text(name="TextBox11"))
    dlg.select_table_range(name="Table1",  # [hl:start]
        cell_range=TableCellRange(left=left,top=top,right=right,bottom=bottom))  # [hl:end]

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_table(name="Table1",rows=14,
        columns=["Heading1","Heading2","Heading3","Heading4","Heading5"],
        layout="Window",width=560,height=260)
    dlg.add_groupbox(name="GroupBox2",text="Position",layout="Window")
    dlg.add_layout(name="Layout3",orientation=orientation.horizontal,
        layout="GroupBox2")
    dlg.add_label(name="Label4",text="Left",layout="Layout3")
    dlg.add_textbox(name="TextBox5",layout="Layout3")
    dlg.add_label(name="Label6",text="Top",layout="Layout3")
    dlg.add_textbox(name="TextBox7",layout="Layout3")
    dlg.add_label(name="Label8",text="Right",layout="Layout3")
    dlg.add_textbox(name="TextBox9",layout="Layout3")
    dlg.add_label(name="Label10",text="Bottom",layout="Layout3")
    dlg.add_textbox(name="TextBox11",layout="Layout3")
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="Select",text="Select",
        width=80,height=30,layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.on_command(name="Select",callfunc=on_click_select)

if __name__=='__main__':
    main()
