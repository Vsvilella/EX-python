from time import sleep
import emoji
for contagem in range(10, -1, -1):
    print(contagem, end=' ')
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVO :boom:',use_aliases=True))