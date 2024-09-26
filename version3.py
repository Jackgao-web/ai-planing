import spacy  # Import SpaCy, a natural language processing library
from sklearn.feature_extraction.text import TfidfVectorizer  # Import TF-IDF vectorizer for text vectorization
from sklearn.metrics.pairwise import cosine_similarity  # Import cosine similarity for calculating text similarity
import tkinter as tk  # Import tkinter for GUI
from tkinter import messagebox  # Import messagebox for showing pop-up messages
from tkcalendar import DateEntry  # Import DateEntry from tkcalendar for date selection widget

# Load SpaCy model for English language processing
nlp = spacy.load('en_core_web_sm')

# Define a list of keywords and corresponding recommendations
keywords = [
    # A comprehensive list of task-related keywords
    "time management", "productivity", "focus", "wash car", "exercise", "healthy eating", "meditation",
    "reading", "study", "work", "email management", "sleep hygiene", "budgeting", "goal setting",
    "meeting preparation", "project planning", "networking", "relaxation", "creative thinking",
    "team collaboration", "presentation skills", "public speaking", "career development", "mental health",
    "mindfulness", "personal growth", "relationship building", "conflict resolution", "task prioritization",
    "delegation", "leadership", "communication skills", "problem solving", "decision making", "strategic thinking",
    "innovation", "customer service", "client management", "time tracking", "self-discipline", "digital detox",
    "hydration", "journaling", "volunteering", "community service", "work-life balance", "financial planning",
    "risk management", "workout routine", "meal planning", "stress management", "mind mapping",
    "conflict management", "negotiation skills", "career transition", "remote work", "flexible work schedule",
    "side hustle", "entrepreneurship", "time blocking", "self-motivation", "positive thinking", "assertiveness",
    "emotional intelligence", "relationship management", "team building", "virtual collaboration", "remote meetings",
    "burnout prevention", "task automation", "software learning", "self-care", "yoga", "walking", "running",
    "cycling", "strength training", "cardio", "brainstorming", "creative writing", "public relations", "brand building",
    "personal branding", "social media management", "content creation", "video production", "photography", "editing",
    "network security", "data privacy", "software updates", "continuous learning", "online courses", "certification",
    "language learning", "project management", "agile methodology", "scrum", "kanban", "lean management", "six sigma",
    "quality assurance", "data analysis", "report writing", "presentation design", "customer retention", "sales strategy",
    "market research", "competitive analysis", "business development", "financial modeling", "investment planning",
    "retirement planning", "tax planning", "legal compliance", "contract management", "supply chain management",
    "logistics", "inventory management", "vendor management", "productivity tools", "software integration",
    "digital marketing", "search engine optimization", "pay-per-click", "email marketing", "content strategy",
    "public speaking", "conflict resolution", "sales funnel optimization", "client engagement", "customer loyalty",
    "market segmentation", "brand strategy", "crisis management", "business continuity planning", "corporate social responsibility"
]

