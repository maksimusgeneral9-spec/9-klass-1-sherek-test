# -*- coding: utf-8 -*-

# Список вопросов, вариантов ответов и правильных ключей
quiz_data = [
    {
        "id": 1,
        "question": "1-baptaǵı kompyuter sistemasınıń tiykarǵı maqseti ne?",
        "options": [
            "A) Kompyuter komponentleri hám olardıń islewin úyreniw",
            "B) Tek internetten paydalanıwdı úyreniw",
            "C) Tek programma jazıwdı úyreniw",
            "D) Tek súwret salıwdı úyreniw",
        ],
        "answer": "A",
    },
    {
        "id": 2,
        "question": "Stol kompyuteri (desktop) ádette qanday bólimlerden turadı?",
        "options": [
            "A) Tek monitor hám printer",
            "B) Monitor, klaviatura, tyshqan hám sistema blogı",
            "C) Tek klaviatura hám tyshqan",
            "D) Tek sistema blogı",
        ],
        "answer": "B",
    },
    {
        "id": 3,
        "question": "All-in-one kompyuterdiń ózgesheligi ne?",
        "options": [
            "A) Tek klaviaturadan turadı",
            "B) Tek mobil telefon sıpatında isleydu",
            "C) Komponentlerdiń kópshiligi monitor korpusına biriktirilgen",
            "D) Printer monitor ishinde jaylasadı",
        ],
        "answer": "C",
    },
    {
        "id": 4,
        "question": "Noutbukta qaysı qurılmalar ádette bir korpusta jaylasadı?",
        "options": [
            "A) Tek printer hám skaner",
            "B) Tek processor hám printer",
            "C) Tek monitor",
            "D) Monitor, klaviatura hám tyshqan ornın basıwshı touchpad",
        ],
        "answer": "D",
    },
    {
        "id": 5,
        "question": "Processor (CPU) kompyuterdegi qaysı wazıypanı atqaradı?",
        "options": [
            "A) Esaplaw hám buyrıqlardı orınlaw",
            "B) Qagaz basıp shıǵarıw",
            "C) Dawıstı ǵana jazıw",
            "D) Internet kabelin uzatıw",
        ],
        "answer": "A",
    },
    {
        "id": 6,
        "question": "ALU degen ne?",
        "options": [
            "A) Sırtqı yad qurılması",
            "B) Aritmetikalıq-logikalıq blok",
            "C) Grafikalıq planshet",
            "D) Kiritıw portı",
        ],
        "answer": "B",
    },
    {
        "id": 7,
        "question": "Processor ishindegi CU neni bildiredi?",
        "options": [
            "A) Qattı diskti",
            "B) Monitor blogın",
            "C) Basqarıw blogın",
            "D) Skanerdi",
        ],
        "answer": "C",
    },
    {
        "id": 8,
        "question": "Yad qurılmasınıń tiykarǵı wazıypası ne?",
        "options": [
            "A) Súwretlerdi qagazǵa basıw",
            "B) Dawıstı kúsheytiw",
            "C) Kursorǵa háreket beriw",
            "D) Maǵlıwmat hám programmalardı saqlaw",
        ],
        "answer": "D",
    },
    {
        "id": 9,
        "question": "Cache yad ne ushın qollanıladı?",
        "options": [
            "A) Processorǵa tez kerek bolatuǵın maǵlıwmattı tez saqlaw ushın",
            "B) Qagazdı skanerlew ushın",
            "C) Monitor ekranın úlkeytiw ushın",
            "D) Printerdi basqarıw ushın",
        ],
        "answer": "A",
    },
    {
        "id": 10,
        "question": "Tiykarǵı plata (motherboard) neniń wazıypasın atqaradı?",
        "options": [
            "A) Tek dawıstı jazadı",
            "B) Kompyuter komponentlerin bir-biri menen baylanıstıradı",
            "C) Tek súwret basıp shıǵaradı",
            "D) Tek internetti ólsheydi",
        ],
        "answer": "B",
    },
    {
        "id": 11,
        "question": "Kompyuterdegi videokarta tiykarınan ne ushın qollanıladı?",
        "options": [
            "A) Dawıstı jazıw",
            "B) Qagazdı skanerlew",
            "C) Grafikalıq maǵlıwmatlardı qayta islew hám ekranǵa shıǵarıw",
            "D) Klaviatura tuymesin basıw",
        ],
        "answer": "C",
    },
    {
        "id": 12,
        "question": "ROM qanday yad túri?",
        "options": [
            "A) Tek dawıs saqlaytuǵın yad",
            "B) Sırtqı printer yadı",
            "C) Grafikalıq ekran",
            "D) Turaqlı yad",
        ],
        "answer": "D",
    },
    {
        "id": 13,
        "question": "RAM qanday yad?",
        "options": [
            "A) Operativ yad",
            "B) Turaqlı optikalıq disk",
            "C) Tek sırtqı yad",
            "D) Printer yadı",
        ],
        "answer": "A",
    },
    {
        "id": 14,
        "question": "RAM-daǵı maǵlıwmatqa ne boladı?",
        "options": [
            "A) Hár waqıt ózgermey saqlanadı",
            "B) Kompyuter óshirgende ádette saqlanbaydı",
            "C) Tek qagazǵa basıladı",
            "D) Internetke avtomat túrde jiberiledi",
        ],
        "answer": "B",
    },
    {
        "id": 15,
        "question": "ROM-ǵa tiyisli belgini anıqlań.",
        "options": [
            "A) Tek kompyuter óshirgende isleydi",
            "B) Tek klaviatura maǵlıwmatın saqlaydı",
            "C) Maǵlıwmat turaqlı saqlanadı",
            "D) Tek súwretlerdi basıp shıǵaradı",
        ],
        "answer": "C",
    },
    {
        "id": 16,
        "question": "Qattı disk (HDD) yamasa SSD ne ushın qollanıladı?",
        "options": [
            "A) Tek kursor júrgiziw ushın",
            "B) Tek dawıs kúsheytiw ushın",
            "C) Tek monitor jarıqlığın ózgertiw ushın",
            "D) Maǵlıwmattı uzaq múddet saqlaw ushın",
        ],
        "answer": "D",
    },
    {
        "id": 17,
        "question": "SSD menen HDD arasındaǵı tiykarǵı ayırmashılıqlardan biri ne?",
        "options": [
            "A) SSD mexanikalıq aynalıwshı bólimlerge súyenbeydi",
            "B) HDD tek RAM sıpatında isleydu",
            "C) SSD tek printer ishinde boladı",
            "D) HDD tek klaviatura ushın qollanıladı",
        ],
        "answer": "A",
    },
    {
        "id": 18,
        "question": "Optikalıq diskke mısal qaysı?",
        "options": ["A) RAM", "B) CD/DVD", "C) CPU", "D) ALU"],
        "answer": "B",
    },
    {
        "id": 19,
        "question": "USB portınıń wazıypası ne?",
        "options": [
            "A) Tek monitor jarıqlığın basqarıw",
            "B) Tek processor tezligin ózgertiw",
            "C) Sırtqı qurılmalardı kompyuterge jalǵaw hám maǵlıwmat almasıw",
            "D) Tek printerdiń siyahın toltırıw",
        ],
        "answer": "C",
    },
    {
        "id": 20,
        "question": "HDMI sıyaqlı port ne ushın qollanıladı?",
        "options": [
            "A) Tek klaviatura tuymesin basıw ushın",
            "B) Tek qattı disk ishindegi fayldı óshiriw ushın",
            "C) Tek temperatura ólshew ushın",
            "D) Audio hám video signalın jetkiziw ushın",
        ],
        "answer": "D",
    },
    {
        "id": 21,
        "question": "Kiritıw qurılmasına qaysı mısal kiredi?",
        "options": ["A) Klaviatura", "B) Monitor", "C) Printer", "D) Dinamik"],
        "answer": "A",
    },
    {
        "id": 22,
        "question": "Shıǵarıw qurılmasına qaysı mısal kiredi?",
        "options": ["A) Klaviatura", "B) Monitor", "C) Mikrofon", "D) Skaner"],
        "answer": "B",
    },
    {
        "id": 23,
        "question": "Klaviaturanıń tiykarǵı wazıypası ne?",
        "options": [
            "A) Súwretti qagazǵa basıw",
            "B) Ekranda súwret kórsetiw",
            "C) Tekst hám buyrıqlardı kompyuterge kiritıw",
            "D) Dawıstı kúsheytiw",
        ],
        "answer": "C",
    },
    {
        "id": 24,
        "question": "Tyshqan (mouse) ne ushın qollanıladı?",
        "options": [
            "A) Tek tekst basıp shıǵarıw ushın",
            "B) Tek temperatura ólshew ushın",
            "C) Tek fayllardı saqlaw ushın",
            "D) Kursordı basqarıw hám obyektti tańlaw ushın",
        ],
        "answer": "D",
    },
    {
        "id": 25,
        "question": "Monitor ne isleydi?",
        "options": [
            "A) Kompyuterdegi maǵlıwmattı ekran arqalı kórsetedi",
            "B) Maǵlıwmattı mikrofon arqalı jazadı",
            "C) Qagazdı skanerleydi",
            "D) Tek fayldı saqlaydı",
        ],
        "answer": "A",
    },
]


def run_quiz():
    score = 0
    total = len(quiz_data)

    print("=== INFORMATIKA 9-KLASS 1-BAP TESTI ===")
    print("Variantlardan birin (A, B, C, D) tańlań:\n")

    for item in quiz_data:
        print(f"Soraw {item['id']}: {item['question']}")
        for opt in item["options"]:
            print(f"  {opt}")

        user_ans = input("Juwabıńız (A/B/C/D): ").strip().upper()

        if user_ans == item["answer"]:
            print("Durıs! ✅\n")
            score += 1
        else:
            print(f"Qáte! ❌ Durıs juwap: {item['answer']}\n")

    print("===================================")
    print(
        f"Test juwmaqlandı! Nátiyje: {score} / {total} ({int(score/total * 100)}%)"
    )


if __name__ == "__main__":
    run_quiz()