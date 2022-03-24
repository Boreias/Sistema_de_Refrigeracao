import requests

from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image
from kivy.core.window import Window
from kivy.utils import get_color_from_hex
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.animation import Animation


Window.clearcolor = get_color_from_hex('#FFFFFF')


class TelaTemperaturaAtual(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaTemperaturaAtual, self).__init__(**kwargs)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)

        try:
            getTotal = requests.get('http://localhost:8000/HistoricoSensor/')
            tamanho = getTotal.json()



            self.logo = Image(source='imagens/logo.png', size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, opacity=0)
            self.add_widget(self.logo)

            self.temperatura = Label(text=str(tamanho[-1]['temperatura']), font_size=200, size_hint=(.5, .1),
                                     pos_hint={'center_x': .5, 'y': .50}, color=(0, 0, 0, 1), opacity=0)
            self.animacaoAparecer.start(self.temperatura)
            self.add_widget(self.temperatura)

            self.botaoVoltar = Button(text='Voltar', font_size=14, size_hint=(.35, .1),
                                      pos_hint={'center_x': .5, 'y': .12}, color='#FFFFFF', background_color='#00b8f5',
                                      opacity=0)
            self.botaoVoltar.on_press = self.Voltar
            self.animacaoAparecer.start(self.botaoVoltar)
            self.add_widget(self.botaoVoltar)

        except:
            self.imagem = Image(source='imagens/erro.png', opacity=1, pos_hint={'y': .2})
            self.animacaoAparecer.start(self.imagem)
            self.add_widget(self.imagem)

            self.botaoVoltarErro = Button(text='Voltar', font_size=14, size_hint=(.35, .1),
                                          pos_hint={'center_x': .5, 'y': .12}, color='#FFFFFF',
                                          background_color='#00b8f5', opacity=1)
            self.animacaoAparecer.start(self.imagem)
            self.botaoVoltarErro.on_press = self.VoltarErro
            self.add_widget(self.botaoVoltarErro)

    def Voltar(self):
        self.animacaoDesaparecer.start(self.temperatura)
        self.animacaoDesaparecer.start(self.botaoVoltar)
        self.animacaoDesaparecer.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())

    def VoltarErro(self):
        self.animacaoDesaparecer.start(self.imagem)
        self.animacaoDesaparecer.start(self.botaoVoltarErro)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())

