image i_mc senang = At('mc senang', sprite_highlight('mc'))
image i_mc serius = At('mc serius', sprite_highlight('mc'))
image i_mc takut = At('mc takut', sprite_highlight('mc'))
image i_mc nangis = At('mc nangis', sprite_highlight('mc'))
image i_mc kaget = At('mc kaget', sprite_highlight('mc'))
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
image i_detektif = At('detektif', sprite_highlight('dt'))
image i_staff = At('staff', sprite_highlight('s'))
image i_arulla datar = At('arulla datar', sprite_highlight('a'))
image i_arulla marah = At('arulla marah', sprite_highlight('a'))
image i_arulla nangis = At('arulla nangis', sprite_highlight('a'))
image i_arulla kaget = At('arulla kaget', sprite_highlight('a'))
image i_arulla senyum = At('arulla senyum', sprite_highlight('a'))
image i_arulla smirk = At('arulla smirk', sprite_highlight('a'))

define pov = Character("[povname]")
define mc = Character("[povname]", image='i_mc', callback=name_callback, cb_name='mc')
define j = Character("Jaksa", image='i_jaksa', callback=name_callback, cb_name='j')
define pc = Character("Penculik", image='i_penculik', callback=name_callback, cb_name='pc')
define d = Character("Direktur", image='i_direktur', callback=name_callback, cb_name='d')
define p = Character("Polisi", image='i_polisi', callback=name_callback, cb_name='p')
define z = Character("Zaki", image='i_zaki', callback=name_callback, cb_name='z')
define pg = Character("Pegawai Kejaksaan", image='i_pegawai', callback=name_callback, cb_name='pg')
define dt = Character("Detektif", image='i_detektif', callback=name_callback, cb_name='dt')
define pgw = Character("Pegawai Walikota", image='i_pegawaiw', callback=name_callback, cb_name='pgw')
define s = Character("Staff Negara", image='i_staff', callback=name_callback, cb_name='s')
define a = Character("Arulla", image='i_arulla', callback=name_callback, cb_name='a')


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
    zoom 1
image arulla senyum:
    "Arulla senyum.png"
    zoom 1
image arulla kaget:
    "Arulla kaget.png"
    zoom 1
image arulla marah:
    "Arulla marah.png"
    zoom 1
image arulla nangis:
    "Arulla nangis.png"
    zoom 1
image arulla datar:
    "Arulla datar.png"
    zoom 1
image mc takut:
    "MC_takut aja.png"
    zoom 0.5
image polisi:
    "Polisi 1_Topi.png"
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
    zoom 1
image jaksa:
    "Jaksa aja.png"
    zoom 0.5
image detektif:
    "Detektif.png"
    zoom 1
image penculik:
    "Penculik.png"
    zoom 0.5
image direktur:
    "Direktur.png"
    zoom 0.5
image pegawai:
    "Pegawai 2.png"
    zoom 1
image pegawaiw:
    "Pegawai 1.png"
    zoom 1
image bg papan:
    "Meja investigasi prolog_plot 1.png"
    zoom 0.7
image bg papan gelap:
    "papan gelap.png"
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
    zoom 1
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
    zoom 1
image bg rek:
    "rek.png"
    zoom 1
image bg walkot:
    "walkot.png"
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
    zoom 1
image bg lorong:
    "lorong.png"
    zoom 1
image bg inter:
    "Ruang Interogasi.png"
    zoom 1
image bg tahan:
    "Ruang Tahanan.png"
    zoom 1

label start:
    scene bg awal with dissolve

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
    scene bg jaksa with fade
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
    jump choices1_common

label choices1_b:
    show i_mc serius at right
    mc "{i}Sebelum memulai semua ini, setelah berhari-hari riset, aku menemukan mereka. Komunitas warga yang tidak hanya protes, tapi juga membawa bukti. Mereka pernah melaporkan sang walikota—meski selalu ditutup dengan alasan klasik: tidak terbukti.{/i}"
    mc "{i}Aku memutuskan untuk menghubungi mereka.{/i}"
    show forum1 at top with moveinbottom
    show forum2 at truecenter with moveinbottom
    "Mereka tidak hanya berani. Mereka siap."
    mc "{i}Bukti yang kukumpulkan dari mereka akan jadi bagian penting—bukan hanya untuk berita, tapi untuk membongkar sistem yang selama ini melindungi sang walikota.{/i}"
    "{i}Sudah tiga malam tanpa tidur. Setiap kalimat harus akurat, setiap data harus bisa diverifikasi. Ini bukan opini—ini peluru yang ditulis dengan fakta.{/i}"
    jump choices1_common