# Corresponding recommendations for each keyword
recommendations = [
    "Use a calendar to schedule your tasks effectively and avoid last-minute rushes.",
    "Take regular breaks to maintain high productivity levels and prevent burnout.",
    "Eliminate distractions such as notifications to improve your focus on important tasks.",
    "Remember to wash your car every two weeks to maintain its condition and appearance.",
    "Incorporate at least 30 minutes of exercise into your daily routine to boost physical and mental health.",
    "Plan your meals in advance and focus on balanced nutrition for better energy levels throughout the day.",
    "Practice meditation daily to reduce stress and increase your mindfulness.",
    "Dedicate at least 20 minutes a day to reading for personal growth and knowledge enhancement.",
    "Set specific study goals and break down your material into manageable sections to improve learning efficiency.",
    "Prioritize your work tasks by importance and urgency to maximize productivity.",
    "Set specific times during the day to check and respond to emails, rather than doing it constantly.",
    "Establish a consistent sleep schedule and create a relaxing bedtime routine to improve your sleep quality.",
    "Track your expenses regularly and set a budget to manage your finances effectively.",
    "Set clear, achievable goals and review them regularly to stay motivated and on track.",
    "Prepare an agenda and necessary materials in advance for a more productive meeting.",
    "Break down large projects into smaller tasks and set deadlines for each to ensure timely completion.",
    "Build and maintain professional relationships by attending networking events and following up with contacts.",
    "Schedule regular downtime to relax and recharge, preventing burnout.",
    "Engage in activities that encourage creative thinking, such as brainstorming sessions or mind mapping.",
    "Foster a collaborative team environment by encouraging open communication and shared goals.",
    "Enhance your presentation skills by practicing regularly and seeking feedback from peers.",
    "Overcome public speaking anxiety by preparing thoroughly and focusing on the message you want to convey.",
    "Identify opportunities for career development through additional training or mentorship programs.",
    "Prioritize your mental health by seeking support when needed and maintaining a work-life balance.",
    "Incorporate mindfulness practices into your daily routine to stay grounded and focused.",
    "Commit to personal growth by setting aside time for self-reflection and learning new skills.",
    "Build strong relationships by showing empathy and actively listening to others.",
    "Address conflicts directly and respectfully to find mutually beneficial resolutions.",
    "Prioritize your tasks based on their impact and urgency to manage your time more effectively.",
    "Delegate tasks to others when appropriate to lighten your workload and empower your team.",
    "Develop leadership skills by taking on new challenges and seeking feedback from your team.",
    "Improve communication skills by being clear, concise, and actively listening to others.",
    "Enhance your problem-solving abilities by approaching challenges systematically and creatively.",
    "Make decisions confidently by gathering all relevant information and considering the consequences.",
    "Strengthen strategic thinking by focusing on long-term goals and considering all possible outcomes.",
    "Foster innovation by encouraging new ideas and experimenting with different approaches.",
    "Deliver excellent customer service by actively listening to clients and addressing their needs promptly.",
    "Manage client relationships effectively by keeping regular contact and being proactive in addressing issues.",
    "Track your time on tasks to identify where you can be more efficient and manage your workload better.",
    "Strengthen your self-discipline by setting clear goals, creating routines, and avoiding procrastination.",
    "Consider taking regular breaks from digital devices to refresh your mind and improve focus.",
    "Drink at least 8 glasses of water daily to stay hydrated and maintain energy levels.",
    "Start journaling to reflect on your thoughts and emotions, helping to clarify your goals and challenges.",
    "Engage in volunteering or community service to give back and gain a sense of fulfillment.",
    "Strive for a work-life balance by setting boundaries between work and personal time.",
    "Plan your finances carefully, including savings, investments, and managing debt.",
    "Identify and mitigate risks in your personal and professional life through careful planning.",
    "Create a consistent workout routine that includes a mix of cardio, strength training, and flexibility exercises.",
    "Plan your meals for the week ahead to save time and ensure a balanced diet.",
    "Develop stress management techniques, such as deep breathing exercises or mindfulness practices.",
    "Use mind mapping to organize your thoughts and ideas visually, making complex topics easier to understand.",
    "Learn and apply conflict management techniques to resolve disputes in a constructive manner.",
    "Enhance your negotiation skills to achieve better outcomes in both personal and professional situations.",
    "Prepare for career transitions by updating your resume, networking, and gaining new skills.",
    "Adopt best practices for remote work, such as creating a dedicated workspace and setting clear boundaries.",
    "Consider a flexible work schedule to improve your work-life balance and productivity.",
    "Explore a side hustle to diversify your income and pursue your passions.",
    "Develop entrepreneurial skills by learning about business planning, finance, and marketing.",
    "Use time blocking to allocate specific time periods for different tasks to stay organized and focused.",
    "Cultivate self-motivation by setting inspiring goals and rewarding yourself for achievements.",
    "Practice positive thinking to improve your outlook on life and increase resilience.",
    "Enhance your assertiveness by confidently expressing your needs and opinions while respecting others.",
    "Improve your emotional intelligence by being aware of your own emotions and empathizing with others.",
    "Manage relationships effectively by maintaining open communication and setting clear expectations.",
    "Organize team-building activities to strengthen relationships and improve collaboration within your team.",
    "Learn to effectively collaborate in virtual environments by using the right tools and maintaining communication.",
    "Improve the efficiency of remote meetings by setting clear agendas and encouraging participation.",
    "Prevent burnout by recognizing the signs early and taking proactive steps to manage stress.",
    "Automate repetitive tasks using software tools to save time and reduce manual effort.",
    "Invest time in learning new software or tools that can enhance your productivity and efficiency.",
    "Prioritize self-care activities, such as relaxation, hobbies, and spending time with loved ones.",
    "Incorporate yoga into your routine to improve flexibility, strength, and mental clarity.",
    "Consider walking or cycling as forms of low-impact exercise that also benefit mental health.",
    "Include strength training in your workout routine to build muscle and improve overall fitness.",
    "Add cardio exercises, such as running or swimming, to your routine to improve cardiovascular health.",
    "Engage in brainstorming sessions to generate creative ideas and solve problems innovatively.",
    "Practice creative writing to express yourself and improve your communication skills.",
    "Enhance your public relations skills by building positive relationships with the media and stakeholders.",
    "Focus on brand building by consistently communicating your brand values and message.",
    "Develop a strong personal brand by showcasing your expertise and values in your professional life.",
    "Learn social media management strategies to effectively engage with your audience and build your brand.",
    "Explore content creation techniques to produce engaging and informative materials for your audience.",
    "Develop video production skills to create compelling visual content for marketing or personal projects.",
    "Hone your photography and editing skills to capture and enhance images for various purposes.",
    "Stay updated on network security best practices to protect your data and prevent cyber threats.",
    "Ensure data privacy by following regulations and implementing secure data handling practices.",
    "Keep your software up to date to avoid vulnerabilities and ensure you have the latest features.",
    "Engage in continuous learning by taking online courses, attending workshops, or reading industry news.",
    "Consider earning certifications to validate your skills and improve your career prospects.",
    "Explore language learning opportunities to expand your communication skills and cultural understanding.",
    "Apply project management techniques, such as Agile or Scrum, to keep your projects on track.",
    "Use Kanban boards to visualize work in progress and manage tasks efficiently.",
    "Adopt Lean management principles to minimize waste and maximize value in your processes.",
    "Implement Six Sigma techniques to improve the quality of your processes and reduce errors.",
    "Develop quality assurance skills to ensure products and services meet the required standards.",
    "Enhance your data analysis skills to make informed decisions based on insights and trends.",
    "Improve your report writing skills to clearly and concisely communicate information.",
    "Focus on presentation design to create visually appealing and informative slides for your audience.",
    "Work on customer retention strategies to build loyalty and increase repeat business.",
    "Develop a sales strategy that aligns with your business goals and meets customer needs.",
    "Conduct market research to understand your target audience and stay ahead of competitors.",
    "Perform competitive analysis to identify strengths, weaknesses, opportunities, and threats in your market.",
    "Explore business development opportunities to expand your company's reach and increase revenue.",
    "Learn financial modeling techniques to make informed business decisions based on financial data.",
    "Plan for retirement by setting long-term financial goals and choosing the right investment vehicles.",
    "Understand tax planning strategies to optimize your financial situation and avoid unnecessary taxes.",
    "Ensure legal compliance by staying updated on relevant laws and regulations for your industry.",
    "Develop contract management skills to ensure all agreements are executed properly and risks are mitigated.",
    "Improve supply chain management practices to streamline operations and reduce costs.",
    "Learn logistics management to optimize the movement of goods and ensure timely delivery.",
    "Enhance your inventory management techniques to maintain optimal stock levels and reduce waste.",
    "Focus on vendor management to build strong relationships with suppliers and negotiate favorable terms.",
    "Utilize productivity tools to automate tasks, manage projects, and collaborate with teams effectively.",
    "Explore software integration options to improve workflow efficiency and reduce manual data entry.",
    "Keep up with digital marketing trends to effectively promote your products and services online.",
    "Optimize your search engine rankings through SEO strategies to drive more traffic to your website.",
    "Implement pay-per-click advertising to increase visibility and attract targeted customers.",
    "Develop an email marketing strategy to build and nurture relationships with your audience.",
    "Create a content strategy to deliver valuable, consistent, and relevant content to your audience.",
    "Strengthen your public speaking skills by practicing regularly and focusing on clear communication.",
    "Improve conflict resolution techniques to resolve disputes constructively and maintain positive relationships.",
    "Optimize your sales funnel to convert more leads into customers and maximize revenue.",
    "Enhance client engagement by actively listening, providing value, and addressing their needs promptly.",
    "Focus on customer loyalty by delivering exceptional service and creating a positive experience.",
    "Use market segmentation to tailor your marketing efforts to specific customer groups.",
    "Develop a brand strategy to communicate your brand values and differentiate yourself from competitors.",
    "Prepare for crisis management by having a plan in place and training your team on how to respond.",
    "Implement business continuity planning to ensure your operations can continue during disruptions.",
    "Incorporate corporate social responsibility into your business model to positively impact society and the environment."
]

