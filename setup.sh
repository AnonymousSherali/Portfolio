#!/bin/bash

# Portfolio Backend Setup Script
# Bu script backend ni avtomatik ravishda sozlaydi

echo "🚀 Portfolio Backend Setup Starting..."
echo ""

# Virtual environment mavjudligini tekshirish
if [ ! -d "venv" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv venv
else
    echo "✅ Virtual environment already exists"
fi

# Virtual environment ni faollashtirish
echo "🔧 Activating virtual environment..."
source venv/bin/activate

# Kerakli paketlarni o'rnatish
echo "📥 Installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt

# Database migrations
echo "🗄️  Running database migrations..."
python manage.py makemigrations
python manage.py migrate

# Media va static directories yaratish
echo "📁 Creating media directories..."
mkdir -p media/profile media/services media/projects media/testimonials media/clients media/blog

# Superuser yaratish (interaktiv)
echo ""
echo "👤 Create a superuser account for Django admin"
python manage.py createsuperuser

echo ""
echo "✨ Setup completed successfully!"
echo ""
echo "To start the development server:"
echo "  source venv/bin/activate"
echo "  python manage.py runserver"
echo ""
echo "Then visit:"
echo "  API: http://localhost:8000/api/"
echo "  Admin: http://localhost:8000/admin/"
echo ""
