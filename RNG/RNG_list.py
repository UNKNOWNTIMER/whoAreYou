#The seed_RNG_list is not directly used in the program; it primarily serves as a random seed in natural language.
import random
#Most countries answered by GPT (if your country is missing, it's not my fault ~ it's GPT's fault) are randomized for QA.
def random_country():
    countries = [
        "Afghanistan", "Albania", "Algeria", "Andorra", "Angola",
        "Antigua and Barbuda", "Argentina", "Armenia", "Australia", "Austria",
        "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados",
        "Belarus", "Belgium", "Belize", "Benin", "Bhutan",
        "Bolivia", "Bosnia and Herzegovina", "Botswana", "Brazil", "Brunei",
        "Bulgaria", "Burkina Faso", "Burundi", "Cape Verde", "Cambodia",
        "Cameroon", "Canada", "Central African Republic", "Chad", "Chile",
        "China", "Colombia", "Comoros", "Congo (DRC)", "Congo (Republic)",
        "Costa Rica", "Croatia", "Cuba", "Cyprus", "Czech Republic",
        "Denmark", "Djibouti", "Dominica", "Dominican Republic", "Ecuador",
        "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", "Estonia",
        "Eswatini", "Ethiopia", "Fiji", "Finland", "France",
        "Gabon", "Gambia", "Georgia", "Germany", "Ghana",
        "Greece", "Grenada", "Guatemala", "Guinea", "Guinea-Bissau",
        "Guyana", "Haiti", "Honduras", "Hungary", "Iceland",
        "India", "Indonesia", "Iran", "Iraq", "Ireland",
        "Israel", "Italy", "Jamaica", "Japan", "Jordan",
        "Kazakhstan", "Kenya", "Kiribati", "North Korea", "South Korea",
        "Kuwait", "Kyrgyzstan", "Laos", "Latvia", "Lebanon",
        "Lesotho", "Liberia", "Libya", "Liechtenstein", "Lithuania",
        "Luxembourg", "Madagascar", "Malawi", "Malaysia", "Maldives",
        "Mali", "Malta", "Marshall Islands", "Mauritania", "Mauritius",
        "Mexico", "Micronesia", "Moldova", "Monaco", "Mongolia",
        "Montenegro", "Morocco", "Mozambique", "Myanmar", "Namibia",
        "Nauru", "Nepal", "Netherlands", "New Zealand", "Nicaragua",
        "Niger", "Nigeria", "North Macedonia", "Norway", "Oman",
        "Pakistan", "Palau", "Panama", "Papua New Guinea", "Paraguay",
        "Peru", "Philippines", "Poland", "Portugal", "Qatar",
        "Romania", "Russia", "Rwanda", "Saint Kitts and Nevis", "Saint Lucia",
        "Saint Vincent and the Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia",
        "Senegal", "Serbia", "Seychelles", "Sierra Leone", "Singapore",
        "Slovakia", "Slovenia", "Solomon Islands", "Somalia", "South Africa",
        "South Sudan", "Spain", "Sri Lanka", "Sudan", "Suriname",
        "Sweden", "Switzerland", "Syria", "Tajikistan", "Tanzania",
        "Thailand", "Timor-Leste", "Togo", "Tonga", "Trinidad and Tobago",
        "Tunisia", "Turkey", "Turkmenistan", "Tuvalu", "Uganda",
        "Ukraine", "United Arab Emirates", "United Kingdom", "United States", "Uruguay",
        "Uzbekistan", "Vanuatu", "Vatican City", "Venezuela", "Vietnam",
        "Yemen", "Zambia", "Zimbabwe"
    ]  
    #  Randomly select a country and return it
    return random.choice(countries)
#Random game types used for QA randomization
def random_game():
    game_types = [
        "Action", "Adventure", "Role-playing", "Simulation",
        "Strategy", "Sports", "Casual", "Multiplayer Online",
        "Education", "Sandbox", "Horror", "Management", "Puzzle",
        "Music", "Racing", "Tactical", "Fighting", "Shooter",
        "Tower Defense", "Card", "Text-based", "Survival", "Historical",
        "Sci-fi", "Fantasy", "Supernatural", "Military", "Western",
        "Futuristic", "Exploration", "Open World", "Real-time Tactics", "Turn-based Strategy",
        "Massively Multiplayer Online", "Virtual Reality", "Augmented Reality", "Social", "Family",
        "Story-driven", "Visual Novel", "Interactive Story", "Sports",
        "Platformer", "Puzzle-solving", "Construction", "Political", "Economic Simulation",
        "Space Exploration", "Stealth", "Detective", "Dating", "Nurturing",
        "Adventure", "Deep Sea Exploration", "Flight Simulation", "Animal Simulation", "Farm Management",
        "Business Simulation", "City Building", "Racing", "Archery", "Bullfighting",
        "Jigsaw Puzzle", "Mystery", "Historical Reenactment", "Fairy Tale", "Mythology",
        "Post-apocalyptic Survival", "Spiritual Exploration", "Psychological Horror", "Otherworldly Exploration", "Time Travel",
        "Religion", "Philosophy", "Poetry", "Art", "Dream Crafting",
        "Hacking", "Cybersecurity", "Programming", "Mathematics", "Physics",
        "Chemistry", "Biology", "Astronomy", "Geography", "Environmental Science",
        "Health Education", "Sports Competition", "Olympics", "Chess", "Bridge",
        "E-sports", "Drone Racing", "Robotics Competition", "Escape Room", "Treasure Hunting"
    ]
    return random.choice(game_types)