label choices1_common:
    scene bg papan with dissolve
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
    "{i}Tombol “Publikasikan” ditekan.{/i}"
    "{i}Berita itu tayang. Lengkap dengan data pendukung, kronologi kasus, dan satu nama yang menjadi pusat semuanya: Walikota Tralalelo tralala.{/i}"
    scene bg comments with fade
    mc "{i}Dalam satu malam, aku berubah dari wartawan lepas tak dikenal menjadi sorotan nasional.{/i}"
    mc "{i}Ada yang mendukung. Ada yang mengancam. Tapi semuanya membaca. Dan itu yang paling penting.{/i}"
    scene bg papan with fade
    "Namun.. ternyata hal tersebut bukanlah hal yang dapat berlalu begitu saja dengan ketenangan."
    "Pagi itu datang dengan semangat baru. Meski berita besar telah dirilis semalam, rasanya belum cukup sebelum sang walikota benar-benar ditangkap."
    show i_mc serius
    mc "{i}Aku kembali membuka laptop, berharap menemukan jejak tambahan yang bisa menjeratnya lebih dalam.{/i}"
    "{i}Tiba-tiba, bunyi ketukan di pintu memecah keheningan.{/i}"
    "{i}Sebuah kotak kecil tergeletak begitu saja di depan rumah. Tidak ada pengantar. Tidak ada suara.{/i}"
    show i_mc kaget
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
    mc "{i}Tentu saja mereka mencoba menakutiku. Tapi ini hanya memperkuat keyakinanku: aku sedang menyentuh sarang yang selama ini dibiarkan utuh.{/i}"
    mc "{i}Mereka berpikir ancaman menjijikkan bisa memadamkan apa yang sudah kubakar.{/i}"
    mc "{i}Kukirim ulang beritanya, kali ini dengan lampiran ancaman. Masyarakat berhak tahu, bahkan tentang bahayanya.{/i}"
    "{i}Dalam beberapa jam, tulisan itu viral.{/i}"
    "{i}Dari simpati muncul keberanian kolektif. Dari keraguan lahir gerakan. Dari suara satu orang, tumbuh gema.{/i}"
    label choices_tolak:
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
    scene bg tua with fade
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
    pc "Salah satu dari dua hal akan terjadi di sini—kamu kasih data itu, atau kamu dikubur dengan berita-beritamu."
    label choices_bukti:
        "Salah satu dari dua hal akan terjadi di sini—kamu kasih data itu, atau kamu dikubur dengan berita-beritamu."
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
    scene bg papan with dissolve
    "{i}Ia duduk di depan laptopnya. Tangan gemetar saat memilih file demi file.{/i}"
    mc "{i}Maaf... semuanya...{/i}"
    "{i}Satu klik, folder bukti terunggah ke link yang telah disiapkan oleh penculik.{/i}"
    scene bg black with fade
    pc "Pintar. Hidup terus, ya. Tapi jangan pikir bisa kembali."
    scene bg rumah laut with fade
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
    jump choices4_common

    label choices4_b:
    pc "Waktu habis. Bukti atau nyawa."
    show i_mc nangis at right
    mc "Kau pikir semua ini akan berhenti kalau aku mati? Akan ada yang meneruskan..."
    "{i}Penculik mencengkeram kerah bajunya dan mengangkat senjatanya lebih dekat.{/i}"
    mc "{i}Sial… ini akhirnya…{/i}"
    "{i}BRAK! Pintu gudang didobrak terbuka. Cahaya senter menyorot tajam ke arah mereka.{/i}"
    dt "Lepaskan dia! Tangan di atas kepala sekarang!"
    "{i}Beberapa orang bersenjata masuk, salah satunya mengenakan jas panjang. Detektif.{/i}"
    hide i_penculik
    show i_detektif at left with fade
    dt "Kita dapat koordinat dari salah satu sumber yang kau hubungi sebelum diputus. Kau beruntung."
    show i_mc senang at right
    "{i}Penculik dilumpuhkan. [povname] nyaris roboh, namun segera ditopang seseorang—bukan petugas, tapi seorang perempuan dengan kacamata tegas dan ID card bertuliskan Direksi Media Aras.{/i}"
    scene bg kantor with fade
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
    jump choices4_common

    label choices4_common:
    scene bg ending 1 with fade
    return

    label choices2_b:
    scene bg papan with fade
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
    label choices2ba_a:
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
    #TODO: editor
    mc "{i}Beberapa minggu berlalu. Aku kembali dengan nama asliku, mengenakan jas resmi dengan ID kantor tergantung di leher. Redaksi baruku dingin, bersih, dan berkilau—tapi penuh bisikan tak terdengar.{/i}"
    mc "{i}Setiap berita yang kutulis tentang korupsi, pembunuhan terselubung, atau rekayasa hukum… hilang. Tak satu pun naik tayang. Diganti dengan trivia, gosip, dan sensasi yang tak berarti.{/i}"
    mc "{i}Apakah ini yang mereka inginkan?{/i}"
    mc "{i}Seorang jurnalis yang diam, dengan pena yang tak lagi tajam?{/i}"
    mc "{i}Aku masih hidup. Tapi bukan sebagai aku.{/i}"
    mc "{i}Kadang aku berpikir, lebih baik aku mati sebagai seorang idealis…{/i}"
    mc "{i}Daripada hidup sebagai alat korporat yang bisu.{/i}"
    scene bg ending 2 with fade
    return
            
    label choices2ba_b:
    jump choices_tolak
        
    label choices2b_b:
    scene bg kamar with fade
    show i_mc serius
    "Aku bangun pagi ini dengan perasaan yang cukup aneh."
    "Biasanya aku menyambut pagi dengan semangat, menyalakan TV sambil menyeduh kopi."
    "Tapi hari ini… aku takut. Bukan takut pada berita. Tapi pada siapa yang mungkin jadi berita berikutnya."
    scene bg news with fade
    "{i}Seorang pemilik sekaligus pengelola panti asuhan Kasih Kita mengalami penyerangan malam tadi. Korban meninggal dunia karena pendarahan akut dan pisau yang dibalur dengan racun.{/i}"
    mc "{i}Tanganku gemetar memegang remote. Itu bukan korban biasa. Itu seseorang yang... pernah membantuku.{/i}"
    scene bg korban with fade
    mc "{i}Dadaku sesak. Kata-kata itu menembus jauh lebih dalam dari peluru.{/i}"
    mc "{i}Mereka tahu siapa saja yang berarti untukku.{/i}"
    mc "{i}Aku…{/i}"
    mc "{i}Aku hanya ingin menyuarakan kebenaran. Tapi apakah harus ada nyawa yang dibayar untuk itu?{/i}"
    scene bg rumah luar with fade
    show i_mc serius at right
    mc "{i}Aku berjalan tanpa arah. Hanya ingin mencari udara. Mencari keheningan.{/i}"
    mc "{i}Sungai itu terlihat cantik dalam cahaya bulan. Tapi malam ini, ia seperti lubuk gelap yang memanggil.{/i}"
    mc "{i}Kugenggam surat kecil yang sudah kusiapkan. Kata-kataku di atas kertas, satu-satunya hal yang tak bisa mereka sensor.{/i}"
    mc "{i}Dalam hitungan ketiga…{/i}"
    mc "{i}Aku menyerah.{/i}"
    scene bg black with fade
    mc "{i}Polisi menemukanku beberapa hari kemudian. Suratku basah, tapi masih bisa dibaca.{/i}"
    mc "{i}Di balik layar komputer… sang peneror tersenyum. Ia menang.{/i}"
    scene bg ending 3 with fade
    return

