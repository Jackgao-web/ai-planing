import tkinter as tk  # Importing tkinter for creating GUI elements
from tkinter import messagebox  # Importing messagebox for popup alerts
from tkcalendar import DateEntry  # Importing DateEntry for date selection calendar widget
from datetime import datetime, timedelta  # Importing datetime and timedelta for date manipulation
from sklearn.feature_extraction.text import TfidfVectorizer  # Importing TfidfVectorizer for keyword matching
from sklearn.metrics.pairwise import cosine_similarity  # Importing cosine_similarity for calculating similarity between tasks
import spacy  # Importing SpaCy for natural language processing


# Load the pre-trained SpaCy model for natural language processing
nlp = spacy.load('en_core_web_sm')
# Keywords and recommendations

keywords = [
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

# Function to preprocess text by converting to lowercase, lemmatizing, and removing stop words/punctuation
def preprocess(text):
    # Use SpaCy to process the text
    doc = nlp(text.lower())
    # Extract the lemma (base form) of each word, excluding stop words and punctuation
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)  # Return the cleaned-up text as a string

# Preprocess a list of task keywords to make them suitable for TF-IDF vectorization
preprocessed_keywords = [preprocess(keyword) for keyword in keywords]
vectorizer = TfidfVectorizer()  # Initialize TF-IDF vectorizer
tfidf_matrix = vectorizer.fit_transform(preprocessed_keywords)  # Fit and transform the preprocessed keywords into a numerical matrix

# Function to provide task recommendations based on keyword matching
def get_recommendation(keyword):
    # Preprocess the user-provided keyword
    keyword_processed = preprocess(keyword)
    # Transform the preprocessed keyword into the same TF-IDF format
    user_tfidf = vectorizer.transform([keyword_processed])
    # Compute cosine similarity between the user's keyword and the task keywords
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    # Find the index of the most similar task
    best_match_index = similarities.argmax()
    # If the similarity score is greater than 0.2, return the matching task recommendation
    if similarities[0, best_match_index] > 0.2:
        return recommendations[best_match_index]
    else:
        # If no similar task is found, return a message saying no recommendation was found
        return "No recommendation found for this keyword."

# Dictionary to store user accounts with username as key and password as value
accounts = {}

# Dictionary to store tasks, where the task name is the key and task details (like deadline, completion status) are the values
tasks = {}

# Function to add a new user account
def add_account():
    custom_font = ("Helvetica", 14)  # Custom font settings for consistent UI
    def add_account_inside():
        # Retrieve the entered username and password
        user_name = new_username_entry.get()
        password = new_password_entry.get()
        # Check if the username already exists
        if user_name in accounts:
            messagebox.showerror("Error", "Account already exists!")
        else:
            # Add the new account to the accounts dictionary
            accounts[user_name] = password
            # Save the updated accounts to a file
            save_accounts()
            # Display success message
            messagebox.showinfo("Success", "Account added successfully!")
            # Clear the input fields and close the add account window
            new_username_entry.delete(0, tk.END)
            new_password_entry.delete(0, tk.END)
            add_account_window.destroy()

    # Create a new window for adding a new account
    add_account_window = tk.Toplevel()
    add_account_window.title('New Account')  # Set the window title
    add_account_window.configure(bg="#e3f2fd")  # Set background color

    # Create input labels and entry fields for the username and password
    new_username_label = tk.Label(add_account_window, text='New Username:', font=custom_font, bg="#e3f2fd")
    new_username_label.grid(row=0, column=0, pady=5, padx=5, sticky='w')

    new_username_entry = tk.Entry(add_account_window, font=custom_font)
    new_username_entry.grid(row=0, column=1, pady=5, padx=5)

    new_password_label = tk.Label(add_account_window, text='New Password:', font=custom_font, bg="#e3f2fd")
    new_password_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

    new_password_entry = tk.Entry(add_account_window, show='*', font=custom_font)  # Password input hidden by asterisks
    new_password_entry.grid(row=1, column=1, pady=5, padx=5)

    # Button to trigger adding the new account
    tk.Button(add_account_window, text='Add Account', command=add_account_inside, fg="white", bg="#007bff", font=custom_font).grid(row=2, column=0, columnspan=2, pady=10)

