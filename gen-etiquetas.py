# -*- coding: utf-8 -*-
# Genera etiquetas.html (Etiquetas de Envío y Vídeo, sin servidor: todo en el móvil) y la añade a index.html
# sin ejecutar gen.py entero (que no conoce las páginas de gen-servidor.py ni minutero.html).
# Copiado de gen-cuida.py.
# ⚠️ La versión en inglés (etiquetas-en.html) se mantiene a mano: si cambias este texto, cámbiala también.
# ⚠️ El modo «Móvil y PC» (wifi de casa) NO está en la versión de Play: si llega a publicarse, hay que declararlo aquí.
import os
os.chdir(r"C:\dev\legal")
src = open("gen.py", encoding="utf-8").read()
g = {}
exec(src[:src.index("APPS = [")], g)
exec(src[src.index('PAG = """'):src.index('IDX = """')], g)
MARCA, TITULAR, EMAIL, CSS, DERECHOS, MENORES, CAMBIOS, PAG = (g[k] for k in "MARCA TITULAR EMAIL CSS DERECHOS MENORES CAMBIOS PAG".split())

APP = dict(slug="etiquetas", nombre="Etiquetas de Envío y Vídeo", pkg="com.liquidsun.etiquetas", fecha="25 de noviembre de 2026",
 claim="Para quien vende por internet: imprime en pegatinas los códigos de tus etiquetas de envío, lleva tus pedidos y graba el embalaje con el nº de pedido y la hora.",
 cuerpo="""
<p class="sub"><a href="./etiquetas-en.html">English version</a></p>
<h2>Resumen</h2>
<div class="box">
<p><strong>Todo lo que guardas en Etiquetas se queda solo en tu teléfono.</strong> No hay cuenta de
usuario ni servidor propio: nosotros no recibimos, no vemos y no guardamos tus pedidos, los datos
de tus compradores, tus capturas, tus vídeos ni tus fotos.</p>
<p>Los archivos solo salen del móvil cuando tú los guardas en la galería o los envías con el menú
<em>Compartir</em> de Android.</p>
<p>La aplicación es gratuita y <strong>se financia con anuncios</strong> de Google AdMob y con una
suscripción opcional (Premium) que se paga a través de Google Play. Con Premium, para el sello de
tiempo solo sale del móvil una <strong>huella</strong> (SHA-256) del acta, nunca el archivo ni los
datos del pedido.</p>
</div>

<h2>Qué datos trata la aplicación</h2>
<table>
<tr><th>Dato</th><th>Para qué</th><th>Dónde acaba</th></tr>
<tr><td>Capturas de las etiquetas de envío que pegas o eliges, y los códigos que la aplicación lee en ellas</td><td>Imprimir los códigos en hojas de pegatinas y preparar la lista para la oficina de envío</td><td>Solo en tu dispositivo (la lectura de los códigos se hace en el propio móvil)</td></tr>
<tr><td>Pedidos: nombre del comprador, ciudad o región, nº de seguimiento, transportista, peso y notas</td><td>Llevar tus pedidos y preparar los mensajes para el comprador</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Vídeos y fotos del embalaje, con el nº de pedido y la hora sobreimpresos</td><td>Tener una prueba de cómo enviaste cada paquete</td><td>En tu dispositivo; en la galería del móvil (carpetas <code>Movies/</code> y <code>Pictures/</code>) o donde tú lo compartas</td></tr>
<tr><td>Almacén: fotos y ubicación de tus artículos (estantería, caja…)</td><td>Encontrar lo que vendes</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Enlace a un mensaje de tu canal de Telegram, si lo copias al portapapeles</td><td>Guardar en el pedido dónde está su vídeo</td><td>Solo en tu dispositivo</td></tr>
<tr><td>Huella SHA-256 del acta de un vídeo o una foto (solo con Premium)</td><td>Obtener un sello de tiempo independiente</td><td>FreeTSA, DigiCert y los servidores públicos de OpenTimestamps</td></tr>
<tr><td>Estado de tu suscripción Premium</td><td>Quitar los anuncios y activar las funciones Premium</td><td>Google Play (que gestiona el pago) y tu dispositivo</td></tr>
<tr><td>Identificador de publicidad, datos técnicos del dispositivo e interacción con los anuncios</td><td>Mostrar y medir los anuncios</td><td>Google AdMob, según tu elección de consentimiento</td></tr>
</table>
<p>Los nombres y ciudades de tus compradores son datos de otras personas que tú tratas para tus
envíos. Como se quedan en tu dispositivo, nosotros no los tratamos en ningún momento. Te
recomendamos proteger tu teléfono con bloqueo de pantalla.</p>
<p>La aplicación no usa tu ubicación, no tiene analítica propia y no envía informes de uso.</p>

<h2>Compartir y galería</h2>
<p>Etiquetas no sube nada por su cuenta. Cuando guardas un vídeo o una foto en la galería, se
queda en las carpetas <code>Movies/</code> y <code>Pictures/</code> de tu teléfono. Cuando pulsas
<em>Compartir</em> (un vídeo, el mensaje para el comprador, el paquete sellado, la copia de
seguridad…) o eliges Telegram, la aplicación entrega el archivo o el texto al menú
<em>Compartir</em> de Android. Eres tú quien elige la aplicación (WhatsApp, Telegram, correo,
Drive…) y el destinatario; a partir de ahí se aplica la política de esa aplicación.</p>

<h2>Sello de autenticidad (Premium)</h2>
<p>Con Premium, cada vídeo o foto puede llevar un acta firmada. La firma se hace con una clave que
se crea y se queda en el almacén seguro de tu teléfono (Android Keystore); nosotros no la tenemos.</p>
<p>Para el sello de tiempo, la aplicación calcula la huella SHA-256 del acta (una cadena de 32
bytes) y la envía a una autoridad de sellado de tiempo (<strong>FreeTSA</strong>, freetsa.org, y
<strong>DigiCert</strong>, timestamp.digicert.com) y a los servidores públicos de calendario de
<strong>OpenTimestamps</strong>. Con esa huella no se puede reconstruir ni el vídeo, ni la foto,
ni ningún dato del pedido: solo sirve para demostrar después que el acta ya existía en ese momento.
Como en cualquier conexión a internet, esos servicios reciben tu dirección IP.</p>
<p>El sello prueba que el archivo existía como muy tarde a esa hora y que no se ha modificado. No es
un sello cualificado eIDAS y no garantizamos que lo admita un juzgado o una plataforma de venta.</p>

<h2>Publicidad (Google AdMob)</h2>
<p>Si no tienes Premium, la aplicación muestra anuncios de <strong>Google AdMob</strong> (Google
Ireland Ltd.): un banner en la parte inferior de algunas pantallas y, como mucho de vez en cuando,
un anuncio a pantalla completa después de imprimir una hoja. No hay anuncios mientras grabas.</p>
<p>Si estás en el Espacio Económico Europeo, el Reino Unido o Suiza, antes de pedir ningún anuncio
la aplicación te muestra el formulario oficial de Google (User Messaging Platform) para que
decidas si aceptas los anuncios personalizados. En los estados de EE. UU. con leyes de privacidad,
el mismo formulario te permite oponerte a la venta o cesión de datos personales para publicidad.
Puedes cambiar esa decisión cuando quieras en <em>Ajustes &rsaquo; Privacidad de anuncios</em>. Si
no das tu consentimiento, los anuncios no serán personalizados.</p>
<p>Para servir y medir los anuncios y evitar fraudes, el SDK de AdMob puede tratar el
<strong>identificador de publicidad</strong>, la dirección IP y datos técnicos del dispositivo y de
uso de los anuncios. Puedes reiniciar o eliminar el identificador de publicidad en los ajustes de
Android (<em>Google &rsaquo; Anuncios</em>). Ese tratamiento lo hace Google según su propia
política: <a href="https://policies.google.com/privacy">policies.google.com/privacy</a> y
<a href="https://policies.google.com/technologies/ads">página de Google sobre publicidad</a>.</p>
<p><strong>Nada de lo que guardas en Etiquetas (pedidos, compradores, capturas, vídeos) se envía a
Google ni se usa para elegir los anuncios.</strong></p>

<h2>Suscripción (Premium)</h2>
<p>Premium es una suscripción trimestral o anual que se compra con el sistema de pagos de
<strong>Google Play</strong>, con 7 días de prueba gratis. Nosotros no vemos ni guardamos tu tarjeta
ni tus datos de pago. La aplicación solo consulta a Google Play si tu cuenta tiene Premium activo.
Las suscripciones se gestionan y se cancelan en Google Play.</p>

<h2>Permisos de Android</h2>
<ul>
<li><strong>Cámara</strong>: para escanear los códigos (también los QR de las cajas del almacén) y grabar los vídeos y las fotos del embalaje. Solo se usa cuando tú abres esas pantallas.</li>
<li><strong>Micrófono</strong>: para el sonido de los vídeos que grabas.</li>
<li><strong>Almacenamiento</strong> (solo en Android 9 o anterior): para guardar los vídeos y las fotos en la galería.</li>
<li><strong>Portapapeles</strong>: para pegar las capturas de las etiquetas y recoger el enlace del mensaje de Telegram cuando tú lo copias.</li>
<li><strong>Internet</strong>: para los anuncios, la suscripción y el sello de tiempo.</li>
</ul>
<p>Android muestra su propio indicador en la barra de estado mientras se usa la cámara o el
micrófono; la aplicación no puede ocultarlo.</p>

<h2>Copia de seguridad</h2>
<p>En <em>Ajustes &rsaquo; Copia de seguridad</em> puedes generar un archivo con tus datos y
guardarlo o enviarlo con <em>Compartir</em> donde quieras; la aplicación no lo envía a ninguna
parte por su cuenta. Si tienes activada la copia de seguridad automática de Android, el sistema
puede incluir los datos de la aplicación en la copia de tu cuenta de Google; esa copia la gestiona
Google y se puede desactivar en los ajustes de Android.</p>

<h2>Conservación y borrado</h2>
<p>Los datos se conservan en tu dispositivo hasta que los borras. Puedes borrar los pedidos
cerrados o <em>Ajustes &rsaquo; Borrar todos los datos</em>, o desinstalar la aplicación. Los vídeos
y fotos que guardaste en la galería siguen en ella hasta que los borres tú. Lo que recibe Google
AdMob se rige por su propia política.</p>

<h2>Aplicación independiente</h2>
<p>Etiquetas no está vinculada a ninguna empresa de mensajería, oficina de envío ni plataforma de
venta, y no se conecta a sus sistemas: solo lee lo que aparece en las capturas que tú le das.</p>
""")

pagina = PAG.format(css=CSS, marca=MARCA, nombre=APP["nombre"], pkgtxt=' — <code>%s</code>' % APP["pkg"],
                    claim=APP["claim"], titular=TITULAR, email=EMAIL, fecha=APP["fecha"], cuerpo=APP["cuerpo"],
                    derechos=DERECHOS.format(email=EMAIL), menores=MENORES, cambios=CAMBIOS)
open(APP["slug"] + ".html", "w", encoding="utf-8").write(pagina)
idx = open("index.html", encoding="utf-8").read()
if './etiquetas.html' not in idx:
    idx = idx.replace("\n</ul>", '\n<li><a href="./etiquetas.html">%s</a> (<a href="./etiquetas-en.html">English</a>) — %s</li>\n</ul>' % (APP["nombre"], APP["claim"]), 1)
    open("index.html", "w", encoding="utf-8").write(idx)
print("ok")
