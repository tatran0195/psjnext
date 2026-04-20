# Title:   Home.Windows.FrameCancel()
# Desc:    Reset placement of document windows to the original.
# Version: 5.1.0
# Docs:    /docs/cli/5.1.0/psj-command/home/Home.Windows.FrameCancel
# ---
# Prepare 2 JPT documents
JPT.CreateNewDocument()
JPT.CreateNewDocument()
Home.Windows.TileHorizontal(iMode=0)

# Cancel to the full window display.
Home.Windows.FrameCancel()  # [hl]
