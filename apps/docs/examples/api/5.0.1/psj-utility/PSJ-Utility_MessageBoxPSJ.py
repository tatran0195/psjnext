# Title:   JPT.MessageBoxPSJ()
# Desc:    Show a Jupiter dialog (Information, Warning)
# Version: 5.0.1
# Docs:    /docs/cli/5.0.1/psj-utility/PSJ-Utility_MessageBoxPSJ
# ---
# Show an information message box
returnValue = JPT.MessageBoxPSJ("Test dialog",JPT.MsgBoxType.MB_INFORMATION_OK)  # [hl]
JPT.Debugger(returnValue) # Return a string object with value = OK
