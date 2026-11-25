# Olá, eu sou o Lucas 👋

Desenvolvedor **backend** em formação, focado em **Java e Spring Boot**. Gosto de construir APIs que resolvem
problemas reais, com a regra de negócio no lugar certo, testes que usam o banco de verdade e cuidado com segurança
desde o início.

🎯 Em busca de **estágio ou vaga júnior** em desenvolvimento backend.

## Stack

![Java](https://img.shields.io/badge/Java-ED8B00?style=flat-square&logo=openjdk&logoColor=white)
![Spring Boot](https://img.shields.io/badge/Spring_Boot-6DB33F?style=flat-square&logo=springboot&logoColor=white)
![Spring Security](https://img.shields.io/badge/Spring_Security-6DB33F?style=flat-square&logo=springsecurity&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Flyway](https://img.shields.io/badge/Flyway-CC0200?style=flat-square&logo=flyway&logoColor=white)
![JUnit 5](https://img.shields.io/badge/JUnit_5-25A162?style=flat-square&logo=junit5&logoColor=white)
![Testcontainers](https://img.shields.io/badge/Testcontainers-291A3F?style=flat-square)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub_Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![Git](https://img.shields.io/badge/Git-F05032?style=flat-square&logo=git&logoColor=white)

## Projeto em destaque

### [Marcai](https://github.com/lucasdanielalbanocorrea-coder/marcai)

API de agendamentos que **lembra o cliente pelo WhatsApp** e confirma ou cancela o horário a partir da resposta
dele. Feita para negócios que perdem dinheiro com faltas sem aviso, como salões, barbearias e clínicas.

- **Sem horários duplicados, mesmo com acessos simultâneos:** a regra fica no próprio PostgreSQL (constraint
  `EXCLUDE`), e não numa checagem no código que deixaria passar condições de corrida.
- **Integração com a WhatsApp Cloud API:** webhook com assinatura HMAC, idempotência e limite de tamanho.
- **Segurança:** OAuth2 (client credentials) e segredos validados na inicialização.
- **Qualidade:** 20 testes, com integração usando PostgreSQL real via Testcontainers, incluindo a jornada completa
  lembrete → resposta → confirmação, e CI no GitHub Actions.

`Java 27` · `Spring Boot 4` · `PostgreSQL 17` · `Flyway` · `Docker` · `Testcontainers`

## Próximos passos

- Evoluir o Marcai para atender **várias empresas** (multi-tenant), cada uma com o próprio número de WhatsApp.
- Preparar o sistema para rodar em **várias instâncias**: lock distribuído no agendador e chaves persistentes.

## Contato

Aberto a conversar sobre oportunidades de estágio e vagas júnior.

[![GitHub](https://img.shields.io/badge/GitHub-lucasdanielalbanocorrea--coder-181717?style=flat-square&logo=github)](https://github.com/lucasdanielalbanocorrea-coder)
<!-- Quando tiver, adicione aqui o LinkedIn:
[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square)](https://www.linkedin.com/in/SEU-USUARIO)
-->
