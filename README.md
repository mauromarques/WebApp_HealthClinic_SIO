## Autores
Mauro Filho, 103411  
Inês Santos, 102484   
Patrícia Cardoso, 103243

## Descrição
Este projeto tem como objetivo desenvolver uma aplicação web para uma clínica de saúde suscetível a vulnerabilidades, e posteriormente uma versão segura da mesma.
A aplicação é constituída pela página principal, "Home", que contém os serviços que a clínica disponibiliza, as especialidades a que se dedica, e os seus médicos. Para além disto, existe uma secção que permite ao utilizador entrar em contacto com a clínica. Esta secção denominada "Contact us" possui como campos, o nome do utilizador, email, assunto e a mensagem que pretende enviar. Todas as mensagens enviadas através da aplicação são salvas dentro de um diretório chamado "Contacts" no servidor, para que eventualmente outros funcionários da clínica possam ter acesso à esta informação e responder às mensagens enviadas.
Existe também, uma página que permite marcar consultas, escolhendo-se qual o serviço pretendido, o médico e a data. No entanto, um utilizador só pode marcar consultas se já tiver efetuado o login.
Para isso, existe a página "Log in to Patient Account". Uma vez feito o login, o utilizador é redirecionado para a página do seu perfil. Esta página contém o seu nome, o seu email e uma lista das suas consultas já agendadas. Para além disso, existem dois botões que permitem, fazer o download do resultado de um teste que o utilizador realizou, e o outro botão para fazer log out. Os ficheiros com os resultados dos testes são armazenados no servidor no diretório "TestResults", que seriam colocados lá por médicos da clínica a partir da sua própria versão da aplicação.

## Vulnerabilidades exploradas
[CWE-89: SQL injection](https://cwe.mitre.org/data/definitions/89.html)
O atacante injeta uma declaração SQL especial num campo de texto. Ao colocar sintaxe SQL em entradas controladas pelo utilizador, a query SQL gerada pode fazer com que o conteúdo dessas entradas seja interpretado como SQL em vez de dados comuns.

[CWE-79: Cross-site scripting](https://cwe.mitre.org/data/definitions/79.html)
São injetados scripts maliciosos em sites confiáveis. As falhas que permitem este tipo de ataque apenas implicam que exista um web request. Após o conteúdo entrar na aplicação,é gerada uma página que contém a informação não confiável.

[CWE-352: Cross-site request forgery](https://cwe.mitre.org/data/definitions/352.html)
A aplicação não verifica corretamente se um pedido foi enviado pelo utilizador. Assim, quando um servidor recebe um pedido sem possuir nenhum mecanismo para verificar a intencionalidade desse pedido, o atacante pode fazer com que o cliente envie um pedido não intencional.

[CWE-22: Improper Limitation of a Pathname to a Restricted Directory](https://cwe.mitre.org/data/definitions/22.html)
A aplicação utiliza input do utilizador para gerar um path para guardar um ficheiro. Esse input não é devidamente verificado, permitindo a que se guarde o ficheiro fora do diretório onde é suposto.

[CWE-798: Use of Hard-coded Credentials](https://cwe.mitre.org/data/definitions/798.html)
A aplicação protege os seus dados com recurso a cifras mas as suas chaves e/ou passwords encontram-se diretamente guardadas no código.

## Instruções de uso
1. Criar um virtual environment:
```bash
python3 -m venv venv
```

2. Ativar o virtual environment:
```bash
source venv/bin/activate
```

3. Atualizar pip para a versão mais recente
```bash
pip install --upgrade pip 
```

4. Instalar as bibliotecas necessárias:
```bash
pip3 install -r requirements.txt
```

5. Correr o servidor:
```bash
cd app
python3 app.py
```
ou 
```bash
cd app_sec
python3 app.py
```

6. Aceder ao endereço:

http://127.0.0.1:10009