# Preprocess function to normalize the text for better matching with keywords
def preprocess(text):
    doc = nlp(text.lower())  # Convert the input text to lowercase and process it with SpaCy
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]  # Lemmatize and remove stopwords/punctuation
    return " ".join(tokens)  # Return the processed text

# Preprocess all keywords before feeding into the TF-IDF model
preprocessed_keywords = [preprocess(keyword) for keyword in keywords]

# Vectorize the keywords using TF-IDF (Term Frequency-Inverse Document Frequency)
vectorizer = TfidfVectorizer()  # Create an instance of the TF-IDF vectorizer
tfidf_matrix = vectorizer.fit_transform(preprocessed_keywords)  # Fit and transform the keywords into a matrix

# Function to get a recommendation based on a keyword
def get_recommendation(keyword):
    keyword_processed = preprocess(keyword)  # Preprocess the input keyword
    user_tfidf = vectorizer.transform([keyword_processed])  # Transform it into TF-IDF format
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)  # Compute cosine similarities with the keyword matrix
    best_match_index = similarities.argmax()  # Get the index of the most similar keyword
    if similarities[0, best_match_index] > 0.2:  # Check if similarity exceeds a threshold
        return recommendations[best_match_index]  # Return the matching recommendation
    else:
        return "No recommendation found for this keyword."  # If no match is found, return a default message

