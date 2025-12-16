SOUNDS = {
    "wake": "beep_activated.wav",
    "stop": "beep_deactivated.wav",
    "done": "beep_done.wav",
    "start": "beep_start.wav",
    "error": "beep_error.wav"
}

PLATFORM_CONNECTORS = [
    "on", "from", "in", "pe", "par"
]

MUSIC_SYNONYMS = {
    "intent": [
        "play", "listen", "start", "put", "खोलो", "चलाओ", "बजाओ"
    ],
    "noun": [
        "song", "songs", "music", "track", "video", "गाना"
    ],
    "platform": [
        "youtube", "yt"
    ]
}

FILLER_WORDS = {
    "english": [
        "please", "pls", "kindly", "can you", "could you",
        "would you", "just", "hey", "ok", "okay"
    ],
    "hindi": [
        "जरा", "थोड़ा", "थोड़ी", "कृपया", "प्लीज़",
        "अरे", "भाई", "यार", "बस"
    ],
    "hinglish": [
        "please kar do", "please karo", "kar do", "karna",
        "kar de", "karna hai"
    ]
}

INTENTS = {
    "wifi": [
        "wifi", "internet", "wi-fi",
        "नेट", "वाईफाई", "इंटरनेट"
    ],

    "bluetooth": [
        "bluetooth", "blue tooth", "bt",
        "ब्लूटूथ", "बीटी", "ब्लू-टूथ"s
    ],

    "volume": [
        "volume", "sound", "loudness", "audio",
        "आवाज़", "आवाज", "आवज़", "वॉल्यूम", "साउंड"
    ],

    "brightness": [
        "brightness", "screen", "light", "display",
        "रोशनी", "चमक", "ब्राइटनेस", "स्क्रीन"
    ],

    "music": [
        "music", "song", "tune", "melody",
        "गाना", "संगीत", "म्यूजिक", "गीत"
    ],

    "system": [
        "system", "pc", "computer", "device", "machine",
        "सिस्टम", "कंप्यूटर", "डिवाइस", "यंत्र", "पीसी"
    ],

    "info": [
        "info", "information", "details", "specs",
        "जानकारी", "सूचना", "विवरण", "डिटेल्स"
    ],

    "assistant": [
        "assistant", "jarvis", "helper", "ai",
        "सहायक", "जार्विस", "असिस्टेंट", "सहायता"
    ]
}

ACTIONS = {
    "set": [
        "set", "fix", "configure", "adjust",
        "रखो", "सेट", "ठीक", "समायोजित"
    ],

    "on": [
        "on", "start", "enable", 
        "चालू", "शुरू", "सक्षम"
    ],

    "off": [
        "off", "disable", 
        "बंद", "अक्षम"
    ],

    "status": [
        "status", "check", "state", "condition",
        "है", "बताओ", "स्थिति", "जांच"
    ],

    "increase": [
        "increase", "up", "raise", "boost", "higher",
        "बढ़ाओ", "बढ़ा", "ऊपर", "तेज़", "ज्यादा"
    ],

    "decrease": [
        "decrease", "down", "lower", "reduce", "less",
        "कम", "घटाओ", "नीचे", "धीमा", "छोटा"
    ],

    "play": [
        "play", "begin",
        "चलाओ", "बजाओ", "प्ले"
    ],

    "lock": [
        "lock", "lock screen", "secure", 
        "लॉक", "स्क्रीन लॉक", "सुरक्षित"
    ],

    "screenshot": [
        "screenshot", "screen shot", "capture", "snapshot",
        "स्क्रीनशॉट", "स्क्रीन फोटो", "कैप्चर", "तस्वीर"
    ],

    "time": [
        "time", "clock", "hour", "current time",
        "समय", "टाइम", "घड़ी", "वर्तमान समय"
    ],

    "date": [
        "date", "calendar", "today", "day-month-year",
        "तारीख", "कैलेंडर", "आज की तारीख", "दिनांक"
    ],

    "day": [
        "day", "weekday", "today", "which day",
        "दिन", "सप्ताह का दिन", "आज", "कौन सा दिन"
    ],

    "battery": [
        "battery", "power", "charge", "battery life",
        "बैटरी", "चार्ज", "पावर", "बैटरी जीवन"
    ],

    "uptime": [
        "uptime", "running time", "system uptime", "how long",
        "अपटाइम", "चलने का समय", "कितनी देर"
    ],

    "sleep": [
        "sleep", "rest", "standby", "hibernate",
        "सो जाओ", "स्लीप", "स्टैंडबाय", "आराम"
    ],

    "wake": [
        "wake", "wake up", "awaken", "activate",
        "जागो", "उठो", "जगाओ"
    ],

    "stop": [
        "stop", "exit", "quit", "shutdown", "end", "deactivate",
        "रुको", "स्टॉप", "बंद करो", "खत्म", "छोड़ो"
    ],

    "humour": [
        "humour", "humor", "joke", "funny", "comedy", "meme",
        "मजाक", "हंसी", "चुटकुला", "मज़ाक", "हास्य", "कॉमेडी"
    ]
}

