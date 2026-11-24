# Projeto DevOps: dupla-21

Site: https://ricardo2809.github.io/projeto-devops-dupla-21/ (status em /status.html)
Imagem: ghcr.io/ricardo2809/projeto-devops-dupla-21

## O fluxo completo
Ao realizar um `git push` na branch `main` ou publicar uma tag no padrão `v*`, o GitHub Actions inicia automaticamente o pipeline de CI/CD. Primeiro, o ambiente instala as dependências e executa a suíte de testes automatizados com `pytest`. Se os testes passam na `main`, o fluxo gera a página `status.html` atualizada e publica no GitHub Pages. Quando uma tag `v*` é enviada, o workflow constrói a imagem Docker injetando o nome da tag na variável `APP_VERSION` e publica no registro `ghcr.io`. Por fim, baixamos a imagem versionada com `docker pull` e subimos o contêiner na porta `5021` com `docker run`.

## Linha do tempo
- **v1:** Primeira versão estável da API publicada como imagem versionada no `ghcr.io`, escutando e respondendo corretamente na porta `5021`.
- **v2:** Simulação de falha com a alteração da porta interna da aplicação para `5022` sem ajustar o mapeamento do contêiner (`5021`); passou nos testes unitários, mas falhou ao responder requisições HTTP em execução.
- **v3:** Rollback definitivo no repositório por meio de `git revert` no commit da porta (`ac2d92a`), gerando o commit de reversão (`083c226`) e publicando uma nova imagem limpa respondendo novamente na porta `5021`.

## O que os testes não pegaram
Os testes unitários utilizam o `test_client()` do Flask em memória, validando o retorno das rotas diretamente no código Python sem subir o servidor HTTP real nem abrir portas de rede. Por isso, não detectaram a divergência entre a porta interna em que o Flask escutava (`5022`) e a porta externa mapeada pelo Docker (`5021`). Para capturar essa falha no pipeline antes da publicação, adicionaríamos um teste de integração que sobe o contêiner em segundo plano e executa uma requisição HTTP real (`curl`) no endpoint `/saude`.

## Quem fez o quê
- **Aluno A (Ricardo Mestre — `Ricardo2809`):** Atuei como dono do repositório `projeto-devops-dupla-21` na porta `5021`, configurei o fluxo de publicação contínua do site com página de status (`pages.yml`), ajustei as permissões de escrita e conferi a visibilidade pública da imagem no `ghcr.io`, executei o rollback operacional para a `v1`, realizei o rollback no repositório via `git revert` publicando a tag `v3` e estruturei o `README.md` final.
- **Aluno B (Leonardo Gil do Prado — `Lpleoo`):** Atuei como colaborador na `dupla-21` (porta `5021`), atualizei o `Dockerfile` com `ARG` e `ENV` para receber `APP_VERSION`, criei o workflow `publicar-imagem.yml` para construir e publicar imagens no `ghcr.io`, publiquei a tag inicial `v1`, simulei a falha de configuração alterando a porta da API para `5022` na tag `v2`, diagnostiquei o problema via `docker logs` e executei o rollback operacional de volta para a `v1`.