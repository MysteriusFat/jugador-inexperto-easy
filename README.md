# Requests

## Options requests
creo que es para verificar que esta ip puede votar antes de cualquier cosa

```
curl 'https://votes.flowics.com/paul/public/votes/o/12416/5f492f838d6fc400476c40b5' \
-X OPTIONS \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0' \
-H 'Accept: */*' \
-H 'Accept-Language: es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3' \
--compressed -H 'Access-Control-Request-Method: POST' \
-H 'Access-Control-Request-Headers: content-type' \
-H 'Referer: https://viz.flowics.com/public/208b11a4a060fb0faee34f51e28ac1b4/5f342daf7e547780c73fecd7/live?fluid=true' \
-H 'Origin: https://viz.flowics.com' \
-H 'Connection: keep-alive' \
```
## Post requests
Es la requests que se hace cada vez que se quiere votar, en este caso es del jugador casanova

```bash
curl 'https://votes.flowics.com/paul/public/votes/o/12416/5f492f838d6fc400476c40b5' \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0' \
-H 'Accept: */*' \
-H 'Accept-Language: es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3' \
--compressed -H 'Referer: https://viz.flowics.com/public/208b11a4a060fb0faee34f51e28ac1b4/5f342daf7e547780c73fecd7/live?fluid=true' \
-H 'content-type: application/vnd.flowics.bulk.v1.avro+json' \
-H 'Origin: https://viz.flowics.com' \
-H 'Connection: keep-alive' \
-H 'TE: Trailers' \
--data-raw $'\x00\x00\x02\x02\x00\x00\x10$\x0467\x082259\n1241605f342daf7e547780c73fecd7\x00\x02\x98\x01https://www.cdf.cl/nacional/Vota-por-Jugador-Experto-Easy-20200828-0014.html\x00\x02\x98\x01Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0\x00\x00\x00\x00\x00\x00\x00\x00\x02\x06n18\x02\x0c\x0205f492f838d6fc400476c40b5\x00\x02.https://www.google.com/\x00\x00\x00\x04vb\x14production\x00\x00\x00\x02\x1a\xa4\x0cxI\xd9I\x8b\x8b\xa1g\x9b\x9f\x12\xff8\x02\xb0\xd2\xa2\x8c\xc5\xb2\xd8\x05\x02\x06\x0005f492f838d6fc400476c40b5\x02Hd80dd991-58b8-42e4-b5b8-4c6149dab9bc\x02\x00\x02\x1a\xa4\x0cxI\xd9I\x8b\x8b\xa1g\x9b\x9f\x12\xff8\x00'
```
```bash
curl 'https://votes.flowics.com/paul/public/votes/o/12416/5f492f838d6fc400476c40b5' \
-H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0' \
-H 'Accept: */*' \
-H 'Accept-Language: es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3' \
--compressed -H 'Referer: https://viz.flowics.com/public/208b11a4a060fb0faee34f51e28ac1b4/5f342daf7e547780c73fecd7/live?fluid=true' \
-H 'content-type: application/vnd.flowics.bulk.v1.avro+json' \
-H 'Origin: https://viz.flowics.com' \
-H 'Connection: keep-alive' \
-H 'TE: Trailers' \
--data-raw $'\x00\x00\x02\x02\x00\x00\x10$\x0467\x082259\n1241605f342daf7e547780c73fecd7\x00\x02\x98\x01https://www.cdf.cl/nacional/Vota-por-Jugador-Experto-Easy-20200828-0014.html\x00\x02\x98\x01Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0\x00\x00\x00\x00\x00\x00\x00\x00\x02\x06n18\x02\x0c\x0205f492f838d6fc400476c40b5\x00\x02.https://www.google.com/\x00\x00\x00\x04vb\x14production\x00\x00\x00\x02\x1a\xa4\x0cxI\xd9I\x8b\x8b\xa1g\x9b\x9f\x12\xff8\x02\xb0\xd2\xa2\x8c\xc5\xb2\xd8\x05\x02\x06\x0005f492f838d6fc400476c40b5\x02Hd80dd991-58b8-42e4-b5b8-4c6149dab9bc\x02\x00\x02\x1a\xa4\x0cxI\xd9I\x8b\x8b\xa1g\x9b\x9f\x12\xff8\x00'
```

## Get requests
Esta petcion se hace cada 5 segundos para ver los resultados

```bash
curl 'https://paul.flowics.com/paul/public/polls/12416/5f492f838d6fc400476c40b5?profile=interactive' -H 'User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:81.0) Gecko/20100101 Firefox/81.0' -H 'Accept: application/json' -H 'Accept-Language: es-CL,es;q=0.8,en-US;q=0.5,en;q=0.3' --compressed -H 'Referer: https://viz.flowics.com/public/208b11a4a060fb0faee34f51e28ac1b4/5f342daf7e547780c73fecd7/live?fluid=true' -H 'Origin: https://viz.flowics.com' -H 'Connection: keep-alive' -H 'If-None-Match: "05ab5be8d38b3b59165803129a2e7a138--gzip"' -H 'TE: Trailers'
```


## timestamp

1601837283033 ?
