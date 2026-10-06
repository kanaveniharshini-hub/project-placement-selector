def chatbot_response(user_message):

    message = user_message.lower()

    if "hello" in message or "hi" in message:
        return "Hello! 👋 I am your Placement Preparation Assistant."

    elif "aptitude" in message:
        return """
Aptitude preparation includes:
• Quantitative Aptitude
• Logical Reasoning
• Verbal Ability

Practice questions daily to improve your speed.
"""

    elif "coding" in message:
        return """
For coding preparation, start with:
• Python or Java
• Arrays
• Strings
• Loops
• Functions
• Data Structures
"""

    elif "interview" in message:
        return """
Common interview questions:
1. Tell me about yourself.
2. What are your strengths?
3. What are your weaknesses?
4. Why should we hire you?
5. Where do you see yourself in 5 years?
"""

    elif "resume" in message:
        return """
Resume tips:
• Keep your resume to 1 page.
• Add your technical skills.
• Mention projects.
• Add internships/certifications.
• Avoid spelling mistakes.
"""

    elif "roadmap" in message:
        return """
Placement Roadmap:

1. Learn programming
2. Practice DSA
3. Study aptitude
4. Build projects
5. Prepare your resume
6. Practice technical interviews
7. Practice HR interviews
8. Take mock tests
"""

    elif "python" in message:
        return "Python is beginner-friendly and useful for coding, AI and data science."

    elif "java" in message:
        return "Java is widely used in software development and is a good language for placements."

    elif "thank" in message:
        return "You're welcome! 😊 Keep preparing for your placements!"

    else:
        return """
I can help you with:

📚 Aptitude
💻 Coding
🎯 Interview
📄 Resume
🗺️ Placement Roadmap
🐍 Python
☕ Java

Try asking me about any of these topics!
"""