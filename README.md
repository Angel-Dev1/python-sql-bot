# Python SQL Bot

Este proyecto es un bot diseñado para recuperar información de una base de datos SQL Server y exportarla a un archivo Excel. El bot está diseñado para funcionar sin interfaz de usuario y se centra en la robustez de las validaciones de datos.

## Estructura del Proyecto

```
python-sql-bot
├── src
│   ├── bot.py                # Punto de entrada del bot
│   ├── db
│   │   └── sql_server.py     # Funciones para conectarse a SQL Server
│   ├── export
│   │   └── excel_exporter.py # Funciones para exportar a Excel
│   ├── validation
│   │   └── validator.py      # Funciones para validar datos
│   └── utils
│       └── helpers.py        # Funciones auxiliares
├── requirements.txt          # Dependencias del proyecto
└── README.md                 # Documentación del proyecto
```

## Instalación

Para instalar las dependencias necesarias, asegúrate de tener `pip` instalado y ejecuta el siguiente comando en la raíz del proyecto:

```
pip install -r requirements.txt
```

## Uso

Para ejecutar el bot, simplemente corre el archivo `bot.py` desde la línea de comandos:

```
python src/bot.py
```

Asegúrate de que la configuración de conexión a la base de datos en `sql_server.py` esté correctamente configurada antes de ejecutar el bot.

## Contribuciones

Las contribuciones son bienvenidas. Si deseas mejorar el proyecto, por favor abre un issue o un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT.