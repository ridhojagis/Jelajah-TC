# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character(("Me"), color= "#ceffc8")
define i = Character("Pak Imam")

default makan = False
default buang_air = False
default shalat_dhuhur = False
default shalat_ashar = False
default lantai = 1

default myClock = Clock(True, 8, 0, 150, False, False) #Analogue or Digital, hours, minutes, size, second hand, military time

screen clock_screen:
    add myClock:
        xalign 1.0
        yalign 0.0

# The game starts here.
label start:

    scene fsm_jelajah_tc1
    with fade

    "FSM Jelajah Teknik Informatika"
    with PushMove(1, "pushup")

    scene fsm_jelajah_tc2
    with Pause(5)

    "Dibuat oleh: \n\n05111940000071-Daffa Amanullah Setyawan \n05111940000170-Ridho Ajiraga Jagiswara"

    scene bg jalan

    # menampilkan jam analog
    show screen clock_screen
    with Dissolve(1)

    scene bg gerbang_dpt1
    with fade

    scene bg gerbang_dpt2
    with fade

    scene bg parkir_mobil1
    with fade

    scene bg parkir_mobil2
    with fade

    scene bg parkir_mobil3
    with fade

    $ myClock.add_time(0,15,1)

    menu:

        "....."

        "Ke parkiran":

            jump parkiran

        "Pulang ke kos":

            jump kos

label kos:

    scene bg parkir_mobil3
    with fade

    scene bg parkir_mobil2
    with fade

    scene bg parkir_mobil1
    with fade

    scene bg gerbang_dpt2
    with fade

    scene bg gerbang_dpt1
    with fade

    scene bg jalan
    with fade

    $ myClock.add_time(0,15,1)

    # END.
    "{b}Bad Ending{/b}."

    return
    # This ends the game.

label parkiran:

    scene bg jalan_ke_parkir1
    with fade

    scene bg jalan_ke_parkir2
    with fade

    scene bg parkir1
    with fade

    scene bg parkir2
    with fade

    $ myClock.add_time(0,5,1)

    menu:

        "....."

        "Masuk ke dalam gedung":

            jump lantai_1

        "Pulang ke kos":

            jump kos

label lantai_1:

    $ lantai = 1

    scene bg lantai1
    with dissolve

    $ myClock.add_time(0,5,1)

    $h, m, s = myClock.get_time()
    if int(h) >= 5 and int(h) <= 7:
        # END.
        "Kelas Sistem Game sudah selesai"
        "Kamu dianggap Alpha dan mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return
    # This ends the game.

    menu:

        "....."

        "Jelajah lantai 1":

            jump jelajah_lt1

        "Naik ke lantai 2":

            scene bg tangga_lantai2
            with fade
            jump lantai_2

        "Ke musala":
            $ myClock.add_time(0,10,1)
            jump musala

        "Pergi ke toilet":
            scene bg toilet
            with fade
            $ myClock.add_time(0,5,1)
            jump toilet

        "Pergi ke kantin":
            $ myClock.add_time(0,10,1)
            jump kantin

        "Kembali ke parkiran":

            jump parkiran


label jelajah_lt1:

    scene bg lorong_utara_lt1_orang
    with fade

    scene bg lorong_utara_lt1_povbarat
    with fade

    scene bg kantin
    with fade

    scene bg musala
    with fade

    scene bg panggung
    with fade

    scene bg lapangan1
    with fade

    scene bg lapangan2
    with fade

    scene bg pikti1
    with fade

    scene bg pikti2
    with fade

    scene bg pikti3
    with fade

    $ myClock.add_time(1,0,3)

    scene bg if_110
    with fade

    scene bg if_110_closeup
    with fade

    scene bg lab_pascasarjana1
    with fade

    scene bg lab_pascasarjana2
    with fade

    scene bg lorong_selatan_lt1
    with fade

    scene bg lapangan3
    with fade

    scene bg lapangan4
    with fade

    scene bg toilet
    with fade

    scene bg depan_dpt1
    with fade

    scene bg depan_dpt2
    with fade

    jump lantai_1

