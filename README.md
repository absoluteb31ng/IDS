# IDS
Un proyecto que se basa en la aplicacion de un IDS sencillo que utiliza python y js

# Servidor de Alertas y Sistema de Detección de Intrusiones (IDS)

Este conjunto de scripts implementa un servidor de alertas y un Sistema de Detección de Intrusiones (IDS) para monitorear el tráfico de red y detectar posibles amenazas o comportamientos no autorizados.

## Características
- **IDS.js**.- Este archivo utiliza tecnologia de node.js, este codigo se integra para la parte de la aplicacion que maneja la logica de alto nivel y la interaccion con el usuario
- **IDS_py**-. Este usa python3 para la captura y analisis de paquetes
## Requisitos

- Python 3.x
- Scapy
- Node.js
- pcap (paquete npm)

## Uso

1. Asegúrate de tener Python y Node.js instalados en tu sistema.
2. Instala el paquete `pcap` para Node.js utilizando npm:

```bash
npm install pcap
```
3. Ejecutar primero el servidor de Node.js
```
node server.js
```
4. Ejecutar el scrip de python
```
python IDS_py.py
```

# Dato
Pueden extender ambos scripts según sus necesidades, agregando más funcionalidad de análisis en Python y más formas de manejar y notificar alertas en Node.js
