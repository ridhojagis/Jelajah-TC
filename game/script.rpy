# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character(("Aris"), color= "#ceffc8")
define i = Character("Pak Imam")
define b = Character("Bu Kantin")

default makan = False
default buang_air = False
default shalat_dhuhur = False
default shalat_ashar = False
default parkir = False
default lantai = 1

default myClock = Clock(True, 8, 0, 150, False, False) #Analogue or Digital, hours, minutes, size, second hand, military time

screen clock_screen:
    add myClock:
        xalign 1.0
        yalign 0.0

# The game starts here.
label start:

    play music "/audio/Cheery Monday.mp3"

    scene fsm_jelajah_tc1
    with fade

    "Berikut adalah FSM Jelajah-TC"
    with PushMove(1, "pushup")

    scene fsm_jelajah_tc2
    with Pause(5)

    "Dibuat oleh: \n\n05111940000071 - Daffa Amanullah Setyawan \n05111940000170 - Ridho Ajiraga Jagiswara"

    scene bg jalan

    "Selamat datang di game Jelajah-TC"
    "Pada game ini kamu akan berperan sebagai Aris, mahasiswa Teknik Informatika"
    "Kamu diharuskan untuk menghadiri kelas Sistem Game pada sore hari untuk melaksanakan ujian dan mendapat nilai bagus"
    "Agar ujianmu lancar, kamu harus menyelesaikan beberapa kegiatan sebelum masuk kelas"
    "Untuk mengetahui waktu saat ini, kamu dapat melihat jam yang ada di kanan atas."

    # menampilkan jam analog
    show screen clock_screen
    with Dissolve(1)

    "Waktu saat ini menunjukkan pukul 8 pagi"
    "Karena sebelumnya telah libur panjang selama 2 minggu, Aris datang di pagi hari untuk melihat-lihat keadaan kampus."

    scene bg gerbang_dpt1
    with fade

    a "Wahh sudah lama rasanya sejak terakhir kali ke kampus"
    a "Masih seperti biasa.."
    a "Keadaan sekitar kampus selalu bersih dan hijau."

    scene bg gerbang_dpt2
    with fade

    with Pause(5)

    scene bg parkir_mobil1
    with fade

    "Dengan kendaraan motornya, Aris mulai memasuki gerbang."

    play sound "/audio/motorcycle-arrive-and-shut-off-01.mp3"

    scene bg parkir_mobil2
    with fade

    "Di depan kampus terlihat sudah ada beberapa mobil yang parkir"
    "Aris harus memarkirkan motornya terlebih dahulu"

    scene bg parkir_mobil3
    with fade

    a "Baik aku harus memarkirkan motor terlebih dahulu"

    $ myClock.add_time(0,15,1)

    stop sound fadeout 1

    menu:

        "Kemana kamu akan pergi?"

        "Ke parkiran motor":

            jump parkiran

        "Pulang ke kos":

            jump kos

label kos:

    play music "/audio/Sneaky Adventure.mp3"

    scene bg parkir_mobil3
    with fade
    with Pause(1)

    scene bg parkir_mobil2
    with fade
    with Pause(1)

    scene bg parkir_mobil1
    with fade
    
    "Aris kembali ke pintu gerbang dengan motornya"

    scene bg gerbang_dpt2
    with fade
    with Pause(1)

    scene bg gerbang_dpt1
    with fade

    "Ia kembali ke kos karena merasa ngantuk"

    scene bg jalan
    with fade

    $ myClock.add_time(0,15,1)

    "Aris pulang ke kos dan kembali tidur"
    "Sampai ia lupa bangun untuk menghadiri kelas."

    # END.
    "{b}Bad Ending{/b}."

    return
    # This ends the game.

label parkiran:

    scene bg jalan_ke_parkir1
    with fade

    "Aris mulai menuju ke parkiran motor"

    play sound "/audio/motorcycle-arrive-and-shut-off-01.mp3"
    if parkir is False:
        
        "Setibanya dia di parkiran motor"
        "Aris terkejut karena parkiran motor sudah terlihat penuh"

    scene bg parkir2
    with fade

    if parkir is False:
        a "Hah??! masih jam segini kenapa parkiran sudah penuh?"
        a "Sepertinya orang-orang ini sangat bersemangat ke kampus karena habis libur panjang"
        a "Baiklah.. aku akan mencari tempat parkir yang ada di ujung"

    scene bg parkir1
    with fade

    $ myClock.add_time(0,5,1)

    
    if parkir is False:
        "Setelah mencari selama 5 menit, Aris akhirnya mendapatkan parkir."
        $ parkir = True

    stop sound fadeout 1

    menu:

        "Kemana selanjutnya kamu akan pergi?"

        "Masuk ke dalam gedung":

            jump lantai_1

        "Pulang ke kos":

            jump kos

