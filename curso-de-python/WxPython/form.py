
import wx
import data
'''
#primeira forma de criacao do formulario
aplicacao = wx.App()
frame = wx.Frame(None, -1, "teste")
frame.Show()
aplicacao.MainLoop()

#segundaforma de ciracao do formulario
from cProfile import label
from operator import pos
from wx import Size
class Formulario(wx.Frame):

    def __init__(self, parent, title):
        super(Formulario,self).__init__(parent, title=title, size=(800, 600))
       
        self.Centre()
        self.Show()
  

aplicacao = wx.App()
Formulario(None, "Testando WxPython")
aplicacao.MainLoop()
'''
#terceira forma de cricacao de formulario
class MenusPopup(wx.Menu):
    def __init__(self, parent):
        super(MenusPopup, self).__init__()
        self.parent = parent

        popupCliente = wx.MenuItem(self, wx.NewId(), "Clientes")
        self.AppendItem(popupCliente)
        self.Bind(wx.EVT_MENU, self.chamaCliente, popupCliente)
    
    def chamaCliente(self, event):
        print("Clicou no botao chama cliente")

class Formulario(wx.Frame):

    def __init__(self, *args, **kwargs):
        super(Formulario,self).__init__(*args, **kwargs)
        self.IniciaFormulario()

    def IniciaFormulario(self):
        self.SetTitle("Testando")
        self.SetSize((800, 600))   

        menuBar = wx.MenuBar()
        fileMenu = wx.Menu()
        sair = wx.MenuItem(fileMenu, 1, 'sairz\tCtrl+S')
        sair.SetBitmap(wx.Bitmap("sair.png"))

        fileMenu.AppendItem(sair)
        

        self.Bind(wx.EVT_MENU, self.OnQuit, id=1)
        
        menuBar.Append(fileMenu, '&Arquivo')
        self.SetMenuBar(menuBar)

        self.StatusBar = self.CreateStatusBar()
        self.StatusBar.SetStatusText("Desenvolvido por Marcus Vinicius "+data.retornaData())
        
        self.checkStatusBar = fileMenu.Append(wx.ID_ANY, "Barra de Status", kind=wx.ITEM_CHECK)
        self.checkToolBar = fileMenu.Append(wx.ID_ANY, "Tool Bar", kind=wx.ITEM_CHECK)
        fileMenu.Check(self.checkStatusBar.GetId(), True)
        fileMenu.Check(self.checkToolBar.GetId(), True)
        self.Bind(wx.EVT_MENU, self.BarraStatus, self.checkStatusBar)
        self.Bind(wx.EVT_MENU, self.MostrarToolBar, self.checkToolBar)

        self.toolbar = self.CreateToolBar()
        toolbarClientes = self.toolbar.AddLabelTool(wx.ID_ANY, '', wx.Bitmap('usuario.png'))
        self.toolbar.AddSeparator()
        toolbarSair = self.toolbar.AddLabelTool(wx.ID_EXIT, '', wx.Bitmap('sair.png'))
        self.toolbar.Realize()
        self.Bind(wx.EVT_TOOL, self.chamaCliente, toolbarClientes)
        self.Bind(wx.EVT_TOOL, self.OnQuit, toolbarSair)

        #chama botao direito do mouse
        self.Bind(wx.EVT_RIGHT_DOWN, self.chamaBotaoDireito)

        self.Centre()
        self.Show()

    def chamaBotaoDireito(self, event):
        self.PopupMenu(MenusPopup(self), event.GetPosition())

    
    def chamaCliente(self, event):
        print("Clicou no botao chama cliente")
    
    def BarraStatus(self, event):
        if self.checkStatusBar.IsChecked():
            self.StatusBar.Show()
        else:
            self.StatusBar.Hide()
    
    def MostrarToolBar(self, event):
        if self.checkToolBar.IsChecked():
            self.toolbar.Show()
        else:
            self.toolbar.Hide()
    
    def OnQuit(self, e):
        self.Close()

def main():
    aplicacao = wx.App()
    Formulario(None)
    aplicacao.MainLoop()

if __name__ == '__main__':
    main()
