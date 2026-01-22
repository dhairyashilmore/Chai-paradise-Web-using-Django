# Chai Paradise 🍵

A beautiful, modern Django web application showcasing a collection of premium chai blends with stunning animations and responsive design.

![Django](https://img.shields.io/badge/Django-5.1.6-green)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![License](https://img.shields.io/badge/License-MIT-yellow)

## 🌟 Features

### Modern UI/UX
- **Glassmorphism Design**: Frosted glass effect with backdrop blur
- **Smooth Animations**: GPU-accelerated animations for seamless performance
- **Gradient Backgrounds**: Warm chai-themed color palette (rust, brown, terracotta)
- **Interactive Elements**: Hover effects with smooth transitions

### Animations & Effects
- ☕ **Animated Tea Cup**: Large floating background element
- 🍃 **Falling Tea Leaves**: Smooth wavy motion animation
- 💨 **Rising Steam**: Blurred steam wisps rising continuously
- 🔄 **Spinning Icon**: Rotating tea cup emoji on home page
- ✨ **Slide-up Animation**: Container entrance animation

### Chai Varieties
Display of 5 premium chai blends with:
- **Ingredient List**: Detailed components for each chai
- **Pricing**: All prices in Indian Rupees (₹)
- **Beautiful Cards**: Gradient backgrounds with hover effects

#### Available Chai Varieties:
1. **Masala Chai** - ₹289
2. **Ginger Chai** - ₹269
3. **Cardamom Chai** - ₹309
4. **Turmeric Chai** - ₹329
5. **Rose Chai** - ₹349

### Responsive Design
- 📱 **Mobile First**: Optimized for all screen sizes
- 💻 **Tablet**: Perfect display on medium screens
- 🖥️ **Desktop**: Full featured experience on large screens
- **Breakpoints**: 
  - Tablet: 768px and below
  - Mobile: 480px and below
  - Small Mobile: 360px and below

### Performance Optimizations
- GPU-accelerated animations using `translateZ(0)`
- `will-change` properties for optimized rendering
- Hardware acceleration hints (`backface-visibility`)
- Font smoothing for better text rendering
- Smooth scrolling behavior

## 📋 Project Structure

```
Chai-Paradise/
├── project1/                 # Main Django project
│   ├── settings.py          # Django settings
│   ├── urls.py              # URL configuration
│   ├── views.py             # Project views
│   ├── asgi.py              # ASGI config
│   └── wsgi.py              # WSGI config
├── chai/                     # Chai app
│   ├── views.py             # App views
│   ├── urls.py              # App URLs
│   ├── models.py            # Database models
│   ├── admin.py             # Admin configuration
│   └── templates/
│       └── chai/
│           └── all_chai.html # Chai varieties page
├── templates/               # Global templates
│   └── index.html          # Home page
├── static/                  # Static files
│   └── style.css           # Global styles
├── manage.py               # Django management script
├── db.sqlite3              # SQLite database
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- Django 5.1.6
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/dhairyashilmore/Chai-paradise-Web-using-Django.git
cd Chai-Paradise-Web-using-Django
```

2. **Create a virtual environment** (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install django
```

4. **Apply migrations**
```bash
python manage.py migrate
```

5. **Run the development server**
```bash
python manage.py runserver
```

6. **Access the application**
Open your browser and navigate to:
```
http://127.0.0.1:8000/
```

## 📖 Usage

### Home Page (`/`)
- Welcome page with animated tea cup and leaves
- Brief description of Chai Paradise
- Call-to-action button to explore chai varieties

### Chai Varieties Page (`/chai/`)
- Displays all available chai blends
- Shows ingredients for each chai
- Displays prices in Indian Rupees
- Beautiful card-based layout with hover effects
- Back button to return home

## 🎨 Design Highlights

### Color Palette
- **Primary**: #f39c12 (Gold/Orange)
- **Secondary**: #3498db (Sky Blue)
- **Accent**: #2ecc71 (Green - for prices)
- **Background**: Gradient from #4a2c1a to #2a1810 (Warm browns)

### Typography
- **Font Family**: Segoe UI, Tahoma, Geneva, Verdana, sans-serif
- **Heading Size**: 3em (desktop), responsive on mobile
- **Body Font Size**: 1.2em (desktop), responsive on mobile

### Animation Timings
- Float: 12s (tea cup), 14s (leaves)
- Steam Rise: 4-6s cycles
- Leaf Fall: 16-20s cycles
- Button Transitions: 0.3s cubic-bezier

## 📱 Responsive Breakpoints

### Desktop (1024px+)
- Full featured experience
- All animations visible
- Large font sizes and spacing

### Tablet (769px - 1024px)
- Reduced animation complexity
- Adjusted font sizes
- Optimized container sizes

### Mobile (481px - 768px)
- Touch-friendly button sizes
- Simplified animations
- Reduced component sizes
- Optimized spacing

### Small Mobile (≤ 480px)
- Ultra-compact layout
- Minimal animations
- Maximum readability
- Single column layout

## 🔧 Technologies Used

- **Backend**: Django 5.1.6
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite3
- **Styling**: CSS3 with Flexbox and Grid
- **Animations**: CSS Keyframes with GPU acceleration
- **Version Control**: Git & GitHub

## 🎯 Features Implemented

✅ Modern, responsive design
✅ Smooth animations and transitions
✅ Mobile-friendly interface
✅ Interactive hover effects
✅ Chai varieties with details
✅ Pricing in Indian Rupees
✅ GPU-accelerated performance
✅ Cross-browser compatible
✅ SEO-friendly HTML structure
✅ Accessible color contrasts

## 📝 Future Enhancements

- Add database models for chai varieties
- Implement add-to-cart functionality
- User authentication system
- Admin panel for managing chai inventory
- Shopping cart and checkout
- Payment integration
- Customer reviews and ratings
- Search and filter functionality
- Order management system

## 📄 License

This project is open source and available under the MIT License.

## 👤 Author

**Dhairyashil More**
- GitHub: [@dhairyashilmore](https://github.com/dhairyashilmore)
- Project: [Chai Paradise](https://github.com/dhairyashilmore/Chai-paradise-Web-using-Django)

## 🤝 Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📞 Support

For support, email or create an issue in the repository.

## 🙏 Acknowledgments

- Django community for the amazing framework
- Inspiration from modern web design trends
- Tea lovers everywhere! ☕

---

**Made with ❤️ and lots of tea** ☕🍵

*Last Updated: January 22, 2026*