label lantai_1:

    play music "/audio/Glitter Blast.mp3"

    $ lantai = 1

    scene bg lantai1
    with dissolve

    "Aris berada di dalam gedung Teknik Informatika."

    $ myClock.add_time(0,5,1)

    $h, m, s = myClock.get_time()
    if int(h) >= 5 and int(h) <= 7:
        play music "/audio/Sneaky Adventure.mp3"
        # END.
        "Kelas Sistem Game sudah selesai"
        "Kamu dianggap Alpha dan mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return
    # This ends the game.

    "Saat ini jam [h]:[m]"

    if makan is False or buang_air is False or shalat_dhuhur is False or shalat_ashar is False:
        "Agar dapat menghadiri kelas Sistem Game dan mendapat nilai bagus, Aris harus makan terlebih dahulu"
        "Selain itu dia juga harus buang air setelah makan"
        "Dan yang terakhir harus menunaikan salat agar mendapat berkah di ujian nantinya."

    menu:

        "Apa yang akan kamu lakukan?"

        "Jelajah lantai 1":

            jump jelajah_lt1

        "Naik ke lantai 2":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg tangga_lantai2
            with fade
            "Aris menaiki tangga menuju Lantai 2."
            jump lantai_2

        "Ke musala":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            $ myClock.add_time(0,10,1)
            "Aris berjalan menuju musala"
            jump musala

        "Pergi ke toilet":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg toilet
            with fade
            $ myClock.add_time(0,5,1)
            "Aris menuju toilet"
            jump toilet

        "Pergi ke kantin":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            $ myClock.add_time(0,10,1)
            "Aris berjalan menuju kantin"
            jump kantin

        "Kembali ke parkiran":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            "Aris berjalan menuju parkiran"
            jump parkiran


label jelajah_lt1:

    play music "/audio/Two Finger Johnny.mp3"

    "Aris berkeliling di lantai 1 karena sudah lama habis liburan sembari menunggu kelas nanti."

    scene bg lorong_utara_lt1_orang
    with fade
    with Pause(1)

    scene bg lorong_utara_lt1_povbarat
    with fade
    with Pause(1)

    scene bg kantin
    with fade
    with Pause(1)

    scene bg musala
    with fade
    
    a "Di musala sini, seingetku ada AC nya, jarang sekali musala ada AC."

    scene bg panggung
    with fade
    with Pause(1)

    scene bg lapangan1
    with fade
    with Pause(1)

    scene bg lapangan2
    with fade
    with Pause(1)

    scene bg pikti1
    with fade
    with Pause(1)

    scene bg pikti2
    with fade
    with Pause(1)

    scene bg pikti3
    with fade
    with Pause(1)

    scene bg if_110
    with fade
    with Pause(1)

    scene bg if_110_closeup
    with fade
    with Pause(1)

    scene bg lab_pascasarjana1
    with fade
    with Pause(1)

    scene bg lab_pascasarjana2
    with fade
    with Pause(1)

    scene bg lorong_selatan_lt1
    with fade
    with Pause(1)

    scene bg lapangan3
    with fade
    
    a "Dilihat-lihat lagi, rumputnya cukup tinggi ya, efek habis liburan."

    scene bg lapangan4
    with fade
    with Pause(1)

    scene bg toilet
    with fade
    with Pause(1)

    scene bg depan_dpt1
    with fade
    with Pause(1)
    
    $ myClock.add_time(0,45,3)

    scene bg depan_dpt2
    with fade
    with Pause(1)

    a "Cukup sampai di sini dulu, sebaiknya aku kembali."

    jump lantai_1

label musala:

    scene bg musala
    with dissolve
    "Aris telah berada di depan musala"

    menu:

        "Apa yang mau kamu lakukan?"

        "Menunaikan salat":
            $h, m, s = myClock.get_time()
            "Saat ini pukul [h]:[m]:[s]"
            if int(h) >= 12 or int(h) <= 5:
                jump salat
            else:
                "Belum memasuki waktu salat."

            jump musala

        "Kembali":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            jump lantai_1

