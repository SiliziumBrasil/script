import pandas as pd
import time
import os
import random
import re
import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException

# --- CONFIGURAÇÕES PRINCIPAIS ---
LISTA_DE_CIDADES = [
"Abdon Batista - SC",
"Abelardo Luz - SC",
"Agrolandia - SC",
"Agronomica - SC",
"Agua Doce - SC",
"Aguas de Chapeco - SC",
"Aguas Frias - SC",
"Aguas Mornas - SC",
"Alfredo Wagner - SC",
"Alto Bela Vista - SC",
"Anchieta - SC",
"Angelina - SC",
"Anita Garibaldi - SC",
"Anitapolis - SC",
"Antonio Carlos - SC",
"Apiuna - SC",
"Arabuta - SC",
"Araquari - SC",
"Ararangua - SC",
"Armazem - SC",
"Arroio Trinta - SC",
"Arvoredo - SC",
"Ascurra - SC",
"Atalanta - SC",
"Aurora - SC",
"Balneario Arroio do Silva - SC",
"Balneario Barra do Sul - SC",
"Balneario Camboriu - SC",
"Balneario Gaivota - SC",
"Balneario Picarras - SC",
"Balneario Rincao - SC",
"Bandeirante - SC",
"Barra Bonita - SC",
"Barra Velha - SC",
"Bela Vista do Toldo - SC",
"Belmonte - SC",
"Benedito Novo - SC",
"Biguacu - SC",
"Blumenau - SC",
"Bocaina do Sul - SC",
"Bom Jardim da Serra - SC",
"Bom Jesus - SC",
"Bom Jesus do Oeste - SC",
"Bom Retiro - SC",
"Bombinhas - SC",
"Botuvera - SC",
"Braco do Norte - SC",
"Braco do Trombudo - SC",
"Brunopolis - SC",
"Brusque - SC",
"Cacador - SC",
"Caibi - SC",
"Calmon - SC",
"Camboriu - SC",
"Campo Alegre - SC",
"Campo Belo do Sul - SC",
"Campo Ere - SC",
"Campos Novos - SC",
"Canelinha - SC",
"Canoinhas - SC",
"Capao Alto - SC",
"Capinzal - SC",
"Capivari de Baixo - SC",
"Catanduvas - SC",
"Caxambu do Sul - SC",
"Celso Ramos - SC",
"Cerro Negro - SC",
"Chapadao do Lageado - SC",
"Chapeco - SC",
"Cocal do Sul - SC",
"Concordia - SC",
"Cordilheira Alta - SC",
"Coronel Freitas - SC",
"Coronel Martins - SC",
"Correia Pinto - SC",
"Corupa - SC",
"Criciuma - SC",
"Cunha Pora - SC",
"Cunhatai - SC",
"Curitibanos - SC",
"Descanso - SC",
"Dionisio Cerqueira - SC",
"Dona Emma - SC",
"Doutor Pedrinho - SC",
"Entre Rios - SC",
"Ermo - SC",
"Erval Velho - SC",
"Faxinal dos Guedes - SC",
"Flor do Sertao - SC",
"Florianopolis - SC",
"Formosa do Sul - SC",
"Forquilhinha - SC",
"Fraiburgo - SC",
"Frei Rogerio - SC",
"Galvao - SC",
"Garopaba - SC",
"Garuva - SC",
"Gaspar - SC",
"Governador Celso Ramos - SC",
"Grao Para - SC",
"Gravatal - SC",
"Guabiruba - SC",
"Guaraciaba - SC",
"Guaramirim - SC",
"Guaruja do Sul - SC",
"Guatambu - SC",
"Herval d Oeste - SC",
"Ibiam - SC",
"Ibicare - SC",
"Ibirama - SC",
"Icara - SC",
"Ilhota - SC",
"Imarui - SC",
"Imbituba - SC",
"Imbuia - SC",
"Indaial - SC",
"Iomere - SC",
"Ipira - SC",
"Ipora do Oeste - SC",
"Ipuacu - SC",
"Ipumirim - SC",
"Iraceminha - SC",
"Irani - SC",
"Irati - SC",
"Irineopolis - SC",
"Ita - SC",
"Itaiopolis - SC",
"Itajai - SC",
"Itapema - SC",
"Itapiranga - SC",
"Itapoa - SC",
"Ituporanga - SC",
"Jabora - SC",
"Jacinto Machado - SC",
"Jaguaruna - SC",
"Jaragua do Sul - SC",
"Jardinopolis - SC",
"Joacaba - SC",
"Joinville - SC",
"Jose Boiteux - SC",
"Jupia - SC",
"Lacerdopolis - SC",
"Lages - SC",
"Laguna - SC",
"Lajeado Grande - SC",
"Laurentino - SC",
"Lauro Muller - SC",
"Lebon Regis - SC",
"Leoberto Leal - SC",
"Lindoia do Sul - SC",
"Lontras - SC",
"Luiz Alves - SC",
"Luzerna - SC",
"Macieira - SC",
"Mafra - SC",
"Major Gercino - SC",
"Major Vieira - SC",
"Maracaja - SC",
"Maravilha - SC",
"Marema - SC",
"Massaranduba - SC",
"Matos Costa - SC",
"Meleiro - SC",
"Mirim Doce - SC",
"Modelo - SC",
"Mondai - SC",
"Monte Carlo - SC",
"Monte Castelo - SC",
"Morro da Fumaca - SC",
"Morro Grande - SC",
"Navegantes - SC",
"Nova Erechim - SC",
"Nova Itaberaba - SC",
"Nova Trento - SC",
"Nova Veneza - SC",
"Novo Horizonte - SC",
"Orleans - SC",
"Otacilio Costa - SC",
"Ouro - SC",
"Ouro Verde - SC",
"Paial - SC",
"Painel - SC",
"Palhoca - SC",
"Palma Sola - SC",
"Palmeira - SC",
"Palmitos - SC",
"Papanduva - SC",
"Paraiso - SC",
"Passo de Torres - SC",
"Passos Maia - SC",
"Paulo Lopes - SC",
"Pedras Grandes - SC",
"Penha - SC",
"Peritiba - SC",
"Pescaria Brava - SC",
"Petrolandia - SC",
"Pinhalzinho - SC",
"Pinheiro Preto - SC",
"Piratuba - SC",
"Planalto Alegre - SC",
"Pomerode - SC",
"Ponte Alta - SC",
"Ponte Alta do Norte - SC",
"Ponte Serrada - SC",
"Porto Belo - SC",
"Porto Uniao - SC",
"Pouso Redondo - SC",
"Praia Grande - SC",
"Presidente Castello Branco - SC",
"Presidente Getulio - SC",
"Presidente Nereu - SC",
"Princesa - SC",
"Quilombo - SC",
"Rancho Queimado - SC",
"Rio das Antas - SC",
"Rio do Campo - SC",
"Rio do Oeste - SC",
"Rio do Sul - SC",
"Rio dos Cedros - SC",
"Rio Fortuna - SC",
"Rio Negrinho - SC",
"Rio Rufino - SC",
"Riqueza - SC",
"Rodeio - SC",
"Romelandia - SC",
"Salete - SC",
"Saltinho - SC",
"Salto Veloso - SC",
"Sangao - SC",
"Santa Cecilia - SC",
"Santa Helena - SC",
"Santa Rosa de Lima - SC",
"Santa Rosa do Sul - SC",
"Santa Terezinha - SC",
"Santa Terezinha do Progresso - SC",
"Santiago do Sul - SC",
"Santo Amaro da Imperatriz - SC",
"Sao Bento do Sul - SC",
"Sao Bernardino - SC",
"Sao Bonifacio - SC",
"Sao Carlos - SC",
"Sao Cristovao do Sul - SC",
"Sao Domingos - SC",
"Sao Francisco do Sul - SC",
"Sao Joao Batista - SC",
"Sao Joao do Itaperiu - SC",
"Sao Joao do Oeste - SC",
"Sao Joao do Sul - SC",
"Sao Joaquim - SC",
"Sao Jose - SC",
"Sao Jose do Cedro - SC",
"Sao Jose do Cerrito - SC",
"Sao Lourenco do Oeste - SC",
"Sao Ludgero - SC",
"Sao Martinho - SC",
"Sao Miguel da Boa Vista - SC",
"Sao Miguel do Oeste - SC",
"Sao Pedro de Alcantara - SC",
"Saudades - SC",
"Schroeder - SC",
"Seara - SC",
"Serra Alta - SC",
"Sideropolis - SC",
"Sombrio - SC",
"Sul Brasil - SC",
"Taio - SC",
"Tangara - SC",
"Tigrinhos - SC",
"Tijucas - SC",
"Timbe do Sul - SC",
"Timbo - SC",
"Timbo Grande - SC",
"Tres Barras - SC",
"Treviso - SC",
"Treze de Maio - SC",
"Treze Tilias - SC",
"Trombudo Central - SC",
"Tubarao - SC",
"Tunapolis - SC",
"Turvo - SC",
"Uniao do Oeste - SC",
"Urubici - SC",
"Urupema - SC",
"Urussanga - SC",
"Vargeao - SC",
"Vargem - SC",
"Vargem Bonita - SC",
"Vidal Ramos - SC",
"Videira - SC",
"Vitor Meireles - SC",
"Witmarsum - SC",
"Xanxere - SC",
"Xavantina - SC",
"Xaxim - SC",
"Zortea - SC"

]

