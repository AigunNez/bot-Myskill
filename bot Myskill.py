from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import *
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

email = 'emailpengguna@gmail.com' #Ubah dengan email masing masing
password = 'password123' #Ubah dengan password masing masing
url_kelas = 'https://myskill.id/learning-path/web-development' #Ubah dengan url kelas yang ingin di automitation

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=options)
driver.maximize_window()
driver.get("https://myskill.id")

time.sleep(3)
tombol_masuk = driver.find_element(By.CLASS_NAME,'mui-style-5fgit3')
tombol_masuk.click()
time.sleep(2)

input_email = driver.find_element(By.NAME, 'email')
input_email.send_keys(email)
input_password = driver.find_element(By.NAME, 'password')
input_password.send_keys(password)

tombol_submit = driver.find_element(By.CLASS_NAME, 'mui-style-s0sm1c')
tombol_submit.click()
time.sleep(5)

driver.get(url_kelas)
time.sleep(5)

def fungsi_durasi():
    tag_video = driver.find_element(By.CLASS_NAME, 'video-container')
    frame_video = tag_video.find_element(By.TAG_NAME, "iframe")
    # frame_video.click()

    driver.switch_to.frame(frame_video)

    coba = driver.find_element(By.TAG_NAME, 'player-ui')
    coba.click()
    time.sleep(2)
    video_dur = driver.execute_script("durasi = document.getElementsByTagName('video')[0].duration")
    time.sleep(2)
    durasi = driver.execute_script("return durasi")
    # print(durasi)
    driver.switch_to.default_content()

    return durasi

def fungsi_jawab():
    tag_soal = driver.find_element(By.CLASS_NAME, 'mui-style-dxv8f')
    data_soal = tag_soal.find_elements(By.CLASS_NAME, 'mui-style-0')

    for index, soal in enumerate(data_soal):
        tombol_jawaban = soal.find_elements(By.CLASS_NAME, 'mui-style-r0az20')

        tombol_jawaban[jawaban_soal[index]].click()

    tombol_selesai = driver.find_element(By.CLASS_NAME, 'mui-style-ttn2kv')
    tombol_selesai.click()

    time.sleep(5)
    nilai_jawaban = driver.find_element(By.CLASS_NAME, 'mui-style-qwujcl')
    nilai_jawaban2 = nilai_jawaban.find_element(By.CLASS_NAME, 'mui-style-b48cml')
    nilai_jawaban3 = nilai_jawaban2.find_elements(By.TAG_NAME, 'b')

    return nilai_jawaban3[2].text

def jawab_pertanyaan(tag):
    tag_kuis = driver.find_element(By.CLASS_NAME, tag)
    tag_kuis2 = tag_kuis.find_element(By.CLASS_NAME, 'mui-style-16hplqz')

    tag_nilai = tag_kuis2.find_element(By.CLASS_NAME, 'mui-style-tavflp')
    nilai = tag_nilai.text

    if not nilai.isnumeric():
        nilai = 0
    nilai = int(nilai)

    if nilai < 99:
        tag_kuis2.click()
        while nilai < 99:
            
            nilai = int(fungsi_jawab())
            tag_hasil = driver.find_element(By.CLASS_NAME, 'mui-style-dxv8f')
            data_hasil = tag_hasil.find_elements(By.CLASS_NAME, 'mui-style-0')
            # print(len(data_hasil), "halo")
            for index, data in enumerate(data_hasil):
                benarsalah = data.find_element(By.CLASS_NAME, 'mui-style-14vsv3w')
                if benarsalah.text == "SALAH":
                    # print(index)
                    jawaban_soal[index] += 1
                print(f"{index}. {benarsalah.text}")

            tombol_ulang = driver.find_element(By.CLASS_NAME, 'mui-style-1de6l4i')
            tombol_ulang.click()

        tombol_tutup = driver.find_element(By.CLASS_NAME, 'mui-style-l8h9j8')
        tombol_tutup.click()
    else :
        print("Nilai Sempurna")

