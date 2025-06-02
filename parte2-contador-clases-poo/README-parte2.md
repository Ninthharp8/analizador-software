# Parte 2 – Contador de Clases y Métodos

Este módulo amplía el contador de líneas de código de la Parte 1. Se agregan capacidades para detectar clases y métodos en archivos fuente, y contabilizar sus líneas asociadas.

---

## 📌 Objetivo

Desarrollar una herramienta que:
- Cuente las **líneas totales del programa**.
- Cuente las **líneas por clase**.
- Cuente el **total de métodos**.
- Reutilice el contador de líneas de la Parte 1.

---

## 📦 Estructura del directorio

```
parte2-contador-clases/
├── src/                         # Código fuente
│   └── ContadorClases.java
├── pruebas/
│   ├── unitarias/
│   └── integracion/
├── clases.exe
├── documento-tecnico.pdf
└── README.md
```

---

## 🛠️ Ejecución

### 🖥️ Ejecutable (.exe)
```
./clases.exe ruta/al/archivo.java
```

### 🧑‍💻 Desde código fuente (Java)

1. Compilar:
   javac src/ContadorClases.java -d bin

2. Ejecutar:
   java -cp bin ContadorClases ruta/al/archivo.java

---

## 🔬 Pruebas

Incluye pruebas para verificar:
- Conteo correcto de clases.
- Conteo de métodos por clase.
- Cálculo total de líneas por clase.
- Compatibilidad con el análisis previo de líneas físicas/lógicas.

---

## 📄 Documentación

Consulta `documento-tecnico.pdf` para más detalles sobre:
- Diseño del sistema.
- Casos de prueba.
- Estándares utilizados.
- Roles del equipo.

---

## 🔁 Relación con otras fases

Este módulo amplía la funcionalidad de la Parte 1:
- [Parte 1: Contador de líneas de código](../parte1-contador-lineas/)
- [Parte 3: Comparador de versiones](../parte3-comparador-versiones/)
