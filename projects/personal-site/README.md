# 🚀 Proyecto: Sitio Web Personal (Miguel Angel Carvajal)

Este proyecto tiene como objetivo crear una presencia digital profesional utilizando el stack tecnológico aprendido en el **Workshop 02 (Flask + Cloud Run)**, con un enfoque en diseño de alta gama y personalización profunda.

## 📋 Plan de Implementación

### 1. Concepto y Diseño
- **Estética**: Moderna, minimalista con toques de "Glassmorphism".
- **Paleta**: Dark Mode (Deep Black) con acentos en Indigo Vibrante.
- **Interactividad**: Micro-animaciones en hover y transiciones suaves.

### 2. Estructura de Datos (app.py)
Utilizaremos el modelo de diccionarios de Flask para manejar:
- **Perfil**: Bio profesional, Social Links, Títulos.
- **Proyectos**: Galería de trabajos realizados en AI Club Condesa.
- **Stack**: Visualización de habilidades técnicas (AI, Cloud, Dev).

### 3. Desarrollo Frontend
- **Layout**: Diseño responsivo primero (Mobile-First).
- **Componentes**: Hero section impactante, Grid de proyectos dinámico.
- **SEO**: Optimización de meta-tags y estructura semántica.

### 4. Despliegue (GCP)
- **Containerización**: Dockerfile optimizado basado en Python Slim.
- **Orquestación**: Google Cloud Run para escalabilidad automática.

---

## 💡 Notas Técnicas

### ¿Por qué usamos `venv`?
En este proyecto utilizamos un **Entorno Virtual (`venv`)** por las siguientes razones:
- **Aislamiento**: Evita conflictos entre las librerías de este sitio y otros proyectos de Python en tu sistema.
- **Reproducibilidad**: Facilita que otros desarrolladores instalen exactamente las mismas versiones de las dependencias.
- **Seguridad**: Permite instalar paquetes sin necesidad de permisos de administrador y sin riesgo de afectar el sistema operativo.

### Comandos Útiles
- **Crear entorno**: `python -m venv venv`
- **Activar (Windows)**: `.\venv\Scripts\activate`
- **Instalar dependencias**: `pip install -r requirements.txt`
