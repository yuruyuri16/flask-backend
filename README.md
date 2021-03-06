# Base de datos 2 - PC4

| Integrantes |
|-|
| Antonio Toche |
| Miguel Yurivilca |

### Prerequisitos

Para macOS
```bash
brew install spatialindex
```

### Consideraciones para el knn-rtree

Borrar los archivos creados con las extensiones ```.dat``` y ```.idx```
cuando se realice una misma consulta por segunda vez

# Experimento 1

| Precision | ED | MD |
|-|-|-|
| K = 4 | 100% | 100% |
| K = 8 | 100% | 100% |
| K = 16 | 100% | 100% |

## Algoritmo

Se implemento un knn usando la distancia euclediana y la de manhattan.

Se itera cada encoding de las imagenes en ```data/``` y se compara con
el encoding de la imagen subida. Ya que los encodings de las imagen son
arreglos, podemos usar las siguientes formulas para calcular la distancia
de un vector de ```n``` dimensiones.

### Euclediana

![alt text](static/screenshots/euclidean.png)

### Manhattan

![alt text](static/screenshots/manhattan.png)

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


# Experimento 2

| Tiempo | knn-rtree | knn-secuencial |
|-|-|-|
| N = 104 | 0.106 | 0.009 |
| N = 212 | 0.239 | 0.020 |
| N = 343 | 0.400 | 0.032 |
| N = 420 | 0.550 | 0.038 |
| N = 529 | 0.692 | 0.049 |
| N = 650 | 1.029 | 0.058 |

## Algoritmo

Para knn-secuencial se usa el knn previo con distancia euclediana.

Para knn rtree se usa una estructura R tree donde se insertan los
```n``` encodings como dataset. Luego, se busca los k vecinos mas
cercanos al encoding de la imagen subida.

#### Evidencia

k = 3

Serena_Williams_0013.jpg, n = 104:
![alt text](static/screenshots/s7.png)

Serena_Williams_0013.jpg, n = 212:
![alt text](static/screenshots/s8.png)

Serena_Williams_0013.jpg, n = 343:
![alt text](static/screenshots/s9.png)

Serena_Williams_0013.jpg, n = 420:
![alt text](static/screenshots/s10.png)

Serena_Williams_0013.jpg, n = 529:
![alt text](static/screenshots/s11.png)

Serena_Williams_0013.jpg, n = 650:
![alt text](static/screenshots/s12.png)

### Directorio ```utils/read_images.py```

Para la guardar los vectores caracteristicos de cada persona en
memoria secundaria y no tener que computar los encodings de las
imagenes otra vez. Estos archivos en memoria secuandaria tienen la extension
```.bin```.