label salat:
    $h, m, s = myClock.get_time()

    a "Aku akan mengambil air wudu dulu"

    play sound "/audio/filling-sink-1.mp3"

    scene bg wudu
    with fade

    "Aris sedang berwudu"

    stop sound fadeout 1

    "Setelah berwudu, Aris segera masuk ke dalam musala"

    scene bg dalam_musala1
    with fade
    with Pause(1)

    scene bg dalam_musala2
    with fade

    #jam dhuhur
    if int(h) >= 12 or int(h) < 3:
        if shalat_dhuhur is False:
            a "Baik.. aku akan solat zuhur dahulu"
            "Aris sedang melaksanakan solat zuhur"
            $shalat_dhuhur = True
            with fade
        
            a "Alhamdulillah..."
            "Aris selesai menunaikan solat zuhur"
        else:
            "Kamu sudah salat zuhur!"
    #jam ashar
    elif int(h) >= 3 and int(h) < 6:
        if shalat_ashar is False:
            a "Baik.. aku akan solat ashar dahulu"
            "Aris sedang melaksanakan solat asar"
            $shalat_ashar = True
            with fade
        
            a "Alhamdulillah..."
            "Aris selesai menunaikan solat asar"
        else:
            "Kamu sudah salat asar!"

    $ myClock.add_time(0,20,1)

    jump musala

label kantin:

    scene bg kantin
    with dissolve

    "Aris berada di kantin TC"

    $h, m, s = myClock.get_time()
    if int(h) >= 9 or int(h) <= 4:
        if makan is False:
            a "Aduhh aku lapar.."
            a "Enaknya makan apa ya?"

            with fade
            a "Bu.. permisi"
            b "Iya nak.."
            a "Ada menu apa aja Bu?"
            b "Ada nasi goreng, mie goreng, sama soto"
            a "Saya pesan mie goreng satu ya Bu"
            b "Pakai telor?"
            a "Iya.. pakai Bu"


    menu:
        "Makan atau kembali?"

        "Makan":
            $h, m, s = myClock.get_time()
            if int(h) >= 9 or int(h) <= 4:
                play music "/audio/656274__miaopolus__outdoor-food-market-ambience.mp3"
                if makan is False:
                    $makan = True
                    play sound "/audio/407594__chenewessels_170017__person-chewing-food.mp3"
                    $ myClock.add_time(0,30,2)
                    stop sound fadeout 1
                    a "Alhamdulillah kenyang."
                    a "Bu, terimakasih ya!"
                    b "EHH!! BAYAR DULU!!"
                    a "Oh iya maaf Bu.. saya lupa hehehe"

                else:
                    "Masih kenyang."
            else:
                "Kantin belum buka"
                a "Sepertinya aku harus menunggu sebentar lagi"

            jump kantin

        "Kembali":
            stop music fadeout 1
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            jump lantai_1

label lantai_2:

    play music "/audio/Glitter Blast.mp3"

    $ lantai = 2

    scene bg lantai2
    with dissolve

    "Aris berada di Lantai 2."

    $ myClock.add_time(0,5,1)

    $h, m, s = myClock.get_time()
    if int(h) >= 5 and int(h) <= 7:
        play music "/audio/Sneaky Adventure.mp3"
        # END.
        "Kelas Sistem Game sudah selesai"
        "Kamu dianggap Alpha dan mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return

    "Saat ini jam [h]:[m]"

    if makan is False or buang_air is False or shalat_dhuhur is False or shalat_ashar is False:
        "Agar dapat menghadiri kelas Sistem Game dan mendapat nilai bagus, Aris harus makan terlebih dahulu"
        "Selain itu dia juga harus buang air setelah makan"
        "Dan yang terakhir harus menunaikan salat agar mendapat berkah di ujian nantinya."

    "Aris agak lupa mengenai jadwal dan lokasi kelas Sistem Game"
    "Informasi jadwal kelas dapat ditanyakan ke Pak Imam di ruang Tata Usaha (TU)"

    menu:

        "Apa yang akan kamu lakukan?"

        "Pergi ke ruang santai":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            $ myClock.add_time(0,5,1)
            "Aris pergi menuju ruang santai"
            jump ruang_santai

        "Pergi ke toilet.":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg toilet
            with fade
            $ myClock.add_time(0,5,1)
            "Aris menuju toilet"
            jump toilet

        "Pergi ke ruang TU.":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg lorong_lantai2
            with fade
            $ myClock.add_time(0,5,1)
            "Aris menuju Ruang TU"
            jump ruang_tu

        "Jelajah lantai 2":

            jump jelajah_lt2

        "Turun ke lantai 1":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg turun_lantai1
            with fade   
            "Aris menuruni tangga menuju Lantai 1."
            jump lantai_1

        "Naik ke lantai 3":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg tangga_lantai3
            with fade
            "Aris menaiki tangga menuju Lantai 3."
            jump lantai_3

