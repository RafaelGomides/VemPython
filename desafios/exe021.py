# Projeto: VemPython/exe021
# Autor: rafael
# Data: 14/03/18 - 11:38
# Objetivo: TODO Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3

import pygame

pygame.init()
pygame.mixer.music.load('exe021.mp3')
pygame.mixer.music.play()
pygame.event.wait()
