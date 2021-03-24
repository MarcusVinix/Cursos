
import wx
from cProfile import label
from operator import pos
class Formulario(wx.Frame):

    def __init__(self, parent, title):
        super(Formulario,self).__init__(parent, title=title, size=(800, 600))
        #posicionar na tela
        #self.Move((400, 100))
        panel = wx.Panel(self)
        botaoSair = wx.Button(panel, label="Sair", pos=(50, 50), size=(40, 40))
        self.Bind(wx.EVT_BUTTON, self.sair, botaoSair)

        botaoImprimir = wx.Button(panel, label="Imprimir", pos=(150, 50), size=(80, 40))
        self.Bind(wx.EVT_BUTTON, self.imprimir, botaoImprimir)

        wx.StaticText(panel, -1, "WxPython", pos=(50, 100))

        labelTitulo = wx.StaticText(panel, -1, "Titulo WxPython", (50, 150),(200, -1), wx.ALIGN_CENTER)
        labelTitulo.SetForegroundColour("Blue")
        labelTitulo.SetBackgroundColour("yellow")

        wx.StaticText(panel, -1, "Digite o nome: ",(50, 200),(100, -1))
        self.editNome = wx.TextCtrl(panel, -1, "Marcus", (160, 200), (100, -1))
        botaoNome = wx.Button(panel, label="Executa", pos=(280, 200), size=(90, -1))
        self.Bind(wx.EVT_BUTTON, self.executa, botaoNome)

        menuBar = wx.MenuBar() #barra de menus
        menuCadastro = wx.Menu()
        menuCadastro.Append(wx.ID_ANY, "Clientes")
        menuCadastro.Append(wx.ID_ANY, "Fornecedores")
        menuCadastro.Append(wx.ID_ANY, "Cidades")
        menuCadastro.AppendSeparator()
        
        menuEstoque = wx.Menu()
        menuEstoque.Append(wx.ID_ANY, "Entrada de Mercadorias")
        menuEstoque.Append(wx.ID_ANY, "Saida de Mercadorias")

        menuCadastro.AppendMenu(wx.ID_ANY, "Estoque", menuEstoque)

        sair = menuCadastro.Append(wx.ID_EXIT, "Sair")
        self.Bind(wx.EVT_MENU, self.sair, sair)
        
        menuArquivo = wx.Menu()
        menuArquivo.Append(wx.ID_NEW, "&Novo Arquivo")
        menuArquivo.Append(wx.ID_OPEN, "&AbrirArquivo")
        menuArquivo.Append(wx.ID_SAVE, "&Salvar Arquivo")

        menuBar.Append(menuCadastro, "Cadastro")             
        menuBar.Append(menuArquivo, "Arquivo Texto")
         
        self.SetMenuBar(menuBar) #para aparecer a barra de menus
        
        self.Centre()
        self.Show()
    
    def executa(self, event):
        print(self.editNome.GetValue())
        self.editNome.SetValue("Marcus Vinicius")

    def sair(self, event):
        self.Close(True)

    def imprimir(self, event):
        print("HELLO")

aplicacao = wx.App()
Formulario(None, "Testando WxPython")
aplicacao.MainLoop()
