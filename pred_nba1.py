# -*- coding: utf-8 -*-
"""
Created on Thu Nov  4 09:48:45 2021
@author: Emmanuel Bonnet
"""
    
# Bibliotheques utilisés:
import pandas as pd
import numpy as np
import streamlit as st
import os #Miscellaneous operating system interfaces
#import cv2 #import OpenCV
#from sklearn import metrics
import matplotlib.pyplot as plt # Pour l'affichage d'images
from matplotlib import cm # Pour importer de nouvelles cartes de couleur
#import itertools # Pour créer des iterateurs
import streamlit as st
import matplotlib.image as mpimg
import PIL
from PIL import Image

# from sklearn.metrics import classification_report

st.set_option('deprecation.showPyplotGlobalUse', False)

###################
#PAGE CONFIGURATION
###################

st.set_page_config(page_title="Projet NBA", 
                   page_icon=":robot_face:",
                   layout="wide",
                   initial_sidebar_state="expanded"
                   )

#########
#SIDEBAR
########
new_title = '<p style="font-family:sans-serif; color:GREEN ; font-size: 42px;">etude données NBA</p>'
st.sidebar.title(new_title,"Projet d'étude prédictive de résultats sportifs NBA")
st.sidebar.write('')

st.sidebar.markdown("NBA Analyse & Prédictions")
st.sidebar.markdown("Emmanuel Bonnet")
st.sidebar.markdown('')
st.sidebar.markdown('')

st.sidebar.markdown("### ** Sommaire **")
navigation = st.sidebar.radio('',["Introduction", "Cas avec table de données unique : analyse des données & modèle primaire classification",  
                                  "Cas avec table de données unique : réalisation de dashboard et graphiques de confrontations",
                                  "Cas avec multi tables : classification non supervisée & supervisée"])  

#CONTACT
########
expander = st.sidebar.expander('SUPPORT')
expander.write("Lien GitHub : ... ")

if navigation == "Introduction":
    st.title("Présentation du projet")
    st.markdown("""
    <style>
    .big-font {
        font-size:20px !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <style>
    .big-font2 {
        font-size:30px !important;
    }
    </style>
    """, unsafe_allow_html=True)
 
    st.markdown('<p class="big-font2">Les techniques analyse exploratoire & modélisation des données historiques sont de plus en plus sollicitées par les entreprises pour: </p>', unsafe_allow_html=True)	
         
    st.markdown('<p class="big-font2"> Capitaliser au mieux le savoir-faire ainsi que les avantages concurrentiels </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">  Etre  précis dans la prédiction &/ou l’anticipation de résultats commerciaux, financiers et autres  </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">  Cibler les meilleurs plans actions possibles en vue de se renforcer et être plus performant que la concurrence </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font">  Ce projet s’inscrit dans le domaine du sport et particulièrement les données NBA récentes et moins récentes  </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font2"> l’objectif du projet est d’analyser les données disponibles sur la NBA.</p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font2"> en vue de la réalisation de modèles de prédiction de résultats pour la saison en cours 2021/2022 </p>', unsafe_allow_html=True)
                   
                     