def selesaikan_topik():
    total_kelas1 = driver.find_element(By.CLASS_NAME, 'mui-style-1los5ln')
    total_kelas2 = total_kelas1.find_elements(By.CLASS_NAME, 'mui-style-17pejtx')
    total_kelas = len(total_kelas2)
    print(total_kelas)

    while True:
        no_stop = 1
        bool_stop = False
        try:   
            for i in range(total_kelas):
                tag_materi = driver.find_element(By.CLASS_NAME, 'mui-style-w42d5a')
                data_materi1 = tag_materi.find_elements(By.CLASS_NAME, 'mui-style-1bmfbzd')

                for index, data_m in enumerate(data_materi1):
                    try:
                        box_centang1 = data_m.find_element(By.CLASS_NAME, "mui-style-g4v1us")
                        box_centang2 = box_centang1.find_element(By.CLASS_NAME, "mui-style-1dtrpo5")
                        # print(data.get_attribute('outerHTML'))

                        time.sleep(4)
                        box_centang2.click()

                        time.sleep(10)

                        durasi = int(fungsi_durasi()) + 20
                        # durasi = 10
                        
                        time.sleep(durasi)
                    except NoSuchElementException:
                        # print(index, " The element does not exist.")
                        pass

                time.sleep(5)
                cek_soal1 = driver.find_element(By.CLASS_NAME, 'mui-style-afroy3')
                cek_soal2 = cek_soal1.find_element(By.CLASS_NAME, 'mui-style-16hplqz')
                time.sleep(1)
                cek_soal2.click()

                total_soal1 = driver.find_element(By.CLASS_NAME, 'mui-style-dxv8f')
                total_soal2 = total_soal1.find_elements(By.CLASS_NAME, 'mui-style-0')

                tombol_tutup = driver.find_element(By.CLASS_NAME, 'mui-style-l8h9j8')
                tombol_tutup.click()

                time.sleep(2)

                global jawaban_soal 
                jawaban_soal = [0 for i in range(len(total_soal2))]
                    
                driver.switch_to.default_content()

                jawab_pertanyaan('mui-style-afroy3')
                jawab_pertanyaan('mui-style-12wznnp')

                time.sleep(5)
                

                driver.refresh()
                time.sleep(15)
                tag_kelas = driver.find_element(By.CLASS_NAME, 'mui-style-1los5ln')
                data_materi2 = tag_kelas.find_elements(By.CLASS_NAME, 'mui-style-17pejtx')
                no_ulang = 0
                for index, data in enumerate(data_materi2):
                    # print(index, '. ', data.get_attribute('innerHTML'))

                    persen_kelas = int(data.find_element(By.CLASS_NAME, 'mui-style-2c61ct').text[:-1])

                    if persen_kelas < 99:
                        tujuan_kelas = data.find_element(By.CLASS_NAME, 'mui-style-1rdvs08')
                        print(tujuan_kelas.get_attribute('href'))
                        # time.sleep(2)
                        driver.get(tujuan_kelas.get_attribute('href'))
                        break
                    time.sleep(1)
                    print(f'{len(data_materi2)} dan {no_ulang}')
                    no_ulang += 1
                if no_ulang == len(data_materi2):
                    print("selesai")
                    bool_stop = True
                    break

                time.sleep(30)
                no_stop += 1
        except:
            print('sesuatu error')
            driver.refresh()
            time.sleep(30)
        if no_stop == total_kelas or bool_stop == True:
            break
    driver.get(url_kelas)

data_topik = driver.find_elements(By.CLASS_NAME, 'mui-style-rcalj5')[2].find_elements(By.CLASS_NAME, 'mui-style-0')
url_topik = [isi.find_element(By.CLASS_NAME, 'mui-style-14zznec').get_attribute("href") for isi in data_topik]
for index, data in enumerate(data_topik):
    print(url_topik[index], end=" ")
    driver.get(url_topik[index])

    time.sleep(5)
    progress_sertif = driver.find_element(By.CLASS_NAME, 'mui-style-1izjpte').text[:-1]
    if int(progress_sertif) < 99:
        print("Progress belum selesai")
        url_materi = driver.find_elements(By.CLASS_NAME, 'mui-style-1rdvs08')[0].get_attribute('href')
        driver.get(url_materi)
        time.sleep(5)
        selesaikan_topik()
    else:
        print("Topik sudah selesai")
driver.get(url_kelas)