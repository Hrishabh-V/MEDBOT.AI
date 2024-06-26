symptoms_to_diseases = {
    'cough': ['common cold', 'influenza', 'pneumonia'],
    'fever': ['common cold', 'influenza', 'pneumonia', 'malaria'],
    'headache': ['migraine', 'tension headache'],
    'sore throat': ['common cold', 'streptococcal infection'],
    'fatigue': ['chronic fatigue syndrome', 'anemia', 'depression'],
    'nausea': ['gastroenteritis', 'migraine', 'pregnancy'],
    ' ': ['gastroenteritis', 'food poisoning'],
    'diarrhea': ['gastroenteritis', 'food poisoning', 'irritable bowel syndrome'],
    'abdominal pain': ['gastroenteritis', 'appendicitis', 'peptic ulcer'],
    'chest pain': ['angina', 'heart attack', 'acid reflux'],
    'shortness of breath': ['asthma', 'pneumonia', 'chronic obstructive pulmonary disease'],
    'joint pain': ['arthritis', 'gout', 'fibromyalgia'],
    'muscle weakness': ['myasthenia gravis', 'polymyositis', 'hypothyroidism'],
    'rash': ['allergic reaction', 'eczema', 'psoriasis'],
    'swollen lymph nodes': ['infection', 'lymphoma', 'mononucleosis'],
    'weight loss': ['cancer', 'diabetes', 'hyperthyroidism'],
    'excessive thirst': ['diabetes', 'dehydration', 'diabetes insipidus'],
    'frequent urination': ['urinary tract infection', 'diabetes', 'overactive bladder'],
    'difficulty swallowing': ['gastroesophageal reflux disease', 'esophageal stricture'],
    'memory loss': ['Alzheimer','sdisease','dementia', 'brain injury'],
    'decreased appetite': ['anorexia', 'depression', 'cancer'],
    'sleep disturbances': ['insomnia', 'sleep apnea', 'restless leg syndrome'],
    'back pain': ['muscle strain', 'herniated disc', 'kidney stones'],
    'dizziness': ['vertigo', 'low blood pressure', 'inner ear infection'],
    'vision changes': ['cataracts', 'glaucoma', 'macular degeneration'],
    'irritability': ['anxiety', 'bipolar disorder', 'premenstrual syndrome'],
    'hair loss': ['alopecia', 'thyroid disorders', 'chemotherapy'],
    'sweating': ['hyperhidrosis', 'menopause', 'anxiety disorders'],
    'stomach bloating': ['gas', 'indigestion', 'constipation'],
    'throat clearing': ['postnasal drip', 'acid reflux', 'vocal cord dysfunction'],
    'nosebleeds': ['dry air', 'nasal trauma', 'high blood pressure'],
    'fainting': ['vasovagal syncope', 'heart arrhythmia', 'hypoglycemia'],
    'muscle cramps': ['dehydration', 'electrolyte imbalance', 'peripheral artery disease'],
    'tingling sensation': ['nerve compression', 'diabetic neuropathy', 'multiple sclerosis'],
    'swollen joints': ['rheumatoid arthritis', 'gout', 'inflammatory osteoarthritis'],
    'headache': ['sinusitis', 'cluster headache'],
    'stomach pain': ['gastritis', 'ulcerative colitis'],
    'backache': ['spinal disc herniation', 'kidney infection'],
    'fatigue': ['hypothyroidism', 'fibromyalgia'],
    'dizziness': ['inner ear disorders', 'meniere\'s disease'],
    'skin rash': ['dermatitis', 'eczema'],
    'chest discomfort': ['angina', 'gastroesophageal reflux disease'],
    'urinary frequency': ['urinary tract infection', 'interstitial cystitis'],
    'shortness of breath': ['asthma', 'chronic bronchitis'],
    'abdominal bloating': ['irritable bowel syndrome', 'celiac disease'],
    'leg pain': ['deep vein thrombosis', 'sciatica'],
    'joint swelling': ['rheumatoid arthritis', 'lupus'],
    'sleep problems': ['sleep apnea', 'insomnia'],
    'memory problems': ['dementia', 'mild cognitive impairment'],
    'weight gain': ['hypothyroidism', 'polycystic ovary syndrome'],
    'mood swings': ['bipolar disorder', 'premenstrual dysphoric disorder'],
    'hair thinning': ['telogen effluvium', 'androgenetic alopecia'],
    'frequent infections': ['immunodeficiency disorders', 'HIV/AIDS'],
    'nose congestion': ['allergic rhinitis', 'sinusitis'],
    'swollen glands': ['infectious mononucleosis', 'lymphadenitis'],
    'eye redness': ['conjunctivitis', 'uveitis'],
    'dry mouth': ['Sjogren\'s syndrome', 'diabetes'],
    'muscle stiffness': ['fibromyalgia', 'multiple sclerosis'],
    'hand tremors': ['essential tremor', 'Parkinson\'s disease'],
    'abnormal bleeding': ['menorrhagia', 'hemophilia'],
    'excessive sweating': ['hyperhidrosis', 'thyroid disorders'],
    'difficulty concentrating': ['attention deficit hyperactivity disorder', 'anxiety'],
    'frequent hiccups': ['gastroesophageal reflux', 'esophageal irritation'],
    'swollen feet': ['edema', 'heart failure'],
    'toothache': ['dental caries', 'periodontal disease'],
    'ringing in the ears': ['tinnitus', 'noise-induced hearing loss'],
    'feeling cold': ['hypothyroidism', 'Raynaud\'s disease'],
    'swollen face': ['allergic reaction', 'facial cellulitis'],
    'blood in urine': ['urinary tract infection', 'kidney stones'],
    'itchy skin': ['dermatitis', 'scabies'],
    'abdominal cramps': ['irritable bowel syndrome', 'appendicitis'],
    'difficulty breathing': ['asthma', 'pulmonary embolism'],
    'excessive thirst': ['diabetes insipidus', 'dehydration'],
    'hoarseness': ['laryngitis', 'vocal cord polyps'],
    'muscle twitches': ['fasciculations', 'motor neuron disease'],
    'difficulty swallowing': ['dysphagia', 'esophageal cancer'],
    'poor balance': ['vertigo', 'cerebellar ataxia'],
    'yellowing of skin': ['jaundice', 'hepatitis'],
    'earache': ['otitis media', 'temporomandibular joint disorder'],
    'sensitivity to light': ['photophobia', 'migraine with aura'],
    'frequent burping': ['gastroesophageal reflux disease', 'gastric ulcer'],
    'cold intolerance': ['hypothyroidism', 'Raynaud',' phenomenon'],
    'flank pain': ['kidney stones', 'urinary tract infection'],
    'restlessness': ['akathisia', 'anxiety'],
    'food cravings': ['pregnancy', 'premenstrual syndrome'],
    'dry eyes': ['dry eye syndrome', 'Sjogren','syndrome'],
    'joint stiffness': ['osteoarthritis', 'ankylosing spondylitis'],
    'increased urination': ['diabetes mellitus', 'diuretic use'],
    'foul-smelling urine': ['urinary tract infection', 'bacterial vaginosis'],
    'thirsty': ['dehydration', 'diabetes'],
    'sudden weight gain': ['fluid retention', 'hypothyroidism'],
    'jaw pain': ['temporomandibular joint disorder', 'dental abscess'],
    'lightheadedness': ['orthostatic hypotension', 'hypoglycemia'],
    'bruising easily': ['thrombocytopenia', 'vitamin K deficiency'],
    'frequent nosebleeds': ['nasal dryness', 'nasal trauma'],
    'tingling in hands': ['carpal tunnel syndrome', 'peripheral neuropathy'],
    'abnormal menstrual bleeding': ['dysfunctional uterine bleeding', 'endometriosis'],
    'difficulty speaking': ['dysarthria', 'aphasia'],
    'facial swelling': ['angioedema', 'allergic reaction'],
    'persistent cough': ['chronic bronchitis', 'pulmonary fibrosis'],
    'frequent infections': ['immunodeficiency disorders', 'leukemia'],
    'hallucinations': ['schizophrenia', 'drug-induced psychosis'],
    'muscle wasting': ['muscular dystrophy', 'amyotrophic lateral sclerosis'],
    'swollen ankles': ['edema', 'heart failure'],
    'nose congestion': ['sinusitis', 'allergic rhinitis'],
    'severe abdominal pain': ['appendicitis', 'pancreatitis'],
    'swollen face': ['angioedema', 'cellulitis'],
    'muscle spasms': ['spasticity', 'tetanus'],
    'difficulty focusing': ['attention deficit hyperactivity disorder (ADHD)', 'migraine'],
    'blurred vision': ['cataracts', 'macular degeneration'],
    'recurring fever': ['typhoid fever', 'brucellosis'],
    'unexplained weight gain': ['hypothyroidism', 'polycystic ovary syndrome (PCOS)'],
    'muscle stiffness': ['fibromyalgia', 'Parkinson','disease'],
    'night sweats': ['menopause', 'tuberculosis'],
    'brittle nails': ['nutritional deficiencies', 'hypothyroidism'],
    'swollen face': ['angioedema', 'cellulitis'],
    'sudden hearing loss': ['sensorineural hearing loss', 'ear infection'],
    'difficulty standing': ['orthostatic hypotension', 'muscle weakness'],
    'hand tremors': ['essential tremor', 'Parkinson',' disease'],
    'blood in urine': ['urinary tract infection', 'kidney stones'],
    'seizures': ['epilepsy', 'brain tumor'],
    'loss of balance': ['vestibular disorders', 'inner ear infection'],
    'muscle rigidity': ['Parkinson',' disease', 'neuroleptic malignant syndrome'],
    'swollen eyelids': ['allergic conjunctivitis', 'blepharitis'],
    'frequent hiccups': ['gastroesophageal reflux disease (GERD)', 'hiatal hernia'],
    'excessive gas': ['flatulence', 'irritable bowel syndrome'],
    'jaw clicking': ['temporomandibular joint (TMJ) disorder', 'bruxism'],
    'chronic cough': ['chronic bronchitis', 'gastroesophageal reflux disease (GERD)'],
    'frequent heartburn': ['gastroesophageal reflux disease (GERD)', 'peptic ulcer'],
    'muscle cramps': ['dehydration', 'electrolyte imbalance'],
    'persistent fatigue': ['chronic fatigue syndrome', 'hypothyroidism'],
    'sudden mood swings': ['bipolar disorder', 'premenstrual dysphoric disorder (PMDD)'],
    # Add more symptoms and corresponding diseases as needed
}