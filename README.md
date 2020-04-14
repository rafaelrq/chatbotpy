# Chatbot
ChatBot utilizando chatterBot

## Configurações
**Instalando o pip**

python3 -m pip install --user --upgrade pip

**Instalando o Virtualenv**

python3 -m pip install --user virtualenv

**Criando a VE**

python3 -m venv env (Para python2 utilze virtualenv, para python3 venv)

**Para ativar sua VE**

source env/bin/activate

**Sair da VE**

Para sair da VE basta digitar o comando "deactivate"

**Instalando o ChatterBot**

pip install chatterbot

## Desenvolvendo o seu chatbot
1. Importando o ChatBot e o ListTrainer

    ```python
    from chatterbot import ChatBot
    from chatterbot.trainers import ListTrainer
    ```

2. Definir instancia do ChatBot 

    ```python
    bot = ChatBot('MyChatBot')
    ```

3. definindo a variável de treinamento. Esta variável contém conversas para que o Bot faça o seu primeiro treinamento. Sendo que, elas trabalham em pares, primeira frase é par da segunda. Como se a primeira fosse uma pergunta e a segunda a resposta.

    ```python
    conversa = ['Olá', 'Olá, tudo bem?', 'Tudo', 'Em que posso ajudar?', 'Você programa?', 'Sim, eu gosto mto de programar :)']
    ```

4. Realizando treinamento
   
   ```python
    trainer = ListTrainer(bot)
    trainer.train(conversa)
    ```

5. Último passo é um loop para a interação entre o usuário e o Bot

    ```python
    while True:
        pergunta = input('Você: ')
        resposta = bot.get_response(pergunta)

        if float(resposta.confidence) > 0.5:
            print('Bot: ', resposta)
        else: 
            print('Bot: Desculpe! Não entendi!')
    ```

6. Executando o bot
    ```python
    python3 chat.py
    ```


## Referências 
Mais informações sobre o [ChatterBot](https://chatterbot.readthedocs.io/en/stable/index.html)