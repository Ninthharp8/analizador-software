# Parte 1 – Contador de Líneas de Código

Este módulo implementa un programa capaz de contar las líneas físicas y lógicas de código en un archivo fuente, omitiendo comentarios y líneas en blanco, siguiendo un estándar de conteo definido.

---

## 📌 Objetivo

Desarrollar una herramienta que:
- Cuente **líneas físicas**: todas las líneas del archivo.
- Cuente **líneas lógicas**: líneas de código significativas, omitiendo comentarios y líneas vacías.

---

## 📦 Estructura del directorio

```
parte1-contador-lineas/
├── src/                         # Código fuente
│   └── ContadorLineas.java
├── pruebas/                    # Pruebas
│   ├── unitarias/
│   └── integracion/
├── contador.exe                # Ejecutable compilado
├── documento-tecnico.pdf       # Documentación formal
└── README.md                   # Este archivo
```

---

## 🛠️ Ejecución

Puedes ejecutar el programa desde línea de comandos o usar el ejecutable directamente:

### 🖥️ Ejecutable (.exe)
```
./contador.exe ruta/al/archivo.java
```

### 🧑‍💻 Desde código fuente (Java)

1. Compilar:
   javac src/ContadorLineas.java -d bin

2. Ejecutar:
   java -cp bin ContadorLineas ruta/al/archivo.java

---

## 🔬 Pruebas

Se realizaron pruebas unitarias y de integración en la carpeta `pruebas/`, que validan:

- El correcto conteo de líneas físicas y lógicas.
- El manejo de comentarios y líneas vacías.

---

## 📄 Documentación

Consulta `documento-tecnico.pdf` para más detalles sobre:
- Estándar de conteo utilizado.
- Ejemplos de uso.
- Casos de prueba.
- Roles del equipo.

---

## 🔁 Relación con otras fases

Este módulo es la base de las siguientes partes:
- [Parte 2: Contador de clases y métodos](../parte2-contador-clases/)
- [Parte 3: Comparador de versiones](../parte3-comparador-versiones/)
