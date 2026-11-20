# Trabajo Práctico Integrador - Gestión de Países

**Materia:** Programación 1  
**Tecnología:** Python 3.x  
**Fecha de Entrega:** 19/11/2026  

---

## 👥 Integrantes del Equipo
- **Agustín Padilla** - Legajo: `55234`
- **Lucas Grzona** - Legajo: `55190`

---

## 📌 Links del Proyecto
- **Repositorio en GitHub:** https://github.com/Agustin678X/UTN_Programacion_1_Trabajo_Pr-ctico_Integrador.git
- **Video Demostrativo:** https://drive.google.com/file/d/1ZvsgTozrPlctWfCm688oinGEqo1ckfNS/view?usp=sharing
- **Informe Académico (PDF):** `Informe_TPI_Programacion_1.pdf` (incluido en la raíz del proyecto)

---

## 📝 Descripción
Aplicación interactiva de consola desarrollada en Python 3 para administrar información sobre países a partir de un archivo CSV. El sistema permite realizar operaciones de alta, modificación, búsqueda, filtrado, ordenamiento y consulta de estadísticas descriptivas, garantizando la persistencia de los datos en disco.

---

## 📁 Estructura del Proyecto
- `main.py`: Código fuente principal del programa interactivo.
- `paises.csv`: Archivo de datos base estructurado con los campos `nombre,poblacion,superficie,continente`.
- `README.md`: Documentación e instrucciones de uso del proyecto.
- `Informe_TPI_Programacion_1.pdf`: Informe académico/técnico con el desarrollo teórico y arquitectura.

---

## 🚀 Requisitos y Ejecución

### Requisitos previos
- Tener instalado Python 3.x en el sistema.

### Ejecución del programa
1. Clonar el repositorio o descargar el archivo `.zip`:
   ```bash
   git clone https://github.com/Agustin678X/UTN_Programacion_1_Trabajo_Pr-ctico_Integrador.git
   cd UTN_Programacion_1_Trabajo_Pr-ctico_Integrador
   ```
2. Ejecutar el script desde la terminal o consola de comandos:
   ```bash
   python main.py
   ```

---

## 💻 Funcionalidades del Menú

1. **Agregar país:** Permite ingresar un nuevo país validando que no haya campos vacíos y que los datos numéricos sean enteros positivos. Guarda automáticamente los cambios en `paises.csv`.
2. **Actualizar país:** Busca un país por nombre y permite actualizar su población y superficie.
3. **Buscar país:** Realiza búsquedas por coincidencia parcial de texto (insensible a mayúsculas y minúsculas) y muestra todos los resultados encontrados.
4. **Filtrar países:** Submenú para filtrar por:
   - Continente
   - Rango de población (mínimo y máximo)
   - Rango de superficie (mínimo y máximo)
5. **Ordenar países:** Permite ordenar el listado por nombre, población o superficie de manera ascendente o descendente mediante `sorted()` y expresiones `lambda`.
6. **Mostrar estadísticas:** Calcula y muestra:
   - País con mayor y menor población
   - Promedio de población y superficie
   - Conteo total de países por continente
7. **Salir:** Finaliza la ejecución del programa.