label choices0_b:
scene bg kantor with fade
show i_mc senang at left
mc "{i}Aku duduk di kubik kerjaku, meniup pelan kopi panas yang baru saja kuambil dari pantry. Suasana masih tenang… sampai notifikasi itu masuk.{/i}"
show i_zaki kaget at right
z "Hah? Lihat ini…"
scene bg rek with fade
mc "“Ini… jumlahnya gila banget. Dan rekening tujuan ini… kelihatan aneh."
scene bg kantor with fade
show i_mc serius
show i_zaki kaget at right
show i_arulla kaget at left
a "Apakah nggak sebaiknya kita lapor ke polisi dulu? Aku merasa ini bisa aja jebakan…"
z "Apa?! Arul, data sekuat ini nggak bisa kita diamkan! Kalau kita nunggu dan ternyata benar, publik bisa dirugikan!"
label choices_saran:
    mc "{i}Zaki emosi. Arulla ragu. Tapi aku harus mengambil keputusan. Ini bisa jadi titik awal, atau justru awal kehancuran.{/i}"
menu:
    "Terima saran Zaki. {i}Kita harus bertindak. Kita selidiki dulu dan publikasikan jika perlu.{/i}":
        jump choices_z
    "Terima saran Arulla. {i}Arulla ada benarnya. Kita nggak bisa gegabah. Lapor dulu.{/i}":
        jump choices_a

