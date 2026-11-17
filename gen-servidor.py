# -*- coding: utf-8 -*-
# Genera ayudas.html, luz.html y oposiciones.html (apps con el servidor api.liquidsun.es)
# (sin ejecutar gen.py entero, que no conoce minutero.html y rehace index.html).
import os, re
os.chdir(r"C:\dev\legal")
src = open("gen.py", encoding="utf-8").read()
g = {}
exec(src[:src.index("APPS = [")], g)
pag_src = src[src.index('PAG = """'):src.index('IDX = """')]
exec(pag_src, g)
MARCA, TITULAR, EMAIL, CSS, MENORES, CAMBIOS, PAG = (g[k] for k in "MARCA TITULAR EMAIL CSS MENORES CAMBIOS PAG".split())
FECHA = "17 de noviembre de 2026"

ANUNCIOS = """<h2>Publicidad (Google AdMob)</h2>
<p>La aplicación es gratuita y se paga con anuncios de <strong>Google AdMob</strong>
(Google Ireland Ltd.): {formatos}</p>
<p>Si estás en el Espacio Económico Europeo, el Reino Unido o Suiza, antes de pedir ningún
anuncio la aplicación te muestra el formulario oficial de Google (User Messaging Platform)
para que decidas si aceptas los anuncios personalizados. Puedes cambiar esa decisión cuando
quieras en <em>Ajustes &rsaquo; Opciones de privacidad de los anuncios</em>. Si no das tu
consentimiento, los anuncios que veas no serán personalizados.</p>
<p>Para servir y medir los anuncios y evitar fraudes, el SDK de AdMob puede tratar el
<strong>identificador de publicidad</strong> del dispositivo, la dirección IP y datos técnicos
del dispositivo y de uso de los anuncios. Puedes reiniciar o eliminar el identificador de
publicidad en los ajustes de Android (<em>Google &rsaquo; Anuncios</em>). Ese tratamiento lo hace
Google según su propia política:
<a href="https://policies.google.com/privacy">policies.google.com/privacy</a> y
<a href="https://policies.google.com/technologies/ads">página de Google sobre publicidad</a>.</p>
<p>{no_ads}</p>"""

SERVIDOR = """<h2>Nuestro servidor</h2>
<p>La aplicación consulta un servidor propio de {marca} (<code>api.liquidsun.es</code>),
alojado en un centro de datos de la Unión Europea. La empresa de alojamiento actúa como
encargada del tratamiento y no usa los datos para nada propio. No hay transferencias
internacionales de datos por nuestra parte.</p>
<p>Como en cualquier conexión a Internet, tu dirección IP llega al servidor para poder
contestarte, pero <strong>no se guarda</strong> en ningún registro.</p>
<p>No vendemos, alquilamos ni cedemos datos a nadie.</p>"""

def derechos(borrar):
    return f"""<h2>Tus derechos</h2>
<p>El Reglamento General de Protección de Datos (RGPD) te reconoce el derecho a acceder a tus
datos, rectificarlos, suprimirlos, limitar u oponerte a su tratamiento y solicitar su
portabilidad.</p>
<p>{borrar}</p>
<p>Para ejercer cualquiera de esos derechos o para cualquier consulta, escribe a
<a href="mailto:{EMAIL}">{EMAIL}</a>. Te contestaremos en un plazo máximo de un mes. Como no
sabemos quién eres (no tenemos tu nombre ni tu correo), puede que no podamos relacionar tu
mensaje con unos datos concretos; por eso la app te deja verlos y borrarlos tú mismo.</p>
<p>Si consideras que tus datos no se han tratado correctamente, puedes presentar una
reclamación ante la Agencia Española de Protección de Datos
(<a href="https://www.aepd.es">www.aepd.es</a>).</p>"""

NO_OFICIAL = """<div class="box"><p><strong>Aplicación independiente y no oficial.</strong> {texto}</p></div>"""

