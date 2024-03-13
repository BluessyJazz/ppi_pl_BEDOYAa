<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <link rel="stylesheet" href="style.css">
    <!-- Script para la tabla de contenido (no mostrar en la vista previa de GitHub) -->
    <!-- <script> type="text/javascript">
        function scrollToSection(id) {
            const element = document.getElementById(id);
            element.scrollIntoView({
                behavior: "smooth",
                block: "start",
                inline: "nearest"
            });
        }
      const navLinks = document.querySelectorAll("#tabla-de-contenido ul li a");
        for (let link of navLinks) {
            link.addEventListener("click", function() {
                scrollToSection(this.getAttribute("href").slice(1));
            });
        }
    </script> -->
</head>
<body>
    <header>
        <h1>Redmi</h1>
    </header>
    <section id="tabla-de-contenido">
        <h2>Tabla de Contenido</h2>
        <ul>
            <li><a href="#introduccion">Introducción</a></li>
            <li><a href="#acerca-de-mi">Acerca de mí</a></li>
            <li><a href="#portafolio">Portafolio</a></li>
            <li><a href="#tecnologías">Tecnologías</a></li>
            <li><a href="#contacto">Contacto</a></li>
        </ul>
    </section>
    <main>
        <section id="introduccion">
            <h2>Introducción</h2>
            <p>Este repositorio es un escaparate de mi trabajo como desarrollador Python freelance. Aquí encontrarás una selección de mis proyectos más destacados, así como información sobre mi experiencia y habilidades.</p>
        </section>
        <section id="acerca-de-mi">
            <h2>Acerca de mí</h2>
            <p>Soy un estudiante de 8º semestre de Ingeniería de Sistemas en la Universidad Nacional. Tengo un fuerte interés en análisis de datos y me apasiona utilizar la tecnología para resolver problemas y mejorar la eficiencia.</p>
        </section>
        <section id="portafolio">
            <h2>Portafolio</h2>
            <ul>
                <li>
                    <h3>[PROYECTO 1]</h3>
                    <p>Descripción breve del proyecto, tecnologías utilizadas y enlace al código fuente.</p>
                </li>
                <li>
                    <h3>[PROYECTO 2]</h3>
                    <p>Descripción breve del proyecto, tecnologías utilizadas y enlace al código fuente.</p>
                </li>
                <li>
                    <h3>[PROYECTO 3]</h3>
                    <p>Descripción breve del proyecto, tecnologías utilizadas y enlace al código fuente.</p>
                </li>
            </ul>
        </section>
        <section id="tecnologías">
            <h2>Tecnologías</h2>
            <ul>
                <li>Python: NumPy, Pandas, Matplotlib</li>
                <li>Web: Streamlit</li>
                <li>Bases de datos: MySQL, SQL Server</li>
            </ul>
        </section>
        <section id="contacto">
            <h2>Contacto</h2>
            <ul>
                <li>Correo electrónico: [CORREO ELECTRÓNICO]</li>
                <li>LinkedIn: [LINKEDIN]</li>
                <li>GitHub: [GITHUB]</li>
            </ul>
        </section>
    </main>
    <footer>
        <p>&copy; 2023 - [Tu nombre]</p>
    </footer>
</body>
</html>

