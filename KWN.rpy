
image i_mc senang = At('mc senang', sprite_highlight('mc'))
image i_mc serius = At('mc serius', sprite_highlight('mc'))
image i_mc takut = At('mc takut', sprite_highlight('mc'))
image i_mc nangis = At('mc nangis', sprite_highlight('mc'))
image i_mc kaget = At('mc kaget', sprite_highlight('mc'))
image i_mc smirk = At('mc smirk', sprite_highlight('mc'))
image i_jaksa = At('jaksa', sprite_highlight('j'))
image i_penculik = At('penculik', sprite_highlight('pc'))
image i_direktur = At('direktur', sprite_highlight('d'))
image i_polisi = At('polisi', sprite_highlight('p'))
image i_zaki serius = At('zaki serius', sprite_highlight('z'))
image i_zaki emosi = At('zaki emosi', sprite_highlight('z'))
image i_zaki smirk = At('zaki smirk', sprite_highlight('z'))
image i_zaki kaget = At('zaki kaget', sprite_highlight('z'))
image i_zaki senyum = At('zaki senyum', sprite_highlight('z'))
image i_zaki mikir = At('zaki mikir', sprite_highlight('z'))
image i_pegawai = At('pegawai', sprite_highlight('pg'))
image i_walkot = At('walkot', sprite_highlight('pgw'))
image i_detektif = At('detektif', sprite_highlight('dt'))
image i_staff = At('staff', sprite_highlight('s'))
image i_arulla datar = At('arulla datar', sprite_highlight('a'))
image i_arulla marah = At('arulla marah', sprite_highlight('a'))
image i_arulla nangis = At('arulla nangis', sprite_highlight('a'))
image i_arulla kaget = At('arulla kaget', sprite_highlight('a'))
image i_arulla senyum = At('arulla senyum', sprite_highlight('a'))
image i_arulla smirk = At('arulla smirk', sprite_highlight('a'))
image i_editor = At('editor', sprite_highlight('e'))

define pov = Character("[povname]")
define mc = Character("[povname]", image='i_mc', callback=name_callback, cb_name='mc')
define j = Character("Jaksa", image='i_jaksa', callback=name_callback, cb_name='j')
define pc = Character("Penculik", image='i_penculik', callback=name_callback, cb_name='pc')
define d = Character("Direktur", image='i_direktur', callback=name_callback, cb_name='d')
define p = Character("Polisi", image='i_polisi', callback=name_callback, cb_name='p')
define z = Character("Zaki", image='i_zaki', callback=name_callback, cb_name='z')
define pg = Character("Pegawai Kejaksaan", image='i_pegawai', callback=name_callback, cb_name='pg')
define dt = Character("Detektif", image='i_detektif', callback=name_callback, cb_name='dt')
define pgw = Character("Pegawai Walikota", image='i_walkot', callback=name_callback, cb_name='pgw')
define s = Character("Staff Negara", image='i_staff', callback=name_callback, cb_name='s')
define a = Character("Arulla", image='i_arulla', callback=name_callback, cb_name='a')
define e = Character("Editor", image='i_editor', callback=name_callback, cb_name='e')


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
image zaki emosi:
    "Zaki_Emosi.png"
    zoom 1
image zaki kaget:
    "Zaki_Kaget.png"
    zoom 1
image zaki smirk:
    "Zaki_Senyum Puas_Smirk.png"
    zoom 1
image zaki senyum:
    "Zaki_Senyum Tipis.png"
    zoom 1
image zaki serius:
    "Zaki_Serius Mikir.png"
    zoom 1
image zaki mikir:
    "MC_takut aja.png"
    zoom 1
image arulla smirk:
    "Arulla smirk.png"
    zoom 1.1
image arulla senyum:
    "Arulla senyum.png"
    zoom 0.8
image arulla kaget:
    "Arulla marah.png"
    zoom 1.1
image arulla nangis:
    "Arulla nangis.png"
    zoom 1.1
image arulla datar:
    "arulla baru.png"
    zoom 3.55
image mc takut:
    "MC_takut aja.png"
    zoom 0.5
image polisi:
    "Polisi 1_Topi.png"
    zoom 0.5
image editor:
    "Editor.png"
    zoom 0.5
image staff:
    "staff.png"
    zoom 0.5
image forum1:
    "4.png"
    zoom 1