#Random game elements used for QA randomization
def random_game_element():
    game_elements = [
        "Open World", "Resource Collection", "Quest System", "Character Customization", "Skill Tree",
        "Crafting System", "Combat System", "Puzzle Elements", "Multiple Endings", "Side Quests",
        "Interactive Dialogue", "Clan System", "Player Market", "Day-Night Cycle", "Seasonal Changes",
        "Dynamic Weather", "Real-time Combat", "Turn-based Combat", "Story Missions", "Exploration",
        "Equipment Upgrades", "Pet System", "Mount System", "Team Dungeons",
        "Solo Dungeons", "Arena", "Real-time PvP", "Trading System", "Farming",
        "Building", "Social Interaction", "Music Creation", "Dance Challenges", "Hidden Elements",
        "Secret Areas", "Achievement System", "Trophy Collection", "Reputation System", "Magic System",
        "Random Events", "World Boss", "Mini-games", "Gambling", "Economy",
        "Political System", "Family Feuds", "Multi-character Management", "Historical Clues", "Epic Quests",
        "Horror Elements", "Survival Challenges", "Shooting", "Fighting Techniques", "Stealth System",
        "Life Simulation", "Space Exploration", "Ocean Exploration", "Archaeological Excavation", "Hunting",
        "Fishing", "Cooking", "Disease System", "Poison Making", "Magic Potions",
        "Time Travel", "Space Manipulation", "Virtual Reality", "Augmented Reality", "NPC Companions",
        "Hostile NPCs", "Friendly NPCs", "Dynamic NPCs", "Destructible Environments", "Constructible Environments",
        "Physics Engine", "HD Graphics", "Pixel Art", "Hand-drawn Scenes", "3D Modeling",
        "Sound Design", "Background Music", "Voice Acting", "Narration", "Cinematic Cutscenes",
        "Retro Style", "Cyberpunk Style", "Fantasy Style", "Sci-fi Style", "Post-apocalyptic Style",
        "Historical Recreation", "Futuristic Setting", "Alternative Reality", "Spiritual Exploration", "Dream Scenarios",
        "Dystopian Setting", "Utopian Setting", "Superheroes", "Religious Elements", "Mythological Elements"
        "Portals", "Otherworld", "Alien Exploration", "Dark Fantasy", "Light Fantasy",
        "Robots", "Artificial Intelligence", "Time Reversal", "Role Switching", "Space Wars",
        "Martial Arts", "Detective", "Mystery", "Criminal Investigation", "Psychological", "City Life",
        "Rural Life", "Nature Exploration", "Pet Rearing", "Island Survival", "Tribal Conflict",
        "Civilization Development", "Interstellar Travel", "Black Technology", "Quantum Technology", "Disaster Survival",
        "Wormhole Exploration", "Dinosaur Era", "Virtual Building", "Wasteland Survival", "Time Management",
        "Dungeon Adventure", "Racing", "Running", "Ocean", "Text-based", "Global Exploration",
        "Space Colonization", "Plant Cultivation", "Virtual Government", "Folktales",
        "Telepathy", "Energy Management", "Mysticism", "Ancient Civilizations", "Underground Society",
        "Prairie Exploration", "Magic Academy", "Virtual Economy", "Psychological Warfare", "Otherworldly Portals",
        "Insect Invasion", "Tomb Raiding", "Ghost Ship", "Antique Restoration", "Underwater City",
        "Horse Racing", "Fashion Design", "Music Festival", "E-sports", "Military Strategy",
        "Tower Defense", "Wildlife Conservation", "Epic Battles", "Elven World", "Wizard School",
        "Secret Societies", "Ancient Temples", "Space Exploration", "Time Machine", "Superpowers",
        "Soul Transfer", "Alien Invasion", "Pirate Life", "Kingdom Building", "Treasure Hunting",
        "Dragon Legends", "Land of Giants", "Inner Earth Exploration", "Phantom City", "Ice Field Exploration",
        "Werewolf Legends", "Vampire Hunting", "Space Pirates", "Interstellar Alliance", "Ancient Behemoths",
        "Martial Arts Duels", "Ninja Training", "Demon Castle", "Angels and Demons", "Dimensional Passages",
        "Quantum Entanglement", "Cosmic Disasters", "Hyperspeed Travel", "Dystopian Society", "Futuristic City",
        "Racing Competition", "Wilderness Survival", "Virtual Travel", "Pet Competitions", "Zoo Management",
        "Period Dramas", "Time Interweaving", "Schizophrenia", "Hypnosis", "Neural Control"
        "Invisibility Technology", "Future Wars", "Drone Operation", "Potion Development", "Virus Outbreak",
        "Alien Civilizations", "Interstellar Wars", "Space Construction", "Parasitic Lifeforms", "Mechanical Evolution",
        "Supercomputing", "Cyber Detective", "Digital Avatar", "Virtual Idol", "Internet Celebrity Culture",
        "Techno-magic", "Unknown Adventure", "Secret Base", "Ruins Puzzle", "Time Fragments",
        "Dimensional Travel", "Primitive Tribes", "Lost Cities", "Spiritual World", "Dream Navigation",
        "Death Game", "Reality Fusion", "Post-apocalyptic Rebirth", "Netherworld", "Paranormal Events",
        "Maritime Exploration", "Space Exploration", "Alternate Dimension", "Metaverse Experience", "Ecological Simulation",
        "Historical Reenactment", "Technological Innovation", "Future Predictions", "Time Management", "Historical Adventure",
        "Virtual Travel", "Sky Cities", "Ancient Wars", "Traditional Crafts", "Cultural Heritage",
        "Earth Defense", "Alien Exploration", "Space Wars", "Future Exploration", "Virtual Building",
        "City Planning", "Astrophysics", "Quantum Physics", "Energy-saving Challenges", "Ecological Conservation",
        "Wildlife", "Underwater World", "Polar Exploration", "Extreme Sports", "Competitive Sports",
        "Historical Simulation", "Civilization Development", "Economic Simulation", "Political Strategy", "Cultural Studies",
        "Artificial Life", "Future Cities", "Epic Construction", "Explorer's Life", "Archaeological Mystery",
        "Animal Behavior", "Dynamic Ecosystems", "Religious Exploration", "Spiritual Exploration", "Philosophical Reflection",
        "Moral Conflict", "Literary Recreation", "Classic Culture", "Modern Art", "Virtual Music",
        "Singing and Dancing Performance", "Studio", "Interstellar Trade", "Resource Management", "Tech Tree",
        "Legend Recreation", "Hero Legends", "Mythical Reenactment", "Cosmic Mythology", "Post-apocalyptic Survival",
        "Paranormal Adventure", "Scientific Exploration", "Astronomical Exploration", "Natural Disasters", "Human History",
        "Retro Revival", "Renaissance", "Industrial Revolution", "Digital Revolution", "Information Age",
        "Cybersecurity", "Cyber Warfare", "Digital Currency", "Economic Crisis", "Global Politics",
        "Environmental Science", "Climate Change", "Global Warming", "Sustainable Development", "Bioengineering",
        "Gene Editing", "Biodiversity", "Wildlife Reserves", "Environmental Degradation", "Nature Conservation",
        "Transportation Revolution", "Space Exploration", "Robotics Revolution", "Artificial Intelligence", "Virtual Reality"
    ]
    return random.choice(game_elements)

