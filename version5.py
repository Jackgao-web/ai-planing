import tkinter as tk
import spacy
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from tkcalendar import Calendar
import datetime
import pytz
from tkinter import messagebox
import os


# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

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

def preprocess(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    return " ".join(tokens)

# Preprocess the keywords and prepare the vectorizer and tf-idf matrix
preprocessed_keywords = [preprocess(keyword) for keyword in keywords]
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(preprocessed_keywords)

def get_recommendation(keyword):
    keyword_processed = preprocess(keyword)
    user_tfidf = vectorizer.transform([keyword_processed])
    similarities = cosine_similarity(user_tfidf, tfidf_matrix)
    best_match_index = similarities.argmax()

    if similarities[0, best_match_index] > 0.2:  # Minimum threshold for similarity
        return recommendations[best_match_index]
    else:
        return "No recommendation found for this keyword."


# Dictionary to store accounts and passwords
accounts = {}
current_user = ""  # Keep track of the current logged-in user

def save_data():
    # Save the account data to a file named "accounts.txt"
    with open("accounts.txt", "w") as f:
        # Iterate over the dictionary items (user_name, password)
        for user_name, password in accounts.items():
            # Write each account entry as "user_name:password" followed by a newline character
            f.write(f"{user_name}:{password}\n")

def load_data():
    try:
        # Attempt to open the "accounts.txt" file for reading
        with open("accounts.txt", "r") as f:
            # Iterate over each line in the file
            for line in f:
                # Remove leading/trailing whitespaces and split the line into user_name and password
                user_name, password = line.strip().split(":")
                # Store the user_name and password in the accounts dictionary
                accounts[user_name] = password
    except FileNotFoundError:
        # If the file is not found, no accounts are loaded
        pass

load_data()

class LoginWindow:
    def __init__(self, root,calendar_app):
        self.root = root
        self.calendar_app = calendar_app
        self.login_window = tk.Toplevel(self.root)  # Create a Toplevel window for login
        self.login_window.title("Login")
        self.root.withdraw()

        self.title_label = tk.Label(self.login_window, text="Login Page", font=("Helvetica", 24, "bold"), bg="#e3f2fd")
        self.title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Create username and password fields with new color scheme
        self.login_window.configure(bg="#e3f2fd")  # Light blue background

        self.username_label = ttk.Label(self.login_window, text="Username:", background="#e3f2fd")
        self.username_label.grid(row=1, column=0, padx=(20, 10), pady=10, sticky="w")

        self.username_entry = ttk.Entry(self.login_window)
        self.username_entry.grid(row=1, column=1, padx=(10, 20), pady=10)

        self.password_label = ttk.Label(self.login_window, text="Password:", background="#e3f2fd")
        self.password_label.grid(row=2, column=0, padx=(20, 10), pady=10, sticky="w")

        self.password_entry = ttk.Entry(self.login_window, show='*')
        self.password_entry.grid(row=2, column=1, padx=(10, 20), pady=10)

        # Create login button
        self.login_button = tk.Button(self.login_window, text="Login", command=self.check_credentials, fg="white", bg="#007bff", font=("Helvetica", 12), padx=10, pady=5)
        self.login_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create sign up button
        self.signup_button = tk.Button(self.login_window, text="Sign Up", command=self.add_account, fg="white", bg="#28a745", font=("Helvetica", 12), padx=10, pady=5)
        self.signup_button.grid(row=5, column=0, columnspan=2, pady=10)

        # Show password checkbox
        self.show_password_var = tk.BooleanVar()
        self.show_password_check = tk.Checkbutton(self.login_window, text="Show Password", variable=self.show_password_var, command=self.toggle_password, background="#e3f2fd")
        self.show_password_check.grid(row=3, column=1, sticky='w')

        self.load_remembered_user()  # Corrected, no need to pass username

    def toggle_password(self):
        """Toggle the visibility of the password."""
        if self.show_password_var.get():
            self.password_entry.config(show='')  # Show password as plain text
        else:
            self.password_entry.config(show='*')  # Hide password as '*'

    def load_remembered_user(self):
        """Automatically load the last remembered username and password."""
        last_login_user = None
        accounts_data = {}

        try:
            with open("remembered_user.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():
                        user, pwd = line.strip().split(":")
                        if user == "last_login":
                            last_login_user = pwd  # The last logged-in user
                        else:
                            accounts_data[user] = pwd  # Read account info
        except FileNotFoundError:
            pass

        # If we found a last login user, fill in their credentials
        if last_login_user and last_login_user in accounts_data:
            self.username_entry.insert(0, last_login_user)
            self.password_entry.insert(0, accounts_data[last_login_user])


    def remember_user(self, username, password):
        """Always save the username and password as the last logged-in user."""
        accounts_data = {}

        # Read existing accounts
        try:
            with open("remembered_user.txt", "r") as f:
                lines = f.readlines()
                for line in lines:
                    if line.strip():
                        user, pwd = line.strip().split(":")
                        accounts_data[user] = pwd
        except FileNotFoundError:
            pass

        # Always update the current user info and mark as last_login
        accounts_data[username] = password  # Update the current user's password

        # Write all users back to the file, with the last logged-in user marked
        with open("remembered_user.txt", "w") as f:
            for user, pwd in accounts_data.items():
                f.write(f"{user}:{pwd}\n")
            f.write(f"last_login:{username}\n")  # Mark the last logged-in user

    def check_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if not username or not password:
            messagebox.showerror("Error", "Username or password cannot be empty!")
            return

        if username in accounts and accounts[username] == password:
            global current_user
            current_user = username
            self.remember_user(username, password)  # Always save the last logged-in user
            messagebox.showinfo("Success", "Login successful!")
            self.login_window.destroy()  # Hide the login window
            self.root.deiconify()
            self.calendar_app.main_frame.pack()
            self.calendar_app.show_calendar()
        else:
            messagebox.showerror("Error", "Invalid username or password!")

    def add_account(self):
        add_account()

def add_account():
    def add_account_inside():
        user_name = new_username_entry.get()
        password = new_password_entry.get()
        if not user_name or not password:
            messagebox.showerror("Error", "Username and password cannot be empty!")
        elif user_name in accounts:
            messagebox.showerror("Error", "Account already exists!")
        else:
            accounts[user_name] = password
            save_data()
            messagebox.showinfo("Success", "Account added successfully!")
            new_username_entry.delete(0, tk.END)
            new_password_entry.delete(0, tk.END)

            add_account_window.destroy()
            
    add_account_window = tk.Toplevel()
    add_account_window.title('New Account')
    add_account_window.configure(bg="#e3f2fd")  # Light blue background

    new_username_label = tk.Label(add_account_window, text='New Username:', font=('Helvetica', 12), bg="#e3f2fd")
    new_username_label.grid(row=0, column=0, pady=5, padx=5, sticky='w')

    new_username_entry = tk.Entry(add_account_window, font=('Helvetica', 12))
    new_username_entry.grid(row=0, column=1, pady=5, padx=5)

    new_password_label = tk.Label(add_account_window, text='New Password:', font=('Helvetica', 12), bg="#e3f2fd")
    new_password_label.grid(row=1, column=0, pady=5, padx=5, sticky='w')

    new_password_entry = tk.Entry(add_account_window, show='*', font=('Helvetica', 12))
    new_password_entry.grid(row=1, column=1, pady=5, padx=5)

    tk.Button(add_account_window, text='Add Account', font=('Helvetica', 12), fg="white", bg="#007bff", command=add_account_inside).grid(row=2, column=0, columnspan=2, pady=10)


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title('Weekly Calendar with Date and Time Selection')
        self.root.configure(bg="#e3f2fd")
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack_forget()

        
        # New Zealand timezone
        self.nz_timezone = pytz.timezone('Pacific/Auckland')

        self.selected_date = datetime.datetime.now(self.nz_timezone).date()

        self.title_label = tk.Label(self.root, text="MindfulTasks", font=("Helvetica", 24, "bold"), bg="#e3f2fd")
        self.title_label.pack(pady=20)


        # Store task data
        self.tasks = {}

        # Get today's date to highlight the current day
        self.current_date = datetime.datetime.now().date()

        # Create the date range label
        self.date_range_label = tk.Label(self.root, text="", font=("Helvetica", 14), bg="#e3f2fd")
        self.date_range_label.pack(pady=10)

        # Create a button to toggle the calendar dropdown
        self.date_button = tk.Button(self.root, text="Select Date Range", command=self.toggle_calendar, fg="white", bg="#007bff", font=("Helvetica", 14), padx=8, pady=8)
         # Configure the font and padding
        self.date_button.config(font=("Helvetica", 14), padx=8, pady=8)

        # Pack the button with padding
        self.date_button.pack(pady=15)

        # Initially, the calendar is hidden
        self.calendar_frame = None
        self.calendar = None

        # Create the time selection UI
        self.create_ui()
        self.update_date_range_label()

        self.exit_button = tk.Button(self.main_frame, text="Exit and Save", command=self.save_and_exit, fg="white", bg="#dc3545", font=("Helvetica", 14), padx=8, pady=8)
        self.exit_button.pack(pady=15)

    def show_calendar(self):
        """Show the main calendar window after login."""
        self.main_frame.pack(fill="both", expand=True)
        self.root.deiconify()  # Make sure the root window is visible
        self.load_tasks()

    def save_and_exit(self):
        """Save tasks to a file and exit the application."""
        self.save_tasks()  # Save the tasks
        self.root.quit()  # Exit the application

    def save_tasks(self):
        if current_user:
            filename = f"{current_user}_tasks.txt"
            with open(filename, "w") as file:
                for (day, hour), task in self.tasks.items():
                    # Save day, hour, start_time, end_time, task description, and project
                    start_time_str = task['start_time'].strftime('%H:%M')  # Convert to string
                    end_time_str = task['end_time'].strftime('%H:%M')      # Convert to string
                    file.write(f"{day},{hour},{start_time_str},{end_time_str},{task['description']},{task['project']}\n")

    def load_tasks(self):
        if current_user:
            filename = f"{current_user}_tasks.txt"
            if os.path.exists(filename):
                with open(filename, "r") as file:
                    for line in file:
                        # Unpack saved task information including the times
                        day, hour, start_time_str, end_time_str, description, project = line.strip().split(",")

                        # Convert the times from strings back to time objects
                        start_time = datetime.datetime.strptime(start_time_str, '%H:%M').time()
                        end_time = datetime.datetime.strptime(end_time_str, '%H:%M').time()

                        day = datetime.datetime.strptime(day, "%Y-%m-%d").date()
                        hour = int(hour)

                        # Store the task in the tasks dictionary
                        self.tasks[(day, hour)] = {
                            'description': description,
                            'project': project,
                            'start_time': start_time,
                            'end_time': end_time
                        }

                        # Display the task in the calendar
                        self.display_task(day, hour, description, project)


    def toggle_calendar(self):
        if self.calendar_frame:
            # Hide the calendar if it's visible
            self.calendar_frame.pack_forget()
            self.calendar_frame = None
            self.calendar = None
        else:
            # Show the calendar if it's not already visible
            self.calendar_frame = ttk.Frame(self.root)
            self.calendar_frame.pack(pady=10)

            self.calendar = Calendar(self.calendar_frame, selectmode="day", date_pattern="yyyy-mm-dd")
            self.calendar.pack(pady=10)
            self.calendar.bind("<<CalendarSelected>>", self.date_selected)


    def create_ui(self):
        # Create a frame for the header (days of the week) to keep it fixed
        self.header_frame = tk.Frame(self.root)
        self.header_frame.pack(side=tk.TOP, fill=tk.X)

        # Create a canvas for scrollable content
        self.canvas = tk.Canvas(self.root)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Create a vertical scrollbar linked to the canvas
        scrollbar = ttk.Scrollbar(self.root, orient="vertical", command=self.canvas.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Create a frame inside the canvas to hold the calendar grid
        self.calendar_frame_content = ttk.Frame(self.canvas)

        # Link the scrollbar to the canvas and set up scrolling
        self.canvas.create_window((0, 0), window=self.calendar_frame_content, anchor="nw")
        self.calendar_frame_content.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self.canvas.configure(yscrollcommand=scrollbar.set)

        # Bind the mouse wheel to the canvas for scrolling
        self.canvas.bind_all("<MouseWheel>", self.on_mouse_wheel)

        # Initial Calendar Grid Creation for the current week
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        self.create_calendar_grid()

    def update_date_range_label(self):
        """Updates the date range label to display the start and end of the current week."""
        monday = self.selected_date - datetime.timedelta(days=self.selected_date.weekday())
        sunday = monday + datetime.timedelta(days=6)
        self.date_range_label.config(text=f"{monday.strftime('%d/%m/%Y')} - {sunday.strftime('%d/%m/%Y')}")

    def create_calendar_grid(self):
        # Clear existing calendar grid
        for widget in self.calendar_frame_content.winfo_children():
            widget.destroy()

        # Create a style for today's highlight
        style = ttk.Style()
        style.configure("Highlight.TLabel", background="lightgreen")

        # Get the selected date and find the Monday of that week
        monday = self.selected_date - datetime.timedelta(days=self.selected_date.weekday())

        cell_height = 60  # Height of each cell
        time_slot_width = 16   # Width of the time slots
        day_width = 16  # Width of the day labels

        self.cells = {}  # Store all the cells in a dictionary for easy access

        # Create the first column (time slots)
        for hour in range(24):
            time_label = ttk.Label(self.calendar_frame_content, text=f'{hour:02}:00', width=time_slot_width, borderwidth=1, relief="solid")
            time_label.grid(row=hour+1, column=0, sticky='ewns', ipady=cell_height // 4)

        # Create the first row (days of the week) inside the header frame to freeze it
        empty_label = ttk.Label(self.header_frame, text='', width=time_slot_width, borderwidth=1, relief="solid")
        empty_label.grid(row=0, column=0, sticky='ewns')

        # Create grid cells and load tasks if they exist
        for i, day in enumerate(self.days):
            day_date = monday + datetime.timedelta(days=i)

            # Apply the highlight style if the day is today
            if day_date == self.current_date:
                day_label = ttk.Label(self.header_frame, text=f'{day}\n{day_date.strftime("%b %d")}', width=day_width, borderwidth=1, relief="solid", style="Highlight.TLabel")
            else:
                day_label = ttk.Label(self.header_frame, text=f'{day}\n{day_date.strftime("%b %d")}', width=day_width, borderwidth=1, relief="solid")

            day_label.grid(row=0, column=i+1, sticky='ewns', ipady=cell_height // 4)

            for hour in range(24):
                cell = tk.Label(self.calendar_frame_content, text='', borderwidth=1, relief="solid", bg="white", width=day_width)
                cell.grid(row=hour+1, column=i+1, sticky='ewns', ipady=cell_height // 4)
                self.cells[(day_date, hour)] = cell  # Use (day_date, hour) as key

                # Bind left click to each cell to show the time entry dialog
                cell.bind("<Button-1>", lambda e, d=day_date, h=hour: self.on_cell_click(d, h))

                # If a task exists for this date and hour, display it
                if (day_date, hour) in self.tasks:
                    task = self.tasks[(day_date, hour)]
                    self.display_task(day_date, hour, task['description'], task['project'])

    def display_task(self, day_date, start_hour, description, project):
        """Display the task on the calendar by merging cells."""
        task_info = self.tasks[(day_date, start_hour)]
        end_hour = task_info['end_time'].hour

        # Clear any previous cells in the range
        for h in range(start_hour, end_hour):
            self.cells[(day_date, h)].config(text='', bg="white")

        # Merge the cells to span across the hours from start to end
        first_cell = self.cells[(day_date, start_hour)]
        first_cell.config(text=f"{description}\n({project})", bg="lightblue")
        first_cell.grid(row=start_hour + 1, column=self.days.index(day_date.strftime('%A')) + 1, rowspan=end_hour - start_hour, sticky='ewns')

        # Hide the other cells in the range as we are merging them
        for h in range(start_hour + 1, end_hour):
            self.cells[(day_date, h)].grid_remove()

    def on_cell_click(self, day, hour):
        # Check if there is a task at this hour
        if (day, hour) in self.tasks:
            task_info = self.tasks[(day, hour)]
            self.edit_task(day, hour, task_info['description'], task_info['project'])
        else:
            # Show time entry dialog to create a new task
            self.show_time_entry_dialog(day, hour)


    def show_time_entry_dialog(self, day, hour):
        dialog = tk.Toplevel(self.root)
        dialog.title("Add time entry")

        # Start and end time fields
        start_time_str = f'{hour:02}:00'
        end_time_str = f'{(hour + 1) % 24:02}:00'

        start_time_entry = ttk.Entry(dialog)
        start_time_entry.insert(0, start_time_str)
        start_time_entry.grid(row=0, column=1, padx=10, pady=10)

        end_time_entry = ttk.Entry(dialog)
        end_time_entry.insert(0, end_time_str)
        end_time_entry.grid(row=0, column=2, padx=10, pady=10)

        # Description field
        description_label = ttk.Label(dialog, text="Description")
        description_label.grid(row=1, column=0, padx=10, pady=10)

        description_entry = tk.Text(dialog, height=3, width=30)
        description_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Recommendation field
        recommendation_label = ttk.Label(dialog, text="Recommendation:")
        recommendation_label.grid(row=2, column=0, padx=10, pady=10)

        recommendation_display = ttk.Label(dialog, text="", wraplength=200, background="lightgray")
        recommendation_display.grid(row=2, column=1, columnspan=3, padx=10, pady=10)

        # Update recommendation when description is entered
        def update_recommendation(event):
            description = description_entry.get("1.0", "end-1c").strip()
            if description:
                recommendation = get_recommendation(description)
                recommendation_display.config(text=recommendation)

        description_entry.bind("<KeyRelease>", update_recommendation)  # Update recommendation in real-time

        # Project dropdown
        project_label = ttk.Label(dialog, text="Project")
        project_label.grid(row=3, column=0, padx=10, pady=10)

        project_combobox = ttk.Combobox(dialog, values=["flagged", "Noted", "Critical"])
        project_combobox.grid(row=3, column=1, padx=10, pady=10)

        # Buttons for saving or canceling
        add_button = ttk.Button(dialog, text="Add", command=lambda: self.add_task(day, hour, description_entry.get("1.0", "end-1c"), project_combobox.get(), start_time_entry.get(), end_time_entry.get(), dialog))
        add_button.grid(row=4, column=2, padx=10, pady=10)

        cancel_button = ttk.Button(dialog, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=4, column=3, padx=10, pady=10)



    def add_task(self, day_date, hour, description, project, start_time_str, end_time_str, dialog):
        try:
            # Automatically append ':00' to input if it's just hours (e.g., 13 -> 13:00)
            if start_time_str.isdigit():
                start_time_str = f"{int(start_time_str):02}:00"
            if end_time_str.isdigit():
                end_time_str = f"{int(end_time_str):02}:00"

            # Convert the strings to time objects
            start_time = datetime.datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.datetime.strptime(end_time_str, '%H:%M').time()

        except ValueError:
            # If the input is not valid, show an error message
            messagebox.showerror("Invalid Input", "Please enter valid numeric time in the format HH:MM.")
            return

        # Ensure the end time is after the start time
        if end_time <= start_time:
            messagebox.showerror("Invalid Time", "End time must be after start time.")
            return

        # Calculate the start and end hours
        start_hour = start_time.hour
        end_hour = end_time.hour

        # Store the task in the tasks dictionary for each hour the task spans
        for h in range(start_hour, end_hour):
            self.tasks[(day_date, h)] = {
                'description': description,
                'project': project,
                'start_time': start_time,
                'end_time': end_time
            }

        # Now call the display_task method with all required parameters
        self.display_task(day_date, start_hour, description, project)

        # Close the dialog
        dialog.destroy()


    def update_task(self, day, description, project, start_time_str, end_time_str, dialog):
        try:
            # Convert the start and end time strings to time objects
            start_time = datetime.datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.datetime.strptime(end_time_str, '%H:%M').time()
        except ValueError:
            # If the input is invalid, show an error message
            messagebox.showerror("Invalid Input", "Please enter valid numeric time in the format HH:MM.")
            return

        # Calculate the start and end hours
        start_hour = start_time.hour
        end_hour = end_time.hour

        # Check that the end time is after the start time
        if end_time <= start_time:
            messagebox.showerror("Invalid Time", "End time must be after start time.")
            return

        # Reset any previous merged cells (remove old task display)
        for h in range(24):
            cell = self.cells[(day, h)]
            if not cell.winfo_ismapped():  # If a cell was previously hidden (due to row span)
                cell.grid()  # Show it again
            cell.config(text='', bg="white")  # Clear the content and reset the background

        # Convert day (which is a datetime.date object) to the weekday name (e.g., "Monday")
        day_name = day.strftime('%A')

        # Update the tasks dictionary with the new times
        for h in range(start_hour, end_hour):
            self.tasks[(day, h)] = {
                'description': description,
                'project': project,
                'start_time': start_time,
                'end_time': end_time
            }

        # Display the task by merging cells
        first_cell = self.cells[(day, start_hour)]
        first_cell.config(text=f"{description}\n({project})", bg="lightblue")
        first_cell.grid(row=start_hour + 1, column=self.days.index(day_name) + 1, rowspan=end_hour - start_hour, sticky='ewns')

        # Hide the cells between start_hour and end_hour since they are merged
        for h in range(start_hour + 1, end_hour):
            self.cells[(day, h)].grid_remove()

        # Close the dialog
        dialog.destroy()


    def delete_task(self, day, hour, dialog):
        # Get the task's start and end time
        start_time = self.tasks[(day, hour)]['start_time']
        end_time = self.tasks[(day, hour)]['end_time']

        # Calculate the range of hours the task spans
        start_hour = start_time.hour
        end_hour = end_time.hour

        # Remove the task and reset the cell state
        for h in range(start_hour, end_hour):
            del self.tasks[(day, h)]  # Delete from tasks dictionary
            cell = self.cells[(day, h)]
            cell.config(text='', bg="white")  # Clear the cell content and reset background
            cell.grid()  # Ensure all hidden cells are shown again

        # Close the dialog window
        dialog.destroy()

    def edit_task(self, day, hour, description, project):
        # Retrieve task info, including the end time
        task_info = self.tasks[(day, hour)]
        start_time = task_info['start_time']
        end_time = task_info['end_time']

        # Create a new Toplevel window for editing the existing task
        dialog = tk.Toplevel(self.root)
        dialog.title("Edit time entry")

        # Time and date section
        time_label = ttk.Label(dialog, text="Time and date")
        time_label.grid(row=0, column=0, padx=10, pady=10)

        # Display the correct start time (including minutes if necessary)
        start_time_str = start_time.strftime('%H:%M')
        end_time_str = end_time.strftime('%H:%M')

        # Create fields for editing the start and end time
        start_time_entry = ttk.Entry(dialog)
        start_time_entry.insert(0, start_time_str)  # Use the actual start time
        start_time_entry.grid(row=0, column=1, padx=10, pady=10)

        end_time_entry = ttk.Entry(dialog)
        end_time_entry.insert(0, end_time_str)  # Use the actual end time
        end_time_entry.grid(row=0, column=2, padx=10, pady=10)

        date_label = ttk.Label(dialog, text=day)
        date_label.grid(row=0, column=3, padx=10, pady=10)

        # Description
        description_label = ttk.Label(dialog, text="Description")
        description_label.grid(row=1, column=0, padx=10, pady=10)

        description_entry = tk.Text(dialog, height=3, width=30)
        description_entry.insert("1.0", description)
        description_entry.grid(row=1, column=1, columnspan=3, padx=10, pady=10)

        # Project dropdown
        project_label = ttk.Label(dialog, text="Project")
        project_label.grid(row=3, column=0, padx=10, pady=10)

        project_combobox = ttk.Combobox(dialog, values=["flagged", "Noted", "Critical"])
        project_combobox.set(project)
        project_combobox.grid(row=3, column=1, padx=10, pady=10)

        # Save and Cancel buttons
        save_button = ttk.Button(dialog, text="Save", command=lambda: self.update_task(
            day, hour, description_entry.get("1.0", "end-1c"),
            project_combobox.get(), start_time_entry.get(), end_time_entry.get(), dialog))
        save_button.grid(row=4, column=2, padx=10, pady=10)

        cancel_button = ttk.Button(dialog, text="Cancel", command=dialog.destroy)
        cancel_button.grid(row=4, column=3, padx=10, pady=10)

        # Recommendation field
        recommendation_label = ttk.Label(dialog, text="Recommendation:")
        recommendation_label.grid(row=2, column=0, padx=10, pady=10)

        recommendation_display = ttk.Label(dialog, text="", wraplength=200, background="lightgray")
        recommendation_display.grid(row=2, column=1, columnspan=3, padx=10, pady=10)


        def update_recommendation(event):
            description = description_entry.get("1.0", "end-1c").strip()
            if description:
                recommendation = get_recommendation(description)
                recommendation_display.config(text=recommendation)

        description_entry.bind("<KeyRelease>", update_recommendation)  # Update recommendation in real-time

        # Delete button
        delete_button = ttk.Button(dialog, text="Delete", command=lambda: self.delete_task(day, hour, dialog))
        delete_button.grid(row=4, column=0, padx=10, pady=10)


    def on_mouse_wheel(self, event):
        # Scroll the canvas using the mouse wheel
        self.canvas.yview_scroll(-1 * int(event.delta / 120), "units")

    def date_selected(self, event):
        # Update the selected date and refresh the calendar grid
        selected_date_str = self.calendar.get_date()
        self.selected_date = datetime.datetime.strptime(selected_date_str, "%Y-%m-%d").date()
        self.create_calendar_grid()
        self.update_date_range_label()

        # Hide the calendar after date is selected
        self.toggle_calendar()

def main():
    root = tk.Tk()
    root.geometry("1100x900")  # Set a larger window size
  # Create the calendar app but keep it hidden initially
    root.withdraw()
    calendar_app = CalendarApp(root)


    # Load login window first, pass the calendar app to it
    LoginWindow(root, calendar_app)
    root.mainloop()

if __name__ == "__main__":
    main()