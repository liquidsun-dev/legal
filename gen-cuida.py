# -*- coding: utf-8 -*-
# Genera cuida.html (Cuida, sin servidor: todo en el móvil) y la añade a index.html
# sin ejecutar gen.py entero (que no conoce las páginas de gen-servidor.py ni minutero.html).
import os, re
os.chdir(r"C:\dev\legal")
src = open("gen.py", encoding="utf-8").read()
g = {}
exec(src[:src.index("APPS = [")], g)
exec(src[src.index('PAG = """'):src.index('IDX = """')], g)
MARCA, TITULAR, EMAIL, CSS, DERECHOS, MENORES, CAMBIOS, PAG = (g[k] for k in "MARCA TITULAR EMAIL CSS DERECHOS MENORES CAMBIOS PAG".split())

APP = dict(slug="cuida", nombre="Cuida", pkg="com.liquidsun.cuida", fecha="23 de noviembre de 2026",
 claim="Organiza en familia el cuidado de tus padres: medicación, citas, tareas, turnos, mediciones y urgencias.",
 cuerpo="""
<h2>Resumen</h2>
<div class="box">
<p><strong>Todo lo que anotas en Cuida se guarda solo en tu teléfono.</strong> No hay cuenta de
usuario ni servidor propio: nosotros no recibimos, no vemos y no guardamos ni la medicación, ni
las citas, ni las mediciones, ni ningún otro dato de la persona que cuidas.</p>
<p>Si compartes datos con tu familia (el «paquete familiar», el resumen o el informe), lo haces tú
con el menú <em>Compartir</em> de Android y llegan solo a quien tú elijas.</p>
<p>La aplicación es gratuita y <strong>se financia con anuncios</strong> de Google AdMob y con una
suscripción opcional (Premium) que se paga a través de Google Play. Tus datos de salud
<strong>nunca</strong> se usan para los anuncios ni se envían a Google.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Datos de la persona cuidada: nombre, fecha de nacimiento, alergias, enfermedades, grupo sanguíneo, nº de tarjeta sanitaria, centro de salud</td><td>Ficha de urgencias e informe</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Medicación, tomas, citas médicas, mediciones (tensión, azúcar, peso…), incidencias y visitas</td><td>Organizar el cuidado y los avisos</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Familiares y contactos de emergencia (nombre, relación, teléfono), tareas y turnos</td><td>Repartir el cuidado y llamar en una urgencia</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Fotos de documentos que tú eliges (DNI, informes…)</td><td>Tenerlos a mano</td><td>Solo en tu dispositivo (no viajan en el paquete familiar)</td></tr>
<tr><td>Cómo te encuentras tú (pregunta semanal)</td><td>Recomendarte la guía del cuidador</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Estado de tu compra de Premium</td><td>Quitar los anuncios y activar las funciones Premium</td><td>Google Play (que gestiona el pago) y tu dispositivo</td></tr>
<tr><td>Identificador de publicidad, datos técnicos del dispositivo e interacción con los anuncios</td><td>Mostrar y medir los anuncios</td><td>Google AdMob, según tu elección de consentimiento</td></tr>
</table>
<p>Muchos de estos datos son <strong>datos de salud</strong> de otra persona (la que cuidas). Como
se quedan en tu dispositivo y los usas en el ámbito familiar, nosotros no los tratamos en ningún
momento. Te recomendamos contar con su conformidad cuando sea posible y proteger tu teléfono con
bloqueo de pantalla.</p>

<h2>Compartir con la familia</h2>
<p>Cuida no sincroniza nada por su cuenta. Cuando pulsas <em>Enviar paquete familiar</em>,
<em>Enviar resumen</em>, <em>Informe para el médico</em>, <em>Hacer copia</em> o <em>Compartir</em>
un documento, la aplicación prepara un archivo o un texto y lo entrega al menú <em>Compartir</em>
de Android. Eres tú quien elige la aplicación (WhatsApp, correo, Drive…) y el destinatario; a
partir de ahí se aplica la política de esa aplicación. Al abrir un paquete recibido, sus datos se
juntan con los tuyos en tu dispositivo.</p>

<h2>Publicidad (Google AdMob)</h2>
<p>Si no tienes Premium, la aplicación muestra anuncios de <strong>Google AdMob</strong> (Google
Ireland Ltd.): un banner en la parte inferior, anuncios a pantalla completa en algunas pausas
(por ejemplo, después de guardar algo o al volver a la aplicación tras un rato), con un límite de
frecuencia, y anuncios con recompensa que tú decides ver a cambio de un extra. La pantalla de
urgencias no tiene anuncios.</p>
<p>Si estás en el Espacio Económico Europeo, el Reino Unido o Suiza, antes de pedir ningún anuncio
la aplicación te muestra el formulario oficial de Google (User Messaging Platform) para que
decidas si aceptas los anuncios personalizados. Puedes cambiar esa decisión cuando quieras en
<em>Más &rsaquo; Privacidad de anuncios</em>. Si no das tu consentimiento, los anuncios no serán
personalizados.</p>
<p>Para servir y medir los anuncios y evitar fraudes, el SDK de AdMob puede tratar el
<strong>identificador de publicidad</strong>, la dirección IP y datos técnicos del dispositivo y de
uso de los anuncios. Puedes reiniciar o eliminar el identificador de publicidad en los ajustes de
Android (<em>Google &rsaquo; Anuncios</em>). Ese tratamiento lo hace Google según su propia
política: <a href="https://policies.google.com/privacy">policies.google.com/privacy</a> y
<a href="https://policies.google.com/technologies/ads">página de Google sobre publicidad</a>.</p>
<p><strong>Nada de lo que anotas en Cuida se envía a Google ni se usa para elegir los anuncios.</strong></p>

<h2>Compras (Cuida Premium)</h2>
<p>Premium se compra con el sistema de pagos de <strong>Google Play</strong>. Nosotros no vemos ni
guardamos tu tarjeta ni tus datos de pago. La aplicación solo consulta a Google Play si tu cuenta
tiene Premium activo. Las suscripciones se gestionan y se cancelan en Google Play.</p>

<h2>Avisos</h2>
<p>Los avisos de medicación y de citas los programa el propio teléfono, sin pasar por ningún
servidor. Su texto (nombre del medicamento y de la persona) puede verse en la pantalla de bloqueo;
puedes ocultarlo en los ajustes de notificaciones de Android.</p>

<h2>Permisos de Android</h2>
<ul>
<li><strong>Internet</strong>: solo para los anuncios y las compras.</li>
<li><strong>Notificaciones, alarmas exactas e inicio del dispositivo</strong>: para que los avisos de medicación suenen a su hora, también después de reiniciar el teléfono.</li>
<li><strong>Facturación de Google Play</strong>: para comprar Premium.</li>
<li><strong>Identificador de publicidad</strong>: lo usa el SDK de AdMob.</li>
</ul>
<p>Las fotos de documentos se eligen con el selector de Android: la aplicación no pide permiso
para leer tu galería ni para usar la cámara por su cuenta.</p>

<h2>Copia de seguridad</h2>
<p>En <em>Más &rsaquo; Ajustes y copias</em> puedes generar un archivo con tus datos (sin las fotos)
y guardarlo donde quieras; la aplicación no lo envía a ninguna parte por su cuenta. Si tienes
activada la copia de seguridad automática de Android, el sistema puede incluir los datos de la
aplicación en la copia de tu cuenta de Google; esa copia la gestiona Google y se puede desactivar
en los ajustes de Android.</p>

<h2>Conservación y borrado</h2>
<p>Los datos se conservan en tu dispositivo hasta que los borras. Puedes borrarlo todo en
<em>Más &rsaquo; Ajustes y copias &rsaquo; Borrar todos mis datos</em>, o desinstalando la
aplicación. Lo que recibe Google AdMob se rige por su propia política.</p>

<h2>No es un producto sanitario</h2>
<p>Cuida es una herramienta de organización. No da diagnósticos ni consejos médicos, no interpreta
las mediciones y no sustituye al médico ni al farmacéutico. Los avisos pueden retrasarse si el
ahorro de batería del teléfono los bloquea.</p>
""")

pagina = PAG.format(css=CSS, marca=MARCA, nombre=APP["nombre"], pkgtxt=' — <code>%s</code>' % APP["pkg"],
                    claim=APP["claim"], titular=TITULAR, email=EMAIL, fecha=APP["fecha"], cuerpo=APP["cuerpo"],
                    derechos=DERECHOS.format(email=EMAIL), menores=MENORES, cambios=CAMBIOS)
open(APP["slug"] + ".html", "w", encoding="utf-8").write(pagina)
idx = open("index.html", encoding="utf-8").read()
if './cuida.html' not in idx:
    idx = idx.replace("\n</ul>", '\n<li><a href="./cuida.html">%s</a> — %s</li>\n</ul>' % (APP["nombre"], APP["claim"]), 1)
    open("index.html", "w", encoding="utf-8").write(idx)
print("ok")
