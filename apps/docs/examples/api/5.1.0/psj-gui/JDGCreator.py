# Title:   JDGCreator()
# Desc:    A Class to generate Dialog in Jupiter
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-gui/JDGCreator
# ---
from pyjdg import *

def main():
    dlg=JDGCreator(title="Jupiter Dialog",description="This is a dialog")  # [hl]
    dlg.generate_window()

if __name__=='__main__':
    main()