def random_Experience():
    game_Experience = [
        "Experience", "Stories", "Anecdotes",
        "Culture", "Technology", "Education", "History", "Politics",
        "Economics", "Agriculture", "Military", "Religion", "Law",
        "Philosophy", "Art", "Music", "Theater", "Dance",
        "Art Exhibitions", "Sculpture", "Pottery", "Literature", "Poetry",
        "Novels", "Magazines", "News", "Media", "Movies",
        "Animation", "Comics", "Games", "Sports", "Travel",
        "Food", "Beverages", "Health", "Diseases", "Medicine",
        "Surgery", "Drugs", "Therapies", "Psychology", "Nursing",
        "Engineering", "Architecture", "Design", "Fashion", "Jewelry",
        "Makeup", "Beauty", "Hairdressing", "Tattoos", "Decoration",
        "Home", "Gardening", "Transportation", "Aviation", "Navigation",
        "Railways", "Highways", "Bridges", "Tunnels", "Building Materials",
        "Environmental Protection", "Resources", "Energy", "Water Conservancy", "Electricity",
        "Nuclear Energy", "Solar", "Wind Energy", "Biology", "Geography",
        "Meteorology", "Oceanography", "Geology", "Astronomy", "Exploration",
        "Adventure", "Extreme", "Rock Climbing", "Diving", "Skiing",
        "Market", "Trade", "Investment", "Stocks", "Bonds",
        "Banking", "Insurance", "Credit", "Leasing", "Taxation",
        "Audit", "Accounting", "Statistics", "Algorithms", "Programming",
        "Historical Fragments", "Personal Insights"
        "Life Tips", "Career Advice", "Travel Memories", "Food Experiences", "Reading Notes",
        "Entrepreneurial Experience", "Tech Discoveries", "Art Understanding", "Music Recommendations", "Movie Recommendations",
        "Health Tips", "Exercise Insights", "Study Methods", "Educational Insights", "Parenting Experience",
        "Plant and Animal Knowledge", "Environmental Awareness", "Psychological Reflections", "Philosophical Thoughts", "Religious Beliefs",
        "Political Views", "Economic Analysis", "Legal Knowledge", "Safety Education", "Programming Skills",
        "Math Problem Solving", "Physics Principles", "Chemistry Experiments", "Biological Phenomena", "Astronomical Observations",
        "Design Inspiration", "Architectural Features", "New Electronics", "Car Modifications", "Upcycling Projects",
        "Handicrafts", "Photography Works", "Travel Guides", "Holiday Activities", "Festive Customs",
        "Funny Incidents", "Childhood Memories", "Teenage Stories", "Love Stories", "Growth Experiences",
        "Friendship Moments", "Work Skills", "Management Strategies", "Teamwork", "Leadership Showcase",
        "Market Trends", "Trade Knowledge", "Investment Insights", "Financial Tips", "Consumer Warnings",
        "Real Estate Knowledge", "Renovation Experience", "Gardening Tips", "Cooking Secrets", "Culinary Culture",
        "Nutrition Planning", "Fitness Plans", "Stress Relief Methods", "Benefits of Early Sleep", "Herbal Applications",
        "Gaming Tips", "Esports Events", "Role-playing", "Puzzle-solving Skills", "Strategy Layouts",
        "Cybersecurity", "Software Applications", "Hardware Assembly", "Data Analysis", "Artificial Intelligence",
        "Machine Learning", "Blockchain Technology", "Cryptocurrency", "VR Experiences", "AR Applications",
        "3D Printing", "Drone Operation", "Remote Control", "Smart Home", "Wearable Devices",
        "Innovative Practices", "Literary Creation", "Script Writing", "Dance Performance", "Concert Experience",
        "Theater Reviews", "Poetry Analysis", "Art Exhibition Impressions", "Sculpting Techniques", "Pottery Craftsmanship",
        "Fashion Trends", "Makeup Tips", "Jewelry Design", "Hairstyle Creativity", "Clothing Matching",
        "Business Insights", "Venture Stories", "Brand Building", "Market Research", "User Experience",
        "Animation Production", "Comic Creation", "Game Design", "Special Effects Technology", "Sound Editing",
        "Video Editing", "TV Programs", "Documentaries", "Advertising Creativity", "News Reporting",
        "Online Education", "Remote Learning", "Language Learning", "Programming Tutorials", "Art Teaching",
        "Transportation", "Aviation Knowledge", "Maritime Technology", "Train Travel", "Driving Experience",
        "Animal Behavior", "Plant Cultivation", "Ecological Protection", "Climate Change", "Environmental Policies",
        "Health Seminars", "Disease Prevention", "Psychological Counseling", "Health Check-ups", "Drug Research",
        "Space Exploration", "Stellar Observation", "Physics Experiments", "Chemical Reactions", "Biological Evolution",
        "Math Puzzles", "Logical Thinking", "Philosophical Discussions", "Religious Beliefs", "Spiritual Practices",
        "Legal Cases", "Judicial Interpretations", "Policy Analysis", "International Relations", "Social Movements",
        "Instrument Playing", "Singing Techniques", "Composition Methods", "Music Theory", "Band Cooperation",
        "Sports Events", "Athletic Training", "Sports Policies", "Olympic Stories", "Extreme Sports",
        "Travel Guides", "Cultural Differences", "Local Customs", "Festive Celebrations", "World Heritage Sites",
        "Natural Wonders", "Mountain Exploration", "Desert Life", "Forest Immersion", "Beach Vacations",
        "Food Recommendations", "Cooking Classes", "Restaurant Reviews", "Eating Habits", "Special Dishes",
        "Foreign Language Communication", "Letter Writing", "Speech Skills", "Public Speaking", "Debate Competitions",
        "Poetry Recitation", "Novel Ideas", "Essays", "Children's Literature", "Science Fiction",
        "Detective Stories", "Horror and Suspense", "Love Stories", "Coming-of-age Novels", "Historical Biographies"
        ]
    #Randomly select a type and return it
    return random.choice(game_Experience)