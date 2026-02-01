import streamlit as st
import random
import time
from datetime import datetime

# Page configuration
st.set_page_config(
    page_title="SA Tourism Guide",
    page_icon="🇿🇦",
    layout="wide"
)

# Custom CSS for South African theme
st.markdown("""
<style>
    .stChatMessage {
        padding: 1rem;
        border-radius: 15px;
        margin: 10px 0;
    }
    .user-message {
        background-color: #007749; /* Green from SA flag */
        color: white;
    }
    .assistant-message {
        background-color: #000000; /* Black from SA flag */
        color: #FFB81C; /* Gold from SA flag */
        border-left: 5px solid #DE3831; /* Red from SA flag */
    }
    .sa-theme {
        background: linear-gradient(135deg, #007749 0%, #000000 50%, #DE3831 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "user_name" not in st.session_state:
    st.session_state.user_name = ""
if "conversation_history" not in st.session_state:
    st.session_state.conversation_history = []

# South Africa tourism knowledge base
SA_KNOWLEDGE = {
    "destinations": {
        "cape town": {
            "description": "The Mother City, famous for Table Mountain, V&A Waterfront, and beautiful beaches.",
            "highlights": ["Table Mountain", "Robben Island", "Cape Winelands", "Kirstenbosch Garden"],
            "best_time": "October to April",
            "fun_fact": "Cape Town is where the Atlantic and Indian Oceans meet."
        },
        "johannesburg": {
            "description": "City of Gold, economic hub with rich history and vibrant culture.",
            "highlights": ["Apartheid Museum", "Soweto", "Constitution Hill", "Gold Reef City"],
            "best_time": "March to May, September to November",
            "fun_fact": "40% of world's gold has come from the Witwatersrand basin near Johannesburg."
        },
        "durban": {
            "description": "Warm coastal city with golden beaches and rich Indian influences.",
            "highlights": ["Golden Mile", "uShaka Marine World", "Victoria Street Market", "Durban Botanic Gardens"],
            "best_time": "Year-round",
            "fun_fact": "Durban has the largest Indian population outside of India."
        },
        "kruger park": {
            "description": "World-renowned safari destination with the Big Five.",
            "highlights": ["Game drives", "Safari walks", "Bird watching", "Wildlife photography"],
            "best_time": "May to September (dry season)",
            "fun_fact": "Kruger National Park is larger than Israel or Wales."
        }
    },
    "activities": {
        "safari": "Experience the Big Five (lion, leopard, rhino, elephant, buffalo) in national parks.",
        "wine tasting": "Visit Cape Winelands - Stellenbosch, Franschhoek, and Paarl regions.",
        "hiking": "Table Mountain trails, Drakensberg Mountains, or Garden Route hikes.",
        "cultural": "Visit Soweto, Robben Island, or traditional villages for cultural experiences.",
        "beach": "Enjoy Durban's warm waters or Cape Town's scenic beaches."
    },
    "cuisine": {
        "braai": "South African barbecue - a social institution",
        "bunny chow": "Durban's famous hollowed-out bread filled with curry",
        "bobotie": "Spiced minced meat baked with an egg-based topping",
        "biltong": "Dried, cured meat similar to jerky",
        "malva pudding": "Sweet, sticky dessert of Dutch origin"
    },
    "practical_info": {
        "currency": "South African Rand (ZAR)",
        "languages": "11 official languages including English, Zulu, Xhosa, Afrikaans",
        "visa": "Check requirements based on your nationality",
        "safety": "General precautions advised in cities, very safe in tourist areas",
        "transport": "Rental cars recommended for flexibility, Uber available in cities"
    }
}

def get_weather_recommendation():
    """Get season-appropriate recommendations"""
    month = datetime.now().month
    seasons = {
        "summer": [12, 1, 2],
        "autumn": [3, 4, 5],
        "winter": [6, 7, 8],
        "spring": [9, 10, 11]
    }
    
    for season, months in seasons.items():
        if month in months:
            return season
    return "summer"

def generate_sa_response(user_input):
    """Generate context-aware South Africa tourism responses"""
    user_input_lower = user_input.lower()
    response_options = []
    
    # Greetings
    if any(word in user_input_lower for word in ["hello", "hi", "hey", "greetings"]):
        greetings = [
            "Ke a leboga! (Thank you in Setswana) Welcome to South Africa Tourism Guide! 🇿🇦",
            "Molo! (Hello in Xhosa) Ready to explore the Rainbow Nation?",
            "Sawubona! (Hello in Zulu) How can I help you plan your South African adventure?"
        ]
        response_options.append(random.choice(greetings))
    
    # Destinations
    for destination in SA_KNOWLEDGE["destinations"]:
        if destination in user_input_lower:
            info = SA_KNOWLEDGE["destinations"][destination]
            response = f"**{destination.title()}** 🏙️\n\n"
            response += f"{info['description']}\n\n"
            response += f"**Top Highlights:** {', '.join(info['highlights'][:3])}\n"
            response += f"**Best Time to Visit:** {info['best_time']}\n"
            response += f"**Fun Fact:** {info['fun_fact']}"
            response_options.append(response)
    
    # Activities
    for activity in SA_KNOWLEDGE["activities"]:
        if activity in user_input_lower:
            response = f"**{activity.title()}** 🎯\n\n"
            response += SA_KNOWLEDGE["activities"][activity]
            
            # Add destination suggestions for activities
            if activity == "safari":
                response += "\n\n**Best Safari Parks:** Kruger National Park, Pilanesberg, Hluhluwe-iMfolozi"
            elif activity == "wine tasting":
                response += "\n\n**Top Wine Regions:** Stellenbosch, Franschhoek, Constantia"
            
            response_options.append(response)
    
    # Food
    for food in SA_KNOWLEDGE["cuisine"]:
        if food in user_input_lower:
            response = f"**{food.title()}** 🍴\n\n"
            response += SA_KNOWLEDGE["cuisine"][food]
            if food == "braai":
                response += "\n\n*Tip: No true South African braai is complete without pap (maize porridge)!*"
            response_options.append(response)
    
    # Practical info
    for info in SA_KNOWLEDGE["practical_info"]:
        if info in user_input_lower.replace(" ", "_"):
            response = f"**{info.replace('_', ' ').title()}** ℹ️\n\n"
            response += SA_KNOWLEDGE["practical_info"][info]
            response_options.append(response)
    
    # Budget questions
    if any(word in user_input_lower for word in ["budget", "cost", "expensive", "price", "money"]):
        responses = [
            "**Budget Tips:** 🇿🇦\n• Street food like bunny chow is affordable (~R50)\n• Mid-range hotels: R800-1500/night\n• Safari lodges: R2000+/night\n• Car rental: ~R300/day\n• National park entry: ~R400/person",
            "**Cost Guide:** 💰\nSouth Africa offers great value! Average daily budget:\n• Budget: R500-1000\n• Mid-range: R1000-2500\n• Luxury: R2500+",
        ]
        response_options.append(random.choice(responses))
    
    # Safety questions
    if any(word in user_input_lower for word in ["safe", "danger", "crime", "security"]):
        responses = [
            "**Safety Tips:** 🛡️\n• Use Uber/taxis at night\n• Don't display valuables\n• Stick to tourist areas\n• Ask locals for advice\n• Most tourist areas are very safe!",
            "**Travel Smart:** 🌟\nSouth Africa is generally safe for tourists with normal precautions. Game reserves and tourist areas have excellent security.",
        ]
        response_options.append(random.choice(responses))
    
    # Season-specific recommendations
    if any(word in user_input_lower for word in ["season", "weather", "when", "time to visit"]):
        season = get_weather_recommendation()
        season_tips = {
            "summer": "**Summer (Dec-Feb):** 🌞 Perfect for beaches in Durban and Cape Town, but book early!",
            "autumn": "**Autumn (Mar-May):** 🍂 Best for wine regions with mild weather and harvest festivals.",
            "winter": "**Winter (Jun-Aug):** ❄️ Ideal for safari (dry season) and whale watching in Hermanus.",
            "spring": "**Spring (Sep-Nov):** 🌸 Wildflowers in Namaqualand, perfect for hiking."
        }
        response_options.append(season_tips.get(season, "Year-round destination with regional variations!"))
    
    # Fallback responses
    if not response_options:
        fallbacks = [
            "I'm your South Africa travel expert! Ask me about:\n• Destinations (Cape Town, Johannesburg, safari parks)\n• Activities (safari, hiking, wine tasting)\n• Food (braai, bunny chow, biltong)\n• Practical info (visas, safety, budget)",
            "🇿🇦 Welcome to the Rainbow Nation! I can help with:\n- Best places to visit\n- Cultural experiences\n- Safari planning\n- Local cuisine tips\n- Travel logistics",
            "Need inspiration? Here are popular queries:\n\"What's the best safari park?\"\n\"Tell me about Cape Town\"\n\"South African food to try\"\n\"Budget for 2 weeks\"\n\"Is it safe to travel?\"",
        ]
        response_options.append(random.choice(fallbacks))
    
    return random.choice(response_options)

def response_generator(response_text):
    """Stream response word by word"""
    for word in response_text.split():
        yield word + " "
        time.sleep(0.03)

# Header with South African theme
st.markdown('<div class="sa-theme">', unsafe_allow_html=True)
st.title("🇿🇦 South Africa Tourism Guide")
st.markdown("Your personal travel assistant for exploring the Rainbow Nation!")
st.markdown('</div>', unsafe_allow_html=True)

# Sidebar with quick links
with st.sidebar:
    st.image("https://upload.wikimedia.org/wikipedia/commons/a/af/Flag_of_South_Africa.svg", width=150)
    st.subheader("Quick Info")
    
    if st.button("🏙️ Top Destinations"):
        st.session_state.messages.append({"role": "user", "content": "top destinations"})
        st.session_state.messages.append({"role": "assistant", "content": generate_sa_response("top destinations")})
        st.rerun()
    
    if st.button("🦁 Safari Tips"):
        st.session_state.messages.append({"role": "user", "content": "safari tips"})
        st.session_state.messages.append({"role": "assistant", "content": generate_sa_response("safari")})
        st.rerun()
    
    if st.button("🍴 Local Food"):
        st.session_state.messages.append({"role": "user", "content": "South African food"})
        st.session_state.messages.append({"role": "assistant", "content": generate_sa_response("braai bunny chow")})
        st.rerun()
    
    if st.button("💰 Budget Guide"):
        st.session_state.messages.append({"role": "user", "content": "budget for South Africa"})
        st.session_state.messages.append({"role": "assistant", "content": generate_sa_response("budget")})
        st.rerun()
    
    st.divider()
    
    # User info
    if not st.session_state.user_name:
        name = st.text_input("Your name (optional):")
        if name:
            st.session_state.user_name = name
            welcome_msg = f"Hallo {name}! Ready to explore South Africa?"
            st.session_state.messages.append({"role": "assistant", "content": welcome_msg})
            st.rerun()
    
    if st.session_state.user_name:
        st.write(f"👋 Welcome, {st.session_state.user_name}!")
    
    if st.button("Clear Chat History"):
        st.session_state.messages = []
        st.rerun()

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input(f"Ask about South Africa travel..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate and display assistant response
    with st.chat_message("assistant"):
        assistant_response = generate_sa_response(prompt)
        response = st.write_stream(response_generator(assistant_response))
    
    # Add to history
    st.session_state.messages.append({"role": "assistant", "content": assistant_response})

# Footer
st.divider()
col1, col2, col3 = st.columns(3)
with col1:
    st.caption("🌍 11 Official Languages")
with col2:
    st.caption("🦁 Home of the Big Five")
with col3:
    st.caption("🍷 World-Class Wine Regions")