class TelaAjusteTemperatura(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaAjusteTemperatura, self).__init__(**kwargs)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)

        try:
            self.resposta = requests.get('http://localhost:8000/Comando/1')
            intermediario = self.resposta.json()
            self.temperaturaAtual = int(intermediario['temperatura'])
            self.logo = Image(source='imagens/logo.png', size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, opacity=0)
            self.add_widget(self.logo)

            self.botaoAumenta = Button(background_normal='imagens/Cima.png', font_size=14, size_hint=(.35, .1),
                                       pos_hint={'center_x': .5, 'y': .80}, color='#FFFFFF', background_color='#00b8f5',
                                       opacity=0)
            self.botaoAumenta.on_press = self.aumentarTemperatura
            self.animacaoAparecer.start(self.botaoAumenta)
            self.add_widget(self.botaoAumenta)

            self.temperatura = Label(text=str(self.temperaturaAtual), font_size=200, size_hint=(.5, .1), pos_hint={'center_x': .5, 'y': .50}, color=(0, 0, 0, 1), opacity = 0)
            self.animacaoAparecer.start(self.temperatura)
            self.add_widget(self.temperatura)

            self.botaoDiminui = Button(background_normal='imagens/Baixo.png', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .23}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
            self.botaoDiminui.on_press = self.diminuirTemperatura
            self.animacaoAparecer.start(self.botaoDiminui)
            self.add_widget(self.botaoDiminui)

            self.botaoSalvar = Button(text='Salvar', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .12}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
            self.botaoSalvar.on_press = self.SalvarDados
            self.animacaoAparecer.start(self.botaoSalvar)
            self.add_widget(self.botaoSalvar)

            self.botaoVoltar = Button(text='Voltar', font_size= 14, size_hint=(.185, .08), pos_hint={'center_x': .85, 'y': .03}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
            self.botaoVoltar.on_press = self.Voltar
            self.animacaoAparecer.start(self.botaoVoltar)
            self.add_widget(self.botaoVoltar)

        except:
            self.imagem = Image(source='imagens/erro.png', opacity=1, pos_hint={'y': .2})
            self.animacaoAparecer.start(self.imagem)
            self.add_widget(self.imagem)

            self.botaoVoltarErro = Button(text='Voltar', font_size=14, size_hint=(.35, .1),
                                          pos_hint={'center_x': .5, 'y': .12}, color='#FFFFFF',
                                          background_color='#00b8f5', opacity=1)
            self.animacaoAparecer.start(self.imagem)
            self.botaoVoltarErro.on_press = self.VoltarErro
            self.add_widget(self.botaoVoltarErro)

    def Voltar(self):
        self.animacaoDesaparecer.start(self.botaoVoltar)
        self.animacaoDesaparecer.start(self.botaoSalvar)
        self.animacaoDesaparecer.start(self.botaoDiminui)
        self.animacaoDesaparecer.start(self.botaoAumenta)
        self.animacaoDesaparecer.start(self.temperatura)
        self.animacaoDesaparecer.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())

    def diminuirTemperatura(self):
        self.temperaturaAtual -= 1
        self.temperatura.text = str(self.temperaturaAtual)

    def aumentarTemperatura(self):
        self.temperaturaAtual += 1
        self.temperatura.text = str(self.temperaturaAtual)

    def SalvarDados(self):
        try:
            requests.put('http://localhost:8000/Comando/1', data={'temperatura': str(self.temperaturaAtual)})
            getTotal = requests.get('http://localhost:8000/HistoricoComandos/')
            tamanho = getTotal.json()
            requests.post('http://localhost:8000/HistoricoComandos/', data={'identificador': str(len(tamanho) + 1),'temperatura': str(self.temperaturaAtual)})
            popup = Popup(title='Resposta',content=Label(text='Temperatura Ajustada'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
            popup.open()
        except:
            popup = Popup(title='ERRO', content=Label(text='Não foi possível se conectar ao servidor'), pos_hint={'center_x': .5, 'center_y': .5}, size_hint=(.3, .3))
            popup.open()

    def VoltarErro(self):
        self.animacaoDesaparecer.start(self.imagem)
        self.animacaoDesaparecer.start(self.botaoVoltarErro)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())


class TelaOpcoes(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaOpcoes, self).__init__(**kwargs)

        self.logo = Image(source='imagens/logo.png', pos_hint={'y':.1})
        self.add_widget(self.logo)

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)
        self.animacaoAjustarLogo = Animation(size_hint=(.2, .2), pos_hint={'x': 0, 'y': .8}, duration=2)

        self.botao1 = Button(text='Ajustar Temperatura', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .25}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botao1.on_press = self.ajustarTemperatura
        self.animacaoAparecer.start(self.botao1)
        self.add_widget(self.botao1)

        self.botao2 = Button(text='Temperatura Atual', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .15}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botao2.on_press = self.temperaturaAtual
        self.animacaoAparecer.start(self.botao2)
        self.add_widget(self.botao2)


    def ajustarTemperatura(self):
        self.animacaoDesaparecer.start(self.botao1)
        self.animacaoDesaparecer.start(self.botao2)
        self.animacaoAjustarLogo.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaAjusteTemperatura())


    def temperaturaAtual(self):
        self.animacaoDesaparecer.start(self.botao1)
        self.animacaoDesaparecer.start(self.botao2)
        self.animacaoAjustarLogo.start(self.logo)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaTemperaturaAtual())


class TelaLogo(FloatLayout):
    def __init__(self, **kwargs):
        super(TelaLogo, self).__init__(**kwargs)

        self.logo = Image(source='imagens/logo.png', opacity=0, pos_hint={'y':.1})

        self.animacaoAparecer = Animation(opacity=1, duration=1.5)
        self.animacaoDesaparecer = Animation(opacity=0, duration=1)

        self.animacaoAparecer.start(self.logo)
        self.add_widget(self.logo)

        self.botao = Button(text='Entrar', font_size= 14, size_hint=(.35, .1), pos_hint={'center_x': .5, 'y': .25}, color='#FFFFFF', background_color='#00b8f5', opacity=0)
        self.botao.on_press = self.botaoPressionado
        self.animacaoAparecer.start(self.botao)
        self.add_widget(self.botao)

    def botaoPressionado(self):
        self.animacaoDesaparecer.start(self.botao)
        tela.root_window.remove_widget(tela.root)
        tela.root_window.add_widget(TelaOpcoes())


class SistemaRefrigeracao(App):
    def build(self):
        return TelaLogo()

if __name__ == '__main__':
    tela = SistemaRefrigeracao()
    tela.run()