APPS = [
dict(slug="ayudas", nombre="Ayudas para mí", pkg="com.liquidsun.ayudas",
 claim="Las ayudas y subvenciones abiertas que encajan contigo, a partir de la Base de Datos Nacional de Subvenciones.",
 cuerpo=NO_OFICIAL.format(texto="No pertenece a ninguna Administración ni actúa en su nombre. La información de las ayudas procede de la Base de Datos Nacional de Subvenciones (Ministerio de Hacienda), que es pública; antes de solicitar una ayuda, comprueba siempre la convocatoria oficial.") + """
<h2>Resumen</h2>
<div class="box">
<p>No hay cuenta de usuario: la app <strong>no te pide nombre, correo, teléfono ni ubicación</strong>.</p>
<p>Para enseñarte tus ayudas, el servidor guarda solo <strong>un número al azar</strong> que crea la
app y tu perfil: si buscas como particular o como negocio, y tu provincia o isla. Lo puedes
borrar en cualquier momento desde la app.</p>
<p>La app es gratuita gracias a los anuncios de Google AdMob, y en la Unión Europea se te pregunta antes.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Identificador al azar creado por la app (no contiene nada tuyo)</td><td>Saber qué perfil es el tuyo sin pedirte una cuenta</td><td>En tu dispositivo y en nuestro servidor</td></tr>
<tr><td>Tu perfil: particular o negocio, y provincia o isla</td><td>Elegir las ayudas que encajan contigo</td><td>En tu dispositivo y en nuestro servidor</td></tr>
<tr><td>Ayudas que has visto o guardado, y tus ajustes</td><td>Que la app funcione</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Dirección IP de la conexión</td><td>Poder contestar a la app</td><td>No se guarda</td></tr>
<tr><td>Identificador de publicidad y datos técnicos</td><td>Anuncios (ver «Publicidad»)</td><td>Google AdMob</td></tr>
</table>
<p>No pedimos ni tratamos datos especialmente protegidos (salud, ideología, etc.), ni tu
nombre, DNI, ingresos o situación personal.</p>

<h2>Base legal</h2>
<ul>
<li><strong>Tu perfil y el identificador:</strong> son necesarios para prestarte el servicio que
pides al usar la app, que es enseñarte tus ayudas (art. 6.1.b RGPD).</li>
<li><strong>Anuncios personalizados:</strong> tu consentimiento, que das o niegas en el formulario de
Google y puedes retirar cuando quieras (art. 6.1.a RGPD).</li>
</ul>
""" + SERVIDOR.format(marca=MARCA) + chr(10) + ANUNCIOS.format(
 formatos="un banner en la lista de ayudas y, como mucho cada pocos minutos, un anuncio a pantalla completa al abrir una convocatoria (nunca la primera de cada sesión).",
 no_ads="Tu perfil (particular o negocio y provincia) no se usa para la publicidad ni se envía a Google.") + """
<h2>Conservación</h2>
<p>Tu perfil se guarda mientras uses la app. <strong>Si no la abres en 12 meses, se borra solo.</strong>
Puedes borrarlo antes cuando quieras en <em>Ajustes &rsaquo; Borrar mis datos</em>: se borra del
dispositivo y del servidor al momento. Desinstalar la app borra lo que hay en el dispositivo.</p>

<h2>Permisos de Android</h2>
<ul>
<li><strong>Internet</strong>: para consultar las ayudas y para los anuncios. La app no pide ningún otro permiso.</li>
</ul>

<h2>Enlaces a otras webs</h2>
<p>Las convocatorias se abren en tu navegador, en la web oficial correspondiente, solo si tú
las pulsas. Esas webs tienen sus propias políticas.</p>
""",
 borrar="Puedes borrar tus datos tú mismo, sin pedírnoslo, en <em>Ajustes &rsaquo; Borrar mis datos</em> (se borran del dispositivo y del servidor al momento)."),

dict(slug="luz", nombre="Precio de la luz", pkg="com.liquidsun.luz",
 claim="El precio de la luz de hoy y mañana hora a hora (PVPC), con las horas más baratas.",
 cuerpo=NO_OFICIAL.format(texto="No pertenece a Red Eléctrica, a ninguna comercializadora ni a ninguna Administración. Los precios proceden de los datos públicos de Red Eléctrica de España.") + """
<h2>Resumen</h2>
<div class="box">
<p>La app <strong>no te pide nombre, correo, teléfono ni ubicación</strong>, no crea cuentas y
no envía a nuestro servidor nada que te identifique: solo pide los precios del día.</p>
<p>La app es gratuita gracias a los anuncios de Google AdMob, y en la Unión Europea se te pregunta antes.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Precios descargados y tus ajustes</td><td>Verlos sin conexión</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Dirección IP de la conexión</td><td>Poder contestar a la app</td><td>No se guarda</td></tr>
<tr><td>Identificador de publicidad y datos técnicos</td><td>Anuncios (ver «Publicidad»)</td><td>Google AdMob</td></tr>
</table>

<h2>Base legal</h2>
<ul>
<li><strong>Conexión con el servidor:</strong> es necesaria para darte los precios que pides (art. 6.1.b RGPD).</li>
<li><strong>Anuncios personalizados:</strong> tu consentimiento, que das o niegas en el formulario de
Google y puedes retirar cuando quieras (art. 6.1.a RGPD).</li>
</ul>
""" + SERVIDOR.format(marca=MARCA) + chr(10) + ANUNCIOS.format(
 formatos="un banner junto a los precios y, como mucho una vez por hora, un anuncio al volver a la app tras un rato fuera.",
 no_ads="Lo que consultas en la app no se usa para la publicidad ni se envía a Google.") + """
<h2>Conservación</h2>
<p>Lo que guarda la app vive en tu dispositivo; desinstalarla o borrar sus datos desde los
ajustes de Android lo elimina por completo. Nuestro servidor no guarda nada sobre ti.</p>

<h2>Permisos de Android</h2>
<ul>
<li><strong>Internet</strong>: para descargar los precios y para los anuncios. La app no pide ningún otro permiso.</li>
</ul>
""",
 borrar="Como nuestro servidor no guarda datos tuyos, no tenemos nada que darte ni que borrar: lo que hay está en tu dispositivo, y desinstalar la app o borrar sus datos en los ajustes de Android lo elimina."),

dict(slug="oposiciones", nombre="Oposiciones BOE", pkg="com.liquidsun.oposiciones",
 claim="Lo que sale en el BOE con tus palabras (convocatorias, admitidos, aprobados) y test de legislación con su artículo.",
 cuerpo=NO_OFICIAL.format(texto="No pertenece al Boletín Oficial del Estado ni a ninguna Administración, ni a ninguna academia. Las disposiciones y los textos legales proceden del BOE (www.boe.es), que es público; comprueba siempre la publicación oficial. Las preguntas de los test las hemos redactado a partir de la legislación consolidada y cada una cita su artículo, pero pueden contener errores y no sustituyen al texto oficial.") + """
<h2>Resumen</h2>
<div class="box">
<p>No hay cuenta de usuario: la app <strong>no te pide nombre, correo, teléfono ni ubicación</strong>.</p>
<p>Para buscarte lo que sale en el BOE, el servidor guarda solo <strong>un número al azar</strong>
que crea la app y <strong>las palabras que eliges</strong> (por ejemplo, «auxiliar administrativo»).
Tus resultados de los test se quedan en tu móvil.</p>
<p>La app es gratuita gracias a los anuncios de Google AdMob, y en la Unión Europea se te pregunta antes.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Identificador al azar creado por la app (no contiene nada tuyo)</td><td>Saber qué búsqueda es la tuya sin pedirte una cuenta</td><td>En tu dispositivo y en nuestro servidor</td></tr>
<tr><td>Tus palabras de búsqueda y si quieres solo convocatorias</td><td>Buscarte lo que sale en el BOE</td><td>En tu dispositivo y en nuestro servidor</td></tr>
<tr><td>Respuestas, fallos y estadísticas de los test</td><td>Que repases y veas tu progreso</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Dirección IP de la conexión</td><td>Poder contestar a la app</td><td>No se guarda</td></tr>
<tr><td>Identificador de publicidad y datos técnicos</td><td>Anuncios (ver «Publicidad»)</td><td>Google AdMob</td></tr>
</table>
<p>Te recomendamos que tus palabras de búsqueda sean sobre la oposición (cuerpo, puesto,
organismo) y no incluyan tu nombre ni otros datos personales.</p>

<h2>Base legal</h2>
<ul>
<li><strong>Tus palabras y el identificador:</strong> son necesarios para prestarte el servicio que
pides al usar la app, que es buscarte lo que sale en el BOE (art. 6.1.b RGPD).</li>
<li><strong>Anuncios personalizados:</strong> tu consentimiento, que das o niegas en el formulario de
Google y puedes retirar cuando quieras (art. 6.1.a RGPD).</li>
</ul>
""" + SERVIDOR.format(marca=MARCA) + chr(10) + ANUNCIOS.format(
 formatos="un banner en la parte inferior y, como mucho una vez cada cuatro minutos, un anuncio a pantalla completa al terminar un test (nunca después del primero).",
 no_ads="Tus palabras de búsqueda y tus resultados de los test no se usan para la publicidad ni se envían a Google.") + """
<h2>Conservación</h2>
<p>Tus palabras se guardan mientras uses la app. <strong>Si no la abres en 12 meses, se borran solas.</strong>
Puedes borrarlas antes cuando quieras en <em>Ajustes &rsaquo; Borrar mis datos</em>: se borran del
dispositivo y del servidor al momento. Desinstalar la app borra lo que hay en el dispositivo.</p>

<h2>Permisos de Android</h2>
<ul>
<li><strong>Internet</strong>: para consultar el BOE y para los anuncios. La app no pide ningún otro permiso.</li>
</ul>

<h2>Enlaces a otras webs</h2>
<p>Las disposiciones se abren en tu navegador, en www.boe.es, solo si tú las pulsas. Esa web
tiene su propia política.</p>
""",
 borrar="Puedes borrar tus datos tú mismo, sin pedírnoslo, en <em>Ajustes &rsaquo; Borrar mis datos</em> (se borran del dispositivo y del servidor al momento)."),
]

items = []
for a in APPS:
    pagina = PAG.format(css=CSS, marca=MARCA, nombre=a["nombre"], pkgtxt=' — <code>%s</code>' % a["pkg"],
                        claim=a["claim"], titular=TITULAR, email=EMAIL, fecha=FECHA, cuerpo=a["cuerpo"],
                        derechos=derechos(a["borrar"]), menores=MENORES, cambios=CAMBIOS)
    open(a["slug"] + ".html", "w", encoding="utf-8").write(pagina)
    items.append('<li><a href="./%s.html">%s</a> — %s</li>' % (a["slug"], a["nombre"], a["claim"]))

idx = open("index.html", encoding="utf-8").read()
for it in items:
    slug = re.search(r'\./([a-z-]+)\.html', it).group(1)
    if f'./{slug}.html' not in idx:
        idx = idx.replace("\n</ul>", "\n" + it + "\n</ul>", 1)
open("index.html", "w", encoding="utf-8").write(idx)
print("ok")
