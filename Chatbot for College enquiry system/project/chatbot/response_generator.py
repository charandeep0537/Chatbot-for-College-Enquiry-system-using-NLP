import random
from typing import Dict, List

class ResponseGenerator:
    """Generate appropriate responses based on classified intents."""
    
    def __init__(self):
        from chatbot.training_data import COLLEGE_INFO
        self.info = COLLEGE_INFO
        self.responses = {
            'greeting': [
                "Hello! Welcome to our college inquiry system. How can I help you today?",
                "Hi there! I'm here to answer your questions about our college. What would you like to know?",
                "Greetings! I'm happy to assist you with any college-related questions you might have.",
                "Welcome! Feel free to ask me anything about admissions, courses, facilities, or campus life."
            ],
            
            'admission_info': [
                f"Applications open on {self.info['admissions']['application_open_date']} and the final deadline is {self.info['admissions']['final_deadline']}. Accepted entrance exams include {', '.join(self.info['admissions']['entrance_exams'])}. Would you like the list of required documents?",
                f"Admissions follow eligibility criteria and relevant entrance exams such as {', '.join(self.info['admissions']['entrance_exams'])}. Applications are accepted from {self.info['admissions']['application_open_date']} until {self.info['admissions']['final_deadline']}.",
                f"You can apply between {self.info['admissions']['application_open_date']} and {self.info['admissions']['final_deadline']}. Let me know your program so I can share exam and document specifics."
            ],
            
            'fee_info': [
                f"Tuition per year is {self.info['fees']['tuition_per_year']}. Other fees are {self.info['fees']['other_fees']}. Hostel fee is {self.info['fees']['hostel_fee']}. Scholarships and installment plans are available.",
                f"For most programs, tuition is {self.info['fees']['tuition_per_year']} per year, plus other fees of {self.info['fees']['other_fees']}. Hostel accommodation is {self.info['fees']['hostel_fee']} per year.",
                f"Annual tuition: {self.info['fees']['tuition_per_year']}. Additional: {self.info['fees']['other_fees']}. Hostel: {self.info['fees']['hostel_fee']}. Would you like scholarship details?"
            ],
            
            'course_info': [
                "We offer a wide range of undergraduate and graduate programs across Engineering, Business, Arts, Science, and Technology. Each program has a comprehensive curriculum designed with industry needs in mind. Which field interests you most?",
                "Our courses are designed to provide both theoretical knowledge and practical skills. We offer Bachelor's, Master's, and Doctoral programs with specializations in various fields. Industry partnerships ensure relevant and updated curriculum. What subject area are you considering?",
                "Course offerings include full-time, part-time, and research programs. Each course emphasizes hands-on learning, projects, and internships. We maintain small class sizes for personalized attention. Which program would you like to explore?"
            ],
            
            'facility_info': [
                "Our campus features state-of-the-art facilities including modern laboratories, a comprehensive library, sports complex, cafeteria, and comfortable hostels. We also provide high-speed WiFi, medical facilities, and transportation services.",
                "Facilities include well-equipped labs, digital library, gymnasium, swimming pool, auditoriums, and recreational areas. Our hostels provide a safe and comfortable living environment with 24/7 security and nutritious meals.",
                "We pride ourselves on excellent infrastructure: advanced research labs, computer centers, workshop facilities, sports grounds, cultural centers, and green campus spaces. All facilities are accessible and maintained to high standards."
            ],
            
            'campus_info': [
                "Our beautiful campus spans 50 acres with modern architecture and green spaces. Located in a peaceful area with easy access to the city center, it provides an ideal learning environment with a vibrant student community.",
                "The campus combines academic excellence with a rich cultural environment. We host regular events, festivals, and activities. Student clubs, societies, and sports teams create a dynamic community atmosphere.",
                "Campus life is diverse and engaging with students from various backgrounds. We encourage participation in extracurricular activities, community service, and leadership opportunities. The environment fosters both personal and academic growth."
            ],
            
            'faculty_info': [
                "Our faculty comprises highly qualified professors and industry experts with advanced degrees and extensive experience. Many hold Ph.D.s from prestigious institutions and maintain active research programs while providing excellent teaching.",
                "Faculty members are dedicated to student success, offering mentorship and guidance beyond the classroom. They bring real-world experience and maintain industry connections that benefit student learning and career opportunities.",
                "We maintain an excellent student-to-faculty ratio ensuring personalized attention. Faculty regularly update their knowledge through research, conferences, and industry collaboration, bringing the latest developments into the classroom."
            ],
            
            'placement_info': [
                "Our placement record is excellent with 85%+ students getting placed in reputable companies. We have dedicated placement cells, career counseling, and skill development programs. Average salary packages range from $30,000-$80,000 annually.",
                "We maintain strong industry partnerships with leading companies for placements and internships. Regular training programs, mock interviews, and skill workshops prepare students for successful careers. Many alumni hold leadership positions in top organizations.",
                "Placement support includes resume building, interview preparation, and industry networking. We host regular job fairs and company visits. Our alumni network provides mentorship and career guidance to current students."
            ],
            
            'scholarship_info': [
                "We offer merit-based and need-based scholarships. Merit awards can cover up to 50% of tuition depending on academic performance, while need-based aid is assessed case by case. Application typically requires transcripts and a brief statement.",
                "Scholarships are available for outstanding academic, sports, and socio-economic backgrounds. You can apply during admission by indicating interest; supporting documents are required. Would you like the eligibility criteria?",
                "Financial aid options include scholarships, grants, and installment plans. Scholarship decisions consider grades, entrance scores, and extracurricular achievements."
            ],
            
            'hostel_info': [
                "Our hostels provide separate accommodation for men and women with 24/7 security, WiFi, study areas, and a hygienic mess. Rooms are available in single, double, and triple sharing.",
                "Hostel facilities include furnished rooms, common lounges, indoor games, laundry, and medical support. Allocation is on a first-come basis post-admission.",
                "Accommodation fees vary by room type and include basic utilities. Quiet hours and wardens ensure a safe environment conducive to study."
            ],
            
            'documents_required': [
                f"Required documents: {', '.join(self.info['admissions']['documents_required'])}. Originals will be verified during admission.",
                f"Please prepare scanned copies of {', '.join(self.info['admissions']['documents_required'])}. Keep ID proof and photos ready as well.",
                f"You will need {', '.join(self.info['admissions']['documents_required'])}. Additional items may be requested per program."
            ],
            
            'application_deadline': [
                f"Applications open on {self.info['admissions']['application_open_date']} and the final deadline is {self.info['admissions']['final_deadline']}.",
                f"Key dates: Open {self.info['admissions']['application_open_date']} • Final deadline {self.info['admissions']['final_deadline']}. Applying early is recommended.",
                f"You can apply from {self.info['admissions']['application_open_date']} until {self.info['admissions']['final_deadline']}."
            ],
            
            'entrance_exam_info': [
                f"Accepted entrance exams include {', '.join(self.info['admissions']['entrance_exams'])}. Cutoffs vary by year and category.",
                f"Programs consider exams such as {', '.join(self.info['admissions']['entrance_exams'])}. Share your program for specific guidance.",
                f"Entrance tests: {', '.join(self.info['admissions']['entrance_exams'])}. I can outline cutoffs and timelines if you specify your program."
            ],
            
            'contact_info': [
                "You can reach us at: Phone: +1-555-0123, Email: admissions@college.edu, or visit our campus at 123 Education Street, University City. Our admissions office is open Monday-Friday, 9 AM-5 PM.",
                "For more information, contact our admissions office at admissions@college.edu or call +1-555-0123. You can also schedule a campus visit through our website or visit us during office hours.",
                "Get in touch: Phone: +1-555-0123, Email: info@college.edu, Address: 123 Education Street, University City. We're also available on social media and through our website's live chat feature."
            ],
            
            'goodbye': [
                "Thank you for your interest in our college! Feel free to reach out anytime if you have more questions. Best of luck with your educational journey!",
                "It was great helping you today! Don't hesitate to contact us if you need any additional information. We look forward to welcoming you to our college community.",
                "Goodbye! I hope I've been helpful. Remember, our admissions team is always available for further assistance. Have a wonderful day!"
            ],
            
            'unknown': [
                "I'm not sure I understand your question completely. Could you please rephrase it or ask about specific topics like admissions, courses, fees, facilities, campus life, faculty, or placements?",
                "I'd be happy to help, but I need a bit more clarity. Are you asking about admissions, course information, fees, campus facilities, or something else? Please feel free to be more specific.",
                "I didn't quite catch that. I can assist you with questions about college admissions, academic programs, fees, facilities, campus life, faculty, and career placements. What would you like to know more about?"
            ]
        }
        
        # Follow-up suggestions based on intent
        self.suggestions = {
            'greeting': [
                "Tell me about admissions",
                "What courses do you offer?",
                "What are the fees?",
                "Show me campus facilities"
            ],
            'admission_info': [
                "What documents are required?",
                "When is the application deadline?",
                "Tell me about entrance exams",
                "What are the eligibility criteria?"
            ],
            'fee_info': [
                "Are scholarships available?",
                "What payment options do you have?",
                "Tell me about additional costs",
                "Can I get financial aid?"
            ],
            'course_info': [
                "What is the curriculum like?",
                "Are there internship opportunities?",
                "How long is the program?",
                "What are the specializations?"
            ],
            'facility_info': [
                "Tell me about hostel facilities",
                "What sports facilities are available?",
                "Do you have research labs?",
                "What about library resources?"
            ],
            'campus_info': [
                "What events happen on campus?",
                "Tell me about student clubs",
                "What is campus life like?",
                "Are there cultural activities?"
            ],
            'faculty_info': [
                "What is the student-faculty ratio?",
                "Do faculty help with research?",
                "What are their qualifications?",
                "How accessible are professors?"
            ],
            'placement_info': [
                "What companies visit for recruitment?",
                "What is the average salary?",
                "Do you provide career counseling?",
                "Are there internship programs?"
            ],
            'scholarship_info': [
                "What are the scholarship eligibility criteria?",
                "How do I apply for scholarships?",
                "Can scholarships be combined with other aid?",
                "Is there a separate scholarship deadline?"
            ],
            'hostel_info': [
                "What are hostel fees?",
                "Do rooms have attached bathrooms?",
                "Is there a curfew or quiet hours?",
                "How is mess food quality?"
            ],
            'documents_required': [
                "Do I need originals during verification?",
                "Are photocopies sufficient at application stage?",
                "Is a transfer certificate mandatory?",
                "Do I need to notarize documents?"
            ],
            'application_deadline': [
                "When do applications open?",
                "Is there an early decision round?",
                "Can I apply after the deadline?",
                "What is the timeline for results?"
            ],
            'entrance_exam_info': [
                "Which exams are accepted for my program?",
                "What are the typical cutoffs?",
                "Is there an interview after the exam?",
                "Are there sample papers available?"
            ]
        }
    
    def generate_response(self, intent_result: Dict, processed_input: Dict, session_id: str) -> Dict:
        """Generate an appropriate response based on the classified intent."""
        intent = intent_result['intent']
        confidence = intent_result['confidence']
        
        # Select base response
        if intent in self.responses:
            response_options = self.responses[intent]
            base_response = random.choice(response_options)
        else:
            base_response = random.choice(self.responses['unknown'])
        
        # Enhance response based on confidence
        if confidence > 0.8:
            prefix = ""
        elif confidence > 0.5:
            prefix = "Here’s what I found: "
        elif confidence > 0.3:
            prefix = "I believe this relates to your question. "
        else:
            prefix = ""
        
        final_response = prefix + base_response
        
        # Get relevant suggestions
        suggestions = self.suggestions.get(intent, [])
        if not suggestions and intent != 'unknown':
            suggestions = self.suggestions['greeting']
        
        return {
            'response': final_response,
            'suggestions': random.sample(suggestions, min(3, len(suggestions))) if suggestions else [],
            'confidence': confidence,
            'intent': intent
        }