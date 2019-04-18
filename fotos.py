#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import PIL
import os
import json
from os import listdir, walk
from os.path import isfile, join


global config_json
data = {}
data['images'] = []
list_splash_android = ""
list_splash_ios = ""
log = ""


def write_config(line):
    line = str(line)
    #print log
    file = open("config.xml.log", "a")
    file.write(str(line)+"\n")
    file.close()


def read_icon():
    mi_path = "./resources/"
    for (path, ficheros, archivos) in walk(mi_path):
        if path == "./resources/android/icon":
            list_icon_android = archivos
        if path == "./resources/ios/icon":
            list_icon_ios = archivos

    for icon in list_icon_android:
        with Image.open("./resources/android/icon/"+icon) as img:
            width, height = img.size
            print icon + "-> " + str(width) + "x" + str(height)
            data['images'].append({
                'name': icon,
                'width': width,
                'height': height,
                'visible': True,
                'platform': "android",
                'type': "icono"
            })

    with open('json_iconos.json', 'w') as file:
        json.dump(data['images'], file)

    for icon in list_icon_ios:
        with Image.open("./resources/ios/icon/"+icon) as img:
            width, height = img.size
            print icon + "-> " + str(width) + "x" + str(height)
            data['images'].append({
                'name': icon,
                'width': width,
                'height': height,
                'visible': True,
                'platform': "ios",
                'type': "icono"
            })
        # json_str = json.dumps(datos)
    with open('json_iconos.json', 'w') as file:
        json.dump(data['images'], file)


def write_icon():
    with open('json_iconos.json') as file:
        config_json = json.load(file)

    for fotos in config_json:
        with open('icono.png', 'r+b') as f:
            if (fotos["platform"] == "android") & (str(fotos["type"]) == "icono"):
                w = fotos['width']
                h = fotos['height']
                try:
                    os.stat("./resources/android/myAndroidIcon/")
                except:
                    os.mkdir("./resources/android/myAndroidIcon/")
                with Image.open(f) as image:
                    newLogo = image.resize((w, h), Image.ANTIALIAS)
                    newLogo.save("./resources/android/myAndroidIcon/" +
                                 fotos['name'], image.format)
                f.close()
                log = "<icon src='./resources/android/icon/" +  fotos['name'] + "' />"
                write_config(log)

    for fotos in config_json:
        with open('icono.png', 'r+b') as f:
            if (fotos["platform"] == "ios") & (str(fotos["type"]) == "icono"):
                w = fotos['width']
                h = fotos['height']
                try:
                    os.stat("./resources/ios/myIosIcon/")
                except:
                    os.mkdir("./resources/ios/myIosIcon/")
                with Image.open(f) as image:
                    newLogo = image.resize((w, h), Image.ANTIALIAS)
                    newLogo.save("./resources/ios/myIosIcon/" +
                                 fotos['name'], image.format)
                f.close()
                log = "<icon src='./resources/ios/icon/" +  fotos['name'] + "' />"
                write_config(log)

    file = open("json_splash.json", "w")
    file.write("")
    file.close()


def read_splash():
    mi_path = "./resources/"
    for (path, ficheros, archivos) in walk(mi_path):
        if path == "./resources/android/splash":
            list_splash_android = archivos
        if path == "./resources/ios/splash":
            list_splash_ios = archivos
    #print list_splash_android
    for splash in list_splash_android:
        with Image.open("./resources/android/splash/"+splash) as img:
            width, height = img.size
            #print splash + "-> " + str(width) + "x" + str(height)
            data['images'].append({
                'name': splash,
                'width': width,
                'height': height,
                'visible': True,
                'platform': "android",
                'type': "splash"
            })
        with open('json_splash.json', 'w') as file:
            json.dump(data['images'], file)
    #print list_splash_ios
    for splash in list_splash_ios:
        with Image.open("./resources/ios/splash/"+splash) as img:
            width, height = img.size
            #print splash + "-> " + str(width) + "x" + str(height)
            data['images'].append({
                'name': splash,
                'width': width,
                'height': height,
                'visible': True,
                'platform': "ios",
                'type': "splash"
            })
        with open('json_splash.json', 'w') as file:
            json.dump(data['images'], file)


def write_splash():
    with open('json_splash.json') as file:
        config_json = json.load(file)

    for fotos in config_json:       
        if ((str(fotos["platform"]) == "android") & (str(fotos["type"]) == "splash")):          
            try:
                os.stat("./resources/android/myAndroidSplash/")
            except:
                os.mkdir("./resources/android/myAndroidSplash/")
            logo = Image.open('./logo.png', 'r')
            fondoW = int(fotos['width'])
            fondoH = int(fotos['height'])
            logoW, logoH = logo.size
            facLogo = int(logoW) / int(logoH)
            ProporcionBgLogo = 5
            color = (255, 255, 255, 255)

            newLogoH = fondoW / ProporcionBgLogo
            newLogoW = newLogoH * facLogo
            newLogo = logo.resize((newLogoW, newLogoH), Image.ANTIALIAS)

            fondo = Image.new('RGBA', (fondoW, fondoH), (color))

            centrado = ((fondoW - newLogoW) / 2, (fondoH - newLogoH) / 2)
            fondo.paste(newLogo, centrado, newLogo)
            fondo.save('./resources/android/myAndroidSplash/'+fotos['name'])
            log = "<icon src='./resources/android/splash/" + \
                fotos['name'] + "' />"
            write_config(log)

    for fotos in config_json:
        if ((str(fotos["platform"]) == "ios") & (str(fotos["type"]) == "splash")):          
            try:
                os.stat("./resources/ios/myIosSplash/")
            except:
                os.mkdir("./resources/ios/myIosSplash/")
            logo = Image.open('./logo.png', 'r')
            fondoW = int(fotos['width'])
            fondoH = int(fotos['height'])
            logoW, logoH = logo.size
            facLogo = int(logoW) / int(logoH)
            ProporcionBgLogo = 5
            color = (255, 255, 255, 255)

            newLogoH = fondoW / ProporcionBgLogo
            newLogoW = newLogoH * facLogo
            newLogo = logo.resize((newLogoW, newLogoH), Image.ANTIALIAS)

            fondo = Image.new('RGBA', (fondoW, fondoH), (color))

            centrado = ((fondoW - newLogoW) / 2, (fondoH - newLogoH) / 2)
            fondo.paste(newLogo, centrado, newLogo)
            fondo.save('./resources/ios/myIosSplash/'+fotos['name'])
            log = "<icon src='./resources/ios/splash/" + fotos['name'] + "' />"
            write_config(log)

read_icon()
write_icon()
read_splash()
write_splash()


