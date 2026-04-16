# Title:   Home.CopyToClipboard()
# Desc:    Save the current display window of Jupiter to the clipboard
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-command/home/Home.CopyToClipboard
# ---
copy = Home.CopyToClipboard(bWhiteBG=False,  # [hl]
                            bTransparentBG=False,  # [hl]
                            bFixedSize=False,  # [hl]
                            iWidth=1200,  # [hl]
                            iHeight=900)  # [hl]

JPT.Debugger(copy)
