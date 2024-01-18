import PySimpleGUI as sg


# layout

def window():

    sg.theme('kayak')
    cel_1 = [
            [sg.Text('Digite os numeros sorteados separados por espaço \n Ex: "02 05 17 22 ... 53"', 
                     font='serif 12')],
            [sg.In(key='-GABARITO-', text_color='blue',font='arial 12',size=45)],
            ]
    
    cel_2 = [
            [sg.Text('Aquivo com as apostas', font='serif 12')],
            [sg.In(key='-GAME-', text_color='blue', font='arial 11',size=40), sg.FileBrowse()],
            ]
            
    coluna1 = [[sg.Frame('', layout=cel_1)], 
              [sg.Frame('', layout=cel_2)], 
              [sg.Submit(button_color=('white', 'green'))],]
    
    coluna2 = [[sg.B('h')]]
    
    layout = [[sg.Col(coluna1, vertical_alignment='center', element_justification='center'), 
               sg.Col(coluna2, vertical_alignment='top')]]
    return sg.Window("Contador da Loteria!", layout, size=(520, 230),finalize=True)


# process

# backend
def solver(sortedos, game_path):
    numeros_sorteados = sortedos.split()

    with open(game_path, 'r') as jogos:
        
        cartela = [jogo[:-2] for jogo in jogos]

        result = ""
        c = 1
        for j in cartela:
    
            if j == '':
                continue

            jogo = j.split()
            numeros_acertados = [numero for numero in jogo if numero in numeros_sorteados]
            result += f"numero de acertos do jogo {c}: {len(numeros_acertados)} \n"
            c += 1
    
    return result


# window logic
win = window()

while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED:
        break

    elif event == 'Submit':
        output = solver(sortedos=values['-GABARITO-'], game_path=values['-GAME-'])
        sg.popup(output, title='Total acertos')

window.close()