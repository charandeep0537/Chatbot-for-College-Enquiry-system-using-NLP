"""Training data for intent classification and response generation."""

TRAINING_DATA = {
    'greeting': {
        'examples': [
            "hello", "hi there", "good morning", "good afternoon", "good evening",
            "hey", "greetings", "how are you", "nice to meet you", "hi", "hello there",
            "hey there", "is anyone there?", "start chat"
        ],
        'keywords': ['hello', 'hi', 'greetings', 'good', 'morning', 'afternoon', 'evening', 'hey', 'start']
    },
    
    'scholarship_info': {
        'examples': [
            "are scholarships available", "tell me about scholarships", "do you offer financial aid",
            "scholarship details", "merit based scholarship", "need based aid",
            "grants and scholarships", "fee concession through scholarship", "how to get a scholarship?",
            "what are the criteria for scholarships?"
        ],
        'keywords': ['scholarship', 'grant', 'aid', 'financial', 'merit', 'need', 'concession']
    },
    
    'hostel_info': {
        'examples': [
            "tell me about hostel", "do you have hostel facilities", "accommodation details",
            "dorm rooms availability", "hostel fees and facilities", "mess and security in hostel",
            "what are the hostel charges?", "is hostel compulsory?"
        ],
        'keywords': ['hostel', 'accommodation', 'dorm', 'room', 'mess', 'security', 'lodging']
    },
    
    'documents_required': {
        'examples': [
            "what documents are required", "documents needed for admission", "which certificates to submit",
            "marksheets and id proof required", "list of documents for application",
            "what paperwork is needed?"
        ],
        'keywords': ['document', 'certificate', 'transcript', 'marksheet', 'id', 'photo', 'proof', 'paperwork']
    },
    
    'application_deadline': {
        'examples': [
            "when is the application deadline", "last date to apply", "closing date for applications",
            "apply by what date", "admission deadline", "what is the final date for submission?"
        ],
        'keywords': ['deadline', 'date', 'closing', 'last', 'apply', 'submission']
    },
    
    'entrance_exam_info': {
        'examples': [
            "is there an entrance exam", "entrance test details", "exam requirements for admission",
            "cutoff for entrance exam", "which entrance exams are accepted", "what is the syllabus for the entrance test?"
        ],
        'keywords': ['entrance', 'exam', 'test', 'cutoff', 'syllabus']
    },
    
    'admission_info': {
        'examples': [
            "how to apply for admission", "what are admission requirements", "admission process",
            "eligibility criteria for admission", "when do admissions start", "how to get admission",
            "admission procedure", "what documents are needed for admission", "admission deadline",
            "entrance exam for admission", "merit list for admission", "admission cut off",
            "how to apply", "application form", "admission form", "I want to apply"
        ],
        'keywords': ['admission', 'apply', 'application', 'eligibility', 'requirements', 'procedure', 'process']
    },
    
    'fee_info': {
        'examples': [
            "what is the fee structure", "how much are the fees", "tuition fees", "college fees",
            "fee details", "cost of studying", "fee payment", "scholarship availability",
            "financial assistance", "fee concession", "installment payment", "total fees",
            "annual fees", "semester fees", "what is the price?"
        ],
        'keywords': ['fee', 'fees', 'cost', 'tuition', 'payment', 'financial', 'money', 'price', 'installment']
    },
    
    'course_info': {
        'examples': [
            "what courses do you offer", "available programs", "degree programs", "subjects available",
            "curriculum details", "course duration", "specializations available", "undergraduate courses",
            "graduate programs", "post graduate courses", "diploma courses", "certificate programs",
            "syllabus information", "course structure", "what can I study?"
        ],
        'keywords': ['course', 'courses', 'program', 'programs', 'degree', 'subject', 'curriculum', 'syllabus', 'study']
    },
    
    'facility_info': {
        'examples': [
            "what facilities are available", "campus facilities", "library facilities", "laboratory facilities",
            "hostel facilities", "sports facilities", "cafeteria facilities", "wifi availability",
            "transport facilities", "medical facilities", "gym facilities", "computer lab",
            "research facilities", "infrastructure details", "what about the labs?"
        ],
        'keywords': ['facilities', 'facility', 'library', 'lab', 'hostel', 'sports', 'cafeteria', 'wifi', 'transport', 'gym', 'infrastructure']
    },
    
    'campus_info': {
        'examples': [
            "tell me about campus", "campus life", "campus environment", "campus location",
            "campus size", "campus culture", "student life", "campus events",
            "campus activities", "college atmosphere", "campus tour", "campus area",
            "college location", "how big is the campus?"
        ],
        'keywords': ['campus', 'location', 'environment', 'life', 'culture', 'events', 'activities', 'atmosphere', 'tour']
    },
    
    'faculty_info': {
        'examples': [
            "tell me about faculty", "faculty qualifications", "teaching staff", "professors information",
            "faculty experience", "teacher to student ratio", "faculty members", "instructor qualifications",
            "teaching quality", "faculty research", "faculty background", "academic staff",
            "teaching methodology", "who are the teachers?"
        ],
        'keywords': ['faculty', 'teacher', 'professor', 'staff', 'instructor', 'teaching', 'qualifications', 'experience', 'academic']
    },
    
    'placement_info': {
        'examples': [
            "placement opportunities", "job placement", "career opportunities", "placement record",
            "company visits", "recruitment drive", "placement statistics", "average salary",
            "placement support", "internship opportunities", "career guidance", "job assistance",
            "employment opportunities", "placement cell", "what jobs can I get?"
        ],
        'keywords': ['placement', 'job', 'career', 'recruitment', 'salary', 'internship', 'employment', 'company']
    },
    
    'contact_info': {
        'examples': [
            "contact information", "how to contact", "phone number", "email address",
            "college address", "office hours", "contact details", "reach out",
            "get in touch", "communication", "office location", "contact office",
            "admissions office contact", "how can I speak to someone?"
        ],
        'keywords': ['contact', 'phone', 'email', 'address', 'office', 'reach', 'touch', 'communication', 'speak']
    },
    
    'goodbye': {
        'examples': [
            "thank you", "goodbye", "bye", "see you later", "thanks for help",
            "that's all", "no more questions", "end conversation", "exit",
            "quit", "thanks", "thank you for information", "bye bye", "great, thanks"
        ],
        'keywords': ['thank', 'thanks', 'goodbye', 'bye', 'exit', 'quit', 'end']
    }
}