if navigation == "Cas avec table de données unique : analyse des données & modèle primaire classification" :

    st.title('Cas simple - EDA')
    st.title('')
    st.title('')

    st.write('''
Cette première étape fait usage de méthodologies basiques d'analyse et modélisation des données par machine learning,
sans intégration de variables complémentaires métier potentiellement plus instructives,et sans usage de séries temporelles dans les modèles.

Cette première étape a pour unique vocation de se familiariser avec les nombreuses données NBA disponibles en Open Source
en vue de réaliser des premiers modèles simples et à représentativité limitée, car excluant de nombreux paramètres métiers et temporels
ayant un impact clé sur les résultats sportifs.     
        
Pour cette première étape de prise de connaissance des données NBA , les travaux suivants ont été réalisés'
            
 - Observation des données manquantes ainsi que des corrélations entre variables
 - Réalisation de modèles simples de classification et observations des résultats sous forme de courbes ROC & matrices de confusion
 - Sélection des variables les plus représentatives à l'aides des méthodologies RFE et Mutual information
            
             ''')

    st.title('')
    st.subheader("Illustration 1 : Table unique _ Données manquantes")
    image = Image.open('nba_simple_dataviz_1_nan.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("Illustration 2 : Table unique _ Analyse des corrélations entre variables")
    image = Image.open('nba_simple_dataviz_2_corr.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("Illustration 3 : Classifieur simple _ Courbe ROC")
    image = Image.open('nba_simple_dataviz_3_ROC_classifier1.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("Illustration 4 : Classifieur simple _ Sélection variables importantes NBA par RFE")
    image = Image.open('nba_simple_dataviz_4_RFE_classifier1.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("Illustration 5 : Classifieur simple _ Sélection variables importantes NBA par méthodologie Mutual Information")
    image = Image.open('nba_simple_dataviz_6_MUTUAL INFO VARIABLES.png')
    st.image(image, 300); 
    
    
    
if navigation == "Cas avec table de données unique : réalisation de dashboard et graphiques de confrontations" :
    st.markdown("""
    <style>
    .big-font3 {
        font-size:25px !important;
    }
    </style>
    """, unsafe_allow_html=True)
         
    st.markdown('<p class="big-font3"> Suite à la présélection des données importantes dans la section précédente </p>', unsafe_allow_html=True)	
    st.markdown('<p class="big-font3"> Réalisation de DASHBOARD HOME & AWAY sur ces données </p>', unsafe_allow_html=True)
    st.markdown('<p class="big-font3"> Illustration d’équipes sur une bonne dynamique ou en difficulté depuis 2 saisons</p>', unsafe_allow_html=True)
    
    st.title('')
    st.subheader("DASHBOARD HOME")
    image = Image.open('nba_simple_dataviz_8_DASHBOARD_HOME.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("DASHBOARD AWAY")
    image = Image.open('nba_simple_dataviz_8_DASHBOARD_HOME.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("Exemple d'équipe NBA sur une bonne dynamique : Los Angeles Clippers")
    image = Image.open('nba_simple_dataviz_10_LAC CONFRONTATIONS 2 ANS_HOME.png')
    st.image(image, 300);  
    
    st.title('')
    st.subheader("Exemple d'équipe NBA en difficulté : CHARLOTTE HORNETS")
    image = Image.open('nba_simple_dataviz_9_CHARLOTTE CONFRONTATIONS 2 ANS_HOME.png')
    st.image(image, 300);
    
    
if navigation == "Cas avec multi tables : classification non supervisée & supervisée" :
    
    
    st.title('Cas simple - EDA')
    st.title('')
    st.title('')

    st.write('''
Cette SECONDE étape fait usage de méthodologies plus avancées d'analyse et de modélisation des données par machine learning,
avec multi aggrégation des données disponible, pour la création et l’intégration de variables métiers complémentaires aux données d'entrainement des modèles,
ainsi que l'usage de données temporelles dans les modèles crées.

Cette seconde étape a donc pour vocation de trouver des modèles prédictifs les plus précis possibles à partir des nombreuses données NBA disponibles en Open Source
        
Pour cette seconde étape d'étude, les travaux suivants ont été réalisés'
            
 - Entrainement de modèle de machine learning non supervisé (type PCA ou Kmeans Clustering)
 - Création de nouvelles variables métiers à forte technicité (TEAM ELO RANKING, PLAYER EFFICIENCY, TEAM FATIGUE)
 - Entrainement de plusieurs modèles avec ces les nouvelles méta données d'entrainement'
            
             ''')
             
    #st.title('')
    #st.subheader("EXEMPLE HISTORIQUE TEMPOREL DES RESULTATS - NBA TEAMS")
    #image = Image.open('Historiques_résultats_1946_2021_FRANCHISES_CELEBRES.png')
    #st.image(image, 300);
      
    st.title('')
    st.subheader("ANALYSE EN COMPOSANTE PRINCIPALE - NBA PLAYERS")
    image = Image.open('nba_advanced_dataviz_11_PCA_PLAYERS.png')
    st.image(image, 300);
    
    st.title('')
    st.subheader("ANALYSE EN COMPOSANTE PRINCIPALE - NBA PLAYERS")
    image = Image.open('nba_advanced_dataviz_12_ELO_TEAM.png')
    st.image(image, 300);
    
    
    
    
    
    