RESPONSES = {

# ================= GENERIC =================
"did_not_understand": {
    "neutral": [
        "मैं समझ नहीं पाया।",
        "मुझे बात क्लियर नहीं हुई।",
        "समझ नहीं आया।"
    ],
    "humour": [
        "ये मेरे पल्ले नहीं पड़ा।",
        "मेरा दिमाग यहाँ अटक गया।",
        "ये थोड़ा ऊपर से निकल गया।",
        "समझ वाला सिग्नल नहीं आया "
    ]
},

"ask_action": {
    "neutral": [
        "क्या करना है?",
        "अगला कदम क्या है?",
        "अब क्या करना है?"
    ],
    "humour": [
        "भाई अब करना क्या है?",
        "सीधा बताओ, करना क्या है?",
        "दिमाग़ घूम रहा है, अब क्या?"
    ]
},

"ask_value": {
    "neutral": [
        "कितना?",
        "कृपया मात्रा बताइए।"
    ],
    "humour": [
        "कितना पड़ेगा भाई?",
        "कितना है ये नुकसान… मतलब कीमत?"
    ]
},

"something_wrong": {
    "neutral": [
        "कुछ गड़बड़ हो गई।",
        "प्रक्रिया में समस्या आई है।"
    ],
    "humour": [
        "लगता है कुछ तो उल्टा-पुल्टा हो गया",
        "यहाँ कुछ ज़बरदस्त कांड हो गया"
    ]
},

# ================= ASSISTANT =================
"assistant_wake": {
    "neutral": [
        "मैं वापस आ गया हूँ।",
        "सिस्टम सक्रिय हो गया है।"
    ],
    "humour": [
        "लो भाई, वापसी हो गया",
        "जिसका डर था वही हुआ… मैं लौट आया"
    ]
},

"assistant_sleep": {
    "neutral": [
        "मैं स्लीप मोड में जा रहा हूँ।"
    ],
    "humour": [
        "अब नींद मुझ पर हमला करने वाली है",
        "चलो, अब थोड़ी नींद"
    ]
},

"assistant_stop": {
    "neutral": [
        "जार्विस बंद हो रहा है।"
    ],
    "humour": [
        "अब छुट्टी पर जा रहा हूँ",
        "फिर मिलेंगे बॉस"
    ]
},

# ================= WIFI =================
"wifi_on": {
    "neutral": [
        "Wi-Fi चालू कर दिया गया है।"
    ],
    "humour": [
        "Wi-Fi ऑन… इंटरनेट फिर से ज़िंदा",
        "अब दिमाग़ भी ऑनलाइन"
    ]
},

"wifi_off": {
    "neutral": [
        "Wi-Fi बंद कर दिया गया है।"
    ],
    "humour": [
        "Wi-Fi ऑफ़… अब शांति",
        "अब फोन भी ध्यान माँग रहा"
    ]
},

# ================= BLUETOOTH =================
"bluetooth_on": {
    "neutral": [
        "Bluetooth चालू कर दिया गया है।"
    ],
    "humour": [
        "Bluetooth ऑन… devices सतर्क",
        "अब कौन कनेक्ट होगा भला"
    ]
},

"bluetooth_off": {
    "neutral": [
        "Bluetooth बंद कर दिया गया है।"
    ],
    "humour": [
        "अब कोई अनचाहा कनेक्शन नहीं",
        "devices को भी चैन मिला"
    ]
},

# ================= VOLUME =================
"volume_increase": {
    "neutral": [
        "आवाज़ बढ़ा दी गई है।"
    ],
    "humour": [
        "वॉल्यूम अप! पड़ोसी भी अपडेट हो गए",
        "अब सबको सुनाई देगा"
    ]
},

"volume_decrease": {
    "neutral": [
        "आवाज़ कम कर दी गई है।"
    ],
    "humour": [
        "कानों को राहत",
        "शांति बहाल"
    ]
},

"volume_set": {
    "neutral": [
        "वॉल्यूम सेट कर दिया गया है।"
    ],
    "humour": [
        "ना ज़्यादा, ना कम… परफेक्ट",
        "फिट बैठ गया"
    ]
},

"volume_mute": {
    "neutral": [
        "आवाज़ म्यूट कर दी गई है।"
    ],
    "humour": [
        "सन्नाटा",
        "आवाज़ छुट्टी पर"
    ]
},

"volume_unmute": {
    "neutral": [
        "आवाज़ चालू कर दी गई है।"
    ],
    "humour": [
        "सन्नाटा टूटा",
        "आवाज़ वापस"
    ]
},

# ================= BRIGHTNESS =================
"brightness_increase": {
    "neutral": [
        "ब्राइटनेस बढ़ा दी गई है।"
    ],
    "humour": [
        "आँखें सतर्क",
        "सूरज भी शर्मा जाए"
    ]
},

"brightness_decrease": {
    "neutral": [
        "ब्राइटनेस कम कर दी गई है।"
    ],
    "humour": [
        "आँखों को आराम",
        "अंधेरा पसंद करने वालों के लिए"
    ]
},

# ================= TIME =================
"time_tell": {
    "neutral": [
        "अभी समय है।"
    ],
    "humour": [
        "समय किसी का इंतज़ार नहीं करता",
        "घड़ी तैयार"
    ]
},

# ================= MUSIC =================
"music_play": {
    "neutral": [
        "संगीत चल रहा है।"
    ],
    "humour": [
        "म्यूज़िक ऑन… मूड सेट",
        "गाना बजा, टेंशन गया"
    ]
},

# ================= BATTERY =================
"battery_status": {
    "neutral": [
        "बैटरी की स्थिति यह है।"
    ],
    "humour": [
        "बैटरी अभी ज़िंदा है",
        "चार्जर ढूँढें या नहीं?"
    ]
},

# ================= SYSTEM =================
"screenshot_done": {
    "neutral": [
        "स्क्रीनशॉट ले लिया गया है।"
    ],
    "humour": [
        "पल कैद कर लिया",
        "सबूत इकट्ठा"
    ]
},

"lock_done": {
    "neutral": [
        "डिवाइस लॉक कर दी गई है।"
    ],
    "humour": [
        "अब कोई चुपके से नहीं देखेगा"
    ]
},

"airplane_on": {
    "neutral": [
        "एयरप्लेन मोड चालू कर दिया गया है।"
    ],
    "humour": [
        "नेटवर्क उड़ान पर",
        "फोन भी ट्रैवल मोड"
    ]
},

"airplane_off": {
    "neutral": [
        "एयरप्लेन मोड बंद कर दिया गया है।"
    ],
    "humour": [
        "लैंडिंग पूरी ",
        "फोन वापस धरती पर"
    ]
}
}

APP_ALIASES = {
    "spotify": "Spotify",
    "chrome": "Google Chrome",
    "google chrome": "Google Chrome",
    "safari": "Safari",
    "vs code": "Visual Studio Code",
    "vscode": "Visual Studio Code",
    "music": "Music",
    "terminal": "Terminal"
}
