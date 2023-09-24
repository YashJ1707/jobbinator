import spacy


def getTags(description: str):
# Load the spaCy English language model
    nlp = spacy.load("en_core_web_sm")

    # Process the text using spaCy
    doc = nlp(description)

    # Define patterns for different categories of information
    languages = ["Java", "CSS", "JavaScript", "C++", "C#", "Ruby", "Swift", "Go", "Kotlin", "Rust", "PHP", "TypeScript", "Dart", "MATLAB", "Perl", "R", "Objective-C", "Scala", "Groovy", "Lua", "Haskell", "Erlang", "COBOL", "Fortran", "Assembly (x86, ARM, etc.)", "SQL", "HTML", "Python", "Shell scripting (Bash)", "PL/SQL", "Visual Basic", "Groovy", "Tcl", "Lisp", "Prolog", "Ada", "Julia", "COOL", "OCaml", "VHDL", "Clojure", "F#", "Apex", "ActionScript", "Kotlin", "COOL", "Apex", "MATLAB", "Dart", "Elixir", "Elm","Flutter"]  # Add more languages
    tools_and_technologies = ["Git", "Docker", "Kubernetes", "React", "Angular", "Vue.js", "TensorFlow", "Node.js", "MongoDB", "MySQL", "PostgreSQL", "Redis", "Elasticsearch", "Spring Boot", "Flask", "Express.js", "Ruby on Rails", "Unity", "PyTorch", "Jupyter", "Visual Studio Code", "IntelliJ IDEA", "Sublime Text", "Atom", "PyCharm", "Eclipse", "NetBeans", "Django", "Laravel", "Apache Kafka", "GraphQL", "Apache Spark", "Hadoop", "Amazon Web Services (AWS)", "Google Cloud Platform (GCP)", "Microsoft Azure", "Heroku", "Firebase", "Jenkins", "Travis CI", "CircleCI", "GitHub Actions", "Ansible", "Puppet", "Chef", "Vagrant", "Docker Compose", "Prometheus", "Grafana"]  # Add more tools and technologies
    skills = ["Web development", "Data analysis", "Machine learning", "Project management", "Software engineering", "Database administration", "Mobile app development", "Front-end development", "Back-end development", "Full-stack development", "Cloud computing", "DevOps", "Version control (Git)", "Agile methodology", "UI/UX design", "Responsive web design", "API development", "Data modeling", "Algorithm design", "Debugging", "Troubleshooting", "Security analysis", "Penetration testing", "Code review", "Unit testing", "Test-driven development (TDD)", "Continuous integration (CI)", "Continuous delivery (CD)", "Containerization", "Serverless computing", "Natural language processing (NLP)", "Computer vision", "Artificial intelligence (AI)", "Big data analytics", "Data visualization", "Blockchain development", "IoT development", "Game development", "Embedded systems programming", "Parallel computing", "Quantum computing", "AR/VR development", "Cybersecurity", "Network administration", "Scripting (e.g., Python)", "Shell scripting (Bash)", "Functional programming", "Object-oriented programming (OOP)", "Data structures and algorithms"]  # Add more skills

    # Initialize dictionaries to store extracted information
    extracted_info =set()

    # Extract information based on patterns
    for token in doc:
        token_text = token.text.lower()
        for lang in languages:
            if token_text == lang.lower():
                extracted_info.add(lang)
        for tool in tools_and_technologies:
            if token_text == tool.lower():
                extracted_info.add(tool)
        for skill in skills:
            if token_text == skill.lower():
                extracted_info.add(skill)

    # Remove duplicate entries
    # for category, values in extracted_info.items():
    #     extracted_info[category] = list(set(values))
    return list(extracted_info)