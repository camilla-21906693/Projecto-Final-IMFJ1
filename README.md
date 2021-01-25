 # Introdução à Matemática e Física Para Videojogos I - Projeto Final

## Introdução

​	Para a elaboração do projeto foi utilizado como base e referência o código disponibilizado no GitHub. Juntamente com as vídeo aulas disponibilizadas no moodle. 

​	Foi decidido que seria utilizado como modelos para o "viewer application" um tetraedro. Para a construção do mesmo foi utilizada a função mesh já existente para a criação de triângulos. 


## Descrição das soluções

​	Para o desenvolvimento das funcionalidades, primeiro utilizei a esfera disponibilizada no Github. Com esse modelo foram implementadas as funcionalidades pedidas.

​	Para a rotação do objeto foi pré-definido um ângulo referência de 15°. Com esse ângulo, há a verificação se o utilizador pressionou ou não as teclas para a a rotação do objeto. Enfim, para a rotação do objeto foram utilizadas vetores em 3D correspondentes aos eixos desejados para a rotação. 

​	Para a movimentação do objeto, foram utilizadas 3 variáveis (x,y e z) iniciadas em 0. Essas variáveis servem como base para o vetor 3D que o objeto encontra-se. Assim que o utilizador pressiona as teclas o objeto move-se uma distância de 0.1 na tela para a direção desejada. 


## Autópsia

​	Para a movimentação de acordo com o eixo Z foi encontrada uma exceção quanto a divisão por zero. Onde a exceção foi tratada nos *if* que verificam se a tecla e ou q foram pressionadas. Única movimentação que possui limite na aplicação para a aplicação funcionar sem *bugs*.

​	No começo do projeto também houve uma certa dificuldade na construção do tetraedro. Essa dificuldade pois não consegui instanciar os vetores em uma primeira tentativa na classe *mesh* da aplicação. Porém foi resolvido esse problema.

​	Uma das dificuldades que não consegui resolver foi definir o limite da movimentação do tetraedro de acordo com a resolução da janela. 


Nome e número: Camilla Faria Gomes - a21906693

Usuário GitHub: camilla-21906693