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
| K = 4 | 100% |  |
| K = 8 |  |  |
| K = 16 |  |  |

#### Evidencia

Serena_Williams_0013.jpg, k=4, ed:
![alt text][static/screenshots/s1.png]

Serena_Williams_0013.jpg, k=4, md:
![alt text][https://github.com/yuruyuri16/flask-backend/blob/develop/static/screenshots/s2.png "S2"]

### Directorio ```utils/read_images.py```

Para la guardar los vectores caracteristicos de cada persona en
memoria secundaria y no tener que computar los encodings de las
imagenes otra vez. Estos archivos en memoria secuandaria tienen la extension
```.bin```.