TERMOS_DE_BUSCA = ["Energia solar", "Fornecedor de equipamentos de energia solar", "Instalação de placa solar", "Empresas de painel solar"]

COORDENADAS_CIDADES = {
"Abdon Batista - SC": {"latitude": -27.61, "longitude": -51.02},
"Abelardo Luz - SC": {"latitude": -26.57, "longitude": -52.32},
"Agrolandia - SC": {"latitude": -27.41, "longitude": -49.82},
"Agronomica - SC": {"latitude": -27.27, "longitude": -49.71},
"Agua Doce - SC": {"latitude": -27.00, "longitude": -51.55},
"Aguas de Chapeco - SC": {"latitude": -27.08, "longitude": -52.98},
"Aguas Frias - SC": {"latitude": -26.88, "longitude": -52.86},
"Aguas Mornas - SC": {"latitude": -27.70, "longitude": -48.82},
"Alfredo Wagner - SC": {"latitude": -27.70, "longitude": -49.33},
"Alto Bela Vista - SC": {"latitude": -27.43, "longitude": -51.90},
"Anchieta - SC": {"latitude": -26.54, "longitude": -53.33},
"Angelina - SC": {"latitude": -27.57, "longitude": -48.99},
"Anita Garibaldi - SC": {"latitude": -27.69, "longitude": -51.13},
"Anitapolis - SC": {"latitude": -27.90, "longitude": -49.13},
"Antonio Carlos - SC": {"latitude": -27.52, "longitude": -48.77},
"Apiuna - SC": {"latitude": -2.70, "longitude": -49.39},
"Arabuta - SC": {"latitude": -27.16, "longitude": -52.14},
"Araquari - SC": {"latitude": -26.38, "longitude": -48.72},
"Ararangua - SC": {"latitude": -28.94, "longitude": -49.49},
"Armazem - SC": {"latitude": -28.25, "longitude": -49.02},
"Arroio Trinta - SC": {"latitude": -26.93, "longitude": -51.34},
"Arvoredo - SC": {"latitude": -27.08, "longitude": -52.45},
"Ascurra - SC": {"latitude": -26.96, "longitude": -49.38},
"Atalanta - SC": {"latitude": -27.42, "longitude": -49.78},
"Aurora - SC": {"latitude": -27.31, "longitude": -0.00},
"Balneario Arroio do Silva - SC": {"latitude": -28.98, "longitude": -49.42},
"Balneario Barra do Sul - SC": {"latitude": -26.46, "longitude": -48.61},
"Balneario Camboriu - SC": {"latitude": -26.99, "longitude": -48.64},
"Balneario Gaivota - SC": {"latitude": -29.15, "longitude": -49.58},
"Balneario Picarras - SC": {"latitude": -26.77, "longitude": -48.68},
"Balneario Rincao - SC": {"latitude": -28.80, "longitude": -49.24},
"Bandeirante - SC": {"latitude": -2.68, "longitude": -53.64},
"Barra Bonita - SC": {"latitude": -26.65, "longitude": -53.44},
"Barra Velha - SC": {"latitude": -26.64, "longitude": -48.69},
"Bela Vista do Toldo - SC": {"latitude": -26.28, "longitude": -50.47},
"Belmonte - SC": {"latitude": -26.84, "longitude": -53.58},
"Benedito Novo - SC": {"latitude": -26.78, "longitude": -49.36},
"Biguacu - SC": {"latitude": -27.50, "longitude": -48.66},
"Blumenau - SC": {"latitude": -2.69, "longitude": -49.07},
"Bocaina do Sul - SC": {"latitude": -2.77, "longitude": -49.94},
"Bom Jardim da Serra - SC": {"latitude": -28.34, "longitude": -49.64},
"Bom Jesus - SC": {"latitude": -26.73, "longitude": -52.39},
"Bom Jesus do Oeste - SC": {"latitude": -26.69, "longitude": -53.10},
"Bom Retiro - SC": {"latitude": -27.80, "longitude": -49.49},
"Bombinhas - SC": {"latitude": -27.14, "longitude": -4.85},
"Botuvera - SC": {"latitude": -27.20, "longitude": -49.07},
"Braco do Norte - SC": {"latitude": -28.27, "longitude": -49.17},
"Braco do Trombudo - SC": {"latitude": -27.36, "longitude": -49.88},
"Brunopolis - SC": {"latitude": -27.31, "longitude": -50.84},
"Brusque - SC": {"latitude": -27.10, "longitude": -48.91},
"Cacador - SC": {"latitude": -26.78, "longitude": -51.01},
"Caibi - SC": {"latitude": -27.07, "longitude": -53.25},
"Calmon - SC": {"latitude": -26.59, "longitude": -51.10},
"Camboriu - SC": {"latitude": -27.02, "longitude": -48.65},
"Campo Alegre - SC": {"latitude": -26.20, "longitude": -4.93},
"Campo Belo do Sul - SC": {"latitude": -2.79, "longitude": -0.01},
"Campo Ere - SC": {"latitude": -26.39, "longitude": -53.09},
"Campos Novos - SC": {"latitude": -27.40, "longitude": -5.12},
"Canelinha - SC": {"latitude": -27.26, "longitude": -48.77},
"Canoinhas - SC": {"latitude": -26.18, "longitude": -50.40},
"Capao Alto - SC": {"latitude": -27.94, "longitude": -50.51},
"Capinzal - SC": {"latitude": -27.35, "longitude": -51.61},
"Capivari de Baixo - SC": {"latitude": -28.45, "longitude": -48.96},
"Catanduvas - SC": {"latitude": -27.07, "longitude": -51.66},
"Caxambu do Sul - SC": {"latitude": -27.16, "longitude": -52.88},
"Celso Ramos - SC": {"latitude": -27.63, "longitude": -51.34},
"Cerro Negro - SC": {"latitude": -27.79, "longitude": -50.87},
"Chapadao do Lageado - SC": {"latitude": -2.76, "longitude": -49.55},
"Chapeco - SC": {"latitude": -27.10, "longitude": -52.62},
"Cocal do Sul - SC": {"latitude": -28.60, "longitude": -4.93},
"Concordia - SC": {"latitude": -27.23, "longitude": -52.03},
"Cordilheira Alta - SC": {"latitude": -26.98, "longitude": -5.26},
"Coronel Freitas - SC": {"latitude": -26.91, "longitude": -52.70},
"Coronel Martins - SC": {"latitude": -26.51, "longitude": -52.67},
"Correia Pinto - SC": {"latitude": -27.59, "longitude": -50.36},
"Corupa - SC": {"latitude": -26.43, "longitude": -49.25},
"Criciuma - SC": {"latitude": -28.67, "longitude": -49.37},
"Cunha Pora - SC": {"latitude": -26.90, "longitude": -53.17},
"Cunhatai - SC": {"latitude": -26.97, "longitude": -53.09},
"Curitibanos - SC": {"latitude": -27.28, "longitude": -50.58},
"Descanso - SC": {"latitude": -26.83, "longitude": -53.50},
"Dionisio Cerqueira - SC": {"latitude": -26.27, "longitude": -53.64},
"Dona Emma - SC": {"latitude": -26.98, "longitude": -49.73},
"Doutor Pedrinho - SC": {"latitude": -26.72, "longitude": -49.48},
"Entre Rios - SC": {"latitude": -26.72, "longitude": -5.26},
"Ermo - SC": {"latitude": -28.99, "longitude": -49.64},
"Erval Velho - SC": {"latitude": -27.27, "longitude": -51.44},
"Faxinal dos Guedes - SC": {"latitude": -26.85, "longitude": -52.26},
"Flor do Sertao - SC": {"latitude": -26.78, "longitude": -53.35},
"Florianopolis - SC": {"latitude": -27.60, "longitude": -48.55},
"Formosa do Sul - SC": {"latitude": -26.65, "longitude": -52.80},
"Forquilhinha - SC": {"latitude": -28.75, "longitude": -49.48},
"Fraiburgo - SC": {"latitude": -27.02, "longitude": -50.92},
"Frei Rogerio - SC": {"latitude": -27.18, "longitude": -50.81},
"Galvao - SC": {"latitude": -26.46, "longitude": -5.27},
"Garopaba - SC": {"latitude": -28.03, "longitude": -48.62},
"Garuva - SC": {"latitude": -26.03, "longitude": -48.85},
"Gaspar - SC": {"latitude": -26.93, "longitude": -48.95},
"Governador Celso Ramos - SC": {"latitude": -27.32, "longitude": -4.86},
"Grao Para - SC": {"latitude": -28.18, "longitude": -49.23},
"Gravatal - SC": {"latitude": -28.32, "longitude": -49.04},
"Guabiruba - SC": {"latitude": -27.08, "longitude": -48.98},
"Guaraciaba - SC": {"latitude": -26.60, "longitude": -53.52},
"Guaramirim - SC": {"latitude": -26.47, "longitude": -49.00},
"Guaruja do Sul - SC": {"latitude": -26.39, "longitude": -0.01},
"Guatambu - SC": {"latitude": -27.13, "longitude": -52.79},
"Herval d Oeste - SC": {"latitude": -27.19, "longitude": -51.49},
"Ibiam - SC": {"latitude": -27.19, "longitude": -51.24},
"Ibicare - SC": {"latitude": -27.09, "longitude": -51.37},
"Ibirama - SC": {"latitude": -27.06, "longitude": -49.52},
"Icara - SC": {"latitude": -28.71, "longitude": -49.31},
"Ilhota - SC": {"latitude": -26.90, "longitude": -48.83},
"Imarui - SC": {"latitude": -28.33, "longitude": -48.82},
"Imbituba - SC": {"latitude": -28.23, "longitude": -48.67},
"Imbuia - SC": {"latitude": -27.49, "longitude": -49.42},
"Indaial - SC": {"latitude": -26.90, "longitude": -49.24},
"Iomere - SC": {"latitude": -27.00, "longitude": -51.24},
"Ipira - SC": {"latitude": -27.40, "longitude": -51.78},
"Ipora do Oeste - SC": {"latitude": -26.99, "longitude": -53.54},
"Ipuacu - SC": {"latitude": -26.63, "longitude": -52.46},
"Ipumirim - SC": {"latitude": -27.08, "longitude": -52.13},
"Iraceminha - SC": {"latitude": -2.68, "longitude": -53.28},
"Irani - SC": {"latitude": -27.03, "longitude": -51.90},
"Irati - SC": {"latitude": -26.65, "longitude": -5.29},
"Irineopolis - SC": {"latitude": -26.24, "longitude": -50.80},
"Ita - SC": {"latitude": -27.28, "longitude": -52.33},
"Itaiopolis - SC": {"latitude": -26.34, "longitude": -49.91},
"Itajai - SC": {"latitude": -26.91, "longitude": -48.67},
"Itapema - SC": {"latitude": -27.09, "longitude": -48.62},
"Itapiranga - SC": {"latitude": -27.17, "longitude": -53.72},
"Itapoa - SC": {"latitude": -26.12, "longitude": -48.62},
"Ituporanga - SC": {"latitude": -27.42, "longitude": -49.60},
"Jabora - SC": {"latitude": -27.17, "longitude": -51.74},
"Jacinto Machado - SC": {"latitude": -29.00, "longitude": -49.76},
"Jaguaruna - SC": {"latitude": -28.62, "longitude": -0.00},
"Jaragua do Sul - SC": {"latitude": -26.49, "longitude": -49.07},
"Jardinopolis - SC": {"latitude": -26.72, "longitude": -5.29},
"Joacaba - SC": {"latitude": -27.17, "longitude": -51.51},
"Joinville - SC": {"latitude": -2.63, "longitude": -48.85},
"Jose Boiteux - SC": {"latitude": -2.70, "longitude": -49.63},
"Jupia - SC": {"latitude": -26.40, "longitude": -52.73},
"Lacerdopolis - SC": {"latitude": -27.26, "longitude": -51.56},
"Lages - SC": {"latitude": -27.82, "longitude": -50.33},
"Laguna - SC": {"latitude": -28.48, "longitude": -48.78},
"Lajeado Grande - SC": {"latitude": -26.86, "longitude": -52.57},
"Laurentino - SC": {"latitude": -27.22, "longitude": -49.73},
"Lauro Muller - SC": {"latitude": -28.39, "longitude": -49.40},
"Lebon Regis - SC": {"latitude": -26.93, "longitude": -50.69},
"Leoberto Leal - SC": {"latitude": -27.51, "longitude": -49.28},
"Lindoia do Sul - SC": {"latitude": -27.05, "longitude": -52.08},
"Lontras - SC": {"latitude": -27.17, "longitude": -49.54},
"Luiz Alves - SC": {"latitude": -26.72, "longitude": -48.93},
"Luzerna - SC": {"latitude": -27.13, "longitude": -51.47},
"Macieira - SC": {"latitude": -26.86, "longitude": -5.14},
"Mafra - SC": {"latitude": -26.12, "longitude": -49.81},
"Major Gercino - SC": {"latitude": -27.42, "longitude": -48.95},
"Major Vieira - SC": {"latitude": -26.37, "longitude": -5.03},
"Maracaja - SC": {"latitude": -28.85, "longitude": -4.95},
"Maravilha - SC": {"latitude": -2.68, "longitude": -53.17},
"Marema - SC": {"latitude": -26.80, "longitude": -52.63},
"Massaranduba - SC": {"latitude": -26.61, "longitude": -49.01},
"Matos Costa - SC": {"latitude": -26.47, "longitude": -51.15},
"Meleiro - SC": {"latitude": -28.82, "longitude": -49.64},
"Mirim Doce - SC": {"latitude": -27.20, "longitude": -50.07},
"Modelo - SC": {"latitude": -26.77, "longitude": -53.04},
"Mondai - SC": {"latitude": -27.10, "longitude": -53.40},
"Monte Carlo - SC": {"latitude": -27.22, "longitude": -50.98},
"Monte Castelo - SC": {"latitude": -26.46, "longitude": -50.23},
"Morro da Fumaca - SC": {"latitude": -28.65, "longitude": -49.22},
"Morro Grande - SC": {"latitude": -28.80, "longitude": -49.72},
"Navegantes - SC": {"latitude": -26.89, "longitude": -4.87},
"Nova Erechim - SC": {"latitude": -26.90, "longitude": -5.29},
"Nova Itaberaba - SC": {"latitude": -26.94, "longitude": -52.81},
"Nova Trento - SC": {"latitude": -27.28, "longitude": -48.93},
"Nova Veneza - SC": {"latitude": -28.63, "longitude": -4.95},
"Novo Horizonte - SC": {"latitude": -26.44, "longitude": -52.83},
"Orleans - SC": {"latitude": -28.35, "longitude": -49.30},
"Otacilio Costa - SC": {"latitude": -27.48, "longitude": -50.12},
"Ouro - SC": {"latitude": -27.34, "longitude": -51.62},
"Ouro Verde - SC": {"latitude": -26.69, "longitude": -52.31},
"Paial - SC": {"latitude": -27.25, "longitude": -5.25},
"Painel - SC": {"latitude": -27.92, "longitude": -50.10},
"Palhoca - SC": {"latitude": -2.76, "longitude": -48.67},
"Palma Sola - SC": {"latitude": -26.35, "longitude": -53.28},
"Palmeira - SC": {"latitude": -27.58, "longitude": -50.16},
"Palmitos - SC": {"latitude": -27.07, "longitude": -53.16},
"Papanduva - SC": {"latitude": -26.41, "longitude": -50.14},
"Paraiso - SC": {"latitude": -26.62, "longitude": -53.67},
"Passo de Torres - SC": {"latitude": -29.31, "longitude": -49.72},
"Passos Maia - SC": {"latitude": -26.78, "longitude": -52.06},
"Paulo Lopes - SC": {"latitude": -27.96, "longitude": -48.67},
"Pedras Grandes - SC": {"latitude": -28.43, "longitude": -49.20},
"Penha - SC": {"latitude": -26.78, "longitude": -48.65},
"Peritiba - SC": {"latitude": -27.38, "longitude": -51.90},
"Pescaria Brava - SC": {"latitude": -2.84, "longitude": -48.88},
"Petrolandia - SC": {"latitude": -27.54, "longitude": -49.69},
"Pinhalzinho - SC": {"latitude": -0.00, "longitude": -52.99},
"Pinheiro Preto - SC": {"latitude": -27.04, "longitude": -51.23},
"Piratuba - SC": {"latitude": -27.42, "longitude": -51.77},
"Planalto Alegre - SC": {"latitude": -27.07, "longitude": -52.87},
"Pomerode - SC": {"latitude": -26.74, "longitude": -49.18},
"Ponte Alta - SC": {"latitude": -2.75, "longitude": -50.38},
"Ponte Alta do Norte - SC": {"latitude": -27.16, "longitude": -50.47},
"Ponte Serrada - SC": {"latitude": -26.87, "longitude": -52.01},
"Porto Belo - SC": {"latitude": -27.16, "longitude": -48.55},
"Porto Uniao - SC": {"latitude": -26.25, "longitude": -51.08},
"Pouso Redondo - SC": {"latitude": -27.26, "longitude": -49.93},
"Praia Grande - SC": {"latitude": -29.20, "longitude": -49.95},
"Presidente Castello Branco - SC": {"latitude": -27.23, "longitude": -51.80},
"Presidente Getulio - SC": {"latitude": -27.04, "longitude": -4.96},
"Presidente Nereu - SC": {"latitude": -27.28, "longitude": -49.39},
"Princesa - SC": {"latitude": -26.44, "longitude": -53.60},
"Quilombo - SC": {"latitude": -26.73, "longitude": -52.72},
"Rancho Queimado - SC": {"latitude": -27.67, "longitude": -49.02},
"Rio das Antas - SC": {"latitude": -26.90, "longitude": -51.07},
"Rio do Campo - SC": {"latitude": -26.95, "longitude": -50.14},
"Rio do Oeste - SC": {"latitude": -27.20, "longitude": -49.80},
"Rio do Sul - SC": {"latitude": -27.22, "longitude": -49.64},
"Rio dos Cedros - SC": {"latitude": -26.74, "longitude": -49.27},
"Rio Fortuna - SC": {"latitude": -28.12, "longitude": -49.11},
"Rio Negrinho - SC": {"latitude": -26.26, "longitude": -49.52},
"Rio Rufino - SC": {"latitude": -27.86, "longitude": -49.78},
"Riqueza - SC": {"latitude": -27.07, "longitude": -53.33},
"Rodeio - SC": {"latitude": -26.92, "longitude": -49.37},
"Romelandia - SC": {"latitude": -26.68, "longitude": -53.32},
"Salete - SC": {"latitude": -26.98, "longitude": -50.00},
"Saltinho - SC": {"latitude": -26.61, "longitude": -53.06},
"Salto Veloso - SC": {"latitude": -26.90, "longitude": -51.40},
"Sangao - SC": {"latitude": -28.63, "longitude": -49.13},
"Santa Cecilia - SC": {"latitude": -26.96, "longitude": -50.43},
"Santa Helena - SC": {"latitude": -26.94, "longitude": -53.62},
"Santa Rosa de Lima - SC": {"latitude": -28.03, "longitude": -49.13},
"Santa Rosa do Sul - SC": {"latitude": -29.14, "longitude": -49.71},
"Santa Terezinha - SC": {"latitude": -26.78, "longitude": -50.01},
"Santa Terezinha do Progresso - SC": {"latitude": -26.62, "longitude": -53.20},
"Santiago do Sul - SC": {"latitude": -26.64, "longitude": -52.68},
"Santo Amaro da Imperatriz - SC": {"latitude": -27.69, "longitude": -48.78},
"Sao Bento do Sul - SC": {"latitude": -0.00, "longitude": -49.38},
"Sao Bernardino - SC": {"latitude": -26.47, "longitude": -52.97},
"Sao Bonifacio - SC": {"latitude": -27.90, "longitude": -4.89},
"Sao Carlos - SC": {"latitude": -27.08, "longitude": -53.00},
"Sao Cristovao do Sul - SC": {"latitude": -27.27, "longitude": -50.44},
"Sao Domingos - SC": {"latitude": -26.56, "longitude": -52.53},
"Sao Francisco do Sul - SC": {"latitude": -26.26, "longitude": -48.63},
"Sao Joao Batista - SC": {"latitude": -27.28, "longitude": -48.85},
"Sao Joao do Itaperiu - SC": {"latitude": -26.62, "longitude": -48.77},
"Sao Joao do Oeste - SC": {"latitude": -27.10, "longitude": -53.60},
"Sao Joao do Sul - SC": {"latitude": -29.22, "longitude": -49.80},
"Sao Joaquim - SC": {"latitude": -28.29, "longitude": -49.95},
"Sao Jose - SC": {"latitude": -27.59, "longitude": -4.86},
"Sao Jose do Cedro - SC": {"latitude": -26.46, "longitude": -53.50},
"Sao Jose do Cerrito - SC": {"latitude": -27.66, "longitude": -50.57},
"Sao Lourenco do Oeste - SC": {"latitude": -26.36, "longitude": -52.85},
"Sao Ludgero - SC": {"latitude": -28.31, "longitude": -49.18},
"Sao Martinho - SC": {"latitude": -28.16, "longitude": -48.99},
"Sao Miguel da Boa Vista - SC": {"latitude": -26.69, "longitude": -53.25},
"Sao Miguel do Oeste - SC": {"latitude": -26.72, "longitude": -53.52},
"Sao Pedro de Alcantara - SC": {"latitude": -2.76, "longitude": -48.81},
"Saudades - SC": {"latitude": -26.93, "longitude": -53.00},
"Schroeder - SC": {"latitude": -26.41, "longitude": -49.07},
"Seara - SC": {"latitude": -27.16, "longitude": -52.30},
"Serra Alta - SC": {"latitude": -26.72, "longitude": -53.04},
"Sideropolis - SC": {"latitude": -2.86, "longitude": -49.43},
"Sombrio - SC": {"latitude": -29.11, "longitude": -49.63},
"Sul Brasil - SC": {"latitude": -26.74, "longitude": -52.96},
"Taio - SC": {"latitude": -27.12, "longitude": -50.00},
"Tangara - SC": {"latitude": -27.10, "longitude": -51.25},
"Tigrinhos - SC": {"latitude": -26.69, "longitude": -5.32},
"Tijucas - SC": {"latitude": -27.24, "longitude": -48.63},
"Timbe do Sul - SC": {"latitude": -28.83, "longitude": -49.84},
"Timbo - SC": {"latitude": -26.83, "longitude": -49.27},
"Timbo Grande - SC": {"latitude": -26.61, "longitude": -50.66},
"Tres Barras - SC": {"latitude": -26.11, "longitude": -50.32},
"Treviso - SC": {"latitude": -28.51, "longitude": -49.46},
"Treze de Maio - SC": {"latitude": -28.55, "longitude": -4.92},
"Treze Tilias - SC": {"latitude": -27.00, "longitude": -51.41},
"Trombudo Central - SC": {"latitude": -27.30, "longitude": -49.79},
"Tubarao - SC": {"latitude": -28.47, "longitude": -49.01},
"Tunapolis - SC": {"latitude": -26.97, "longitude": -53.64},
"Turvo - SC": {"latitude": -28.93, "longitude": -49.68},
"Uniao do Oeste - SC": {"latitude": -26.76, "longitude": -52.85},
"Urubici - SC": {"latitude": -28.02, "longitude": -4.96},
"Urupema - SC": {"latitude": -27.96, "longitude": -49.87},
"Urussanga - SC": {"latitude": -28.52, "longitude": -49.32},
"Vargeao - SC": {"latitude": -26.86, "longitude": -52.16},
"Vargem - SC": {"latitude": -27.49, "longitude": -50.97},
"Vargem Bonita - SC": {"latitude": -27.01, "longitude": -51.74},
"Vidal Ramos - SC": {"latitude": -27.39, "longitude": -49.36},
"Videira - SC": {"latitude": -27.01, "longitude": -51.15},
"Vitor Meireles - SC": {"latitude": -26.88, "longitude": -49.83},
"Witmarsum - SC": {"latitude": -2.69, "longitude": -49.80},
"Xanxere - SC": {"latitude": -26.88, "longitude": -5.24},
"Xavantina - SC": {"latitude": -27.07, "longitude": -52.34},
"Xaxim - SC": {"latitude": -26.96, "longitude": -52.54},
"Zortea - SC": {"latitude": -27.45, "longitude": -51.55}

}
NOME_ARQUIVO_FINAL = "contatos_versao_finalSC.xlsx"

