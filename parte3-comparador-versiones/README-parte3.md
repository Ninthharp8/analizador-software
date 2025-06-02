# Parte 3 – Comparador de Versiones de Código

Este módulo implementa una herramienta que compara dos versiones de un archivo fuente para detectar líneas añadidas, borradas y modificadas. Integra funcionalidades de análisis de líneas, clases y métodos de las fases anteriores.

---

## 📌 Objetivo

Desarrollar una herramienta que:
- Compare dos versiones del mismo archivo.
- Identifique líneas:
  - Originales (no modificadas)
  - Añadidas
  - Borradas
- Cuente líneas de cambio y etiquete con comentarios.
- Mantenga el conteo por clases, métodos y líneas del programa.

---

## 📦 Estructura del directorio

```
parte3-comparador-versiones/
├── src/
│   └── ComparadorVersiones.java
├── pruebas/
│   ├── unitarias/
│   └── integracion/
├── comparador.exe
├── documento-tecnico.pdf
└── README.md
```

---

## 🛠️ Ejecución

### 🖥️ Ejecutable (.exe)
```
./comparador.exe ruta/archivo_antiguo.java ruta/archivo_nuevo.java
```

### 🧑‍💻 Desde código fuente (Java)

1. Compilar:
   javac src/ComparadorVersiones.java -d bin

2. Ejecutar:
   java -cp bin ComparadorVersiones archivo1.java archivo2.java

---

## 🔬 Pruebas

Incluye pruebas para:
- Detección precisa de líneas añadidas/borradas.
- Manejo de líneas reubicadas (se consideran añadidas + borradas).
- Identificación de modificaciones menores.
- Etiquetado automático con comentarios.
- Validación de métricas heredadas: clases, métodos, líneas.

---

## 📄 Documentación

Consulta `documento-tecnico.pdf` para:
- Descripción de criterios de comparación.
- Estándares de formato (líneas ≤ 80 caracteres).
- Casos de prueba y decisiones de diseño.

---

## 🔁 Relación con otras fases

Este módulo depende de:
- [Parte 1: Contador de líneas de código](../parte1-contador-lineas/)
- [Parte 2: Contador de clases y métodos](../parte2-contador-clases/)