image forum2:
    "5.png"
    zoom 1
image surat:
    "surat.png"
    zoom 3
image jaksa:
    "Jaksa aja.png"
    zoom 0.5
image detektif:
    "Detektif.png"
    zoom 0.5
image penculik:
    "Penculik.png"
    zoom 0.5
image direktur:
    "Direktur.png"
    zoom 0.5
image pegawai:
    "Pegawai 2.png"
    zoom 0.5
image walkot:
    "walkot.png"
    zoom 0.5
image tikus:
    "Paket Tikus.png"
    zoom 0.5
image babi:
    "Paket Kepala Babi.png"
    zoom 0.5
image bg papan:
    "Meja investigasi prolog_plot 1.png"
    zoom 1
image bg papan gelap:
    "papan gelap.png"
    zoom 1
image bg kantor gelap:
    "kantor gelap.png"
    zoom 0.5
image bg awal:
    "awal.png"
    zoom 0.7
image bg tua:
    "gedung tua .png"
    zoom 1.25
image bg laut:
    "Rumah dekat laut_rumah adat NTT.png"
    zoom 0.7
image bg rumah laut:
    "POV rumah NTT.png"
    zoom 0.7
image bg ending 1:
    "ending 1.png"
    zoom 1
image bg ending 2:
    "ending 2.png"
    zoom 1
image bg ending 3:
    "ending 3.png"
    zoom 1
image bg ending 5:
    "ending 5.png"
    zoom 1
image bg ending 6:
    "ending 6.png"
    zoom 1
image bg ending 7:
    "ending 7.png"
    zoom 1
image bg ending 8:
    "ending 8.png"
    zoom 1
image bg ending 9:
    "ending 9.png"
    zoom 1
image bg jaksa:
    "Kantor Kejaksaan.png"
    zoom 0.7
image bg kamar:
    "Kamar Tidur.png"
    zoom 1
image bg kantor:
    "Kantor Redaksi.png"
    zoom 0.5
image bg rumah asli:
    "Raumah_Revisi.png"
    zoom 1
image bg laptop:
    "laptop.png"
    zoom 1
image bg comments:
    "comments.png"
    zoom 1
image bg anon:
    "anon.png"
    zoom 1
image bg black:
    "black.png"
    zoom 2
image bg cerita:
    "cerita.png"
    zoom 1
image bg temui:
    "temui.png"
    zoom 1
image bg balas:
    "balas.png"
    zoom 1
image bg chance:
    "chance.png"
    zoom 1
image bg bijak:
    "bijak.png"
    zoom 1
image bg news:
    "news.png"
    zoom 1
image bg korban:
    "korban.png"
    zoom 1
image bg rumah luar:
    "rumah luar.png"
    zoom 3.5
image bg rek:
    "rek.png"
    zoom 1
image bg kapol:
    "kapol.png"
    zoom 1
image bg bulan:
    "bulan.png"
    zoom 1
image bg hari:
    "hari.png"
    zoom 1
image bg pub:
    "pub.png"
    zoom 1
image bg sn:
    "sn.png"
    zoom 1
image bg hotel:
    "hotel.png"
    zoom 0.5
image bg lorong:
    "lorong.png"
    zoom 0.5
image bg inter:
    "Ruang Interogasi.png"
    zoom 1
image bg tahan:
    "Ruang Tahanan.png"
    zoom 1
image bg tolak:
    "tolak.png"
    zoom 1
image bg tangkap:
    "tangkap.png"
    zoom 1
image bg dark:
    "dark.png"
    zoom 1
image bg govt:
    "govt.png"
    zoom 1

label start:
    scene bg papan gelap with dissolve
    play music "audio/Misterius.mp3" fadein 1.0 volume 0.5

    $povname = renpy.input("Enter your name to start the investigation", length=32)
    $povname = povname.strip()

    mc "{i}Seorang wanita muda dengan jiwa idealis.{/i}"
    mc "{i}Itu aku.{/i}"
    mc "{i}Baru lulus, dan sudah menetapkan satu tujuan: Membongkar kasus korupsi pejabat Kota XX.{/i}"
    mc "{i}Kasus yang selama ini hanya dibisikkan, tak pernah diselesaikan.{/i}"
    mc "{i}Dan kini, aku berdiri di awal jalan—di depan dua pilihan.{/i}"
    show i_mc serius with fade
    mc "Kerja sendiri... atau gabung tim investigasi yang sudah punya pengalaman?"
    mc "Risikonya beda, tapi tujuannya sama."
    scene bg laptop with dissolve
