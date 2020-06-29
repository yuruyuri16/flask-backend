# Base de datos 2 - PC4

# Prerequisitos

```bash
brew install spatialindex
```

# Consideraciones para el knn-rtree

Borrar los archivos creados con las extensiones ```.dat``` y ```.idx```
cuando se realice una misma consulta por segunda vez

| Precision | ED | MD |
|-|-|-|
| K = 4 | 100% | 100% |
| K = 8 | 100% | 100% |
| K = 16 | 100% | 100% |

#### Evidencia

Serena_Williams_0013.jpg, k=4, ed:
![alt text](static/screenshots/s1.png)

Serena_Williams_0013.jpg, k=4, md:
![alt text](static/screenshots/s2.png)

Serena_Williams_0013.jpg, k=8, ed:
![alt text](static/screenshots/s3.png)

Serena_Williams_0013.jpg, k=8, md:
![alt text](static/screenshots/s4.png)

Serena_Williams_0013.jpg, k=16, ed:
![alt text](static/screenshots/s5.png)

Serena_Williams_0013.jpg, k=16, md:
![alt text](static/screenshots/s6.png)


### Directorio ```utils/read_images.py```

Para la guardar los vectores caracteristicos de cada persona en
memoria secundaria y no tener que computar los encodings de las
imagenes otra vez. Estos archivos en memoria secuandaria tienen la extension
```.bin```.
