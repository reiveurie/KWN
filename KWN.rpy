image i_mc senang = At('mc senang', sprite_highlight('mc'))
image i_mc serius = At('mc serius', sprite_highlight('mc'))
image i_mc takut = At('mc takut', sprite_highlight('mc'))
image i_mc nangis = At('mc nangis', sprite_highlight('mc'))

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
    zoom 0.7
image bg awal:
    "awal.png"
    zoom 0.7
image bg tua:
    "gedung tua.png"
    zoom 0.7
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

label start:
    scene bg awal with dissolve

    $povname = renpy.input("Enter your name to start the investigation", length=32)
    $povname = povname.strip()

    "Seorang wanita muda dengan jiwa idealis."
    "Itu aku."
    "Baru lulus, dan sudah menetapkan satu tujuan:
    Membongkar kasus korupsi pejabat Kota XX."
    "Kasus yang selama ini hanya dibisikkan, tak pernah diselesaikan."
    "Dan kini, aku berdiri di awal jalan—di depan dua pilihan."
    mc "Kerja sendiri... atau gabung tim investigasi yang sudah punya pengalaman?"
    mc "Risikonya beda, tapi tujuannya sama."


    scene bg papan with pixellate
    "{i}Pencahayaan temaram. Sebuah papan penuh catatan dan foto terpasang di dinding. [povname] duduk di depan laptop, wajahnya serius.{/i}"
    show i_mc serius with fade
    "Sudah berminggu-minggu aku menggali, membaca laporan keuangan, wawancara orang-orang yang takut menyebut nama sebenarnya."
    "Anggaran yang raib tanpa jejak, proyek pembangunan yang hanya ada di atas kertas, dan janji kampanye yang tak pernah ditepati…"
    "Semua itu seperti benang kusut—tapi jika ditarik perlahan, semuanya berujung pada satu nama: wali kota."

label choices_tempat:
    "Aku harus mulai dari satu tempat. Entah bekerja sama dengan penegak hukum... atau mencari suara warga."
menu:
    "Bekerja sama dengan penegak hukum":
        jump choices1_a
    "Mencari fakta lewat komunitas warga":
        jump choices1_b
label choices1_a:
    "{i}[povname] menyandarkan tubuh di kursi. Di layar laptopnya, terbuka lembar catatan digital berisi puluhan dokumen: laporan pengeluaran kota, transkrip wawancara, foto-foto proyek mangkrak.{/i}"
    "Aku punya cukup data untuk mulai menggali lebih dalam. Tapi data saja tidak cukup."
    "Kalau aku bertindak sendirian, bisa-bisa aku menjadi bulan-bulanan para…… itu bisa hilang tanpa jejak."
    "Tidak semua orang di sistem ini busuk, mungkin…mungkin saja masih ada satu-dua orang yang mau menegakkan hukum."
    "Dan aku tahu harus mulai dari mana."
    scene bg with fade
    show i_mc serius at right with easeinright
    "[povname] berdiri gugup di ruang tunggu. Ia memegang amplop coklat berisi berkas. Tatapannya menyapu para jaksa dan pengacara muda yang berlalu-lalang. Beberapa menatapnya aneh, sisanya terlalu sibuk."
    "Aku pernah dengar tentang satu jaksa muda. Idealismenya masih hidup. Katanya, dia menolak sogokan dari kontraktor besar dan hampir dipindah paksa."
    "Aku tak punya pilihan selain mencoba menemuinya."
    jump choices1_common

label choices1_b:
    "Sebelum memulai semua ini, setelah berhari-hari riset, aku menemukan mereka. Komunitas warga yang tidak hanya protes, tapi juga membawa bukti. Mereka pernah melaporkan sang walikota—meski selalu ditutup dengan alasan klasik: tidak terbukti."
    "Aku memutuskan untuk menghubungi mereka."
    show i_mc serius at right
    "Mereka tidak hanya berani. Mereka siap."
    "Bukti yang kukumpulkan dari mereka akan jadi bagian penting—bukan hanya untuk berita, tapi untuk membongkar sistem yang selama ini melindungi sang walikota."
    "Sudah tiga malam tanpa tidur. Setiap kalimat harus akurat, setiap data harus bisa diverifikasi. Ini bukan opini—ini peluru yang ditulis dengan fakta."
    jump choices1_common

