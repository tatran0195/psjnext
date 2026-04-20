# Title:   dlg.set_item_font()
# Desc:    Set font properties to the text inside the component
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/dlg-set_item_font
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Dialog",resizable=True,validation=True)
    dlg.add_textbox(name="TextBox2",layout="Window", width=350, 
        height=35, text_color=255)
    font_TextBox2=PSJFont()
    font_TextBox2.size=18
    font_TextBox2.bold=True
    font_TextBox2.italic=True
    font_TextBox2.underline=True
    font_TextBox2.strikeout=False
    dlg.add_hlayout(name="footer",layout="Window")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.add_button(name="ButtonOk",text="Ok",layout="footer")
    dlg.add_button(name="ButtonCancel",text="Cancel",layout="footer")
    dlg.add_space(orientation="horizontal",layout="footer")
    dlg.generate_window()
    dlg.set_item_font(name="TextBox2",font=font_TextBox2)  # [hl]
    dlg.set_item_text(name="TextBox2", text="This is a sample text")
if __name__=='__main__':
    main()
