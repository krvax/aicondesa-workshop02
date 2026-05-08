# Workshop 06 — Lab 01: Create No-Code Agents with Gemini Enterprise

Este laboratorio se enfoca en la creación de agentes sin código utilizando las capacidades de **Gemini Enterprise** y el **Agent Registry** en Google Cloud.

## 🎯 Objetivos

- Habilitar las APIs necesarias para Gemini Enterprise y Agent Registry.
- Configurar el entorno de Discovery Engine.
- Crear y registrar agentes inteligentes.

## 🛠️ APIs Habilitadas

Se han habilitado los siguientes servicios para este laboratorio:
- `discoveryengine.googleapis.com`
- `agentregistry.googleapis.com`
- `iap.googleapis.com`
- `cloudapiregistry.googleapis.com`
- `aiplatform.googleapis.com`
- `iam.googleapis.com`

---

## 🚀 Paso 1: Configuración de Gemini Enterprise

Sigue estos pasos para configurar tu suscripción de prueba y tu aplicación de tenant:

### 1.1 Crear suscripción de prueba
Puedes probar Gemini Enterprise por 30 días con una cuenta de facturación activa.

1.  Navega a la consola de **Gemini Enterprise**.
2.  Verás una pantalla de bienvenida:
    ![Bienvenida a Gemini Enterprise](./assets/welcome_screen.png)
3.  Haz clic en el botón **Start 30 day trial** (o "Iniciar la prueba gratuita de 30 días").
4.  Aparecerá un mensaje emergente para habilitar la API necesaria (Discovery Engine); confirma la activación.

### 1.2 Crear la Aplicación de Tenant
Gemini Enterprise te permite crear aplicaciones en diversas regiones.

1.  Ve a la página de **Gemini Enterprise**.
2.  Haz clic en el botón **Create app** en la parte superior.
3.  Se abrirá el formulario de creación:
    ![Formulario de Creación de App](./assets/create_app_screen.png)
4.  **Nombre de la app**: El sistema genera uno por defecto, pero puedes personalizarlo.
5.  **Ubicación**: Se recomienda elegir la ubicación **global (Global)** si no tienes requisitos específicos de residencia de datos.
6.  Haz clic en **Crear**.

Una vez completado, tu aplicación de tenant de Gemini Enterprise estará lista para usarse.

---

## ⚙️ Paso 2: Configurar la Aplicación de Gemini Enterprise

En este paso configurarás la identidad, las funciones del diseñador y la observabilidad.

### 2.1 Configurar Identidad
Esto permitirá usar Google Identity para iniciar sesión en la aplicación.

1.  Regresa a la página de inicio de **Gemini Enterprise**.
2.  En el menú de la izquierda, haz clic en **Settings** (Configuración).
3.  Ve a la pestaña **Authentication**.
4.  Haz clic en el icono del lápiz junto a la región `global`.
5.  Selecciona **Google Identity** como el proveedor de identidad.
6.  Haz clic en **Save**.

### 2.2 Configurar Funciones y Observabilidad
Habilitaremos el Diseñador de Agentes y las opciones de compartido.

1.  Haz clic en el enlace **Apps** en el menú de la izquierda.
2.  Haz clic en el nombre de tu aplicación (ej. `gemini-enterprise-1778209095308`).
3.  Haz clic en **Configurations** en el menú izquierdo.
4.  En la pestaña **Feature Management**, habilita lo siguiente:
    - [x] **Enable agent Designer**
    - [x] **Enable session sharing**
    - [x] **Enable agent sharing**
    - *(Opcional)* Habilita los modelos **Gemini 3 Flash** o **Gemini 3.1 Pro**.
5.  Ve a la pestaña **Observability** y habilita:
    - [x] **Enable instrumentation of OpenTelemetry traces and logs**
    - [x] **Enable logging of prompt inputs and response outputs**
6.  Haz clic en **Save**.

---

## 🐍 Paso 3: Crear el Agente (Camino Alternativo - Agent Platform)

Si el "Agent Designer" visual de Gemini Enterprise está bloqueado por falta de una configuración de Organización/Identidad corporativa, utilizaremos la **Plataforma de Agentes de Vertex AI** (el "motor" pro-code).

### 3.1 Acceso a la Plataforma de Agentes
1. En la consola de Google Cloud, busca **Vertex AI**.
2. En el menú lateral, selecciona **Agent Platform** (o Plataforma de Agentes).
3. Haz clic en **Agent Garden** para ver las plantillas disponibles.

### 3.2 Implementación mediante Cloud Shell
Para saltar las restricciones de la interfaz, usaremos un "Starter Pack" oficial de Google desde la terminal.

1. Abre la **Cloud Shell** (icono `>_` arriba a la derecha).
2. Ejecuta el siguiente comando maestro para crear, instalar y registrar tu agente:

```bash
# Define el nombre (máximo 26 caracteres)
export AGENT_NAME=coatl-finanzas-${RANDOM}

# Crea e implementa el agente
uvx agent-starter-pack==0.15.4 create ${AGENT_NAME} \
  -d agent_engine -ag -a adk@financial-advisor && \
  cd ${AGENT_NAME} && \
  make install && \
  make backend && \
  make register-gemini-enterprise
```

---

## 📝 Configuración Sugerida (Agente Cóatl IA)

Utiliza estos parámetros para personalizar tu agente una vez desplegado:

