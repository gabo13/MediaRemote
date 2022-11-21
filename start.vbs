Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c C:\Users\horva\PycharmProjects\htmlserver\start.cmd"
oShell.Run strArgs, 0, false