label musala:

    scene bg musala

    menu:

        "....."

        "Menunaikan salat":
            $h, m, s = myClock.get_time()
            "It is [h]:[m]:[s]"
            if int(h) >= 12 or int(h) <= 5:
                jump salat
            else:
                "Belum memasuki waktu salat."

            jump musala

        "Kembali":

            jump lantai_1

label salat:
    $h, m, s = myClock.get_time()

    scene bg wudu
    with fade

    scene bg dalam_musala1
    with fade

    scene bg dalam_musala2

    #jam dhuhur
    if int(h) >= 12 or int(h) < 3:
        if shalat_dhuhur is False:
            "*Sedang melaksanakan solat zuhur"
            $shalat_dhuhur = True
        else:
            "Kamu sudah salat zuhur!"
    #jam ashar
    elif int(h) >= 3 and int(h) < 6:
        if shalat_ashar is False:
            "*Sedang melaksanakan solat asar"
            $shalat_ashar = True
        else:
            "Kamu sudah salat asar!"

    $ myClock.add_time(0,20,1)

    jump musala

label kantin:

    scene bg kantin

    menu:

        "....."

        "Makan":
            $h, m, s = myClock.get_time()
            if int(h) >= 9 or int(h) <= 4:
                if makan is False:
                    $makan = True
                    $ myClock.add_time(0,30,2)
                    "Alhamdulillah kenyang."
                else:
                    "Masih kenyang."
            else:
                "Kantin belum buka"

            jump kantin

        "Kembali":
            jump lantai_1

label lantai_2:

    $ lantai = 2

    scene bg lantai2
    with dissolve

    "Lantai 2"

    $ myClock.add_time(0,5,1)

    $h, m, s = myClock.get_time()
    if int(h) >= 5 and int(h) <= 7:
        # END.
        "Kelas Sistem Game sudah selesai"
        "Kamu dianggap Alpha dan mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return

    menu:

        "..."

        "Pergi ke ruang santai":

            $ myClock.add_time(0,5,1)
            jump ruang_santai

        "Pergi ke toilet.":

            scene bg toilet
            with fade
            $ myClock.add_time(0,5,1)
            jump toilet

        "Pergi ke ruang TU.":

            scene bg lorong_lantai2
            with fade
            $ myClock.add_time(0,5,1)
            jump ruang_tu

        "Jelajah lantai 2":

            jump jelajah_lt2

        "Turun ke lantai 1":

            scene bg turun_lantai1
            with fade   
            jump lantai_1

        "Naik ke lantai 3":

            scene bg tangga_lantai3
            with fade
            jump lantai_3

label ruang_santai:

    if lantai == 2:
        scene bg rg_santai_lt2
        with dissolve

    elif lantai == 3:
        scene bg rg_santai_lt3
        with dissolve

    menu:

        "...."

        "Kembali":
            if lantai == 2:
                jump lantai_2
            elif lantai == 3:
                jump lantai_3

        "Bersantai 1 jam":

            "Wahh enaknya bersantai sebelum kelas"
            $ myClock.add_time(1,0,1)
            if lantai == 2:
                jump lantai_2
            elif lantai == 3:
                jump lantai_3

label ruang_tu:

    scene bg rg_tu
    with dissolve

    menu:

        "...."

        "Kembali":

            jump lantai_2

        "Bertanya jadwal kelas":

            a "Permisi Pak"

            show dosen2
            with dissolve
            i "Iya ada apa?"
            a "Saya ingin bertanya mengenai jadwal kelas Sistem Game"

            $ myClock.add_time(0,10,1)
            jump ruang_tu

label jelajah_lt2:

    scene bg lantai2
    with fade

    scene bg lorong_lantai2
    with fade

    scene bg ruang-aula
    with fade

    scene bg rg_santai_lt2
    with fade

    scene bg toilet_lt2
    with fade

    scene bg lorong_lantai2_2
    with fade

    scene bg ruang-sidang
    with fade

    scene bg rg_tu
    with fade


    $ myClock.add_time(0,30,3)

    jump lantai_2

