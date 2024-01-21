import PySimpleGUI as sg
from loteria_caixa import *



loterias = ['MegaSena', 'LotoFacil', 'Quina', 'LotoMania', 'TimeMania', 'DuplaSena', 'Federal', 'Loteca', 'DiadeSorte', 'SuperSet']    


# layout
def window():

    sg.theme('kayak')
    sg.TRANSPARENT_BUTTON = (sg.theme_background_color(), sg.theme_background_color())

    cel_0 = [[sg.Text('Loteria: ', font='serif 12'), sg.Combo(loterias,size=25, key='-LOTERIA-',
                                                              readonly=True, enable_events=True),
               sg.Text('Concurso: ', font='serif 12'), sg.In(font='arial 11', key='-CONCURSO-', 
                                                              size=4, enable_events=True)]]

    cel_1 = [[sg.Text('Resultado do sorteio', 
                        font='serif 12')],
             [sg.Text('', key='-GABARITO-', text_color='blue',font='arial 12',size=45)],]
    
    cel_2 = [[sg.Text('Aquivo com as apostas', font='serif 12')],
             [sg.In(key='-GAME-', text_color='blue', font='arial 11',size=41), sg.FileBrowse(size=5)],]
            
    coluna1 = [[sg.Frame('', layout=cel_0)],
               [sg.Frame('', layout=cel_1, key='-CEL1-', visible=False)], 
               [sg.Frame('', layout=cel_2)], 
               [sg.Submit(font='serif 13 italic' , size=(6,1), button_color=('white', 'green'))],]
    
    coluna2 = [[sg.B('Help', button_color=sg.TRANSPARENT_BUTTON, image_size=(15, 15), image_filename='question-sign-circles_41943.png', image_subsample=2, border_width=0)]]
    
    layout = [[sg.Col(coluna1, vertical_alignment='center', element_justification='center'),
               sg.Col(coluna2, vertical_alignment='top')]]
    return sg.Window("Contador da Loteria!", layout, size=(510, 250),finalize=True)


# process

def obter_numeros_sorteados():
    numero_concurso = int(values['-CONCURSO-'])
    loteria = values['-LOTERIA-']

    match loteria:
        case 'MegaSena':
            sortedos = MegaSena(numero_concurso).listaDezenas()
        case 'LotoFacil':
            sortedos = LotoFacil(numero_concurso).listaDezenas()
        case 'Quina':
            sortedos = Quina(numero_concurso)
        case 'LotoMania':
            sortedos = LotoMania(numero_concurso).listaDezenas()
        case 'TimeMania':
            sortedos = TimeMania(numero_concurso).listaDezenas()
        case 'DuplaSena':
            sortedos = DuplaSena(numero_concurso).listaDezenas()
        case 'Federal':
            sortedos = Federal(numero_concurso).listaDezenas()
        case 'DiadeSorte':
            sortedos = DiadeSorte(numero_concurso).listaDezenas()
        case 'SuperSet':
            sortedos = SuperSet(numero_concurso).listaDezenas()

    return sortedos


def solver(game_path):

    sorteados = obter_numeros_sorteados()

    with open(game_path, 'r') as jogos:
        
        cartela = [jogo[:-2] for jogo in jogos]

        result = ""
        c = 1
        for j in cartela:
    
            if j == '':
                continue

            jogo = j.split()
            numeros_acertados = [numero for numero in jogo if numero in sorteados]
            result += f"numero de acertos do jogo {c}: {len(numeros_acertados)} \n"
            c += 1
    
    return result


# window logic
win = window()

while True:
    win, event, values = sg.read_all_windows()

    if values['-LOTERIA-'] and values['-CONCURSO-'] != '':
        win['-CEL1-'].update(visible=True)
        numeros_sorteados = ', '.join(obter_numeros_sorteados())
        win['-GABARITO-'].update(numeros_sorteados)
    else:
        win['-GABARITO-'].update('')
        win['-CEL1-'].update(visible=False)



    if event == sg.WIN_CLOSED:
        break
    
    elif event == 'Submit':
        output = solver(game_path=values['-GAME-'])
        sg.popup(output, title='Total acertos')
    
    elif event == 'Help':
        mensagem = 'certifique-se de que os jogos da loteria contidos no aquivo estejam separados por espaço e tenha um "." no fim de cada linha'
        sg.popup(mensagem, image='question-sign-circles_41943.png')


window.close()