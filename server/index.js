const fastify = require('fastify')({ logger: true });

// Habilitando CORS
fastify.register(require('@fastify/cors'), { 
    origin: '*'
});

// Rotas de acesso à API do Spotify

// Rota para obter a música que está tocando no momento
fastify.get('/current-playing', async (request, reply) => {
    try {
        const response = await fetch('https://api.spotify.com/v1/me/player/currently-playing', {
            method: 'GET',
            headers: {
                'Authorization': request.headers.authorization
            }
        });

        if (!response.ok) { // Verifica se a resposta foi bem-sucedida
            throw new Error(`Error fetching data from Spotify: ${response.status}`);
        }


        const respData = await response.json();

        const data = {
            item: {
                name: respData.item ? respData.item.name : 'Nenhuma música tocando'
            }
        };

        reply.status(200).send(data);
    } catch (error) {
        console.error('Erro ao buscar dados da API do Spotify:', error);
        reply.status(500).send({ error: 'Erro ao obter a música atual' });
    }
});

// Rota para reproduzir a faixa atual
fastify.put('/play-track', async (request, reply) => {
    try {
        const url = 'https://api.spotify.com/v1/me/player/play';
        const headers = {
            'Authorization': request.headers.authorization
        };

        const response = await fetch(url, {
            method: 'PUT',
            headers: headers
        });

        if (!response.ok) {  // Verifica se a resposta foi bem-sucedida
            throw new Error(`Error playing track on Spotify: ${response.status}`);
        }

        reply.status(204).send();  // 204 No Content indica sucesso sem corpo de resposta
    } catch (error) {
        console.error('Erro ao reproduzir faixa na API do Spotify:', error);
        reply.status(500).send({ error: 'Erro ao reproduzir a faixa' });
    }
});

// Rota para pausar a faixa atual
fastify.put('/pause-track', async (request, reply) => {
    try {
	console.log(request);
        const url = 'https://api.spotify.com/v1/me/player/pause';
        const headers = {
            'Authorization': request.headers.authorization
        };

        const response = await fetch(url, {
            method: 'PUT',
            headers: headers
        });

        console.log(response)

        if (!response.ok) {  // Verifica se a resposta foi bem-sucedida
            throw new Error(`Error pausing track on Spotify: ${response.status}`);
        }

        reply.status(204).send();  // 204 No Content indica sucesso sem corpo de resposta
    } catch (error) {
        console.error('Erro ao pausar faixa na API do Spotify:', error);
        reply.status(500).send({ error: 'Erro ao pausar a faixa' });
    }
});

// Iniciando o servidor
const start = async () => {
    try {
        await fastify.listen({ port: 8080, host: '0.0.0.0' });
    } catch (err) {
        fastify.log.error(err);
        process.exit(1);
    }
};

start();
