'''
Created on 15/10/2020

@author: eegomez
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select



class EncuestaCovid(unittest.TestCase):

    def setUp(self):
        global driver
        driver = webdriver.Chrome()
        driver.get("http://test-repoit.api.ifxcorp.com/")

        alerta = driver.switch_to.alert
        time.sleep(2)
        alerta.accept()
        
    def test1(self):
        
        pais =driver.find_element_by_id("subsidiaryList")
        if pais is not None:
            paisSel = Select(pais)
            paisSel.select_by_value("3")

        sucursal =driver.find_element_by_id("branchList")
        if sucursal is not None:
            sucursalSel = Select(sucursal)
            sucursalSel.select_by_value("Sede Cali")
        time.sleep(1)
        
        tipo =driver.find_element_by_id("typeVisit")
        if tipo is not None:
            tipoSel = Select(tipo)
            tipoSel.select_by_value("1")

        nombre = driver.find_element_by_id("employee")
        if nombre is not None:
            nombre.send_keys("Edisson Esteban Gomez Pinzon")       
        time.sleep(1)
        
        documentNumber = driver.find_element_by_id("documentNumber")
        if documentNumber is not None:
            documentNumber.send_keys("1030602922")
        time.sleep(1)

        temperatura =driver.find_element_by_id("temperature")
        if temperatura is not None:
            temperaturaSel = Select(temperatura)
            temperaturaSel.select_by_value("1")
        time.sleep(1)

        garganta =driver.find_element_by_id("garganta")
        if garganta is not None:
            gargantaSel = Select(garganta)
            gargantaSel.select_by_value("1")
        time.sleep(1)
        
        nasal =driver.find_element_by_id("nasal")
        if nasal is not None:
            nasalSel = Select(nasal)
            nasalSel.select_by_value("1")
        time.sleep(1)
        
        tos =driver.find_element_by_id("tos")
        if tos is not None:
            tosSel = Select(tos)
            tosSel.select_by_value("1")
        time.sleep(1)
        
        respirar =driver.find_element_by_id("respirar")
        if respirar is not None:
            respirarSel = Select(respirar)
            respirarSel.select_by_value("1")       
        time.sleep(1)
        
        fatiga =driver.find_element_by_id("fatiga")
        if fatiga is not None:
            fatigaSel = Select(fatiga)
            fatigaSel.select_by_value("1")   
        time.sleep(1)

        escalofrios =driver.find_element_by_id("escalofrios")
        if escalofrios is not None:
            escalofriosSel = Select(escalofrios)
            escalofriosSel.select_by_value("1")
        time.sleep(1)

        muscular =driver.find_element_by_id("muscular")
        if muscular is not None:
            muscularSel = Select(muscular)
            muscularSel.select_by_value("1")
        time.sleep(1)

        perdidaolfato =driver.find_element_by_id("perdidaolfato")
        if perdidaolfato is not None:
            perdidaolfatoSel = Select(perdidaolfato)
            perdidaolfatoSel.select_by_value("1")
        time.sleep(1)
        
        perdidasabor =driver.find_element_by_id("perdidasabor")
        if perdidasabor is not None:
            perdidasaborSel = Select(perdidasabor)
            perdidasaborSel.select_by_value("1")
        time.sleep(1)
        
        diarrea =driver.find_element_by_id("diarrea")
        if diarrea is not None:
            diarreaSel = Select(diarrea)
            diarreaSel.select_by_value("1")
        time.sleep(1)

        contactoSintomas =driver.find_element_by_id("contactoSintomas")
        if contactoSintomas is not None:
            contactoSintomasSel = Select(contactoSintomas)
            contactoSintomasSel.select_by_value("1")
        time.sleep(1)
        
        aislamiento =driver.find_element_by_id("aislamiento")
        if aislamiento is not None:
            aislamientoSel = Select(aislamiento)
            aislamientoSel.select_by_value("1")
        time.sleep(1)
        
        repatriado =driver.find_element_by_id("repatriado")
        if repatriado is not None:
            repatriadoSel = Select(repatriado)
            repatriadoSel.select_by_value("1")
        time.sleep(1)

        sospechaCovid =driver.find_element_by_id("sospechaCovid")
        if sospechaCovid is not None:
            sospechaCovidSel = Select(sospechaCovid)
            sospechaCovidSel.select_by_value("1")
        time.sleep(1)

        contactoCovid =driver.find_element_by_id("contactoCovid")
        if contactoCovid is not None:
            contactoCovidSel = Select(contactoCovid)
            contactoCovidSel.select_by_value("1")
        time.sleep(1)
        
        grados = driver.find_element_by_id("temperatureGrade")
        if grados is not None:
            grados.send_keys("37")
        time.sleep(1)
        
        comments = driver.find_element_by_id("comments")
        if comments is not None:
            comments.send_keys("Reunion con el cliente")    
        time.sleep(1)
        
        botonRegistrar = driver.find_element_by_css_selector(".btn")
        if botonRegistrar is not None:
           botonRegistrar.click()
        alerta = driver.switch_to.alert
        time.sleep(2)
        texto = alerta.text
        print("Prueba 1: flujo basico exitoso:", texto)
        alerta.accept()

    def test2(self):
        
        pais =driver.find_element_by_id("subsidiaryList")
        if pais is not None:
            paisSel = Select(pais)
            paisSel.select_by_value("3")

        sucursal =driver.find_element_by_id("branchList")
        if sucursal is not None:
            sucursalSel = Select(sucursal)
            sucursalSel.select_by_value("Sede Cali")
        time.sleep(1)
        
        tipo =driver.find_element_by_id("typeVisit")
        if tipo is not None:
            tipoSel = Select(tipo)
            tipoSel.select_by_value("1")

#        nombre = driver.find_element_by_id("employee")
#        if nombre is not None:
#            nombre.send_keys("Edisson Esteban Gomez Pinzon")       
#        time.sleep(1)
        
#        documentNumber = driver.find_element_by_id("documentNumber")
#        if documentNumber is not None:
#            documentNumber.send_keys("1030602922")
#        time.sleep(1)

        temperatura =driver.find_element_by_id("temperature")
        if temperatura is not None:
            temperaturaSel = Select(temperatura)
            temperaturaSel.select_by_value("1")
        time.sleep(1)

        garganta =driver.find_element_by_id("garganta")
        if garganta is not None:
            gargantaSel = Select(garganta)
            gargantaSel.select_by_value("1")
        time.sleep(1)
        
        nasal =driver.find_element_by_id("nasal")
        if nasal is not None:
            nasalSel = Select(nasal)
            nasalSel.select_by_value("1")
        time.sleep(1)
        
        tos =driver.find_element_by_id("tos")
        if tos is not None:
            tosSel = Select(tos)
            tosSel.select_by_value("1")
        time.sleep(1)
        
        respirar =driver.find_element_by_id("respirar")
        if respirar is not None:
            respirarSel = Select(respirar)
            respirarSel.select_by_value("1")       
        time.sleep(1)
        
        fatiga =driver.find_element_by_id("fatiga")
        if fatiga is not None:
            fatigaSel = Select(fatiga)
            fatigaSel.select_by_value("1")   
        time.sleep(1)

        escalofrios =driver.find_element_by_id("escalofrios")
        if escalofrios is not None:
            escalofriosSel = Select(escalofrios)
            escalofriosSel.select_by_value("1")
        time.sleep(1)

        muscular =driver.find_element_by_id("muscular")
        if muscular is not None:
            muscularSel = Select(muscular)
            muscularSel.select_by_value("1")
        time.sleep(1)

        perdidaolfato =driver.find_element_by_id("perdidaolfato")
        if perdidaolfato is not None:
            perdidaolfatoSel = Select(perdidaolfato)
            perdidaolfatoSel.select_by_value("1")
        time.sleep(1)
        
        perdidasabor =driver.find_element_by_id("perdidasabor")
        if perdidasabor is not None:
            perdidasaborSel = Select(perdidasabor)
            perdidasaborSel.select_by_value("1")
        time.sleep(1)
        
        diarrea =driver.find_element_by_id("diarrea")
        if diarrea is not None:
            diarreaSel = Select(diarrea)
            diarreaSel.select_by_value("1")
        time.sleep(1)

        contactoSintomas =driver.find_element_by_id("contactoSintomas")
        if contactoSintomas is not None:
            contactoSintomasSel = Select(contactoSintomas)
            contactoSintomasSel.select_by_value("1")
        time.sleep(1)
        
        aislamiento =driver.find_element_by_id("aislamiento")
        if aislamiento is not None:
            aislamientoSel = Select(aislamiento)
            aislamientoSel.select_by_value("1")
        time.sleep(1)
        
        repatriado =driver.find_element_by_id("repatriado")
        if repatriado is not None:
            repatriadoSel = Select(repatriado)
            repatriadoSel.select_by_value("1")
        time.sleep(1)

        sospechaCovid =driver.find_element_by_id("sospechaCovid")
        if sospechaCovid is not None:
            sospechaCovidSel = Select(sospechaCovid)
            sospechaCovidSel.select_by_value("1")
        time.sleep(1)

        contactoCovid =driver.find_element_by_id("contactoCovid")
        if contactoCovid is not None:
            contactoCovidSel = Select(contactoCovid)
            contactoCovidSel.select_by_value("1")
        time.sleep(1)
        
        grados = driver.find_element_by_id("temperatureGrade")
        if grados is not None:
            grados.send_keys("37")
        time.sleep(1)
        
        comments = driver.find_element_by_id("comments")
        if comments is not None:
            comments.send_keys("Reunion con el cliente")    
        time.sleep(1)
        
        botonRegistrar = driver.find_element_by_css_selector(".btn")
        if botonRegistrar is not None:
           botonRegistrar.click()
        alerta = driver.switch_to.alert
        time.sleep(2)
        texto = alerta.text
        print("Prueba 2: flujo con campos faltantes:", texto)
        alerta.accept()

    def tearDown(self):
        driver.quit()

if __name__ == "__main__":
   unittest.main()
