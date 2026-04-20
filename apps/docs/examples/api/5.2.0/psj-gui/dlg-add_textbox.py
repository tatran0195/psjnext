# Title:   dlg.add_textbox()
# Desc:    Add a Textbox to the creating dialog
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-add_textbox
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",include_apply=False)
    dlg.add_layout(name="Layout2",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label3",text="String Type",width=100,text_halign="left",text_valign="top",layout="Layout2")
    dlg.add_textbox(name="TextBox4",width=150,height=25,readonly=True,  # [hl:start]
        text="TechnoStar",type="string",text_align="left",layout="Layout2")  # [hl:end]
    dlg.add_layout(name="Layout6",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label7",text="String Type",width=100,text_halign="left",text_valign="top",layout="Layout6")
    dlg.add_textbox(name="TextBox8",width=150,height=25,readonly=False,  # [hl:start]
        text="12345",type="string",bk_color=16711168,text_color=255,text_align="left",layout="Layout6")  # [hl:end]
    dlg.add_layout(name="Layout9",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label10",text="Integer Type",width=100,text_halign="left",text_valign="top",layout="Layout9")
    dlg.add_textbox(name="TextBox11",width=150,height=25,readonly=False,  # [hl:start]
        text="TechnoStar",type="integer",text_align="center",layout="Layout9")  # [hl:end]
    dlg.add_layout(name="Layout12",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label13",text="Integer Type",width=100,text_halign="left",text_valign="top",layout="Layout12")
    dlg.add_textbox(name="TextBox14",width=150,height=25,readonly=True,  # [hl:start]
        text="12345",bk_color=65535,text_color=255,type="integer",text_align="center",layout="Layout12")  # [hl:end]
    font_TextBox14=PSJFont()
    font_TextBox14.size=12
    font_TextBox14.bold=True
    font_TextBox14.italic=False
    font_TextBox14.underline=True
    font_TextBox14.strikeout=False
    dlg.set_item_font(name="TextBox14",font=font_TextBox14)
    dlg.add_layout(name="Layout15",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label16",text="Double Type",width=100,text_halign="left",text_valign="top",layout="Layout15")
    dlg.add_textbox(name="TextBox17",width=150,height=25,readonly=False,  # [hl:start]
        text="TechnoStar",type="double",text_align="right",layout="Layout15")  # [hl:end]
    dlg.add_layout(name="Layout18",orientation=orientation.horizontal,layout="Window")
    dlg.add_label(name="Label19",text="Double Type",width=100,text_halign="left",text_valign="top",layout="Layout18")
    dlg.add_textbox(name="TextBox20",width=150,height=25,readonly=True,  # [hl:start]
        text="12345.123",type="double",text_align="right",layout="Layout18")  # [hl:end]
    font_TextBox20=PSJFont()
    font_TextBox20.size=12
    font_TextBox20.bold=False
    font_TextBox20.italic=True
    font_TextBox20.underline=True
    font_TextBox20.strikeout=False
    dlg.set_item_font(name="TextBox20",font=font_TextBox20)
    dlg.generate_window()

if __name__=='__main__':
    main()
