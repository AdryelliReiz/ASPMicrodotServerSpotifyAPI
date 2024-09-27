# ASP & Spotify API

## Descrição

Este repositório contém um projeto que permite subir um servidor em um ESP32 utilizando MicroPython e consumir a [API pública do Spotify](https://developer.spotify.com/documentation/web-api). O projeto envolve a comunicação entre o ESP32 e uma API intermediária que filtra as respostas da API do Spotify para otimizar o uso de memória no dispositivo.

## Estrutura do Projeto

O projeto está organizado em duas partes principais:

1. **Servidor Microdot no ESP32**: Um servidor web rodando no ESP32 que permite realizar requisições à API do Spotify.
2. **API Intermediária**: Um servidor Node.js que atua como um intermediário entre o ESP32 e a API do Spotify para filtrar e simplificar as respostas, contornando o problema de memória limitada do ESP32.

## Motivação e Desafios

O ESP32 possui apenas 512 KB de memória, o que pode ser insuficiente para lidar com grandes volumes de dados retornados pela API do Spotify. Para superar essa limitação, uma API intermediária é utilizada para filtrar e processar as respostas, enviando apenas os dados essenciais ao ESP32.

## Funcionalidades Atuais

O projeto ainda possui funcionalidades básicas, mas já oferece interações interessantes com o servidor. Atualmente, você pode:

1. **Visualizar a Música Atual**: Exibe o nome da música no display oled.
2. **Pausar a Reprodução**: Permite pausar a música em reprodução.
3. **Retomar a Reprodução**: Reproduz a música pausada com um único click.

## Componentes Necessários

### Hardware
- ESP32;
- 4 jumpers;
- Display OLED 128x96;
- Protoboard;
- Cabo USB compatível com o ESP32;
- Computador (opcional).

### Software
- [Thonny](https://thonny.org/): IDE para programação em MicroPython;
- [Git](https://git-scm.com/): Controle de versão;
- [Node.js](https://nodejs.org/): Ambiente de execução para a API intermediária;
- Navegador web para acessar o servidor;
- Editor de código de sua preferência (opcional).

## Conectando o Hardware

1. Monte os componentes na protoboard, conectando os pinos do display OLED ao ESP32 da seguinte forma:
   - **GND** do display OLED ao **GND** do ESP32;
   - **VCC** do display OLED ao **3v3** do ESP32;
   - **SCL** do display OLED ao **D4** do ESP32;
   - **SDA** do display OLED ao **D5** do ESP32.
   
2. Conecte o cabo USB ao ESP32 e ao seu computador.

![Conexão do ESP32 com Display OLED](https://cdn.discordapp.com/attachments/865710630833225748/1289201837181763644/IMG_20240926_171916.jpg?ex=66f7f646&is=66f6a4c6&hm=528ca410e8138370fb7ebd1ca8f06f7a9d6fd4a0429cea752cdb7473b62f7e1c&)

## Clonando o Repositório e Configurando o Ambiente

Para baixar o projeto e configurar o ambiente, siga os passos abaixo:

1. Clone o repositório:
   ```bash
   git clone https://github.com/AdryelliReiz/ASPMicrodotServerSpotifyAPI.git
   cd ASPMicrodotServerSpotifyAPI
   ```

2. O projeto é dividido em duas partes:
   - **Servidor Microdot**: Arquivos para rodar no ESP32.
   - **API Intermediária**: Localizada na pasta `server`. Utilize o comando abaixo para instalar as dependências:
   ```bash
   cd server
   npm install
   ```
   Para iniciar a API, use:
   ```bash
   node index.js
   ```
   Os logs no terminal exibirão o IP e a porta de acesso.

## Configuração de Variáveis de Ambiente no ESP32

1. No arquivo `connectAsAp.py`, configure as variáveis `wifi` e `password` com o nome e a senha da rede Wi-Fi. Lembre-se que o ESP32 suporta apenas redes 2.4 GHz. Se a sua rede wifi só possui conexão 5G, será necessário criar uma sub-rede para dispositivos IoTs 2.4G nas configurações do seu roteador.

2. No arquivo `pagehome.py`, configure as variáveis `client_id` e `client_secret` com o ID e o segredo da sua aplicação do Spotify. Siga os passos abaixo para obter essas informações:
   - Acesse o [Spotify Developer Dashboard](https://developer.spotify.com/dashboard) e crie uma aplicação.
   - Copie o `Client ID` e o `Client Secret` e cole nas variáveis correspondentes.
   - Defina a URL de redirecionamento como `http://IP_DO_ESP32:PORT/callback`.

3. No mesmo arquivo, defina `url_api` com o IP e a porta da API intermediária e `redirect_uri` com a URL de redirecionamento configurada no Spotify.

## Transferência e Execução dos Arquivos no ESP32

1. Conecte o ESP32 ao computador e abra o Thonny.
2. Carregue todos os arquivos `.py` do diretório do projeto para o ESP32.
3. Execute o arquivo `main.py` diretamente pelo Thonny para iniciar o servidor Microdot.

## Testando a Aplicação

1. Abra seu Spotify app e coloque alguma música para tocar.
2. Verifique o IP do ESP32 na rede e acesse-o via navegador (exemplo: `http://192.168.0.10:8000`).
3. Realize o processo de autenticação do Spotify, seguindo o fluxo de autorização da API.
4. Utilize a interface para realizar ações como reproduzir e pausar músicas.

![Interface do nosso servidor web](https://cdn.discordapp.com/attachments/865710630833225748/1289202952707244072/image.png?ex=66f7f750&is=66f6a5d0&hm=479bf62d47eac5e08cc92f4a20334d2ec6d62204cf869f6b7ebb398c81bf553e&)

## Considerações Finais

Este projeto demonstra a integração do ESP32 com a API do Spotify utilizando uma abordagem criativa para contornar limitações de hardware. Diversas outras funcionalidades podem ser implementadas com base neste template, dependendo da criatividade e das necessidades do usuário.

## Créditos

Este projeto foi desenvolvido com base em um trabalho apresentado na disciplina de Computação Física e Aplicações, ministrada pelo Professor Fábio Nakano na Universidade de São Paulo, Campus USP Leste. A ideia inicial veio de um repositório criado pelo professor, ao qual eu dei continuidade e adaptei para um novo propósito.

- **Repositório Original**: [BasicESP32SetupWithMicropython](https://github.com/FNakano/CFA/tree/master/projetos/BasicESP32SetupWithMicropython)
- **Desenvolvido por**: Adryelli Reis, aluna de Graduação em Sistemas de Informação da Universidade de São Paulo.
- **Contribuidor** -[Edgar Lira](https://github.com/EdgarLiraa), aluno de Graduação em Sistemas de Informação da Universidade de São Paulo.

Agradeço ao Professor Fábio Nakano pelo conteúdo inspirador e suporte ao longo do curso.