label choices_awal:
    mc "{i}Aku harus mulai dari satu tempat. Entah bekerja sama dengan penegak hukum... atau mencari suara warga.{/i}"
menu:
    "Bekerja secara individu.":
        jump choices0_a
    "Bekerja dalam tim":
        jump choices0_b
label choices0_a:
    scene bg papan with pixellate
    "{i}Pencahayaan temaram. Sebuah papan penuh catatan dan foto terpasang di dinding. [povname] duduk di depan laptop, wajahnya serius.{/i}"
    show i_mc serius with fade
    mc "{i}Sudah berminggu-minggu aku menggali, membaca laporan keuangan, wawancara orang-orang yang takut menyebut nama sebenarnya.{/i}"
    mc "{i}Anggaran yang raib tanpa jejak, proyek pembangunan yang hanya ada di atas kertas, dan janji kampanye yang tak pernah ditepati…{/i}"
    mc "{i}Semua itu seperti benang kusut—tapi jika ditarik perlahan, semuanya berujung pada satu nama: wali kota.{/i}"

label choices_tempat:
    mc "{i}Aku harus mulai dari satu tempat. Entah bekerja sama dengan penegak hukum... atau mencari suara warga.{/i}"
menu:
    "Bekerja sama dengan penegak hukum":
        jump choices1_a
    "Mencari fakta lewat komunitas warga":
        jump choices1_b
label choices1_a:
    "{i}[povname] menyandarkan tubuh di kursi. Di layar laptopnya, terbuka lembar catatan digital berisi puluhan dokumen: laporan pengeluaran kota, transkrip wawancara, foto-foto proyek mangkrak.{/i}"
    mc "{i}Aku punya cukup data untuk mulai menggali lebih dalam. Tapi data saja tidak cukup."
    mc "{i}Kalau aku bertindak sendirian, bisa-bisa aku menjadi bulan-bulanan para…… itu bisa hilang tanpa jejak.{/i}"
    mc "{i}Tidak semua orang di sistem ini busuk, mungkin…mungkin saja masih ada satu-dua orang yang mau menegakkan hukum.{/i}"
    mc "{i}Dan aku tahu harus mulai dari mana.{/i}"
    stop music fadeout 1.0
    scene bg jaksa with fade
    play music "audio/Damai.mp3" fadein 1.0 volume 0.5
    show i_mc serius at right with easeinright
    "[povname] berdiri gugup di ruang tunggu. Ia memegang amplop coklat berisi berkas. Tatapannya menyapu para jaksa dan pengacara muda yang berlalu-lalang. Beberapa menatapnya aneh, sisanya terlalu sibuk."
    mc "{i}Aku pernah dengar tentang satu jaksa muda. Idealismenya masih hidup. Katanya, dia menolak sogokan dari kontraktor besar dan hampir dipindah paksa.{/i}"
    mc "{i}Aku tak punya pilihan selain mencoba menemuinya.{/i}"
    show i_jaksa at left with fade
    j "Anda wartawan yang mengirim email minggu lalu? Yang soal kasus wali kota?"
    mc "Iya. Saya punya bukti. Tapi saya butuh sistem hukum untuk melindungi sumber saya... dan juga diri saya sendiri."
    j "Kami sudah mendengar banyak tuduhan. Tapi sejauh ini, semua cuma rumor. Anda yakin punya sesuatu yang bisa membawa kasus ini naik ke penyidikan?"
    mc "Saya punya nama, rekaman, catatan transfer, dan beberapa foto dari lokasi proyek fiktif yang tak pernah selesai. Semua ini tidak akan ada artinya tanpa akses dan wewenang dari pihak Anda."
    j "..."
    "Ini bisa jadi jebakan... tapi bisa juga satu-satunya jalan. Aku hanya bisa berharap, idealisme masih hidup di antara setumpuk berkas dan rutinitas hukum."
    j "Saya akan menyampaikan ini ke atas. Tapi saya harus jujur — setelah ini, Anda akan masuk ke dalam lingkaran. Anda tidak bisa keluar dengan mudah. Dan Anda harus siap menghadapi tekanan dari luar maupun dalam."
    mc "..."
    mc "Kalau saya takut tekanan, saya tidak akan memulai ini dari awal."
    mc "{i}Aku tahu langkah ini mengubah segalanya. Tapi lebih baik mati karena kebenaran... daripada hidup di antara kebohongan yang kubiarkan sendiri.{/i}"
    stop music fadeout 1.0
    jump choices1_common

