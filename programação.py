#IMPORTAR A BIBLIOTECA FLET
import flet as ft
#DEFINIR FUNÇÃO MAIN
def main(page:ft.Page):
    #DEFINE UMA TELA/INTERFACE
    texto=ft.Text(value="Chico se tu me quiseres")
    #ENVIAR CONTEUDO DE TEXTO PARA A INTERFACE
    page.add(texto)
    #FIM DA FUNÇÃO MAIN
ft.app(target=main)
#PIP INSTALL FLET
#FLET RUN (PASTA)