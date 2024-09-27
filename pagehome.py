from microdot import Microdot, Response, redirect
from display import saySomething
import urequests as requests
import ubinascii

app = Microdot()

#dados de autenticação do Spotify
client_id = ""
client_secret = ""
#dados de redirecionamento
redirect_uri = 'http://IP_DO_ASP:8000/callback'
url_api = 'http://IP_DA_API_FASTIFY:8000'
#escopos de permissão
scope = 'user-read-private user-read-email user-read-currently-playing app-remote-control streaming'
#variavel global
spotify_bearer_token = ""

def get_spotify_token(auth_code):
    url = 'https://accounts.spotify.com/api/token'
    
    #string de autenticação "Basic" e codificação base64
    auth_string = client_id + ':' + client_secret
    auth_base64 = ubinascii.b2a_base64(auth_string.encode()).decode().strip()
    
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'Basic ' + auth_base64
    }
    
    #dados da requisição
    data = 'grant_type=authorization_code&code=' + auth_code + '&redirect_uri=' + redirect_uri
    
    response = requests.post(url, headers=headers, data=data)
    
    #verificando se a resposta foi bem-sucedida
    if response.status_code == 200:
        response_json = response.json()
        token = response_json.get('access_token')
        response.close()
        return token
    else:
        print('Error:', response.text)
        response.close()
        return None
    

def get_playing_now(token):
    url = url_api + '/current-playing'
    headers = {
        'Authorization': 'Bearer ' + token
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response_json = response.json()
        track_name = response_json['item']['name']
        print("Nome da música atual:", track_name)
        saySomething("Playing " + track_name)

    else:
        print("Erro na requisição:", response.status_code)

    response.close()

    
def play_track():
    url = url_api + '/play-track'
    headers = {
        'Authorization': 'Bearer ' + spotify_bearer_token
    }

    requests.put(url, headers=headers)

    saySomething("Play")
    print("Play")

def pause_track():
    url = url_api + '/pause-track'
    headers = {
        'Authorization': 'Bearer ' + spotify_bearer_token
    }
    requests.put(url, headers=headers)

    saySomething("Pause")
    print("Pause")


callback_html = '''<!DOCTYPE html>
<html>
    <head>
        <title>Microdot Example Page</title>
        <meta charset="UTF-8">
        <script>
           async function pause() {
                await fetch('/pause', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
            }
            async function play() {
                await fetch('/play', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    }
                });
            }
            
        </script>
    </head>
    <body>
        <div>
            <h1>Spotify Callback</h1>
            <button onClick="pause()">Pause</button>
            <button onClick="play()">Play</button>
        </div>
    </body>
</html>
'''
    
@app.route('/')
async def home(request):
    #redireciona para a página de autorização do Spotify
    auth_url = f'https://accounts.spotify.com/authorize?response_type=code&client_id={client_id}&redirect_uri={redirect_uri}&scope={scope}'
    return redirect(auth_url)

@app.route('/callback')
async def callback(request):
    #obtém o código de autorização da URL
    auth_code = request.args.get('code')
    
    if auth_code:
        global spotify_bearer_token
        spotify_bearer_token = get_spotify_token(auth_code)

        if spotify_bearer_token:
            get_playing_now(spotify_bearer_token)
            
            return callback_html, 200, {'Content-Type': 'text/html'}
        else:
            return Response('Error obtaining token'), 500
            
    else:
        return Response('Authorization failed'), 400
    
@app.route('/pause', methods=['POST'])
async def pause(request):
    pause_track()
    return "", 200

@app.route('/play', methods=['POST'])
async def play(request):
    play_track()
    return "", 200

#inicia o servidor na porta 8000
app.run(port=8000)
