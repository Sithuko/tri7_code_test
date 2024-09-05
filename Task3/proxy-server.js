const http = require('http');
const httpProxy = require('http-proxy');

const proxy = httpProxy.createProxyServer({});

const server = http.createServer((req, res) => {
  proxy.web(req, res, { target: 'http://localhost:3000' });
});

const port = process.argv[2] || 8001;

server.listen(port, () => {
  console.log(`Proxy server listening on port ${port}`);
});