# Self Management System class to handle users and tasks
class SelfManagementSystem:
    def __init__(self):
        self.users = {"1": "1"}  # A default user account for login (username: 1, password: 1)
        self.tasks = []  # List to store tasks

    # Function to log in users based on username and password
    def login(self, username, password):
        return self.users.get(username) == password  # Return True if login credentials match

    # Function to add a task with a name and deadline
    def add_task(self, name, deadline):
        self.tasks.append({"name": name, "deadline": deadline, "completed": False})  # Add a new task with "incomplete" status

    # Function to view tasks, showing task details like name, deadline, and completion status
    def view_tasks(self):
        return [f"{i + 1}. {task['name']} - {task['deadline']} - {'Completed' if task['completed'] else 'Incomplete'}" 
                for i, task in enumerate(self.tasks)]  # Display tasks in a formatted list

    # Function to mark a task as completed based on its ID
    def mark_task_completed(self, task_id):
        if 0 <= task_id < len(self.tasks):  # Check if the task ID is valid
            self.tasks[task_id]["completed"] = True  # Mark the task as completed

    # Function to delete a task based on its ID
    def delete_task(self, task_id):
        if 0 <= task_id < len(self.tasks):  # Check if the task ID is valid
            self.tasks.pop(task_id)  # Remove the task from the list