| Campo | Valor |
| :--- | :--- |
| **Nombre** | Agente Cóatl IA |
| **Objetivo** | Proveer análisis experto en tecnología, deportes y finanzas para la comunidad Cóatl. |
| **Tono** | Profesional, amigable y motivador. |

**Instrucciones del Sistema (System Prompt):**
> "Eres el Agente Cóatl IA, un consultor experto diseñado para asistir a los miembros de Cóatl. Tienes conocimiento profundo en: Tecnología (IA, Software), Deportes (Resultados, Estrategia) y Finanzas (Mercados, Inversiones). Si te preguntan algo fuera de estos temas, redirige educadamente a tu especialidad."

---

## 🏆 Guía de Supervivencia y Éxito (Workshop 06)

Este documento resume la jornada técnica para desplegar el **Agente Cóatl Finanzas**, superando obstáculos de configuración y facturación en Google Cloud.

### 🏗️ 1. El Desafío: El "Muro" de la Organización
Al intentar usar el **Agent Designer (No-Code)** de Gemini Enterprise, nos encontramos con un bloqueo: el sistema exige una Identidad de Organización configurada.
- **Síntoma**: El chat de creación de agentes no activaba el editor visual.

### 🛠️ 2. La Solución: El Camino "Pro-Code"
Usamos la **Plataforma de Agentes de Vertex AI** y el **Agent Starter Pack** de Google desde la **Cloud Shell** para saltar las restricciones de la interfaz.

**Comando Maestro:**
```bash
export AGENT_NAME=coatl-finanzas-${RANDOM}
uvx agent-starter-pack==0.15.4 create ${AGENT_NAME} -d agent_engine -ag -a adk@financial-advisor
cd ${AGENT_NAME} && make install && make backend && make register-gemini-enterprise
```

### 🚀 3. El Resultado Final
El agente se registró exitosamente y ya es funcional en la Web App de Gemini Enterprise.
- **ID del Agente**: `8544371628222189320`
- **Capacidad**: Análisis financiero profesional y orquestación de sub-agentes.

**¡Misión Cumplida!** 🐍🔥🚀

---

## 🌐 Cómo Acceder y Compartir el Agente

Tras las pruebas en vivo, confirmamos que el URL de acceso para una instancia corporativa sigue este patrón:

`https://vertexaisearch.cloud.google.com/home/cid/<CUSTOMER_ID>/r/agent/<AGENT_ID>`

*   **Tu Agent ID**: `8544371628222189320`
*   **Tu Customer ID (CID)**: `947f744a-0690-499b-82a5-22d91d67b103`

---

## 🚀 Siguientes Pasos: ¿Cómo hacerlo 100% Público?

Actualmente, el link directo requiere que el usuario esté logueado en la consola. Para que sea accesible para cualquier visitante de tu sitio personal (sin login), la estrategia recomendada es:

1.  **Configurar Integración**: En la consola de GCP, ve a **Integración > Widget de Chat**.
2.  **Habilitar Acceso No Autenticado**: Activa la opción para que el widget sea público.
3.  **Embeber en HTML**: Copia el código `<script>` generado y pégalo en el `index.html` de tu `personal-site`.
4.  **Whitelist**: Asegúrate de añadir el dominio `personal-site-383578626035.us-central1.run.app` a la lista de dominios permitidos en la configuración de seguridad del agente.

---

## ⚠️ Consideraciones de Acceso Público

¿Sería una locura hacerlo público? Aquí un análisis rápido para decidir:

| Aspecto | Consideración | Riesgo |
| :--- | :--- | :--- |
| **Costos** 💰 | Gemini Enterprise consume créditos/dinero por sesión. Un agente público sin control puede agotar tu presupuesto. | **Alto** |
| **Seguridad** 🔒 | El agente tiene acceso a tu System Prompt y posibles herramientas (Tools). | **Medio** |
| **Identidad** 🆔 | Por defecto, requiere cuenta de Google. Abrirlo a "cualquiera" requiere desactivar IAP o usar un Widget externo. | **Bajo** |

**Recomendación**: Mantén el acceso restringido a cuentas autorizadas (vía Google Identity) mientras esté en fase de prueba. Si deseas hacerlo público, considera implementar cuotas de uso (quotas) en GCP.

---

## 📚 Recursos y Referencias

Para profundizar en la ingeniería de agentes y el ecosistema de IA:

*   **Documentación Oficial**: [Gemini Enterprise Docs](https://docs.cloud.google.com/gemini/enterprise/docs)
*   **Google Cloud Next '26**: [Codelab: Run and Share Agents](https://developers.google.com/profile/badges/events/cloud/next/2026/codelab/run-and-share-agents/award)
*   **MLflow**: [Plataforma para el ciclo de vida de ML](https://mlflow.org/)
*   **Claude Plugins**: [Ralph Loop](https://claude.com/plugins/ralph-loop)
*   **Ingeniería de Agentes**: [Agent Harness Engineering por Addy Osmani](https://addyosmani.com/blog/agent-harness-engineering/)

---

## 🙏 Agradecimientos

Un agradecimiento especial a **AI Condesa** por el espacio, la comunidad y el apoyo constante para explorar las fronteras de la Inteligencia Artificial Generativa.

---
> *Este laboratorio es parte de la serie de talleres de AI Club Condesa.*
