from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.scrollview import ScrollView

class Tarefas(BoxLayout):
	
	def adiciona(self, texto="Sem texto"):
		self.ids.box.add_widget(Tarefa(texto=texto))


class Tarefa(BoxLayout):
	def __init__(self, texto):
		super().__init__()
		
		self.ids.label.text = texto


class Appzao(App):
	def build(self):
		inst = Tarefas()
		
		for c in range(10): inst.adiciona(str(c))
		
		return inst
		
Appzao().run()