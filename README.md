# Spotify Repeated Tracks
Script escrito em Python para detectar se existem faixas com o mesmo nome em uma mesma playlist do Spotify.
O script faz uso das APIs oficial do Spotify.

## Como usar
### Sem Docker
Instalando as dependências:
```
$ pip install --no-cache-dir -r requirements.txt
```

Rodando:
```
$ python main.py <client_id> <client_secret> <playlist_id>
```

### Com Docker
Requer o Docker instalado em sua máquina. 

Construindo a imagem:
```
$ docker build -t srt .
```
Rodando:
```
$ docker run --rm srt <client_id> <client_secret> <playlist_id>
```