# Function to display the task management page after successful login
def show_task_management_page():
    login_frame.pack_forget()  # Hide the login frame
    task_management_frame.pack()  # Show the task management frame

# Function to show the login frame again (logout)
def show_frame1():
    task_management_frame.pack_forget()  # Hide the task management frame
    login_frame.pack()  # Show the login frame
    # Clear the input fields for username and password
    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

# Store the currently logged-in user's username
current_user = ""

# Function to check login credentials
def check_credentials():
    global current_user
    # Get the entered username and password
    username = username_entry.get()
    password = password_entry.get()

    # Validate the credentials
    if username in accounts and accounts[username] == password:
        current_user = username  # Set the current user
        load_tasks()  # Load tasks for the logged-in user
        messagebox.showinfo("Success", "Login successful!")  # Show success message
        show_task_management_page()  # Display the task management page
    else:
        # Show error if credentials are invalid
        messagebox.showerror("Error", "Invalid username or password!")

# Function to save accounts to a text file
def save_accounts():
    with open("accounts.txt", "w") as f:
        for user_name, password in accounts.items():
            f.write(f"{user_name}:{password}\n")  # Write each account as "username:password"

def load_accounts():
    try:
        with open("accounts.txt", "r") as f:
            for line in f:
                parts = line.strip().split(":")
                if len(parts) == 2:
                    user_name, password = parts
                    accounts[user_name] = password
                else:
                    print(f"Skipping malformed line: {line.strip()}")
    except FileNotFoundError:
        pass  # If the file doesn't exist yet, do nothing


# Function to save tasks to a file for the current user
def save_tasks():
    global current_user
    if current_user:  # Ensure there's a logged-in user
        with open(f"{current_user}_tasks.txt", "w") as f:
            for task_name, details in tasks.items():
                f.write(f"{task_name},{details['deadline']},{details['completed']},{details.get('completion_date', '')}\n")

# Function to load tasks from a file for the current user
def load_tasks():
    global current_user
    if current_user:
        try:
            with open(f"{current_user}_tasks.txt", "r") as f:
                global tasks
                tasks = {}  # Clear existing tasks
                for line in f:
                    parts = line.strip().split(",")
                    if len(parts) == 4:
                        task_name, deadline, completed, completion_date = parts
                        tasks[task_name] = {
                            "deadline": deadline,
                            "completed": completed == "True",
                            "completion_date": completion_date
                        }
                    else:
                        print(f"Skipping malformed line: {line}")  # Handle improperly formatted lines
            update_task_list()  # Update the displayed task list
        except FileNotFoundError:
            tasks = {}  # If no file exists, create an empty tasks dictionary

# Load account data at the start of the program
load_accounts()

# Initialize the main tkinter window
root = tk.Tk()
root.title("Time Management")  # Set the window title
root.configure(bg="#e3f2fd")  # Set background color

custom_font = ("Helvetica", 14)  # Custom font for UI elements

# Create the login frame (initial screen)
login_frame = tk.Frame(root, bg="#e3f2fd")  # Set background color
login_frame.pack()  # Display the login frame
login_frame.pack(fill='both', expand=True, padx=25, pady=20)

# Username label and entry field for the login form
username_label = tk.Label(login_frame, text='Username:', font=custom_font, bg="#e3f2fd")
username_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

username_entry = tk.Entry(login_frame, font=custom_font)
username_entry.grid(row=1, column=1, pady=5, padx=5)

# Password label and entry field for the login form
password_label = tk.Label(login_frame, text='Password:', font=custom_font, bg="#e3f2fd")
password_label.grid(row=2, column=0, pady=5, padx=5, sticky='w')

password_entry = tk.Entry(login_frame, show='*', font=custom_font)  # Hide password input with asterisks
password_entry.grid(row=2, column=1, pady=5, padx=5)