label choices_z:
mc "Arulla, aku ngerti kekhawatiranmu… tapi aku pikir Zaki benar kali ini."
show i_zaki serius at right
z "Serius? Jadi kita ambil langkah ini?"
show i_mc serius
mc "Iya, kita ambil langkah, tapi tetap hati-hati. Data ini terlalu besar untuk langsung diumumkan. Kita butuh konfirmasi tambahan."
show i_zaki smirk at right
z "Akhirnya! Aku setuju banget. Kita gali lebih dalam. Besok kita ke kejaksaan dulu."
a "Kalau ini jebakan, aku harap kita cukup siap menanggung risikonya..."
mc "Kita kerja berdasarkan data, bukan asumsi. Dan kita nggak sendirian."
scene bg jaksa with fade
show i_mc serius 
show i_zaki serius at right
show i_pegawai at left
pg "Maaf, kami tidak bisa memberikan data detail tanpa surat resmi. Tapi... kalau maksud kalian soal aliran dana proyek revitalisasi, itu memang sempat jadi pembicaraan di internal."
hide i_pegawai
show i_arulla datar at left
z "Proyek revitalisasi? Tapi ini bukan dana dari DPKAD…"
mc "Berarti ada kemungkinan sumber dana dari luar anggaran resmi?"
pg "Itu kalian yang harus buktikan. Tapi saya sarankan, coba cek bagian pengadaan dan kepegawaian. Kadang mereka yang tahu lebih dulu."
scene bg walkot with fade
show i_pegawaiw at left
show i_mc serius
show i_zaki serius at right
pgw "Kalau soal rekening itu… beberapa staf pernah dengar, tapi nggak berani komentar. Yang jelas, beberapa hari ini ruangan kepala dinas dikunci terus."
hide i_pegawaiw
show i_arulla datar at left
mc "Kita makin dekat. Tapi kita belum punya cukup bukti untuk ditayangkan."
z "Mungkin waktunya main ‘off the record’ sama orang dalam."
a "Atau kita akan memancing masalah yang lebih besar dari yang kita duga."
mc "{i}Kebenaran memang nggak pernah datang tanpa harga. Tapi sekarang kita sudah terlalu dalam untuk mundur.{/i}"
jump choicest_common

label choices_a:
mc "Arulla ada benarnya. Kita nggak bisa gegabah. Data ini anonim, dan kalau ini jebakan… kita yang habis."
show i_zaki emosi at right
show i_arulla datar at left
z "Jadi kita lapor polisi? Dan nunggu? Sementara orang-orang yang bersalah bisa ngelap jejak mereka?"
a "Zaki… kita cuma mau semua ini tetap aman. Buat kita juga."
mc "Aku ngerti kamu frustasi. Tapi ini suara terbanyak. Kita serahkan dulu ke pihak yang berwenang."
scene bg bulan with fade
scene bg kantor with fade
show i_zaki emosi at right
show i_mc serius
show i_arulla datar at left
z "Sudah sebulan, dan nggak ada kabar apa-apa! Mereka nunda, nutupin, atau… atau emang sengaja?"
mc "Zaki, tolong… sabar dulu. Mungkin mereka sedang kumpulkan bukti…"
z "Atau mungkin mereka nggak akan pernah bertindak. Dan saat kita terus nunggu, kasus ini hilang begitu aja!"
show i_mc takut
a "Aku juga mulai ngerasa aneh. Tapi kalau kita nekat sekarang, bisa-bisa kita yang kena."
mc "{i} Aku terus menenangkannya. Tapi di dalam hati, aku juga mulai ragu.{/i}"
mc "{i}Apa ini memang jebakan?{/i}"
mc "{i} Atau… ada sesuatu yang jauh lebih besar, yang menunggu di depan?{/i}"
jump choicest_common