# --- AJUSTE DE EFICIÊNCIA ---
# Interromper a busca para uma cidade após X resultados errados seguidos.
LIMITE_DESCARTES = 5
# ---------------------------------

def inicializar_driver_zerado():
    print("   Iniciando uma instância de navegador zerada (em modo oculto)...")
    options = webdriver.ChromeOptions()
    
    # --- ALTERAÇÕES AQUI ---
    options.add_argument("--headless")  # Executa o Chrome em modo headless (sem interface gráfica)
    options.add_argument("--disable-gpu") # Necessário em alguns sistemas ao usar o modo headless
    options.add_argument("--window-size=1920,1080") # Define um tamanho de janela para evitar problemas de layout
    # -----------------------

    options.add_argument("--lang=pt-BR")
    options.add_argument("--incognito")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    
    driver = webdriver.Chrome(options=options)
    return driver

def set_geolocation(driver, lat, long):
    params = {"latitude": lat, "longitude": long, "accuracy": 100}
    driver.execute_cdp_cmd("Emulation.setGeolocationOverride", params)

def normalize_text(text):
    if not text: return ""
    nfkd_form = unicodedata.normalize('NFKD', text.lower())
    return "".join([c for c in nfkd_form if not unicodedata.combining(c)])

def buscar_dados_com_endereco(driver, wait):
    nome, telefone, endereco = "Não encontrado", "Não encontrado", "Não encontrado"
    try:
        nome = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h1"))).text
    except: pass
    try:
        buttons = driver.find_elements(By.CSS_SELECTOR, "button[data-item-id]")
        for btn in buttons:
            aria_label = btn.get_attribute('aria-label'); data_id = btn.get_attribute('data-item-id')
            if not aria_label: continue
            if data_id and 'phone:tel:' in data_id:
                telefone = aria_label.strip().replace('Telefone: ', ''); continue
            if 'Endereço:' in aria_label:
                endereco = aria_label.replace('Endereço:', '').strip()
    except: pass
    return nome, telefone, endereco