# Main function that runs the application
def main():
    system = SelfManagementSystem()  # Instantiate the task management system

    # Function for handling login logic
    def login():
        username = username_entry.get()  # Get the entered username
        password = password_entry.get()  # Get the entered password
        if system.login(username, password):  # If login is successful
            messagebox.showinfo("Login Status", "Login Successful!")  # Show success message
            login_window.destroy()  # Close the login window
            main_menu()  # Open the main menu
        else:
            messagebox.showerror("Login Status", "Invalid Username or Password.")  # Show error message

    # Function to show the main menu (task management interface)
    def main_menu():
        main_menu_window = tk.Tk()  # Create a new window for the main menu
        main_menu_window.title("Task Management System - Main Menu")  # Set window title
        main_menu_window.geometry("400x500")  # Set window size
        main_menu_window.configure(bg="#f0f8ff")  # Set background color

        # Label for the main menu window
        tk.Label(main_menu_window, text="Task Management System", font=("Helvetica", 16, "bold"), fg="#1f77b4", 
                 bg="#f0f8ff").grid(row=0, column=0, columnspan=2, pady=10)

        # Function to refresh the list of tasks in the interface
        def refresh_task_list():
            task_listbox.delete(0, tk.END)  # Clear the task listbox
            for task in system.view_tasks():  # Add each task to the listbox
                task_listbox.insert(tk.END, task)

        # Function to add a new task
        def add_task():
            name = task_name_entry.get()  # Get the task name
            deadline = task_deadline_entry.get()  # Get the task deadline
            system.add_task(name, deadline)  # Add the task to the system
            messagebox.showinfo("Task Added", f"Task '{name}' added with a deadline of {deadline}.\nRecommendation: {get_recommendation(name)}")  # Show confirmation with a recommendation
            task_name_entry.delete(0, tk.END)  # Clear the input fields
            refresh_task_list()  # Refresh the task list

        # Function to mark a task as completed
        def mark_task_completed():
            selected_task_index = task_listbox.curselection()  # Get the selected task index
            if selected_task_index:
                task_id = selected_task_index[0]  # Get the task ID
                system.mark_task_completed(task_id)  # Mark the task as completed
                messagebox.showinfo("Task Completed", f"Task {task_id + 1} marked as completed.")  # Show confirmation message
                refresh_task_list()  # Refresh the task list

        # Function to delete a task
        def delete_task():
            selected_task_index = task_listbox.curselection()  # Get the selected task index
            if selected_task_index:
                task_id = selected_task_index[0]  # Get the task ID
                system.delete_task(task_id)  # Delete the task
                messagebox.showinfo("Task Deleted", f"Task {task_id + 1} deleted.")  # Show confirmation message
                refresh_task_list()  # Refresh the task list

        # Create input fields and buttons for adding tasks
        tk.Label(main_menu_window, text="Task Name", font=("Helvetica", 12), bg="#f0f8ff").grid(row=1, column=0, padx=10, pady=5)
        task_name_entry = tk.Entry(main_menu_window)
        task_name_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(main_menu_window, text="Task Deadline (DD-MM-YYYY)", font=("Helvetica", 12), bg="#f0f8ff").grid(row=2, column=0, padx=10, pady=5)
        task_deadline_entry = DateEntry(main_menu_window, date_pattern='dd-mm-yyyy')
        task_deadline_entry.grid(row=2, column=1, padx=10, pady=5)

        add_task_button = tk.Button(main_menu_window, text="Add Task", font=("Helvetica", 12, "bold"), fg="white", bg="#28a745", command=add_task)
        add_task_button.grid(row=3, columnspan=2, pady=10)

        # Create a listbox to show tasks
        task_listbox = tk.Listbox(main_menu_window, font=("Helvetica", 12), width=40, height=10)
        task_listbox.grid(row=5, column=0, columnspan=2, pady=5)

        mark_task_completed_button = tk.Button(main_menu_window, text="Mark Task as Completed", font=("Helvetica", 12, "bold"), fg="white", bg="#ffc107", command=mark_task_completed)
        mark_task_completed_button.grid(row=6, columnspan=2, pady=5)

        delete_task_button = tk.Button(main_menu_window, text="Delete Task", font=("Helvetica", 12, "bold"), fg="white", bg="#dc3545", command=delete_task)
        delete_task_button.grid(row=7, columnspan=2, pady=5)

        refresh_task_list()  # Refresh the task list when opening the main menu
        main_menu_window.mainloop()  # Start the main menu loop

    # Create the login window
    login_window = tk.Tk()
    login_window.title("Task Management System - Login")  # Set the login window title
    login_window.geometry("350x250")  # Set the login window size
    login_window.configure(bg="#e3f2fd")  # Set the background color of the login window

    tk.Label(login_window, text="Username", font=("Helvetica", 12), bg="#e3f2fd").pack(pady=10)
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    tk.Label(login_window, text="Password", font=("Helvetica", 12), bg="#e3f2fd").pack(pady=10)
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    login_button = tk.Button(login_window, text="Login", font=("Helvetica", 12, "bold"), fg="white", bg="#007bff", command=login)
    login_button.pack(pady=20)

    login_window.mainloop()  # Start the login window loop

if __name__ == "__main__":
    main()  # Run the main function to start the application