label choicest_common:
scene bg kantor with fade
show i_mc serius
mc "{i} Pagi itu, kami menemukan sebuah kotak misterius di depan pintu kantor. Tidak ada kurir, tidak ada pemberitahuan. Tapi yang membuatku gemetar… nama kami bertiga tertulis jelas di atas kotak itu.{/i}"
show i_zaki emosi at right
show i_arulla kaget at left
z "Siapa yang ngirim ini?! Siapa yang berani main-main begini?!"
a "Jangan dibuka dulu… baunya... itu bukan bau biasa..."
"{i} Hanya satu benda di dalamnya.{/i}"
show i_mc takut
show i_arulla nangis at left
"{i}Seekor kepala babi. Masih mentah. Bau amis darahnya menyengat.{/i}"
"{i}Ini bukan peringatan biasa. Ini ancaman.{/i}"
"{i}Dan mereka tahu siapa kami.{/i}"
z "Kita nggak bisa diam lagi! Ini… ini udah gila! Kita harus teriak ke publik! Semua orang harus tahu ini!"
a "Kita harus berhenti. Ini bukan cuma soal data lagi. Kita bisa mati…"
mc "{i}Dan di sinilah aku, berdiri di antara dua jurang.{i/}"
mc "{i} Menjaga nyawa…{/i}"
label choices_t:
    mc "{i}Atau menyuarakan kebenaran.{/i}"
menu:
    "Tinggalkan kasus demi keselamatan":
        jump choicest_a
    "Publikasi berita teror terhadap jurnalis":
        jump choicest_b

label choicest_a:
mc "{i} Setelah semalam tanpa tidur, aku membuat keputusan.{/i}"
mc "{i}Keselamatan kami… jauh lebih penting daripada semuanya.{/i}"
show i_mc serius
mc "Kita mundur. Sampai di sini saja."
a "Terima kasih… aku nggak tahu harus bagaimana kalau kamu tetap maju."
show i_zaki serius at right
z "Baik. Tapi aku nggak akan berhenti. Aku akan cari jalanku sendiri."
scene bg hari with fade
mc "{i}Arulla mengundurkan diri keesokan harinya. Katanya ia ingin hidup yang tenang bersama keluarganya.{/i}"
mc "{i}Zaki… dia tetap bertarung, tapi sendirian. Aku tidak tahu ke mana dia pergi setelah itu.{/i}"
scene bg papan with fade
show i_mc serius
mc "{i}Dan aku… tetap di sini.{/i}"
mc "{i}Menjalani hidup yang stabil, mengejar berita-berita ringan seperti cita-citaku waktu kecil.{/i}"
scene bg papan gelap
show i_mc serius
mc "{i}Tapi jauh di dalam hati… aku tahu, kejahatan sang walikota mungkin tidak akan pernah terungkap.{/i}"
scene bg ending 5 with fade
return

