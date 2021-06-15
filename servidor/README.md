# Servidor de leitura

👋 Olá, Seja Bem-vindo(a) ao Servidor de leitura.

## Exigências

**:warning: Atenção:** É necessário que os desenvolvedores usem o Docker no seu ambiente de desenvolvimento.

- **🛠 Modo Desenvolvimento Docker**
    - :computer: [Linux Ubuntu LTS](https://ubuntu.com/download/desktop)
    - 🐳 [Docker](https://docs.docker.com/engine/installation/) Deve estar instalado.
    - 🐳 [Docker Compose](https://docs.docker.com/compose/) Deve estar instalado.
    - **💡 Dica:** [Documentação do Docker](https://docs.docker.com/)


## Instalando

### 🐳 Modo Desenvolvimento com Docker

Após instalar o docker e docker-compose, estando na pasta raiz do projeto, execute:

```sh
docker-compose up
```

Para se certificar que os seus containers subiram corretamente, todos os containers deve estar com o status `UP`, execute:

```sh
docker-compose ps -a
```

Para acessar o container da aplicação, execute:

```sh
docker-compose run --rm web bash
```

Para acessar a instância do banco de dados, execute:

```sh
docker exec -it [nome do db] bash
```

Para derrubar e subir a instância do docker novamente, execute:

```sh
docker-compose down && docker-compose up
```

🚀 :clap: Para visualizar o sistema basta acessar no navegador no endereço: [localhost:3000](localhost:3000) 


![servidor](https://raw.githubusercontent.com/claudimf/projeto_fatec/main/servidor/servidor.gif)

## Tecnologias utilizadas

- [Ruby on Rails 6.1.3 - Para a aplicação](https://api.rubyonrails.org/v6.1.3.2/)
- [HotWire Rails - Para a atualização dos dados](https://github.com/hotwired/hotwire-rails)
- [Redis 4.0 - Adaptador para rodar o Action Cable](https://github.com/redis/redis-rb)
- [Postgres 13.0 - Banco de dados](https://hub.docker.com/_/postgres)
- [Adaptador de Postgres para RoR versão 1.1](https://github.com/ged/ruby-pg)

## Referencias utilizadas:
[1° Rails 6.1 - Hotwire (Simple Realtime SPA)](https://btihen.me/post_ruby_rails/rails_6_1_hotwire_simple_realtime/)  
[2° Turbo Rails](https://github.com/hotwired/turbo-rails)  
[3° Atualização de 'partials' em tempo real utilizando Ruby On Rails](https://dev.to/mikerogers0/real-time-partial-updates-in-ruby-on-rails-using-hotwire-rails-1j1j)  