# Additional data for enhancing responses
COLLEGE_INFO = {
    'name': 'Rajeev Gandhi Memorial College of Engineering and Technology',
    'established': '1995',
    'location': 'Nandyal, Andhra Pradesh',
    'accreditation': 'NAAC with A+ Grade',
    'ranking': 'Top 100 Universities',
    'student_count': '15900+',
    'faculty_count': '295+',
    'campus_size': '32.04 acres',
    'admissions': {
        'application_open_date': 'July 1, 2025',
        'final_deadline': 'August 31, 2025',
        'entrance_exams': ['EAMCET', 'ECET', 'PGECET', 'ICET'],
        'documents_required': [
            'Caste certificate (if applicable)',
            'SSC (10th Class) Marksheet',
            'Intermediate (12th Class) Marks memo',
            'Transfer Certificate (TC)',
            'Migration Certificate (if applicable)'
        ]
    },
    'fees': {
        'tuition_per_year': 'Contact office for details',
        'other_fees': 'Contact office for details',
        'hostel_fee': 'Contact office for details'
    },
    'departments': [
        'Electronics & Communication Engineering',
        'Electrical & Electronics Engineering',
        'Civil Engineering',
        'Mechanical Engineering',
        'Master of Business Administration',
        'Master of Computer Applications',
        'Computer Science & Engineering',
        'Computer Science & Engineering (Data Science)',
        'Computer Science & Engineering (AI & ML)',
        'Computer Science & Engineering (Cyber Security)',
        'CSE & Business Systems'
    ]
}