label choicest_b:
mc "{i}Kami memutuskan untuk tidak diam.{/i}"
mc "{i}Kami mempublikasikan teror itu.{/i}"
mc "{i}Kami percaya… jika kami bersuara, kami tidak akan sendirian.{/i}"
scene bg pub with fade
"{i}Artikel diunggah, ratusan komentar dan retweet menyambutnya{/i}."
z "Kita mulai perang ini… Tapi kali ini, kita punya penonton."
a "Semoga ini cukup buat bikin mereka takut."
scene bg hari with fade
scene bg black
mc "{i}Artikel kami meledak. Bukan hanya masyarakat yang marah, tapi juga para jurnalis dari redaksi lain. Ternyata, kami bukan satu-satunya yang pernah diteror. Satu per satu mereka bergabung.{/i}"
scene bg sn
s "Kejadian ini adalah bentuk ancaman terhadap demokrasi. Ketika kebebasan pers mulai dibungkam, itu berarti Pancasila bangsa telah dilukai."
"Staff Negara X Dipecat Setelah Komentar Kontroversial."
mc "{i}Komentarnya viral, tapi posisinya hilang. Ia dipecat, diganti begitu saja… oleh sosok yang tidak banyak bicara, namun kami tahu siapa yang menarik benangnya.{/i}"
scene bg kantor with fade
show i_mc serius at left
show i_zaki serius at right
show surat at truecenter with moveinbottom
mc "{i}Sebuah undangan makan malam tiba. Hotel mewah, jamuan elegan. Bukan hanya kami — hampir seluruh jurnalis nasional diundang. Tidak disebutkan agenda, hanya silaturahmi dan apresiasi atas peran media.{/i}"
hide surat with fade
show i_zaki emosi at right
show i_mc serius
show i_arulla kaget at left
z "Ini bukan silaturahmi. Ini bentuk tekanan."
a "Kalau kita nggak datang… bukankah itu bisa jadi celah? Mereka bisa bilang kita anti-dialog."
label choices_m:
    mc "{i}Dua arah terbentang di hadapan kami…{/i}"
menu:
    "Datang ke Jamuan Makan Malam":
        jump choicesm_a
    "Tidak Datang":
        jump choicesm_b

label choicesm_a:
scene bg lorong with fade
mc "{i}Kami memutuskan untuk datang.{/i}"
mc "{i} Berada di kandang yang sama dengan lawan... adalah kesempatan terbaik untuk menggali lebih dalam.{/i}"
mc "{i}Siapa tahu, satu langkah lebih dekat ke bukti.{/i}"
show i_polisi at left
show i_zaki serius at right
show i_mc serius
p "Mohon maaf, sesuai prosedur keamanan, semua tamu dilarang membawa alat perekam, ponsel, atau perangkat elektronik lainnya."
hide i_polisi
show i_arulla datar at left
z "Mereka tahu... Mereka tahu kita akan coba menyadap."
a "Kita tetap masuk? Atau pulang saja?"
mc "{i}Kami menepi sebentar dari antrean masuk.{/i}"
label choices_r:
    mc "{i} Rapat kecil di lorong hotel jadi tempat penentu.{/i}"
menu:
    "Sembunyikan penyadap dan kamera mini":
        jump choicesr_a
    "Turuti aturan dan masuk dengan tangan kosong":
        jump choicesr_b

label choicesr_a:
mc "{i} Zaki dulunya anak SMK kelistrikan.{/i}"
mc "{i} Meski kini lebih akrab dengan kata dan data, kemampuannya tidak sepenuhnya hilang—dan koneksinya lebih hidup dari sebelumnya.{/i}"
show i_zaki senyum at right
z "Aku sudah menduga hal ini sebelumnya. Ini kamera mini, bisa merekam suara dan gambar. Kalau kutaruh di jas kamu, enggak bakal ada yang curiga."
show i_arulla kaget at left
a "Kok bisa nemu alat begini secepat itu?"
show i_zaki smirk at right
z "Ada teman lamaku yang biasanya bikin ini buat sasaeng. Tapi karena kali ini buat keadilan, dia kasih gratis. Lumayan mahal kalau beli."
mc "{i}Kami menyematkan kamera-kamera kecil itu di kancing jas, bros, bahkan di mata boneka gantungan Arulla.{/i}"
mc "{i}Tak ada satu pun terlihat mencolok.{/i}"
mc "{i}Ini berisiko, tapi kali ini kami harus ambil jalan ini.{/i}"
mc "{i}Kami datang dengan senyum.{/i}"
mc "{i}Tapi kali ini... kami tidak datang dengan tangan kosong.{/i}"

label choicesr_b:
mc "{i} Sesuai dugaan.{/i}"
mc "{i}Jamuan ini bukan sekadar makan malam biasa.{/i}"
mc "{i}Ruangan dijaga ketat oleh polisi dan tentara.{/i}"
mc "{i}Tiap tamu diperiksa seperti penjahat.{/i}"
mc "Kita jalankan rencana."
mc "{i}Kami sudah menyiapkan semua ini.{/i}"
label choices_e:
    mc "{i}Sekarang waktunya eksekusi.{/i}"
