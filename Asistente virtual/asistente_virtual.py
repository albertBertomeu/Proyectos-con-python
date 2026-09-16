import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia


#escuchar nuestro micro y devolver el audio como texto

def trasformar_audio_texto():

    # almacenar recognizer en variable
    r = sr.Recognizer()
    #configurar el micro
    with sr.Microphone() as origen:
        #tiempo de espera
        r.pause_threshold = 0.8
    # informar que comenzo la grabacion
        print('ya puedes hablar')
        # guardar lo que escuche como audio
        audio = r.listen(origen)
        try:
             #buscar en google
            pedido = r.recognize_google(audio, language='es-es')

            # prueba de que pudo ingresar
            print('dijiste : ' + pedido)
            return pedido
        #en caso de que no comprenda
        except sr.UnknownValueError:
            # prueba de que no comprendio el audio
            print('ups , no entendí')

            # devolver error
            return 'sigo esperando'
        # en caso de no resolver el pedido

        except sr.RequestError:
            # prueba de que no comprendio el audio
            print('ups , no hay servicio')

            # devolver error
            return 'sigo esperando'
        # error inesperado

        except:
            # prueba de que no comprendio el audio
            print('ups , algo salió mal')

            # devolver error
            return 'sigo esperando'

# funcion para que el asistente pueda ser escuchado

def hablar (mensaje):

    # encender el motor de pyttsx3
    engine= pyttsx3.init()

    # pronunciar mensaje
    engine.say(mensaje)
    engine.runAndWait()


# informar el dia de la semana
def pedir_dia():
     # crear variable con datos de hoy
    dia = datetime.date.today()
    print(dia)

    # crear variable para el dia de semana
    dia_semana= dia.weekday()
    print(dia_semana)
    # diccionario con nombres de dias
    calendario = { 0:'Lunes',
                   1:'Martes',
                   2:'Miércoles',
                   3:'Jueves',
                   4:'Viernes',
                   5:'Sábado',
                   6:'Domingo'}
     #decir el dia de la semana
    hablar(f'hoy es {calendario[dia_semana]}')


# Informa que hora es

def pedir_hora():

    #crear una variable con datos de la hora
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos y {hora.second} segundos'
    #decir la hora
    hablar( hora)


# saludo inicial
def saludo_inicial():
    # crear variable con datos de hora
    hora = datetime.datetime.now()
    if hora.hour< 6 or hora.hour>20:
        momento = 'Buenas noches'
    elif 6 <= hora.hour < 13:
        momento ='Buen día'
    else:
        momento = 'Buenas tardes'
    # decir el saludo
    hablar(f'{momento}, hola soy Alberto, tu asistente personal. Por favor dime en que te puedo ayudar')

def pedir_cosas():
    # activar el saludo inicial
    saludo_inicial()
    comenzar = True
    while comenzar:
        # activar el micro y guardar el pedido en una string
        pedido= trasformar_audio_texto().lower()

        if 'abrir youtube' in pedido:
            hablar('con gusto , estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir navegador' in pedido:
            hablar(' claro que abriré el navegador')
            webbrowser.open('https://google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'busca en wikipedia' in pedido:
            hablar('buscando en wikipedia')
            pedido= pedido.replace('busca en wikipedia','')
            wikipedia.set_lang('es')
            resultado= wikipedia.summary(pedido,sentences=1 )
            hablar('wikipedia dice lo siguiente:')
            hablar(resultado)
            continue
        elif 'busca en internet' in pedido:
            hablar('ya busco en internet')
            pedido= pedido.replace('busca en internet','')

            pywhatkit.search(pedido)
            hablar('esto es lo que he encontrado')
            continue
        elif 'reproducir' in pedido:
            hablar('Buena idea ya reproduzco tu eleccion')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion= pedido.split('de')[-1].strip()
            cartera = {'apple':'AAPL','amazon':'AMZN','google':'GOOGL','oracle':'ORCL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada= yf.Ticker(accion_buscada)
                precio_actual= accion_buscada.info['regularMarketPrice']
                hablar(f'La he encontrado, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('perdón pero no la encontré')
                continue
        elif 'adiós' in pedido:
            hablar('me voy, hasta la proxima')
            break

pedir_cosas()












