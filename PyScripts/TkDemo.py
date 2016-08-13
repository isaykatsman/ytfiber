import wx

app = wx.PySimpleApp()
progressMax = 100
dialog = wx.ProgressDialog("A progress box", "Time remaining", progressMax,
        style=wx.PD_CAN_ABORT)
keepGoing = True
count = 0
while keepGoing and count < progressMax:
    count = count + 1
    wx.Usleep(200)
    keepGoing = dialog.Update(count, "Updated")

dialog.Destroy()