menu:
    "Menghindari pemeriksaan":
        jump choicese_a
    "Berusaha tetap santai":
        jump choicese_b

label choicese_a:
mc "{i}Kami memilih untuk menghindari pemeriksaan.{/i}"
mc "{i}Menyelinap lewat celah kecil di antara para tamu dan penjaga.{/i}"
mc "{i}Kami kira kami cukup hati-hati...{/i}"
mc "{i}Tapi mereka ternyata lebih siap dari dugaan kami.{/i}"
hide i_arulla datar
show i_polisi at left
p "Temuan alat ilegal. Bawa mereka ke ruang interogasi."
scene bg inter with fade
show i_mc serius
show i_zaki serius at right
show i_arulla datar at left
mc "{i}Kamera ditemukan. Penyadap pun terbongkar.{/i}"
mc "{i}Dalam berita keesokan harinya, kami bukan jurnalis.{/i}"
mc "{i}Kami adalah 'penyusup bersenjata alat spionase'.{/i}"
mc "{i}Mereka membalikkan segalanya.{/i}"
scene bg tahan with fade
mc "{i}Kami dikriminalisasi... dan akhirnya dijebloskan ke penjara.{/i}"
scene bg ending 6 with fade
return

label choicese_b:
mc "{i}Aku memutuskan untuk tetap santai.{/i}"
mc "{i}Kami tidak bisa kabur dari pemeriksaan, tapi kami juga tidak bisa menunjukkan rasa takut.{/i}"
mc "{i}Kami menyamarkan kamera itu sebaik mungkin.{/i}"
mc "{i}Kalau pun mereka tak melihat, metal detector bisa saja menangkapnya.{/i}"
mc "{i}Tapi keajaiban terjadi—kami berhasil masuk.{/i}"
scene bg hotel with fade
show i_mc serius
show i_zaki serius at right
show i_arulla datar at left
mc "{i}Kami mendapatkan semua bukti yang kami butuhkan.{/i}"
mc "{i}Rekaman, foto, percakapan.{/i}"
mc "{i}Semua dikumpulkan rapi, ditranskrip hati-hati, dan dicocokkan dengan data sebelumnya.{/i}"
scene bg kantor
show i_mc serius
show i_zaki serius at right
show i_arulla datar at left
mc "Kita simpan salinan di semua perangkat. Cloud, flashdisk, bahkan kartu SIM."
a "Kalau satu dihancurkan, puluhan lainnya akan tetap menyala."
"{i}Pagi hari. Artikel dipublikasikan. Judul mencolok: 'Teror dan Korupsi: Malam Gelap di Balik Pemerintahan Kota XX'.{/i}"
mc "{i}Artikel itu meledak.{/i}"
mc "{i}Semua tikus itu tamat.{/i}"
mc "{i}Berapapun mereka membayar polisi, bukti sekuat ini tak akan bisa membebaskan mereka dari jerat hukum.{/i}"
scene bg ending 7 with fade
return

label choicesr_b:
scene bg hotel with fade
show i_mc serius
show i_zaki serius at right
show i_arulla datar at left
mc "{i}Kami datang dengan tangan kosong.{/i}"
mc "{i}Tak ada kamera, tak ada penyadap.{/i}"
mc "{i}Hanya telinga kami yang kami bawa—siap menangkap setiap celah yang mereka buka.{/i}"
mc "{i}Mereka mengira kami akan terlena oleh jamuan menjijikkan ini.{/i}"
mc "{i}Padahal, kami justru mencatat./i}"
mc "{i}Nama-nama. Lokasi. Angka-angka. Semua tersimpan rapi di kepala kami.{/i}"
scene bg kantor
show i_mc serius
show i_zaki serius at right
show i_arulla datar at left
z "Dengar, tadi dia sebut soal proyek fiktif di Pelabuhan Selatan. Kita mulai dari situ."
a "Aku juga dengar soal perusahaan ‘topeng’ di balik dana pendidikan. Gila…"
z "Ayo. Investigasi sesungguhnya dimulai."




















