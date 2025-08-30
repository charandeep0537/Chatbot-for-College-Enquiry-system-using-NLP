"""Training data for intent classification and response generation."""

TRAINING_DATA = {
    'greeting': {
        'examples': [
            "hello",
            "hi there",
            "good morning",
            "good afternoon",
            "good evening",
            "hey",
            "greetings",
            "how are you",
            "nice to meet you",
            "hi",
            "hello there",
            "hey there"
        ],
        'keywords': ['hello', 'hi', 'greetings', 'good', 'morning', 'afternoon', 'evening', 'hey']
    },
    
    'scholarship_info': {
        'examples': [
            "are scholarships available",
            "tell me about scholarships",
            "do you offer financial aid",
            "scholarship details",
            "merit based scholarship",
            "need based aid",
            "grants and scholarships",
            "fee concession through scholarship"
        ],
        'keywords': ['scholarship', 'grant', 'aid', 'financial', 'merit', 'need']
    },
    
    'hostel_info': {
        'examples': [
            "tell me about hostel",
            "do you have hostel facilities",
            "accommodation details",
            "dorm rooms availability",
            "hostel fees and facilities",
            "mess and security in hostel"
        ],
        'keywords': ['hostel', 'accommodation', 'dorm', 'room', 'mess', 'security']
    },
    
    'documents_required': {
        'examples': [
            "what documents are required",
            "documents needed for admission",
            "which certificates to submit",
            "marksheets and id proof required",
            "list of documents for application"
        ],
        'keywords': ['document', 'certificate', 'transcript', 'marksheet', 'id', 'photo', 'proof']
    },
    
    'application_deadline': {
        'examples': [
            "when is the application deadline",
            "last date to apply",
            "closing date for applications",
            "apply by what date",
            "admission deadline"
        ],
        'keywords': ['deadline', 'date', 'closing', 'last', 'apply']
    },
    
    'entrance_exam_info': {
        'examples': [
            "is there an entrance exam",
            "entrance test details",
            "exam requirements for admission",
            "cutoff for entrance exam",
            "which entrance exams are accepted"
        ],
        'keywords': ['entrance', 'exam', 'test', 'cutoff']
    },
    
    'admission_info': {
        'examples': [
            "how to apply for admission",
            "what are admission requirements",
            "admission process",
            "eligibility criteria for admission",
            "when do admissions start",
            "how to get admission",
            "admission procedure",
            "what documents are needed for admission",
            "admission deadline",
            "entrance exam for admission",
            "merit list for admission",
            "admission cut off",
            "how to apply",
            "application form",
            "admission form"
        ],
        'keywords': ['admission', 'apply', 'application', 'eligibility', 'requirements', 'procedure', 'process', 'entrance', 'exam']
    },
    
    'fee_info': {
        'examples': [
            "what is the fee structure",
            "how much are the fees",
            "tuition fees",
            "college fees",
            "fee details",
            "cost of studying",
            "fee payment",
            "scholarship availability",
            "financial assistance",
            "fee concession",
            "installment payment",
            "total fees",
            "annual fees",
            "semester fees"
        ],
        'keywords': ['fee', 'fees', 'cost', 'tuition', 'payment', 'scholarship', 'financial', 'money', 'price']
    },
    
    'course_info': {
        'examples': [
            "what courses do you offer",
            "available programs",
            "degree programs",
            "subjects available",
            "curriculum details",
            "course duration",
            "specializations available",
            "undergraduate courses",
            "graduate programs",
            "post graduate courses",
            "diploma courses",
            "certificate programs",
            "syllabus information",
            "course structure"
        ],
        'keywords': ['course', 'courses', 'program', 'programs', 'degree', 'subject', 'curriculum', 'syllabus']
    },
    
    'facility_info': {
        'examples': [
            "what facilities are available",
            "campus facilities",
            "library facilities",
            "laboratory facilities",
            "hostel facilities",
            "sports facilities",
            "cafeteria facilities",
            "wifi availability",
            "transport facilities",
            "medical facilities",
            "gym facilities",
            "computer lab",
            "research facilities",
            "infrastructure details"
        ],
        'keywords': ['facilities', 'facility', 'library', 'lab', 'hostel', 'sports', 'cafeteria', 'wifi', 'transport', 'gym']
    },
    
    'campus_info': {
        'examples': [
            "tell me about campus",
            "campus life",
            "campus environment",
            "campus location",
            "campus size",
            "campus culture",
            "student life",
            "campus events",
            "campus activities",
            "college atmosphere",
            "campus tour",
            "campus area",
            "college location",
            "campus facilities"
        ],
        'keywords': ['campus', 'location', 'environment', 'life', 'culture', 'events', 'activities', 'atmosphere']
    },
    
    'faculty_info': {
        'examples': [
            "tell me about faculty",
            "faculty qualifications",
            "teaching staff",
            "professors information",
            "faculty experience",
            "teacher to student ratio",
            "faculty members",
            "instructor qualifications",
            "teaching quality",
            "faculty research",
            "faculty background",
            "academic staff",
            "teaching methodology"
        ],
        'keywords': ['faculty', 'teacher', 'professor', 'staff', 'instructor', 'teaching', 'qualifications', 'experience']
    },
    
    'placement_info': {
        'examples': [
            "placement opportunities",
            "job placement",
            "career opportunities",
            "placement record",
            "company visits",
            "recruitment drive",
            "placement statistics",
            "average salary",
            "placement support",
            "internship opportunities",
            "career guidance",
            "job assistance",
            "employment opportunities",
            "placement cell"
        ],
        'keywords': ['placement', 'job', 'career', 'recruitment', 'salary', 'internship', 'employment', 'company']
    },
    
    'contact_info': {
        'examples': [
            "contact information",
            "how to contact",
            "phone number",
            "email address",
            "college address",
            "office hours",
            "contact details",
            "reach out",
            "get in touch",
            "communication",
            "office location",
            "contact office",
            "admissions office contact"
        ],
        'keywords': ['contact', 'phone', 'email', 'address', 'office', 'reach', 'touch', 'communication']
    },
    
    'goodbye': {
        'examples': [
            "thank you",
            "goodbye",
            "bye",
            "see you later",
            "thanks for help",
            "that's all",
            "no more questions",
            "end conversation",
            "exit",
            "quit",
            "thanks",
            "thank you for information",
            "bye bye"
        ],
        'keywords': ['thank', 'thanks', 'goodbye', 'bye', 'exit', 'quit', 'end']
    }
}

# Additional data for enhancing responses
COLLEGE_INFO = {
    'name': 'RGM College of Engineering and Technology',
    'established': '1995',
    'location': 'Nandyala, Andhra Pradesh',
    'accreditation': 'Nationally Accredited',
    'ranking': 'Top 100 Universities',
    'student_count': '15000+',
    'faculty_count': '800+',
    'campus_size': '50 acres',
    'admissions': {
        'application_open_date': '01-07-2025',
        'final_deadline': '31-08-2025',
        'entrance_exams': ['EAMCET', 'ECET'],
        'documents_required': [
            'Caste certificate',
            'SSC MarkList',
            'Intermediate Marks memo',
            'Transfer certificate',
            'Migration certificate'
        ]
    },
    'fees': {
        'tuition_per_year': '₹2,10,000',
        'other_fees': '₹19,000',
        'hostel_fee': '₹94,000'
    },
    'departments': [
        'Engineering & Technology',
        'Business & Management',
        'Arts & Sciences',
        'Computer Science',
        'Medicine & Health Sciences',
        'Law',
        'Education'
    ]
}