# Buttons for adding accounts and logging in
tk.Button(login_frame, text='Add Account', command=add_account, fg="white", bg="#28a745", font=custom_font).grid(row=5, column=0, columnspan=2, pady=5)
tk.Button(login_frame, text='Login', command=check_credentials, fg="white", bg="#007bff", font=custom_font).grid(row=3, column=0, columnspan=2, pady=10)

# Create the task management frame (displayed after login)
task_management_frame = tk.Frame(root, bg="#f0f8ff")  # Set a light blue background

# Function to add a new task to the task list
def add_task():
    task_name = task_name_entry.get()  # Get the entered task name
    task_deadline = task_deadline_entry.get_date().strftime('%Y-%m-%d')  # Get the selected deadline date
    if task_name and task_deadline:  # Ensure both task name and deadline are provided
        tasks[task_name] = {"deadline": task_deadline, "completed": False, "completion_date": ""}  # Add the task to the dictionary
        update_task_list()  # Update the task display
        save_tasks()  # Save the tasks to file
        task_name_entry.delete(0, tk.END)  # Clear the task name input field
        task_deadline_entry.set_date(datetime.today())  # Reset the date picker to today
        # Generate a recommendation for the task and show it to the user
        recommendation = get_recommendation(task_name)
        messagebox.showinfo("Success", f"Task '{task_name}' added with a deadline of {task_deadline}.\nRecommendation: {recommendation}")

# Function to mark a selected task as completed
def mark_task_completed():
    selected_task = task_listbox.curselection()  # Get the selected task from the listbox
    if selected_task:
        task_name = task_listbox.get(selected_task).split(' - ')[0]  # Extract the task name
        if tasks.get(task_name):  # Check if the task exists
            tasks[task_name]["completed"] = True  # Mark the task as completed
            tasks[task_name]["completion_date"] = datetime.today().strftime('%Y-%m-%d')  # Record the completion date
            update_task_list()  # Update the task display
            save_tasks()  # Save the updated tasks to file
            messagebox.showinfo("Success", f"Task '{task_name}' marked as completed.")
    else:
        # Show a warning if no task is selected
        messagebox.showwarning("Warning", "No task selected.")


# Function to delete a selected task (mark as deleted)
def delete_task():
    selected_task = task_listbox.curselection()  # Get the selected task from the listbox
    if selected_task:
        task_name = task_listbox.get(selected_task).split(' - ')[0]  # Extract the task name
        if task_name in tasks:
            tasks[task_name]["deleted"] = True  # Mark the task as deleted
            update_task_list()  # Update the task display
            save_tasks()  # Save the updated tasks to file
            messagebox.showinfo("Success", f"Task '{task_name}' marked as deleted.")
    else:
        # Show a warning if no task is selected
        messagebox.showwarning("Warning", "No task selected.")


def update_task_list():
    task_listbox.delete(0, tk.END)  # Clear the current task list display
    today = datetime.today()  # Get today's date
    sorted_tasks = sorted(tasks.items(), key=lambda x: datetime.strptime(x[1]['deadline'], '%Y-%m-%d'))
    
    for task, details in sorted_tasks:
        if details.get("deleted", False):  # Skip tasks that are marked as deleted
            continue

        deadline_date = datetime.strptime(details['deadline'], '%Y-%m-%d')  # Parse the deadline date
        days_remaining = (deadline_date - today).days  # Calculate the number of days remaining until the deadline
        status = "Completed" if details["completed"] else "Pending"  # Determine the task status
        
        # Check if the task is overdue
        if days_remaining < 0:
            display_text = f"{task} - Deadline: {details['deadline']} - The Mission Already Due! - Status: {status}"
        else:
            display_text = f"{task} - Deadline: {details['deadline']} ({days_remaining} days left) - Status: {status}"
        
        task_listbox.insert(tk.END, display_text)  # Add the task to the listbox for display