label ruang_santai:

    if lantai == 2:
        scene bg rg_santai_lt2
        with dissolve

    elif lantai == 3:
        scene bg rg_santai_lt3
        with dissolve

    "Aris sedang berada di ruang santai"

    a "Wahh disini sepertinya nyaman"
    a "Sambil menunggu kelas dimulai, mungkin aku istirahat dulu"

    menu:

        "Apa yang akan kamu lakukan?"

        "Kembali":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            if lantai == 2:
                jump lantai_2
            elif lantai == 3:
                jump lantai_3

        "Bersantai 1 jam":

            "Aris bersantai selama 1 jam"
            with fade

            $ myClock.add_time(1,0,1)

            a "Wahh enaknya bersantai sebelum kelas"
            if lantai == 2:
                jump lantai_2
            elif lantai == 3:
                jump lantai_3

label ruang_tu:

    scene bg rg_tu
    with dissolve

    "Aris berada di Ruang TU"

    menu:

        "Apa yang ingin dilakukan?"

        "Kembali":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            jump lantai_2

        "Bertanya jadwal kelas":
            $h, m, s = myClock.get_time()
            if int(h) >= 10:
                play sound "/audio/door-2-open.mp3"
                a "Permisi Pak, Saya Aris NRP 170"

                show dosen2
                with dissolve
                i "Iya Aris, ada apa?"
                a "Saya ingin bertanya mengenai jadwal dan lokasi kelas Sistem Game Pak"
                i "Kelas Sistem Game dimulai pada pukul setengah 4 sore ya.. lokasinya ada di ruang LP 1 Lantai 3, cari aja yang ada tulisan Lab Pemrograman"
                a "Baik terimakasih banyak Pak Imam"
                i "Ya.. sama-sama"

                $ myClock.add_time(0,10,1)

            else:
                "Tidak ada siapa-siapa di ruang TU."
                
            jump ruang_tu

label jelajah_lt2:

    play music "/audio/Two Finger Johnny.mp3"

    "Aris menjelajahi lantai 2 gedung departemen Teknik Informatika."

    scene bg lantai2
    with fade

    scene bg lorong_lantai2
    with fade

    scene bg ruang-aula
    with fade

    scene bg rg_santai_lt2
    with fade

    "Sepertinya kalau ingin santai-santai lebih baik di ruang lantai 3 daripada di sini."

    scene bg toilet_lt2
    with fade

    scene bg lorong_lantai2_2
    with fade

    scene bg ruang-sidang
    with fade

    scene bg rg_tu
    with fade

    $ myClock.add_time(0,30,3)
    
    "Sisi utara gedung ini tempatnya s2, mending tidak aku lewati dulu."

    jump lantai_2

label lantai_3:

    play music "/audio/Glitter Blast.mp3"

    $ lantai = 3

    scene bg lantai3
    with dissolve

    "Aris berada di Lantai 3."

    $ myClock.add_time(0,5,1)

    $h, m, s = myClock.get_time()
    if int(h) >= 5 and int(h) <= 7:
        play music "/audio/Sneaky Adventure.mp3"
        # END.
        "Kelas Sistem Game sudah selesai"
        "Kamu dianggap Alpha dan mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return

    "Saat ini jam [h]:[m]"

    if makan is False or buang_air is False or shalat_dhuhur is False or shalat_ashar is False:
        "Agar dapat menghadiri kelas Sistem Game dan mendapat nilai bagus, Aris harus makan terlebih dahulu"
        "Selain itu dia juga harus buang air setelah makan"
        "Dan yang terakhir harus menunaikan salat agar mendapat berkah di ujian nantinya."

    menu:

        "Apa yang akan kamu lakukan?"

        "Pergi ke ruang santai":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            $ myClock.add_time(0,5,1)
            "Aris pergi menuju ruang santai"
            jump ruang_santai

        "Pergi ke toilet.":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg toilet
            with fade
            $ myClock.add_time(0,5,1)
            "Aris menuju toilet"
            jump toilet

        "Jelajah lantai 3":

            jump jelajah_lt3

        "Turun ke lantai 2":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            scene bg turun_lantai2
            with fade
            "Aris menuruni tangga ke Lantai 2."
            jump lantai_2

        "Pergi ke LP 1":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            $ myClock.add_time(0,5,1)
            "Aris berjalan menuju LP 1."
            jump lp_1