label lantai_3:

    $ lantai = 3

    scene bg lantai3
    with dissolve

    $ myClock.add_time(0,5,1)

    $h, m, s = myClock.get_time()
    if int(h) >= 5 and int(h) <= 7:
        # END.
        "Kelas Sistem Game sudah selesai"
        "Kamu dianggap Alpha dan mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return

    menu:

        "...."

        "Pergi ke ruang santai":

            $ myClock.add_time(0,5,1)
            jump ruang_santai

        "Pergi ke toilet.":

            scene bg toilet
            with fade
            $ myClock.add_time(0,5,1)
            jump toilet

        "Jelajah lantai 3":

            jump jelajah_lt3

        "Turun ke lantai 2":

            scene bg turun_lantai2
            with fade
            jump lantai_2

        "Pergi ke LP 1":

            $ myClock.add_time(0,5,1)
            jump lp_1

label lp_1:

    scene bg depan_lp_1
    with dissolve

    menu:
        
        "....."

        #jika jam 15:30
        "Masuk kelas Sistem Game":
            $h, m, s = myClock.get_time()
            "It is [h]:[m]:[s]"
            if ((int(h) == 3 and int(m) >= 30 ) or int(h) == 4):
                jump kelas_sistem_game
            else:
                "Masih ada kelas lain, tunggu beberapa saat lagi."
                jump lp_1

        "Tunggu":

            $h, m, s = myClock.get_time()
            if ((int(h) == 3 and int(m) >= 30 ) or int(h) == 4):
                "Kelas sudah dimulai, segera masuk!"
                jump lp_1
            else:
                "Menunggu kelas dimulai"
                $ myClock.add_time(0,5,1)
                jump lp_1

        "Kembali ke lantai 3":

            jump lantai_3

label kelas_sistem_game:

    scene black

    if (makan is True and buang_air is True and shalat_dhuhur is True and shalat_ashar is True):

        "Dapat nilai bagus"

        "{b}Good Ending{/b}."

        return

    elif (makan is False or buang_air is False):

        "Kamu tidak fokus dalam kelas karena belum makan dan buang air terlebih dahulu"
        "Dan akhirnya kamu mendapat nilai jelek"
        "{b}Bad Ending{/b}."
        return
    # This ends the game.

    elif (shalat_dhuhur is False or shalat_ashar is False):

        "Kamu belum shalat wajib!"
        "Sehingga mendapat nilai jelek karena tidak mendapat berkah"
        "{b}Bad Ending{/b}."
        return
    # This ends the game.

label jelajah_lt3:

    scene bg lantai3
    with fade

    scene bg rg_santai_lt3
    with fade

    scene bg rg_santai_lt3_2
    with fade

    scene bg depan_lp_1
    with fade

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

    scene bg lab_microsoft
    with fade

    scene bg lab_rpl
    with fade

    scene bg sekretariat_hmtc
    with fade

    scene bg residensi_pascasarjana
    with fade

    scene bg lorong_selatan_lt3
    with fade

    scene bg kantin_lt3
    with fade

    $ myClock.add_time(0,30,3)

    jump lantai_3


label toilet:

    scene bg wastafel
    with fade

    menu:

        "....."

        "Cuci muka":
            "Hmm segar kembali"
            $ myClock.add_time(0,5,1)
            jump toilet

        "Buang air":
            if makan == True:
                scene bg kamar_mandi
                if buang_air is False:
                    $ myClock.add_time(0,15,1)
                    $buang_air = True
                    "ah leganya..."
                else:
                    "*Baru saja tadi buang air"
            else:
                "Isi perut masih kosong."

            jump toilet

        "Kembali":
            if lantai == 1:
                jump lantai_1
            elif lantai == 2:
                jump lantai_2
            elif lantai == 3:
                jump lantai_3