label choices1_b:
    show i_mc serius at right with fade
    play music "audio/Tegang.mp3" fadein 1.0 volume 0.5
    mc "{i}Sebelum memulai semua ini, setelah berhari-hari riset, aku menemukan mereka. Komunitas warga yang tidak hanya protes, tapi juga membawa bukti. Mereka pernah melaporkan sang walikota—meski selalu ditutup dengan alasan klasik: tidak terbukti.{/i}"
    mc "{i}Aku memutuskan untuk menghubungi mereka.{/i}"
    show forum1 at top with moveinbottom
    show forum2 at truecenter with moveinbottom
    "Mereka tidak hanya berani. Mereka siap."
    mc "{i}Bukti yang kukumpulkan dari mereka akan jadi bagian penting—bukan hanya untuk berita, tapi untuk membongkar sistem yang selama ini melindungi sang walikota.{/i}"
    "{i}Sudah tiga malam tanpa tidur. Setiap kalimat harus akurat, setiap data harus bisa diverifikasi. Ini bukan opini—ini peluru yang ditulis dengan fakta.{/i}"
    jump choices1_common

label choices1_common:
    scene bg papan with fade
    show i_mc serius
    mc "{i}Kutatap naskah final berita di laptopku.{/i}"
    mc "{i}Berita ini akan mengguncang kota. Akan menggoyahkan nama besar.{/i}"
    mc "{i}Dan sekarang tinggal satu hal yang belum kuputuskan{/i}:"
    label choices_nama:
        "Apakah aku akan menulis dengan namaku sendiri… atau bersembunyi di balik nama pena?"
    menu:
        "Gunakan identitas asli. {i}Risikonya nyata. Tapi kebenaran harus punya wajah.{/i}":
            jump choices2_a
        "Gunakan nama pena. {i}Yang penting adalah isi beritanya, bukan siapa yang menulis.{/i}":
            jump choices2_b
    label choices2_a:
    mc "{i}Aku tahu risikonya: intimidasi, gugatan hukum, bahkan ancaman fisik. Tapi kalau aku ingin warga percaya pada berita ini, aku sendiri harus berdiri di depannya.{/i}"
    mc "{i}Tak ada lagi ruang untuk keraguan.{/i}"
    "{i}Klik.{/i}"
    play sound "audio/Klik.mp3" volume 0.5
    "{i}Tombol “Publikasikan” ditekan.{/i}"
    "{i}Berita itu tayang. Lengkap dengan data pendukung, kronologi kasus, dan satu nama yang menjadi pusat semuanya: Walikota Tralalelo tralala.{/i}"
    stop music fadeout 1.0
    scene bg comments with fade
    play music "audio/Damai.mp3" fadein 1.0 volume 0.5
    mc "{i}Dalam satu malam, aku berubah dari wartawan lepas tak dikenal menjadi sorotan nasional.{/i}"
    mc "{i}Ada yang mendukung. Ada yang mengancam. Tapi semuanya membaca. Dan itu yang paling penting.{/i}"
    scene bg papan with fade
    "Namun.. ternyata hal tersebut bukanlah hal yang dapat berlalu begitu saja dengan ketenangan."
    "Pagi itu datang dengan semangat baru. Meski berita besar telah dirilis semalam, rasanya belum cukup sebelum sang walikota benar-benar ditangkap."
    stop music fadeout 1.0
    show i_mc serius
    play music "audio/Tegang.mp3" fadein 1.0 volume 0.5
    mc "{i}Aku kembali membuka laptop, berharap menemukan jejak tambahan yang bisa menjeratnya lebih dalam.{/i}"
    "{i}Tiba-tiba, bunyi ketukan di pintu memecah keheningan.{/i}"
    play sound "audio/Ketukan.mp3" volume 0.5
    "{i}Sebuah kotak kecil tergeletak begitu saja di depan rumah. Tidak ada pengantar. Tidak ada suara.{/i}"
    show i_mc kaget
    show tikus at truecenter
    pause
    hide tikus
    "{i}Isinya... lima bangkai tikus. Tanpa kepala.{/i}"
    label choices_ancaman:
        "Ancaman pertama."
    menu:
        "Rilis balasan teror":
            jump choices3_a
        "Diamkan ":
            jump choices3_b
    stop music fadeout 1.0
    label choices3_a:
    scene bg kamar with fade
    play music "audio/Damai.mp3" fadein 1.0 volume 0.5
    show i_mc serius
    mc "{i}Tentu saja mereka mencoba menakutiku. Tapi ini hanya memperkuat keyakinanku: aku sedang menyentuh sarang yang selama ini dibiarkan utuh.{/i}"
    mc "{i}Mereka berpikir ancaman menjijikkan bisa memadamkan apa yang sudah kubakar.{/i}"
    mc "{i}Kukirim ulang beritanya, kali ini dengan lampiran ancaman. Masyarakat berhak tahu, bahkan tentang bahayanya.{/i}"
    "{i}Dalam beberapa jam, tulisan itu viral.{/i}"
    "{i}Dari simpati muncul keberanian kolektif. Dari keraguan lahir gerakan. Dari suara satu orang, tumbuh gema.{/i}"
    stop music fadeout 1.0
    label choices_tolak:
    play music "audio/Tegang.mp3" fadein 1.0 volume 0.5
    mc "{i}Aku mengira semuanya selesai. Ternyata belum.{/i}"
    scene bg anon with fade
    "Email masuk, tanpa subjek. Isinya hanya dua baris:"
    "Nama lengkapku. Alamat rumah."
    mc "{i}Teror kali ini nyata. Mereka tahu siapa aku.{/i}"
    scene bg kamar with fade
    show i_mc takut
    mc "{i}Kukunci pintu. Kuselipkan alat darurat ke dalam tas kecilku—senter kecil, cutter, bahkan sebotol semprotan lada.{/i}"
    mc "{i}Kupikir aku siap.{/i}"
    mc "{i}Tapi pagi itu, petugas kebersihan yang biasa menyapu gangku… ternyata bukan petugas.{/i}"
    stop music fadeout 1.0
    scene bg tua with fade
    play music "audio/Adrenalin.mp3" fadein 1.0 volume 0.5
    "{i}Ruangan itu lembap, dinding-dindingnya ditumbuhi lumut. Bau besi karat dan debu menyengat. Tali di pergelangan tangannya sudah mulai menggesek kulit, tapi ia tak peduli.{/i}"
    show i_mc nangis at right
    show i_penculik at left
    "{i}[povname] menatap tajam sang penculik. Menunggunya mengeluarkan kata kata.{/i}"
    pc "“Kamu benar-benar nekad, ya? Menulis pakai nama asli, seakan nggak sadar sedang melawan apa."
    mc "Kalau kamu cukup takut untuk culik aku, berarti tulisan itu benar, kan?"
    pc "Kamu pikir kamu pahlawan? Dunia ini nggak sesimpel idealismemu. Yang kamu ganggu bukan cuma satu walikota."
    mc "Jadi kamu baru ngaku. Bukan cuma dia, kan? Siapa lagi yang kamu lindungi?"
    pc "Tidak penting. Yang penting sekarang, kamu bawa salinan datanya ke mana?"
    mc "Itu sudah dipublikasikan. Apa pun yang kamu lakukan, publik sudah tahu."
    pc "Berita bisa hilang. Bukti bisa dilenyapkan. Tapi kalau kamu mati... berita akan berhenti. Kamu ngerti maksudku?"
    mc "Aku ngerti. Tapi kamu juga harus ngerti satu hal: aku nggak sendiri."
    label choices_bukti:
        pc "Salah satu dari dua hal akan terjadi di sini—kamu kasih data itu, atau kamu dikubur dengan berita-beritamu."
    menu:
        "Serahkan semua bukti":
            jump choices4_a
        "Tolak menyerah sampai akhir ":
            jump choices4_b
    label choices4_a:
    show i_mc takut at right
    "{i}Penculik menodongkan senjata ke pelipisnya. Napasnya memburu, pelipisnya basah oleh keringat dingin.{/i}"
    pc "Serahkan semua. Sekarang. Kalau tidak, hidupmu selesai di sini."
    mc "{i}Kalau aku mati di sini... semuanya percuma.{/i}"
    show i_mc serius at right
    mc "Oke. Tapi janji... lepasin aku."
    pc "Buktinya?"
    mc "Drive-nya ada di rumah. Laptopku. Aku kasih semuanya. Asal... jangan cari yang lain."
    stop music fadeout 1.0
    scene bg papan with dissolve
    play music "audio/Sedih.mp3" fadein 1.0 volume 0.5
    "{i}Ia duduk di depan laptopnya. Tangan gemetar saat memilih file demi file.{/i}"
    mc "{i}Maaf... semuanya...{/i}"
    "{i}Satu klik, folder bukti terunggah ke link yang telah disiapkan oleh penculik.{/i}"
    play sound "audio/Klik.mp3" volume 0.5
    scene bg black with fade
    pc "Pintar. Hidup terus, ya. Tapi jangan pikir bisa kembali."
    stop music fadeout 1.0
    scene bg rumah laut with fade
    play music "audio/Damai.mp3" fadein 1.0 volume 0.5
    show i_mc serius
    "{i}Angin masih menerpa tirai tipis di jendela. Lampu meja menyala redup. Di depannya, laptop terbuka, tapi tak ada folder bernama 'korupsi' atau 'bukti'.{/i}"
    scene bg anon with fade
    "{i}Di dalam kotak masuk, ada email dari seorang teman jurnalis lama. 'Kau masih ingin buka suara? Ada cerita baru, lebih besar.'{/i}"
    "{i}Ia membaca, lalu diam.{/i}"
    "{i}Tangannya gemetar, bukan karena dingin.{/i}"
    scene bg rumah laut with fade
    show i_mc serius
    mc "Aku nggak bisa balik ke sana. Nggak sekarang..."
    scene bg cerita with fade
    "{i}Lalu ia membuka dokumen baru. Judulnya: "Kisah Kopi Pagi dan Tukang Roti di Ujung Jalan".{/i}"
    "{i}Terdengar konyol. Tapi kali ini, tidak ada ancaman. Tidak ada teror. Hanya cerita. Dan sunyi.{/i}"
    mc "Aku masih bisa menulis. Cuma... bukan lagi untuk menyulut, tapi untuk menyembuhkan."
    "{i}Ia menekan save. Di pojok bawah tidak lagi tertulis namanya, yang tertulis hanya lah sebuah identitas kosong 'Anonim'.{/i}"
    stop music fadeout 1.0
    jump choices4_common

    label choices4_b:
    play music "audio/Adrenalin.mp3" fadein 1.0 volume 0.5
    pc "Waktu habis. Bukti atau nyawa."
    show i_mc nangis at right
    mc "Kau pikir semua ini akan berhenti kalau aku mati? Akan ada yang meneruskan..."
    "{i}Penculik mencengkeram kerah bajunya dan mengangkat senjatanya lebih dekat.{/i}"
    mc "{i}Sial… ini akhirnya…{/i}"
    "{i}BRAK! Pintu gudang didobrak terbuka. Cahaya senter menyorot tajam ke arah mereka.{/i}"
    play sound "audio/Brak.mp3" volume 0.5
    dt "Lepaskan dia! Tangan di atas kepala sekarang!"
    "{i}Beberapa orang bersenjata masuk, salah satunya mengenakan jas panjang. Detektif.{/i}"
    hide i_penculik
    show i_detektif at left with fade
    dt "Kita dapat koordinat dari salah satu sumber yang kau hubungi sebelum diputus. Kau beruntung."
    show i_mc senang at right
    "{i}Penculik dilumpuhkan. [povname] nyaris roboh, namun segera ditopang seseorang—bukan petugas, tapi seorang perempuan dengan kacamata tegas dan ID card bertuliskan Direksi Media Aras.{/i}"
    stop music fadeout 1.0
    scene bg kantor with fade
    play music "audio/Damai.mp3" fadein 1.0 volume 0.5
    show i_mc senang at right
    show i_direktur at left
    "{i}Satu minggu kemudian. Suasana kantor penuh aktivitas. Ia kini duduk di kursi putar di ruang kaca kecil yang bertuliskan 'Editor Tamu–[povname]'.{/i}"
    d "Kau nyaris mati karena tulisanmu. Tapi justru itu yang membuat semua orang di sini menghormatimu."
    show i_mc serius at right
    mc "Aku... nggak tahu harus menulis apa lagi setelah ini."
    d "Tulis apa saja yang penting buatmu. Kau tidak harus terus menyuarakan dunia—cukup suaramu sendiri. Itu pun berharga."
    show i_mc senang at right
    "{i}Ia menatap layar laptop barunya. File baru dibuka. Judulnya masih kosong.{/i}"
    mc "Mungkin... ini bab berikutnya."
    stop music fadeout 1.0
    jump choices4_common

    label choices4_common:
    scene bg ending 1 with fade
    pause
    return

    label choices2_b:
    scene bg papan
    play music "audio/Misterius.mp3" fadein 1.0 volume 0.5
    show i_mc serius
    "{i}Di bawah tulisan tajam itu, terpampang nama 'Sasaran'. Nama pena itu telah digunakan sejak tahun pertama kuliah—pilihan yang kini terasa semakin tepat. Dunia maya mengenalnya sebagai pengungkap fakta gelap, tapi dunia nyata tak tahu siapa di baliknya.{/i}"
    "{i}Tulisan terakhirnya viral. Nama 'Sasaran' kembali menjadi bahan pembicaraan. Banyak yang penasaran, bertanya-tanya, dan bahkan mencoba menebak siapa identitas di balik nama itu.{/i}"
    scene bg temui with fade
    mc "{i}Satu lagi… tapi yang ini… berbeda.{/i}"
    label choices_pesan:
        "{i}Biasanya ia mengabaikan pesan misterius seperti ini. Tapi ada sesuatu dalam kata-katanya yang… memancing rasa penasaran.{/i}"
    menu:
        "Beri respon":
            jump choices2b_a
        "Abaikan":
            jump choices2b_b
    label choices2b_a:
    mc "{i}Bodoh kalau aku langsung memilih menemuinya. Tapi diam juga tak akan membawa apa-apa. Aku penasaran apa yang sebenarnya ia cari… atau tawarkan.{/i}"
    mc "{i}Aku mengetik balasan. 'Beri imbalan atau janji baru akan kupertimbangkan.'{/i}"
    scene bg balas with fade
    mc "{i}Dia tahu… terlalu banyak. Dia tahu… terlalu banyak. Nama samaran, email rahasia, bahkan ritme aku online tiap malam. Aku tidak pernah menyebarkan itu ke siapa pun.{/i}"
    mc "{i}Seseorang membocorkan ini… atau lebih buruk, aku sedang dipantau dari dalam. Tapi… apakah ini jalan untuk menyusup lebih dalam, atau justru jebakan?{/i}"
    label choices:
        "{i}Biasanya ia mengabaikan pesan misterius seperti ini. Tapi ada sesuatu dalam kata-katanya yang… memancing rasa penasaran.{/i}"
    menu:
        "Terima tawaran ":
            jump choices2ba_a
        "Tolak":
            jump choices2ba_b
    stop music fadeout 1.0
    label choices2ba_a:
    play music "audio/Tegang.mp3" fadein 1.0 volume 0.5
    scene bg papan
    show i_mc serius
    mc "{i}Ancaman nyawaku, artikel yang tak lagi aman, dan tawaran yang terlalu rapi untuk jadi kebetulan...{/i}"
    mc "{i}Semua itu membuat kepalaku nyaris meledak.{/i}"
    mc "{i}Mungkin… aku bisa bertahan hidup, dan menyusup lebih dalam?{/i}"
    mc "{i}Tapi semakin kupikirkan, semakin jelas—aku tidak sedang mengendalikan permainan ini.{/i}"
    mc "{i}Aku hanya pion.{/i}"
    mc "{i}Apa aku terlalu naif? Berjuang sendirian untuk kebenaran yang bahkan orang lain tak peduli?{/i}"
    mc "{i}Mereka sudah tahu identitasku. Mereka tahu semua dataku. Dan sekarang, mereka memberiku jalan keluar.{/i}"
    mc "{i}Bukan kemenangan... tapi setidaknya bukan kematian.{/i}"
    scene bg chance with fade
    mc "{i}Jariku gemetar di atas keyboard.{/i}"
    mc "{i}Bukan karena takut... tapi karena aku tahu, setelah ini, takkan ada jalan kembali.{/i}"
    mc "{i}Aku mengirim balasan lagi. '...Baik. Aku terima. Tapi ingat, ini bukan karena aku takut. Aku hanya… memilih bertahan hidup.'{/i}"
    scene bg bijak with fade
    stop music fadeout 1.0
    pause
    play music "audio/Damai.mp3" fadein 1.0 volume 0.5
    scene bg kantor with fade
    show i_mc serius at right
    show i_editor at left
    mc "{i}Beberapa minggu berlalu. Aku kembali dengan nama asliku, mengenakan jas resmi dengan ID kantor tergantung di leher. Redaksi baruku dingin, bersih, dan berkilau—tapi penuh bisikan tak terdengar.{/i}"
    e "Tulis soal aktor yang ribut sama pacarnya di Bali. Itu trending. Deadline sore ini."
    mc "Baik..."
    hide i_editor
    mc "{i}Setiap berita yang kutulis tentang korupsi, pembunuhan terselubung, atau rekayasa hukum… hilang. Tak satu pun naik tayang. Diganti dengan trivia, gosip, dan sensasi yang tak berarti.{/i}"
    mc "{i}Apakah ini yang mereka inginkan?{/i}"
    mc "{i}Seorang jurnalis yang diam, dengan pena yang tak lagi tajam?{/i}"
    mc "{i}Aku masih hidup. Tapi bukan sebagai aku.{/i}"
    mc "{i}Kadang aku berpikir, lebih baik aku mati sebagai seorang idealis…{/i}"
    mc "{i}Daripada hidup sebagai alat korporat yang bisu.{/i}"
    scene bg ending 2 with fade
    stop music fadeout 1.0
    pause
    return
            
    label choices2ba_b:
    jump choices_tolak
        
    label choices2b_b:
    play music "audio/.mp3" fadein 1.0 volume 0.5
    scene bg kamar with fade
    show i_mc serius
    mc "{i}Aku bangun pagi ini dengan perasaan yang cukup aneh.{/i}"
    mc "{i}Biasanya aku menyambut pagi dengan semangat, menyalakan TV sambil menyeduh kopi.{/i}"
    mc "{i}Tapi hari ini… aku takut. Bukan takut pada berita. Tapi pada siapa yang mungkin jadi berita berikutnya.{/i}"
    stop music fadeout 1.0
    play music "audio/Tegang.mp3" fadein 1.0 volume 0.5
    scene bg news with fade
    "{i}Seorang pemilik sekaligus pengelola panti asuhan Kasih Kita mengalami penyerangan malam tadi. Korban meninggal dunia karena pendarahan akut dan pisau yang dibalur dengan racun.{/i}"
    mc "{i}Tanganku gemetar memegang remote. Itu bukan korban biasa. Itu seseorang yang... pernah membantuku.{/i}"
    scene bg korban with fade
    mc "{i}Dadaku sesak. Kata-kata itu menembus jauh lebih dalam dari peluru.{/i}"
    mc "{i}Mereka tahu siapa saja yang berarti untukku.{/i}"
    mc "{i}Aku…{/i}"
    mc "{i}Aku hanya ingin menyuarakan kebenaran. Tapi apakah harus ada nyawa yang dibayar untuk itu?{/i}"
    stop music fadeout 1.0
    play music "audio/Sedih.mp3" fadein 1.0 volume 0.5
    scene bg rumah luar with fade
    show i_mc nangis at right
    mc "{i}Aku berjalan tanpa arah. Hanya ingin mencari udara. Mencari keheningan.{/i}"
    mc "{i}Sungai itu terlihat cantik dalam cahaya bulan. Tapi malam ini, ia seperti lubuk gelap yang memanggil.{/i}"
    mc "{i}Kugenggam surat kecil yang sudah kusiapkan. Kata-kataku di atas kertas, satu-satunya hal yang tak bisa mereka sensor.{/i}"
    mc "{i}Dalam hitungan ketiga…{/i}"
    mc "{i}Aku menyerah.{/i}"
    scene bg black with fade
    mc "{i}Polisi menemukanku beberapa hari kemudian. Suratku basah, tapi masih bisa dibaca.{/i}"
    mc "{i}Di balik layar komputer… sang peneror tersenyum. Ia menang.{/i}"
    scene bg ending 3 with fade
    pause
    stop music fadeout 1.0
    return

