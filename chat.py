# -*- coding: utf-8 -*-
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

bot = ChatBot('MyChatBot')

conversa = ['Olá', 'Olá, tudo bem?', 'Tudo', 'Em que posso ajudar?', 'Você programa?', 'Sim, eu gosto mto de programar :)']

trainer = ListTrainer(bot)
trainer.train(conversa)

while True:
    pergunta = input('Você: ')
    resposta = bot.get_response(pergunta)

    if float(resposta.confidence) > 0.5:
        print('Bot: ', resposta)
    else: 
        print('Bot: Desculpe! Não entendi!')
