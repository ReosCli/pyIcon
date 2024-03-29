#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os, json
from PIL import Image
from os import listdir, walk
from os.path import isfile, join
data = {}
data['images'] = []

# Parametros editables
icono_original      = 'icon.png'    # min size 1024 x 1024
logo_original       = 'logo.jpg'    # min size 1024 x 1024
ProporcionBgLogo    = 5             # 5 = Escala 1:5 AnchoFondo:AnchoLogo
color_fondo         = (255, 255, 255, 255)

def write_config(line):
    line = str(line)
    print line
    file = open("config.xml.log", "a")
    file.write(str(line)+"\n")
    file.close()


def read_icon():
    try:
        os.remove('config.xml.log')
    except:
        pass
    mi_path = "./resources/"
    for (path, ficheros, archivos) in walk(mi_path):
        if path == "./resources/android/icon":
            list_icon_android = archivos
        if path == "./resources/ios/icon":
            list_icon_ios = archivos

    for icon in list_icon_android:
        with Image.open("./resources/android/icon/"+icon) as img:
            width, height = img.size
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
            data['images'].append({
                'name': icon,
                'width': width,
                'height': height,
                'visible': True,
                'platform': "ios",
                'type': "icono"
            })
    with open('json_iconos.json', 'w') as file:
        json.dump(data['images'], file)


def write_icon():
    with open('json_iconos.json') as file:
        config_json = json.load(file)
    write_config('<platform name="android">')
    for fotos in config_json:
        with open(icono_original, 'r+b') as f:
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
                log = '\t<icon src="./resources/android/icon/' +  fotos['name'] + '" platform="'+fotos['platform']+'" width="'+str(fotos['width'])+'" height="'+str(fotos['height'])+'" />'
                write_config(log)
    write_config('</platform>')

    write_config('<platform name="ios">')
    for fotos in config_json:
        with open(icono_original, 'r+b') as f:
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
                log = '\t<icon src="./resources/ios/icon/' +  fotos['name'] + '" platform="'+fotos['platform']+'" width="'+str(fotos['width'])+'" height="'+str(fotos['height'])+'" />'
                write_config(log)
    write_config('</platform>')
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

    for splash in list_splash_android:
        with Image.open("./resources/android/splash/"+splash) as img:
            width, height = img.size
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

    for splash in list_splash_ios:
        with Image.open("./resources/ios/splash/"+splash) as img:
            width, height = img.size
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
    color = color_fondo   
    with open('json_splash.json') as file:
        config_json = json.load(file)
        
    write_config('<platform name="android">')
    for fotos in config_json:       
        if ((str(fotos["platform"]) == "android") & (str(fotos["type"]) == "splash")):          
            try:
                os.stat("./resources/android/myAndroidSplash/")
            except:
                os.mkdir("./resources/android/myAndroidSplash/")

            logo = Image.open(logo_original, 'r')
            fondoW = int(fotos['width'])
            fondoH = int(fotos['height'])           
            logoW, logoH = logo.size                                    
            facLogo  =   float(logoW) / float(logoH)           
            newLogoH = fondoW / ProporcionBgLogo
            newLogoW = newLogoH * facLogo     
            newLogoH = int(newLogoH)
            newLogoW = int(newLogoW)   
            newLogo = logo.resize((newLogoW, newLogoH), Image.ANTIALIAS)    
            fondo = Image.new('RGBA', (fondoW, fondoH), (color))
            centrado = ((fondoW - newLogoW) / 2, (fondoH - newLogoH) / 2)            
            try:
                fondo.paste(newLogo, centrado, newLogo)
            except:
                fondo.paste(newLogo, centrado)
            fondo.save('./resources/android/myAndroidSplash/' + fotos['name'])
            fondo.close
            log = '\t<splash src="./resources/android/splash/'+  fotos['name'] + '" platform="'+fotos['platform']+'" width="'+str(fotos['width'])+'" height="'+str(fotos['height'])+'" />'          
            write_config(log)
    write_config('</platform>')
                
    
    write_config('<platform name="ios">')
    for fotos in config_json:
        if ((str(fotos["platform"]) == "ios") & (str(fotos["type"]) == "splash")):          
            try:
                os.stat("./resources/ios/myIosSplash/")
            except:
                os.mkdir("./resources/ios/myIosSplash/")

            logo = Image.open(logo_original, 'r')
            fondoW = int(fotos['width'])
            fondoH = int(fotos['height'])           
            logoW, logoH = logo.size         
            facLogo  =   float(logoW) / float(logoH)           
            newLogoH = fondoW / ProporcionBgLogo
            newLogoW = newLogoH * facLogo     
            newLogoH = int(newLogoH)
            newLogoW = int(newLogoW)   
            newLogo = logo.resize((newLogoW, newLogoH), Image.ANTIALIAS)    
            fondo = Image.new('RGBA', (fondoW, fondoH), (color))
            centrado = ((fondoW - newLogoW) / 2, (fondoH - newLogoH) / 2)
            try:
                fondo.paste(newLogo, centrado, newLogo)
            except:
                fondo.paste(newLogo, centrado)
            fondo.save('./resources/ios/myIosSplash/' + fotos['name'])
            fondo.close          
            log = '\t<splash src="./resources/ios/splash/' +  fotos['name'] + '" platform="'+fotos['platform']+'" width="'+str(fotos['width'])+'" height="'+str(fotos['height'])+'" />'
            write_config(log)
    write_config("</platform>")





read_icon()
write_icon()
read_splash()
write_splash()


