image i_mc senang = At('mc senang', sprite_highlight('mc'))
image i_mc serius = At('mc serius', sprite_highlight('mc'))

define pov = Character("[povname]")
define mc = Character("[povname]", image='i_mc', callback=name_callback, cb_name='mc')

#define images:
image mc serius:
    "MC_serius.png"
    zoom 0.5
image mc senang:
    "MC_Senang.png"
    zoom 0.5
image mc semirik:
    "MC_semirik.png"
    zoom 0.5
image mc kaget:
    "MC_Kaget Shock Berat.png"
    zoom 0.5
image mc semangat:
    "MC_Semangat bgt.png"
    zoom 0.5
image mc smirk:
    "MC_semirik.png"
    zoom 0.5
image mc takut:
    "MC_takut aja.png"
    zoom 0.5
image mc nangis:
    "MC_takut tp sambil nangis.png"
    zoom 0.5
image polisi:
    "Polisi 1_Topi.png"
    zoom 0.5
image bg papan:
    "Meja investigasi prolog_plot 1.png"
    zoom 0.8

label start:
    scene bg papan

    $povname = renpy.input("What is your name?", length=32)
    $povname = povname.strip()

    "Pencahayaan temaram. Sebuah papan penuh catatan dan foto terpasang di dinding. [povname] duduk di depan laptop, wajahnya serius."
    show i_mc serius
    "Sudah berminggu-minggu aku menggali, membaca laporan keuangan, wawancara orang-orang yang takut menyebut nama sebenarnya."
    "Anggaran yang raib tanpa jejak, proyek pembangunan yang hanya ada di atas kertas, dan janji kampanye yang tak pernah ditepati…"
    "Semua itu seperti benang kusut—tapi jika ditarik perlahan, semuanya berujung pada satu nama: wali kota."

label choices:
    mc "Aku harus mulai dari satu tempat. Entah bekerja sama dengan penegak hukum... atau mencari suara warga."
menu:
    "Bekerja sama dengan penegak hukum":
        jump choices1_a
    "Mencari fakta lewat komunitas warga":
        jump choices1_b
label choices1_a:
    "[povname] menyandarkan tubuh di kursi. Di layar laptopnya, terbuka lembar catatan digital berisi puluhan dokumen: laporan pengeluaran kota, transkrip wawancara, foto-foto proyek mangkrak."
    mc "Aku punya cukup data untuk mulai menggali lebih dalam. Tapi data saja tidak cukup."
    mc "Kalau aku bertindak sendirian, bisa bisa aku menjadi   bulan bulanan para …… itu/bisa hilang tanpa jejak."
    mc "Tidak semua orang di sistem ini busuk, mungkin…mungkin saja masih ada satu-dua orang yang mau menegakkan hukum."
    mc "Dan aku tahu harus mulai dari mana."

    return