label lp_1:

    scene bg depan_lp_1
    with dissolve

    "Aris berada di depan ruang LP 1."

    menu:
        
        "Apa yang harus dilakukan?"

        #jika jam 15:30
        "Masuk kelas Sistem Game":
            $h, m, s = myClock.get_time()
            "Saat ini jam [h]:[m]"
            if ((int(h) == 3 and int(m) >= 30 ) or int(h) == 4):
                jump kelas_sistem_game
            else:
                "Masih ada kelas lain, tunggu beberapa saat lagi."
                jump lp_1

        "Tunggu kelas dimulai":

            $h, m, s = myClock.get_time()
            if ((int(h) == 3 and int(m) >= 30 ) or int(h) == 4):
                "Kelas sudah dimulai, segera masuk!"
                jump lp_1
            else:
                "Menunggu kelas dimulai"
                $ myClock.add_time(0,5,1)
                jump lp_1

        "Kembali":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            jump lantai_3

label kelas_sistem_game:
    play sound "/audio/door-2-open.mp3"
    "Aris memasuki kelas"

    scene black
    with fade

    "Aris mengerjakan ujian Sistem Game"

    if (makan is True and buang_air is True and shalat_dhuhur is True and shalat_ashar is True):
        
        play music "/audio/Life's Is Incredible Again - Bgm.mp3"
        scene bg good_ending
        with fade

        "Aris sudah memenuhi apa yang harus dilakukan sebelum ujian."

        "Sehingga ujian yang dia kerjakan terasa lancar tanpa hambatan."

        a "Alhamdulillah aku mengerjakan semua soal dengan lancar."
        a "Semoga nilaiku bagus.."
        a "Aamiin.."
        
        "Dan akhirnya Aris mendapatkan nilai bagus"

        a "Horee!!"

        "{b}Good Ending{/b}."

        return

    elif (makan is False or buang_air is False):
        play music "/audio/Sneaky Adventure.mp3"

        "Kamu tidak fokus dalam kelas karena belum makan dan buang air terlebih dahulu"
        "Dan akhirnya kamu mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return
    # This ends the game.

    elif (shalat_dhuhur is False or shalat_ashar is False):
        play music "/audio/Sneaky Adventure.mp3"

        "Kamu belum solat wajib!"
        "Apa yang kamu kerjakan menjadi tidak berkah"
        "Dan akhirnya mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return
    # This ends the game.

label jelajah_lt3:

    play music "/audio/Two Finger Johnny.mp3"

    "Aris berkeliling di lantai 3 melihat-lihat berbagai lab yang ada di departemen."

    scene bg lantai3
    with fade

    scene bg rg_santai_lt3
    with fade

    "Yap di sini kesannya lebih luas daripada di lantai 2."

    scene bg rg_santai_lt3_2
    with fade

    scene bg depan_lp_1
    with fade

    "Nanti aku kelas di LP 1."

    scene bg lab_ajk
    with fade

    scene bg lab_alpro
    with fade

    scene bg lab_igs
    with fade

    scene bg lab_kbj
    with fade

    scene bg lab_kcv
    with fade

    scene bg lab_mi
    with fade

    # scene bg lab_microsoft
    # with fade

    scene bg lab_rpl
    with fade

    scene bg sekretariat_hmtc
    with fade

    "Kelihatannya tidak ada anggota yang sedang rapat."

    scene bg residensi_pascasarjana
    with fade

    scene bg lorong_selatan_lt3
    with fade

    scene bg kantin_lt3
    with fade

    "Kalau kantin mini ini sedianya cuman jajanan."

    $ myClock.add_time(0,30,3)


    jump lantai_3


label toilet:

    stop sound fadeout 1

    scene bg wastafel
    with fade

    "Aris berada di toilet"

    menu:

        "Apa yang ingin kamu lakukan?"

        "Cuci muka":
            a "Mukaku terasa berminyak"
            a "Aku juga sedikit mengantuk"
            a "Aku harus cuci muka!"
            with fade

            play sound "/audio/filling-sink-1.mp3"
            a "Hmm segar kembali"
            $ myClock.add_time(0,5,1)
            jump toilet

        "Buang air":
            if makan == True:
                scene bg kamar_mandi
                if buang_air is False:
                    a "Aduhh perutku sakit karena tadi habis makan"
                    a "Aku harus segera buang air"
                    with fade

                    $ myClock.add_time(0,15,1)
                    $buang_air = True
                    play sound "/audio/toilet-flush-3.mp3"
                    a "ah leganya..."
                else:
                    "*Baru saja tadi buang air"
            else:
                "Isi perut masih kosong."

            jump toilet

        "Kembali":
            play sound "/audio/446094__sophiemezam__footsteps3.mp3"
            if lantai == 1:
                jump lantai_1
            elif lantai == 2:
                jump lantai_2 
            elif lantai == 3:
                jump lantai_3
