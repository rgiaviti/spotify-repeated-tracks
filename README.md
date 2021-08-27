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

## LICENSE
```
MIT License

Copyright (c) 2021 Ricardo Giaviti

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
