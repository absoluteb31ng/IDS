const net = require('net');
const PORT = 65432;

const server = net.createServer((socket) => {
    socket.on('data', (data) => {
        const alert = data.toString();
        console.log(`Alerta recibida: ${alert}`);
    });

    socket.on('error', (err) => {
        console.error('Error en la conexión del socket:', err);
    });
});

server.listen(PORT, () => {
    console.log(`Servidor de alertas escuchando en el puerto ${PORT}`);
});

const pcap = require('pcap');
const tcpTracker = new pcap.TCPTracker();
const pcapSession = pcap.createSession("", "ip proto \\tcp");

pcapSession.on('error', function (err) {
    console.error('Error en la sesión pcap:', err);
});

pcapSession.on('packet', handlePacket);
tcpTracker.on('session', handleSessionStart);

function handleSessionStart(session) {
    console.log(`Inicio de sesión TCP entre ${session.src_name} y ${session.dst_name}`);
    session.on('end', handleSessionEnd.bind(null, session.src_name, session.dst_name));
}

function handleSessionEnd(srcName, dstName) {
    console.log(`Fin de sesión TCP entre ${srcName} y ${dstName}`);
}

function handlePacket(rawPacket) {
    try {
        const packet = pcap.decode.packet(rawPacket);
        tcpTracker.track_packet(packet);
    } catch (err) {
        console.error('Error al manejar el paquete:', err);
    }
}

function init() {
    console.log('Iniciando IDS...');
}

init();
