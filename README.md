# Spotify Repeated Tracks

Script escrito em Python para detetar se existem faixas similares em uma mesma _playlist_ do Spotify. 
O script usa as APIs oficial do Spotify e considera somente o nome da música para saber se ela é similar a 
outra música na mesma _playlist_. Isso é útil quando uma mesma música é colocada em diversos albuns diferentes. 
Falsos positivos podem acontecer quando artistas diferentes gravam a mesma música ou fazem _covers_.

Como esse script utiliza similaridade entre o nome das músicas, foi definido o limite de 85% de similaridade entre os
nomes que são checados. Isso significa que se os nomes de duas músicas forem "parecidos" em 85% ou mais, o nome dessas
músicas são considerados similares.

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

Requer o Docker instalado na sua máquina.

Construindo a imagem:

```
$ docker build -t srt .
```

Rodando:

```
$ docker run --rm srt <client_id> <client_secret> <playlist_id>
```
