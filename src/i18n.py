# src/i18n.py

TRANSLATIONS = {
    "English": {
        "app_title": "AI-GIS FVWPS",
        "app_subtitle": "Flood Vulnerability & Public Welfare Prioritization System",
        "filter_scope": "Filter Scope",
        "district_boundary": "District Boundary",
        "welfare_priority": "Welfare Priority Filter",
        "target_village": "Target Village",
        "ui_language": "Interface Language",
        "all_districts": "All Districts",
        "all_priorities": "All Priorities",
        "live_status": "GIS & ML Model Active",
        "rank_prefix": "Rank",
        "in_target_region": "in Target Region",
        
        # Priorities
        "priority_high": "High",
        "priority_moderate": "Moderate",
        "priority_low": "Low",
        
        # KPI Cards
        "kpi_flood_exp": "Flood Exposure",
        "kpi_flood_sub": "Total area submerged",
        "kpi_vuln_idx": "Vulnerability Index",
        "kpi_vuln_sub": "Scale of 0 – 100",
        "kpi_welfare_score": "Welfare Score",
        "kpi_welfare_sub": "Allocation weight",
        "kpi_hospital_dist": "Hospital Distance",
        "kpi_hospital_sub": "Nearest critical clinic",
        "kpi_service_gap": "Service Gap",
        "kpi_service_sub": "Infrastructure deficit",
        
        # Tabs
        "tab_map": "🗺️ Spatial Operations Map",
        "tab_analytics": "📊 Community Risk Analytics",
        "tab_copilot": "🤖 AI Decision Copilot",
        "tab_dataset": "📋 Tabular Ledger",
        
        # Map Tab
        "layer_control": "Layer Control",
        "layer_desc": "Toggle geospatial vector boundaries.",
        "layer_flood": "Flood Extent Inundation",
        "layer_rivers": "River Drainage Network",
        "layer_hospitals": "Emergency Healthcare",
        "layer_roads": "Primary Road Corridors",
        
        # Analytics Tab
        "contrib_heading": "Model Vulnerability Contributions",
        "contrib_desc": "Weighted indicators driving prioritization.",
        "infra_heading": "Infrastructure Gaps",
        "infra_desc": "Relative deficits across civil services.",
        "factor_flood": "Inundation Exposure",
        "factor_pop": "Demographic Density",
        "factor_service": "Service Accessibility Gap",
        "factor_river": "River Proximity Hazard",
        "gap_health": "Healthcare Access",
        "gap_water": "Potable Water Systems",
        "gap_drainage": "Stormwater Drainage",
        
        # Copilot Tab
        "ai_heading": "Automated Synthesis & Directives",
        "ai_desc": "Generative field directives compiled from current GIS spatial features.",
        "ai_btn": "Generate Assessment Directive",
        "ai_spinner": "Compiling structured action directive...",
        "ai_urgency": "Executive Action Notice",
        "ai_factors_title": "Key Risk Factors",
        "ai_tactical_title": "Immediate Tactical Directives",
        
        # Ledger Tab
        "ledger_heading": "Assessed Regional Cohort",
        "ledger_desc": "Inspect, sort, and download prioritized village cohorts.",
        "export_btn": "Export View to CSV",
        
        # Warnings
        "no_records": "No records match the current filter criteria."
    },
    "Marathi": {
        "app_title": "एआय-जीआयएस एफव्हीडब्ल्यूपीएस",
        "app_subtitle": "पूर असुरक्षितता आणि सार्वजनिक कल्याण प्राधान्यक्रम प्रणाली",
        "filter_scope": "फिल्टर व्याप्ती",
        "district_boundary": "जिल्हा सीमा",
        "welfare_priority": "कल्याण प्राधान्य फिल्टर",
        "target_village": "लक्ष्यित गाव",
        "ui_language": "इंटरफेस भाषा",
        "all_districts": "सर्व जिल्हे",
        "all_priorities": "सर्व प्राधान्यता",
        "live_status": "जीआयएस आणि मॉडेल सक्रिय",
        "rank_prefix": "क्रमांक",
        "in_target_region": "लक्ष्यित विभागात",
        
        # Priorities
        "priority_high": "उच्च",
        "priority_moderate": "मध्यम",
        "priority_low": "कमी",
        
        # KPI Cards
        "kpi_flood_exp": "पूर बाधा क्षेत्र",
        "kpi_flood_sub": "पाण्याखाली गेलेले क्षेत्र",
        "kpi_vuln_idx": "असुरक्षितता निर्देशांक",
        "kpi_vuln_sub": "श्रेणी ० – १००",
        "kpi_welfare_score": "कल्याण प्राधान्य गुण",
        "kpi_welfare_sub": "वाटप भार",
        "kpi_hospital_dist": "रुग्णालयाचे अंतर",
        "kpi_hospital_sub": "जवळचे आपत्कालीन केंद्र",
        "kpi_service_gap": "सेवा अंतर निर्देशांक",
        "kpi_service_sub": "पायाभूत सुविधांची तूट",
        
        # Tabs
        "tab_map": "🗺️ नकाशा व भौगोलिक माहिती",
        "tab_analytics": "📊 जोखीम व सेवा विश्लेषण",
        "tab_copilot": "🤖 एआय कृती सहाय्यक",
        "tab_dataset": "📋 डेटा सारणी",
        
        # Map Tab
        "layer_control": "स्तर नियंत्रण (Layers)",
        "layer_desc": "भौगोलिक सीमा व स्तर टॉगल करा.",
        "layer_flood": "पूर बाधित क्षेत्र",
        "layer_rivers": "नदी व जलप्रवाह जाळे",
        "layer_hospitals": "आपत्कालीन रुग्णालये",
        "layer_roads": "मुख्य रस्ते मार्ग",
        
        # Analytics Tab
        "contrib_heading": "असुरक्षितता घटक योगदान",
        "contrib_desc": "प्राधान्यक्रम ठरवणारे मॉडेल घटक.",
        "infra_heading": "पायाभूत सुविधांमधील तूट",
        "infra_desc": "नागरी सेवांमधील सापेक्ष कमतरता.",
        "factor_flood": "पूर प्रकटीकरण प्रभाव",
        "factor_pop": "लोकसंख्या घनता",
        "factor_service": "सेवा उपलब्धता अंतर",
        "factor_river": "नदी समीपतेचा धोका",
        "gap_health": "आरोग्य सेवा उपलब्धता",
        "gap_water": "पिण्याच्या पाण्याची सुविधा",
        "gap_drainage": "सांडपाणी व निचरा व्यवस्था",
        
        # Copilot Tab
        "ai_heading": "स्वयंचलित मूल्यांकन आणि कृती निर्देश",
        "ai_desc": "जीआयएस आणि मॉडेल निर्देशकांवर आधारित स्वयंचलित कृती आराखडा.",
        "ai_btn": "मूल्यांकन अहवाल तयार करा",
        "ai_spinner": "मराठीमध्ये अहवाल तयार केला जात आहे...",
        "ai_urgency": "आपत्कालीन कृती सूचना",
        "ai_factors_title": "मुख्य धोक्याचे घटक",
        "ai_tactical_title": "तातडीचे क्षेत्रीय उपाय",
        
        # Ledger Tab
        "ledger_heading": "मूल्यांकन केलेली गावे",
        "ledger_desc": "प्राधान्यक्रमित गावांची माहिती तपासा आणि डाउनलोड करा.",
        "export_btn": "सीएसव्ही (CSV) डाउनलोड करा",
        
        # Warnings
        "no_records": "निवडलेल्या निकषांनुसार कोणतीही नोंद आढळली नाही."
    },
    "Hindi": {
        "app_title": "एआई-जीआईएस एफवीडब्ल्यूपीएस",
        "app_subtitle": "बाढ़ संवेदनशीलता एवं जन-कल्याण प्राथमिकता प्रणाली",
        "filter_scope": "फ़िल्टर दायरा",
        "district_boundary": "ज़िला सीमा",
        "welfare_priority": "कल्याण प्राथमिकता फ़िल्टर",
        "target_village": "लक्षित गाँव",
        "ui_language": "इंटरफ़ेस भाषा",
        "all_districts": "सभी ज़िले",
        "all_priorities": "सभी प्राथमिकताएँ",
        "live_status": "जीआईएस व मॉडल सक्रिय",
        "rank_prefix": "रैंक",
        "in_target_region": "लक्षित क्षेत्र में",
        
        # Priorities
        "priority_high": "उच्च",
        "priority_moderate": "मध्यम",
        "priority_low": "निम्न",
        
        # KPI Cards
        "kpi_flood_exp": "बाढ़ प्रभावित क्षेत्र",
        "kpi_flood_sub": "जलमग्न कुल क्षेत्रफल",
        "kpi_vuln_idx": "संवेदनशीलता सूचकांक",
        "kpi_vuln_sub": "पैमाना ० – १००",
        "kpi_welfare_score": "कल्याण प्राथमिकता अंक",
        "kpi_welfare_sub": "आवंटन भार",
        "kpi_hospital_dist": "अस्पताल की दूरी",
        "kpi_hospital_sub": "निकटतम आपातकालीन केंद्र",
        "kpi_service_gap": "सेवा अंतर सूचकांक",
        "kpi_service_sub": "बुनियादी ढांचा घाटा",
        
        # Tabs
        "tab_map": "🗺️ स्थानिक परिचालन मानचित्र",
        "tab_analytics": "📊 जोखिम एवं सेवा विश्लेषण",
        "tab_copilot": "🤖 एआई निर्णय सहायक",
        "tab_dataset": "📋 डेटा तालिका",
        
        # Map Tab
        "layer_control": "परत नियंत्रण (Layers)",
        "layer_desc": "भू-स्थानिक सीमाएँ और परतें चालू/बंद करें।",
        "layer_flood": "बाढ़ फैलाव क्षेत्र",
        "layer_rivers": "नदी जल निकासी तंत्र",
        "layer_hospitals": "आपातकालीन स्वास्थ्य केंद्र",
        "layer_roads": "मुख्य सड़क मार्ग",
        
        # Analytics Tab
        "contrib_heading": "संवेदनशीलता योगदान कारक",
        "contrib_desc": "प्राथमिकता तय करने वाले मॉडल कारक।",
        "infra_heading": "बुनियादी ढांचे में कमियाँ",
        "infra_desc": "नागरिक सेवाओं में सापेक्ष अंतर।",
        "factor_flood": "जलभराव का प्रभाव",
        "factor_pop": "जनसंख्या घनत्व",
        "factor_service": "सेवा पहुँच अंतराल",
        "factor_river": "नदी निकटता जोखिम",
        "gap_health": "स्वास्थ्य सेवा पहुँच",
        "gap_water": "पेयजल प्रणाली",
        "gap_drainage": "जल निकासी व्यवस्था",
        
        # Copilot Tab
        "ai_heading": "स्वचालित मूल्यांकन एवं कार्रवाई निर्देश",
        "ai_desc": "जीआईएस और मॉडल संकेतकों पर आधारित जन-कल्याण कार्य योजना।",
        "ai_btn": "मूल्यांकन रिपोर्ट तैयार करें",
        "ai_spinner": "हिंदी में रिपोर्ट तैयार की जा रही है...",
        "ai_urgency": "आपातकालीन कार्य योजना सूचना",
        "ai_factors_title": "मुख्य जोखिम कारक",
        "ai_tactical_title": "तत्काल राहत उपाय",
        
        # Ledger Tab
        "ledger_heading": "मूल्यांकित गाँव सूची",
        "ledger_desc": "प्राथमिकता प्राप्त गाँवों की सूची देखें और डाउनलोड करें।",
        "export_btn": "सीएसवी (CSV) डाउनलोड करें",
        
        # Warnings
        "no_records": "चुने गए फ़िल्टर के अनुसार कोई रिकॉर्ड नहीं मिला।"
    }
}