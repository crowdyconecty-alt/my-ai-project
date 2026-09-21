import streamlit as st

st.set_page_config(page_title="TechCart | Better tech, simply", page_icon="✦", layout="wide")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;700&family=Space+Grotesk:wght@500;600;700&display=swap');
    :root { --ink:#17232d; --muted:#66727b; --cream:#f7f4ee; --lime:#d9f35b; --line:#dfe3dc; }
    .stApp { background:var(--cream); color:var(--ink); font-family:'DM Sans', sans-serif; }
    .block-container { max-width:1240px; padding:2rem 3rem 4rem; }
    h1,h2,h3 { font-family:'Space Grotesk', sans-serif !important; color:var(--ink) !important; letter-spacing:0 !important; }
    h1 { font-size:clamp(2.8rem, 6vw, 5.7rem) !important; line-height:.98 !important; }
    h2 { font-size:2.25rem !important; }
    p { color:var(--muted); }
    [data-testid='stHeader'] { background:transparent; }
    .brand { font:700 1.45rem 'Space Grotesk'; letter-spacing:-.04em; color:var(--ink); }
    .brand span { color:#82990c; }
    .eyebrow { color:#82990c; text-transform:uppercase; font-weight:700; letter-spacing:.14em; font-size:.75rem; }
    .hero { padding:4rem 0 3.5rem; border-bottom:1px solid var(--line); }
    .hero-copy { padding:1.5rem 0; }
    .hero-copy p { max-width:440px; font-size:1.1rem; line-height:1.65; }
    .hero-art { background:#e4e8db; min-height:390px; display:flex; align-items:center; justify-content:center; position:relative; overflow:hidden; border-radius:4px; }
    .hero-art:before { content:''; width:280px; height:280px; border-radius:50%; background:#cadf45; position:absolute; top:-80px; right:-45px; }
    .hero-device { font-size:9rem; position:relative; z-index:1; filter:drop-shadow(18px 25px 14px rgba(23,35,45,.18)); transform:rotate(-8deg); }
    .section { padding:3.5rem 0 1rem; }
    .category { border:1px solid var(--line); padding:1.3rem; min-height:120px; background:rgba(255,255,255,.32); }
    .category strong { display:block; font-family:'Space Grotesk'; font-size:1.05rem; margin-top:.8rem; }
    .category small { color:var(--muted); }
    .product { background:#fff; border:1px solid var(--line); padding:0 0 1.2rem; height:100%; }
    .product-img { background:#edf0e9; height:180px; display:flex; align-items:center; justify-content:center; font-size:5.5rem; }
    .product-info { padding:1rem 1.1rem 0; }
    .product-info h3 { font-size:1.1rem !important; margin:.15rem 0 .35rem; }
    .price { font-weight:700; font-size:1.05rem; color:var(--ink); }
    .tag { color:#82990c; text-transform:uppercase; font-size:.68rem; font-weight:700; letter-spacing:.1em; }
    .trust { background:#17232d; color:#fff; padding:1.4rem 1.6rem; margin:3rem 0 1rem; }
    .trust p, .trust strong { color:#fff; margin:0; }
    .trust strong { font-family:'Space Grotesk'; font-size:1.05rem; }
    .footer { border-top:1px solid var(--line); margin-top:4rem; padding-top:1.4rem; color:var(--muted); font-size:.9rem; }
    div.stButton > button { border-radius:0; border:1px solid var(--ink); background:var(--ink); color:white; padding:.65rem 1.2rem; font-weight:700; }
    div.stButton > button:hover { border-color:#82990c; background:#82990c; color:white; }
    </style>
    """,
    unsafe_allow_html=True,
)

PRODUCTS = [
    ("Nova Air Pro", "Audio", "PKR 36,900", "🎧", "Immersive sound, all day"),
    ("Orbit Desk Lamp", "Workspace", "PKR 18,500", "💡", "Light that thinks with you"),
    ("Keychron K2", "Workspace", "PKR 25,500", "⌨️", "Your daily driver, upgraded"),
    ("Pixel Buds Mini", "Audio", "PKR 13,900", "🎵", "Small case. Big presence."),
]

if "cart" not in st.session_state:
    st.session_state.cart = []

top_left, top_mid, top_right = st.columns([3, 4, 1])
with top_left:
    st.markdown("<div class='brand'>tech<span>cart</span> ✦</div>", unsafe_allow_html=True)
with top_mid:
    menu = st.radio("Navigate", ["Home", "Shop", "About"], horizontal=True, label_visibility="collapsed")
with top_right:
    st.markdown(f"<div style='text-align:right;padding-top:.5rem;font-weight:700'>Bag ({len(st.session_state.cart)})</div>", unsafe_allow_html=True)

if menu == "Home":
    left, right = st.columns([1, 1], gap="large")
    with left:
        st.markdown("<div class='hero-copy'><div class='eyebrow'>Curated tech for real life</div>", unsafe_allow_html=True)
        st.title("Good tech\nshould feel easy.")
        st.write("Thoughtful tools, beautiful objects, and everyday upgrades chosen to make your days work a little better.")
        if st.button("Explore the collection →"):
            st.session_state.shop_requested = True
        st.markdown("</div>", unsafe_allow_html=True)
    with right:
        st.markdown("<div class='hero-art'><div class='hero-device'>💻</div></div>", unsafe_allow_html=True)

    st.markdown("<div class='section'><div class='eyebrow'>Shop by mood</div><h2>Find your next favorite.</h2></div>", unsafe_allow_html=True)
    categories = [("◒", "Focus mode", "Desks & tools"), ("◉", "Good vibrations", "Audio & sound"), ("⌁", "On the move", "Portable tech"), ("✦", "Little luxuries", "Daily upgrades")]
    category_cols = st.columns(4)
    for column, (icon, name, detail) in zip(category_cols, categories):
        with column:
            st.markdown(f"<div class='category'><div style='font-size:1.8rem'>{icon}</div><strong>{name}</strong><small>{detail}</small></div>", unsafe_allow_html=True)
else:
    st.markdown("<div class='section'><div class='eyebrow'>The collection</div><h1>Useful things,\nbeautifully chosen.</h1></div>", unsafe_allow_html=True)
    if menu == "About":
        st.write("TechCart is an independent edit of technology that earns its place in your life. We look for thoughtful design, reliable performance, and products that stay useful beyond the unboxing.")
    else:
        st.write("A small, intentional selection for desks, commutes, and everything in between.")
        filter_value = st.selectbox("Browse", ["All products", "Audio", "Workspace"])
        visible_products = PRODUCTS if filter_value == "All products" else [product for product in PRODUCTS if product[1] == filter_value]
        for row_start in range(0, len(visible_products), 4):
            product_cols = st.columns(4)
            for column, product in zip(product_cols, visible_products[row_start:row_start + 4]):
                name, category, price, icon, description = product
                with column:
                    st.markdown(f"<div class='product'><div class='product-img'>{icon}</div><div class='product-info'><div class='tag'>{category}</div><h3>{name}</h3><p>{description}</p><span class='price'>{price}</span></div></div>", unsafe_allow_html=True)
                    if st.button("Add to bag", key=f"add_{name}"):
                        st.session_state.cart.append(name)
                        st.toast(f"{name} added to your bag")

st.markdown("<div class='trust'><div class='eyebrow' style='color:#d9f35b'>The TechCart promise</div></div>", unsafe_allow_html=True)
trust_cols = st.columns(3)
for column, title, detail in zip(trust_cols, ["Free delivery", "30-day returns", "Human support"], ["On every order over PKR 15,000", "No awkward questions", "Real people, real answers"]):
    with column:
        st.markdown(f"<div style='padding:0 .3rem 1rem'><strong>{title}</strong><p>{detail}</p></div>", unsafe_allow_html=True)

st.markdown("<div class='footer'>© 2026 TechCart <span style='float:right'>Made for better everyday moments.</span></div>", unsafe_allow_html=True)


