from keras.models import load_model 
from PIL import Image, ImageOps  
import numpy as np
from typing import Final
import telebot
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
import time
from caloriefinder import get_nutrient_info 
import random
from telebot import types
import pyodbc
import mysql.connector
from telebot.types import Message, Location,InlineKeyboardMarkup, InlineKeyboardButton
from conditions import conditions
import wikipedia
import requests
from bs4 import BeautifulSoup
from location import share_location