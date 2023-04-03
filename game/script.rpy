# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Ari")
define i = Character("Pak Imam")

default makan = False
default buang_air = False
default shalat_dhuhur = False
default shalat_ashar = False


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg depan_dpt
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    scene bg dpt
    with dissolve

    # These display lines of dialogue.
    menu:
    "....."

        "Ke parkiran.":

            jump parkiran

        "Pulang ke kos.":

            jump kos


    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

label parkiran:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg parkir
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    menu:
    "....."

        "Masuk gedung.":

            jump lantai_1

        "Pulang ke kos.":

            jump kos


    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

label lantai_1:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg lt_1
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    menu:
    "....."

        "Ke musholla.":

            jump musholla

        "Pergi ke toilet.":

            jump toilet

        "Pergi ke kantin":

            jump kantin

        "Kembali ke parkiran"

            jump parkiran

        "Jelajah lantai 1"

            jump jelajah_lt1

        "Naik ke lantai 2"

            jump lantai_2


    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"

label jelajah_lt1:

    scene bg 1
    scene bg 2

    jump lantai_1

label lantai_2:

    scene bg lt_2

    menu:

    "Pergi ke ruang santai"

        jump ruang_santai

    "Pergi ke toilet.":

            jump toilet   

    "Pergi ke ruang TU.":

            jump ruang_tu

    "Jelajah lantai 2"

            jump jelajah_lt2

    "Turun ke lantai 1"

            jump lantai_1

    "Naik ke lantai 3"

            jump lantai_3

label ruang_santai:

    scene bg santai_room

    menu:

    "Kembali"

    jump lantai_2

    "Bersantai 1 jam"

    jump ruang_santai

label ruang_tu:

    scene bg tu_room

    menu:

    "Kembali"

    jump lantai_2

    "Bertanya jadwal kelas"

    jump ruang_santai

label jelajah_lt2:

    scene bg 1
    scene bg 2

    jump lantai_2

label lantai_3:

    scene bg lt_3

    menu:

    "Pergi ke ruang santai"

        jump ruang_santai

    "Pergi ke toilet.":

            jump toilet   

    "Jelajah lantai 3"

            jump jelajah_lt3

    "Turun ke lantai 2"

            jump lantai_2

    "Pergi ke LP 1:

            jump lp_1

label lp_1:

    scene bg depan_lp_1

    #jika jam 15:30
    jump kelas_sistem_game

    "Kembali ke lantai 3"

        jump lantai_3

label kelas_sistem_game:

    if ($ makan = True && $ buang_air = True && shalat_dhuhur = True && shalat_ashar = True)

        "Dapat nilai bagus"
        
        "{b}Good Ending{/b}."

    else if ($ makan = False || $ buang_air = False)
        
        "...."
        "{b}Bad Ending{/b}."

    else if ($ shalat_dhuhur = False || $ shalat_ashar = False)
        
        "...."
        "{b}Bad Ending{/b}."

label jelajah_lt3:

    scene bg 1
    scene bg 2

    jump lantai_3

label musholla:

    scene bg musholla

    menu:

    "Kembali ke lantai 1"

        jump lantai_1

    "Shalat"

        jump shalat

label shalat:

    #jam dhuhur
    shalat_dhuhur = True

    #jam ashar
    shalat_ashar = True

    scene bg wudhu
    scene bg dalam_musholla

    jump musholla

label toilet:

    scene bg dalam_toilet

    menu:

    "Cuci muka"
        play sound keran
        jump toilet

    "Buang air"
        jump toilet

    "Kembali ke lantai 1"
        jump lantai_1

label kantin:

    scene bg depan_kantin

    menu:

    "Makan"
        jump kantin

    "Kembali ke lantai 1"
        jump lantai_1

label kos:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg jalan_pulang
    with dissolve

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # END.
    "{b}Bad Ending{/b}."

    return
