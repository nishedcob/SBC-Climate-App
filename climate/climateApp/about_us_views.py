from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View


class GenericAboutUsView(View):
    template_name = "pages/about_us.html"


class UTPLAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - UTPL",
        'item_1': True,
        'heading_1': "Mision",
        'text_1': "El Humanismo de Cristo, que en su manifestación histórica y el desarrollo de su pensamiento en la tradición de la Iglesia Católica, propugna una universalidad potenciadora, conforme a la dignidad que el ser humano tiene como “hijo de Dios”, que hace a la Universidad acoger, defender y promover en la sociedad, el producto y la reflexión de toda experiencia humana.",
        'image_1': None,
        'image_before_text_1': False,
        'item_2': True,
        'heading_2': "Vision",
        'text_2': "Buscar la verdad y formar al hombre, a través de la ciencia para que sirva a la sociedad",
        'image_2': None,
        'image_before_text_2': False,
        'item_3': True,
        'heading_3': None,
        'text_3': None,
        'image_3': 'img/escudo-utpl.jpg',
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class SBCAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - Sistemas Basados en el Conocimiento",
        'item_1': True,
        'heading_1': "Docente",
        'text_1': "Janneth Chicaiza",
        'image_1': None,
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class MADBAAboutUsView(GenericAboutUsView):
    context = {
        'title': "Acerca de Nosotros - Marcelo Bravo",
        'item_1': True,
        'heading_1': "Formación:",
        'text_1': "Estudiante de la Carrera de Ingenieria  de Sistemas informaticos en la Universidad Tecnica "
                  "Particular de Loja, conocimiento en sistemas operativos como Debian, Ubuntu, los lenguajes con los "
                  "que ha trabajado son Java, Python, C, C++, tambien ha usado bases de datos MySQL y PostgresSQL, "
                  "trabajo en proyectos de inteligencia artificial mediante el uso de la biblioteca OpenCV, "
                  "Proyectos de reconocimiento de objetos con dichas librerias",
        'image_1': "img/marcelo.jpg",
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)


class NSEDAboutUsView(GenericAboutUsView):

    context = {
        'title': "Acerca de Nosotros - Nicholas Earley",
        'item_1': True,
        'heading_1': "Formación:",
        'text_1':  "Programador y Analista de Backend con experiencia en C, Python, Java, Bash, "
                     "PHP, Administrador de Sistemas con experiencia con Sistemas Operativos "
                     " en Debian, CentOS, Ubuntu, Fedora, Archlinux, Xen; Experiencia en "
                     " Clusters con PelicanHPC y Rocks; Experience con proveedores como:"
                     " Servidores Físicos, Microsoft Azure, IBM Softlayer. Administrador "
                     "de Bases de Datos con experiencia SQL en PostgreSQL, MySQL/MariaDB "
                     "en adición a Diseño de Bases de Datos  Relacionales; experiencia NoSQL "
                     "con Neo4J, MongoDB y Redis; Experiencia Triplestore con Mapeo de Datos "
                     "como RDF y N-Tuplas, y consultas a la DBPedia mediante SPARQL. Arquitecto "
                     "de Despliegue de  Sistemas para el diseño e implementación de planes de "
                     "alto nivel de despliegue y  mantenimiento de N-Capa sistemas distribuidos "
                     "en M-Niveles para proveer atributos de calidad como  Portabilidad, "
                     "Escalabilidad y Seguridad. Experiencia limitado en diseño de arquitecturas SOA y "
                     "Microservicios. Algo de experiencia en Gestión de Proyecto especialmente con estimación "
                     "de costo y tiempo basado en puntos de función en adición a estimaciones de progreso "
                     "basados en Gestión del Valor Ganado. Experiencia en el despliegue y mantenimiento de Aplicaciones como  "
                     "NGinX, UWSGI, Docker(Docker-Compose and Docker-Swarm), ProFTPD, HTCondor, CronD,"
                     " SystemD, SELinux, Fail2Ban, OpenSSH, OpenVPN, y GitLab CE",
        'image_1': "img/nicho1.jpg",
        'image_before_text_1': False,
        'item_2': False,
        'heading_2': None,
        'text_2': None,
        'image_2': None,
        'image_before_text_2': False,
        'item_3': False,
        'heading_3': None,
        'text_3': None,
        'image_3': None,
        'image_before_text_3': False
    }

    def get(self, request):
        return render(request, self.template_name, context=self.context)