# Responses for the chatbot
RESPONSES = {
    'greeting': [
        "Hello! Welcome to the inquiry system for {name}. How can I assist you today?",
        "Hi there! I'm here to answer your questions about {name}. What would you like to know?",
        "Greetings! I'm happy to help you with any questions you have about our college."
    ],
    'admission_info': [
        "For admissions at {name}, applications open on {admissions[application_open_date]} and the final deadline is {admissions[final_deadline]}. We accept scores from entrance exams like {admissions[entrance_exams]}. Would you like to know about the required documents?",
        "The admission process involves meeting eligibility criteria and having valid scores in exams such as {admissions[entrance_exams]}. The application window is from {admissions[application_open_date]} to {admissions[final_deadline]}.",
    ],
    'fee_info': [
        "For fee details, please contact the college administration. They will provide you with the most accurate and up-to-date information on tuition, hostel, and other fees.",
        "The fee structure varies by program. It's best to contact the admissions office for detailed information on fees and any available financial aid options.",
    ],
    'course_info': [
        "We offer a wide range of undergraduate and graduate programs, including: {departments}. Each program is designed to meet industry needs. Which field are you interested in?",
        "Our courses provide a blend of theoretical knowledge and practical skills. We offer Bachelor's, Master's, and Doctoral programs with various specializations. The main departments are: {departments}. Which area of study interests you?",
    ],
    'facility_info': [
        "Our campus has state-of-the-art facilities, including modern labs, a well-stocked library, a sports complex, a cafeteria, and comfortable hostels. We also provide campus-wide WiFi, medical facilities, and transportation services.",
        "We provide excellent infrastructure, including advanced research labs, computer centers, and sports grounds. Our hostels are safe and comfortable, with 24/7 security.",
    ],
    'campus_info': [
        "Our beautiful campus spans {campus_size} and is located in {location}. It offers a vibrant and ideal learning environment.",
        "Campus life at {name} is diverse and engaging, with numerous student clubs, societies, and sports teams. We host regular events and festivals to foster a dynamic community atmosphere.",
    ],
    'faculty_info': [
        "Our faculty consists of over {faculty_count} highly qualified professors and industry experts with extensive experience. Many hold PhDs from prestigious institutions and are active in research.",
        "Our faculty members are dedicated to student success and provide mentorship beyond the classroom. They bring real-world experience, which greatly benefits our students.",
    ],
    'placement_info': [
        "We have an excellent placement record, with over 85% of students placed in reputable companies. Our dedicated placement cell provides career counseling and skill development programs.",
        "We have strong industry partnerships for placements and internships. We conduct regular training programs, mock interviews, and skill workshops to prepare students for their careers.",
    ],
    'scholarship_info': [
        "We offer both merit-based and need-based scholarships. Merit scholarships can cover up to 50% of tuition fees based on academic performance. Need-based financial aid is also available.",
        "Scholarships are available for students with outstanding academic records, achievements in sports, and from different socio-economic backgrounds. Would you like to know the eligibility criteria?",
    ],
    'hostel_info': [
        "Our hostels provide separate accommodation for male and female students with 24/7 security, WiFi, and study areas. Rooms are available in single, double, and triple sharing formats.",
        "The hostel facilities include furnished rooms, common lounges, and laundry services. For fee details, please contact the college administration.",
    ],
    'documents_required': [
        "The required documents for admission are: {admissions[documents_required]}. Please ensure you have originals for verification.",
        "For the application, you will need to submit the following documents: {admissions[documents_required]}. It's a good idea to have scanned copies ready.",
    ],
    'application_deadline': [
        "The application portal opens on {admissions[application_open_date]} and the final deadline to apply is {admissions[final_deadline]}.",
        "Important dates for admission are: Applications open on {admissions[application_open_date]} and close on {admissions[final_deadline]}. We recommend applying early!",
    ],
    'entrance_exam_info': [
        "We accept scores from the following entrance exams: {admissions[entrance_exams]}. The cutoff scores may vary each year depending on the program.",
        "For admission, you need to have a valid score in one of these exams: {admissions[entrance_exams]}. If you tell me your desired program, I can provide more specific details.",
    ],
    'contact_info': [
        "You can contact us at: Phone: +91 85142 75203, Email: principal.9@jntua.ac.in, or visit our campus at Nerawada 'X' Roads, Nandyal, Andhra Pradesh 518501.",
        "For more information, please email our admissions office at principal.9@jntua.ac.in or call +91 85142 75203. You can also schedule a campus visit through our website.",
    ],
    'goodbye': [
        "Thank you for your interest in our college! If you have more questions, feel free to ask. Have a great day!",
        "It was a pleasure assisting you! Don't hesitate to reach out again if you need more information. Goodbye!",
    ],
    'unknown': [
        "I'm sorry, I'm not sure how to answer that. Could you please rephrase your question? I can help with topics like admissions, courses, fees, and facilities.",
        "I'm having a little trouble understanding. You can ask me about admissions, courses, fees, facilities, campus life, faculty, or placements.",
    ]
}

# Follow-up suggestions
SUGGESTIONS = {
    'greeting': ["Tell me about admissions", "What courses do you offer?", "What are the fees?"],
    'admission_info': ["What documents are required?", "When is the application deadline?", "Tell me about entrance exams"],
    'fee_info': ["Are scholarships available?", "What are the hostel fees?", "Can I pay in installments?"],
    'course_info': ["What is the course duration?", "Are there any new courses?", "Tell me about the faculty"],
    'facility_info': ["Tell me about hostel facilities", "What sports facilities are available?", "Do you have a library?"],
    'campus_info': ["What is campus life like?", "Tell me about student clubs", "Are there cultural events?"],
    'faculty_info': ["What are their qualifications?", "What is the student-faculty ratio?", "How accessible are the professors?"],
    'placement_info': ["What companies recruit from campus?", "What is the average salary package?", "Do you provide internship support?"],
    'scholarship_info': ["What are the eligibility criteria?", "How do I apply for a scholarship?", "When are scholarships announced?"],
    'hostel_info': ["What are the hostel fees?", "What amenities are in the rooms?", "Is there a curfew?"],
    'documents_required': ["Are originals required for verification?", "Is a migration certificate mandatory?", "Where do I submit the documents?"],
    'application_deadline': ["When do applications open?", "Is there a late fee for submission?", "When will the results be announced?"],
    'entrance_exam_info': ["What is the exam pattern?", "Are there sample papers available?", "What are the typical cutoff scores?"],
    'default': ["What are the admission requirements?", "Tell me about the courses.", "What is the fee structure?"]
}