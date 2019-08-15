tell application "System Preferences"
    reveal anchor "keyboardTab" of pane id "com.apple.preference.keyboard"
    activate
    tell application "System Events"
        tell application process "System Preferences"
            click checkbox "Use F1, F2, etc. keys as standard function keys" of tab group 1 of window 1
        end tell
    end tell
    quit
end tell