label choices1_common:
    "Berita ini akan mengguncang kota. Akan menggoyahkan nama besar."
    "Dan sekarang tinggal satu hal yang belum kuputuskan:"
    label choices_nama:
        "Apakah aku akan menulis dengan namaku sendiri… atau bersembunyi di balik nama pena?"
    menu:
        "Gunakan identitas asli. {i}Risikonya nyata. Tapi kebenaran harus punya wajah.{/i}":
            jump choices2_a
        "Gunakan nama pena. {i}Yang penting adalah isi beritanya, bukan siapa yang menulis.{/i}":
            jump choices2_b
    label choices2_a:
    "Aku tahu risikonya: intimidasi, gugatan hukum, bahkan ancaman fisik. Tapi kalau aku ingin warga percaya pada berita ini, aku sendiri harus berdiri di depannya."
    "Tak ada lagi ruang untuk keraguan."
    "{i}Klik.{/i}"
    "{i}Berita itu tayang. Lengkap dengan data pendukung, kronologi kasus, dan satu nama yang menjadi pusat semuanya: Walikota Tralalelo tralala.{/i}"
    "Dalam satu malam, aku berubah dari wartawan lepas tak dikenal menjadi sorotan nasional."
    "Ada yang mendukung. Ada yang mengancam. Tapi semuanya membaca. Dan itu yang paling penting."
    "Namun.. ternyata hal tersebut bukanlah hal yang dapat berlalu begitu saja dengan ketenangan."
    "Pagi itu datang dengan semangat baru. Meski berita besar telah dirilis semalam, rasanya belum cukup sebelum sang walikota benar-benar ditangkap."
    "Aku kembali membuka laptop, berharap menemukan jejak tambahan yang bisa menjeratnya lebih dalam."
    "{i}Tiba-tiba, bunyi ketukan di pintu memecah keheningan.{/i}"
    "{i}Sebuah kotak kecil tergeletak begitu saja di depan rumah. Tidak ada pengantar. Tidak ada suara.{/i}"
    show i_mc takut at right
    "{i}Isinya... lima bangkai tikus. Tanpa kepala.{/i}"
    label choices_ancaman:
        "Ancaman pertama."
    menu:
        "Rilis balasan teror":
            jump choices3_a
        "Diamkan ":
            jump choices3_b
    label choices3_a:
    scene bg kamar with fade
    show i_mc serius
    "Tentu saja mereka mencoba menakutiku. Tapi ini hanya memperkuat keyakinanku: aku sedang menyentuh sarang yang selama ini dibiarkan utuh."
    "Mereka berpikir ancaman menjijikkan bisa memadamkan apa yang sudah kubakar."
    "Kukirim ulang beritanya, kali ini dengan lampiran ancaman. Masyarakat berhak tahu, bahkan tentang bahayanya."
    "{i}Dalam beberapa jam, tulisan itu viral.{/i}"
    "{i}Dari simpati muncul keberanian kolektif. Dari keraguan lahir gerakan. Dari suara satu orang, tumbuh gema.{/i}"
    "Aku mengira semuanya selesai. Ternyata belum."
    "Email masuk, tanpa subjek. Isinya hanya dua baris:"
    "Nama lengkapku. Alamat rumah."
    "Teror kali ini nyata. Mereka tahu siapa aku."
    "Kukunci pintu. Kuselipkan alat darurat ke dalam tas kecilku—senter kecil, cutter, bahkan sebotol semprotan lada."
    "Kupikir aku siap."
    "Tapi pagi itu, petugas kebersihan yang biasa menyapu gangku… ternyata bukan petugas."
    scene bg tua
    show i_mc nangis at left with fade
    "{i}Ruangan itu lembap, dinding-dindingnya ditumbuhi lumut. Bau besi karat dan debu menyengat. Tali di pergelangan tangannya sudah mulai menggesek kulit, tapi ia tak peduli.{/i}"
    "{i}[povname] menatap tajam sang penculik. Menunggunya mengeluarkan kata kata.{/i}"
    label choices_bukti:
        "Salah satu dari dua hal akan terjadi di sini—kamu kasih data itu, atau kamu dikubur dengan berita-beritamu."
    menu:
        "Serahkan semua bukti":
            jump choices4_a
        "Tolak menyerah sampai akhir ":
            jump choices4_b
    label choices4_a:
    scene bg papan with dissolve
    "{i}Ia duduk di depan laptopnya. Tangan gemetar saat memilih file demi file.{/i}"
    mc "{i}Maaf... semuanya...{/i}"
    scene bg rumah laut
    show i_mc serius with fade
    "{i}Angin masih menerpa tirai tipis di jendela. Lampu meja menyala redup. Di depannya, laptop terbuka, tapi tak ada folder bernama 'korupsi' atau 'bukti'.{/i}"
    "{i}Di dalam kotak masuk, ada email dari seorang teman jurnalis lama. 'Kau masih ingin buka suara? Ada cerita baru, lebih besar.'{/i}"
    "{i}Ia membaca, lalu diam.{/i}"
    "{i}Tangannya gemetar, bukan karena dingin.{/i}"
    mc "Aku nggak bisa balik ke sana. Nggak sekarang..."
    "{i}Lalu ia membuka dokumen baru. Judulnya: "Kisah Kopi Pagi dan Tukang Roti di Ujung Jalan".{/i}"
    "{i}Terdengar konyol. Tapi kali ini, tidak ada ancaman. Tidak ada teror. Hanya cerita. Dan sunyi.{/i}"
    mc "Aku masih bisa menulis. Cuma... bukan lagi untuk menyulut, tapi untuk menyembuhkan."
    "{i}Ia menekan save. Di pojok bawah tidak lagi tertulis namanya, yang tertulis hanya lah sebuah identitas kosong 'Anonim'.{/i}"
    jump choices4_common

    label choices4_b:
    show i_mc senang
    "{i}Ia menatap layar laptop barunya. File baru dibuka. Judulnya masih kosong.{/i}"
    mc "Mungkin... ini bab berikutnya."
    jump choices4_common

    label choices4_common:
    scene bg ending 1

    label choices2_b:
    show i_mc serius
    label choices_pesan:
        "{i}Biasanya ia mengabaikan pesan misterius seperti ini. Tapi ada sesuatu dalam kata-katanya yang… memancing rasa penasaran.{/i}"
    menu:
        "Beri respon":
            jump choices2b_a
        "Abaikan":
            jump choices2b_b
    label choices2b_a:
    "Bodoh kalau aku langsung memilih menemuinya. Tapi diam juga tak akan membawa apa-apa. Aku penasaran apa yang sebenarnya ia cari… atau tawarkan."
    mc "Dia tahu… terlalu banyak. Dia tahu… terlalu banyak. Nama samaran, email rahasia, bahkan ritme aku online tiap malam. Aku tidak pernah menyebarkan itu ke siapa pun."
    mc "Seseorang membocorkan ini… atau lebih buruk, aku sedang dipantau dari dalam. Tapi… apakah ini jalan untuk menyusup lebih dalam, atau justru jebakan?"
    label choices:
        "{i}Biasanya ia mengabaikan pesan misterius seperti ini. Tapi ada sesuatu dalam kata-katanya yang… memancing rasa penasaran.{/i}"
    menu:
        "Terima tawaran ":
            jump choices2ba_a
        "Tolak":
            jump choices2ba_b
    label choices2ba_a:
    "Ancaman nyawaku, artikel yang tak lagi aman, dan tawaran yang terlalu rapi untuk jadi kebetulan..."
    "Semua itu membuat kepalaku nyaris meledak."
    "Mungkin… aku bisa bertahan hidup, dan menyusup lebih dalam?"
    "Tapi semakin kupikirkan, semakin jelas—aku tidak sedang mengendalikan permainan ini."
    "Aku hanya pion."
    "Apa aku terlalu naif? Berjuang sendirian untuk kebenaran yang bahkan orang lain tak peduli?"
    "Mereka sudah tahu identitasku. Mereka tahu semua dataku. Dan sekarang, mereka memberiku jalan keluar."
    "Bukan kemenangan... tapi setidaknya bukan kematian."
    "Apakah ini yang mereka inginkan?"
    "Seorang jurnalis yang diam, dengan pena yang tak lagi tajam?"
    "Aku masih hidup. Tapi bukan sebagai aku."
    "Kadang aku berpikir, lebih baik aku mati sebagai seorang idealis…"
    "Daripada hidup sebagai alat korporat yang bisu."
    scene bg ending 2
            
    label choices2ba_b:
    jump choices2_a
        
    label choices2b_b:
    "Aku bangun pagi ini dengan perasaan yang cukup aneh."
    "Biasanya aku menyambut pagi dengan semangat, menyalakan TV sambil menyeduh kopi."
    "Tapi hari ini… aku takut. Bukan takut pada berita. Tapi pada siapa yang mungkin jadi berita berikutnya."

















    return
