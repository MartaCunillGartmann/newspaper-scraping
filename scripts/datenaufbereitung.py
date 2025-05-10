# datenaufbereitung.py

"""Hilfsfunktionen zur Datenaufbereitung für Pressemitteilungen (z. B. BVG)

Dieses Modul enthält Funktionen zum Einlesen, Bereinigen und Verarbeiten von
HTML-Dokumenten sowie zur Zählung von Wörtern. Es kann in Textanalysen, 
Explorationen und Pre-Processing-Pipelines verwendet werden.
"""

import os
import pandas as pd
import requests
from bs4 import BeautifulSoup


def load_stopwords(url=None):
    """Lädt eine Liste deutscher Stoppwörter von GitHub

    Die Datei enthält allgemeine Stoppwörter zur Textbereinigung. Die ersten
    9 Zeilen der Datei werden übersprungen, da sie Kommentare enthalten.

    Args:
        url (str, optional): URL zur Textdatei. Falls None, wird eine Standardquelle verwendet.

    Returns:
        list: Liste von Stoppwörtern als Strings
    """
    if url is None:
        url = "https://raw.githubusercontent.com/solariz/german_stopwords/master/german_stopwords_full.txt"
    response = requests.get(url, allow_redirects=True)
    return response.text.split("\n")[9:]


def read_html_file(filepath, encoding="utf-8"):
    """Liest eine HTML-Datei als Textstring

    Args:
        filepath (str): Pfad zur HTML-Datei
        encoding (str): Zeichenkodierung (Standard: 'utf-8')

    Returns:
        str: Inhalt der HTML-Datei als Text
    """
    with open(filepath, "r", encoding=encoding) as f:
        return f.read()


def process_html(html, stopwords_list):
    """Bereinigt HTML-Text und extrahiert Wörter

    Wandelt den HTML-Inhalt in Kleinbuchstaben um, entfernt Stoppwörter und 
    sehr kurze Wörter (1 Zeichen). Der sichtbare Text wird aus dem HTML-Dokument
    extrahiert und in Wörter aufgeteilt.

    Args:
        html (str): HTML-Inhalt als Text
        stopwords_list (list): Liste mit Stoppwörtern

    Returns:
        list: Wörterliste ohne Stoppwörter
    """
    soup = BeautifulSoup(html, "html.parser")
    text = soup.get_text(separator=" ").lower()
    tokens = text.replace("\n", " ").split(" ")
    return [t for t in tokens if len(t) > 1 and t not in stopwords_list]

def extract_date_from_html(html):
    soup = BeautifulSoup(html, "html.parser")
    time_tag = soup.find("time")

    if time_tag and time_tag.has_attr("datetime"):
        date_str = time_tag["datetime"][:10]
        year = int(date_str.split("-")[0])
    else:
        date_str = None
        year = None

    return date_str, year