# Function to generate a weekly report based on completed tasks
def generate_weekly_report():
    today = datetime.today()
    start_date = today - timedelta(days=today.weekday())  # Start of the week (Monday)

    # Filter tasks completed this week, even if they are deleted
    completed_tasks = [
        task for task, details in tasks.items()
        if details['completed'] and datetime.strptime(details['completion_date'], '%Y-%m-%d') >= start_date
    ]

    # Filter overdue tasks completed this week
    overdue_tasks = [
        task for task, details in tasks.items()
        if details['completed'] and datetime.strptime(details['deadline'], '%Y-%m-%d') < datetime.strptime(details['completion_date'], '%Y-%m-%d')
    ]

    if completed_tasks:
        praise_message = "Great job! You were productive this week."
        if overdue_tasks:
            praise_message += f"\nYou completed {len(completed_tasks)} tasks, but some were overdue. Let's aim to complete tasks on time next week!"
        else:
            praise_message += f"\nYou completed {len(completed_tasks)} tasks this week, all on time! Keep up the excellent work!"
    else:
        praise_message = "You didn't complete any tasks this week. Let's try to tackle them next week!"

    messagebox.showinfo("Weekly Report", praise_message)


# Function to get a task suggestion based on a selected task name
def get_task_suggestion():
    selected_task = task_listbox.curselection()  # Get the selected task from the listbox
    if selected_task:
        task_name = task_listbox.get(selected_task).split(' - ')[0]  # Extract the task name
        recommendation = get_recommendation(task_name)  # Get a recommendation based on the task name
        messagebox.showinfo("Suggestion", f"Recommendation for '{task_name}':\n{recommendation}")
    else:
        # Show a warning if no task is selected
        messagebox.showwarning("Warning", "No task selected.")

# UI elements for the task management frame
task_management_frame_title = tk.Label(task_management_frame, text="Time Management", font=("Helvetica", 16, "bold"), bg="#f0f8ff", fg="#1f77b4")
task_management_frame_title.grid(row=0, column=0, columnspan=3, pady=10)

instruction_label = tk.Label(task_management_frame, text="Select a task to delete, mark as complete", 
                             font=("Helvetica", 10), bg="#f0f8ff", fg="gray")
instruction_label.grid(row=3, column=2, columnspan=3, pady=5)

task_name_label = tk.Label(task_management_frame, text='Task Name:', font=custom_font, bg="#f0f8ff")
task_name_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

task_name_entry = tk.Entry(task_management_frame, font=custom_font)
task_name_entry.grid(row=1, column=1, pady=5, padx=5)

task_deadline_label = tk.Label(task_management_frame, text='Task Deadline:', font=custom_font, bg="#f0f8ff")
task_deadline_label.grid(row=2, column=0, pady=5, padx=5, sticky='w')

task_deadline_entry = DateEntry(task_management_frame, date_pattern='y-mm-dd', font=custom_font)
task_deadline_entry.grid(row=2, column=1, pady=5, padx=5)

# Buttons for task management actions
button_frame = tk.Frame(task_management_frame, bg="#f0f8ff")
button_frame.grid(row=3, column=0, columnspan=2, pady=10)

add_task_button = tk.Button(button_frame, text='Add Task', command=add_task, fg="white", bg="#28a745", font=custom_font)
add_task_button.grid(row=0, column=0, padx=20)

suggestion_button = tk.Button(button_frame, text='Get Suggestion', command=get_task_suggestion, fg="white", bg="#007bff", font=custom_font)
suggestion_button.grid(row=0, column=3, padx=20)

mark_task_completed_button = tk.Button(button_frame, text='Mark Task as Completed', command=mark_task_completed, fg="white", bg="#ffc107", font=custom_font)
mark_task_completed_button.grid(row=0, column=1, padx=20)

delete_task_button = tk.Button(button_frame, text='Delete Task', command=delete_task, fg="white", bg="#dc3545", font=custom_font)
delete_task_button.grid(row=0, column=2, padx=20)

# Listbox to display tasks
task_listbox = tk.Listbox(task_management_frame, width=90, height=20, font=custom_font)
task_listbox.grid(row=4, column=0, columnspan=3, pady=10, padx=10)

# Button to generate the weekly report
tk.Button(task_management_frame, text="Weekly Report", width=15, command=generate_weekly_report, fg="white", bg="#007bff", font=custom_font).grid(row=5, column=0, columnspan=3, pady=5)

# Call the function to update the task list when the app starts
update_task_list()

# Start the main loop to run the application
root.mainloop()