def salvar_em_excel_consolidado(novos_dados, nome_arquivo):
    if not novos_dados: return
    df_novos = pd.DataFrame(novos_dados)
    if os.path.exists(nome_arquivo):
        df_existente = pd.read_excel(nome_arquivo)
        df_final = pd.concat([df_existente, df_novos], ignore_index=True)
    else:
        df_final = df_novos
    df_final.drop_duplicates(subset=["Nome da Empresa", "Telefone"], keep='last', inplace=True)
    df_final.to_excel(nome_arquivo, index=False)
    print(f"   Dados salvos! O arquivo agora tem {len(df_final)} contatos validados.")

def processar_cidade_definitivo(driver, wait, cidade_alvo, termo_de_busca, coords):
    print(f"   Processando '{cidade_alvo}' com a estratégia definitiva...")
    
    print(f"      1. Isolando o mapa em '{cidade_alvo}'...")
    driver.get("https://www.google.com/maps")
    try:
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchboxinput")))
        search_box.clear(); time.sleep(0.5)
        search_box.send_keys(cidade_alvo); search_box.send_keys(Keys.RETURN)
        time.sleep(random.uniform(9, 12))
    except Exception as e:
        print(f"      ! Falha ao isolar a cidade: {e}"); return []

    print(f"      2. Forjando a localização GPS do navegador para '{cidade_alvo}'...")
    set_geolocation(driver, coords['latitude'], coords['longitude'])

    termo_completo = f"{termo_de_busca} em {cidade_alvo}"
    print(f"      3. Buscando por '{termo_completo}' com GPS forjado...")
    try:
        search_box = wait.until(EC.element_to_be_clickable((By.ID, "searchboxinput")))
        search_box.clear(); time.sleep(0.5)
        search_box.send_keys(termo_completo); search_box.send_keys(Keys.RETURN)
        # PAUSA ESTRATÉGICA ADICIONAL PARA CIDADES GRANDES
        print("      Aguardando página de resultados carregar...")
        time.sleep(random.uniform(8, 12))
    except Exception as e:
        print(f"      ! Falha ao buscar o termo: {e}"); return []

    print("      4. Coletando e validando dados...")
    links_visitados, dados_validados = [], []
    cidade_pura = re.split(r'\s*-\s*', cidade_alvo)[0].strip()
    try:
        scroll_panel = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'div[role="feed"]')))
        while True:
            resultados = driver.find_elements(By.CSS_SELECTOR, 'a[href*="/maps/place/"]')
            links_antes = len(links_visitados)
            for r in resultados:
                try:
                    link = r.get_attribute('href')
                    if link and link not in links_visitados: links_visitados.append(link)
                except: continue
            if len(links_visitados) == links_antes and len(links_visitados) > 0: break
            driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", scroll_panel)
            time.sleep(random.uniform(3, 5))
            try:
                if driver.find_element(By.XPATH, '//*[contains(text(), "Você chegou ao final da lista")]'): break
            except NoSuchElementException: continue
    except:
        print(f"      Nenhum resultado para '{cidade_alvo}'."); return []

    descartes_consecutivos = 0
    for link in links_visitados:
        try:
            driver.get(link)
            time.sleep(random.uniform(1.5, 2.5))
            nome, telefone, endereco = buscar_dados_com_endereco(driver, wait)
            if normalize_text(cidade_pura) in normalize_text(endereco):
                print(f"         > VÁLIDO: {nome} | {telefone}")
                dados_validados.append({"Termo de Busca": termo_de_busca, "Nome da Empresa": nome, "Telefone": telefone, "Cidade Alvo": cidade_alvo, "Endereço Verificado": endereco})
                descartes_consecutivos = 0
            else:
                if nome != "Não encontrado":
                     print(f"         > DESCARTADO: {nome} (Endereço em outra cidade)")
                descartes_consecutivos += 1
            
            if descartes_consecutivos >= LIMITE_DESCARTES:
                print(f"\n      !! ATENÇÃO: Atingido o limite de {LIMITE_DESCARTES} resultados consecutivos de outras cidades.")
                print("      Interrompendo a busca nesta cidade para otimizar o tempo.")
                break
        except: continue
    return dados_validados

if __name__ == "__main__":
    for cidade in LISTA_DE_CIDADES:
        for termo in TERMOS_DE_BUSCA:
            print(f"\n--- INICIANDO CICLO | CIDADE: {cidade} | TERMO: {termo} ---")
            if cidade not in COORDENADAS_CIDADES:
                print(f"   ! Coordenadas para '{cidade}' não encontradas. Pulando.")
                continue
            driver = None
            try:
                driver = inicializar_driver_zerado()
                # AUMENTANDO O TEMPO DE ESPERA PRINCIPAL
                wait = WebDriverWait(driver, 30) # <-- MUDANÇA AQUI (DE 20 PARA 30)
                dados = processar_cidade_definitivo(driver, wait, cidade, termo, COORDENADAS_CIDADES[cidade])
                if dados:
                    salvar_em_excel_consolidado(dados, NOME_ARQUIVO_FINAL)
            except Exception as e:
                print(f"!! ERRO CRÍTICO NO CICLO: {e} !!")
            finally:
                if driver:
                    driver.quit()
                print(f"--- CICLO FINALIZADO | CIDADE: {cidade} | TERMO: {termo} ---")
    print("\n\n--- PROCESSO TOTALMENTE FINALIZADO ---")