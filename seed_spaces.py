import os
import django
import random
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont
from django.core.files.base import ContentFile

# === Configure Django settings module ===
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'event_mngt.settings')  # Change to your_project.settings
django.setup()

# Import the Space model
from venue.models import Space  # Change to the app label where Space is defined

# Sample data for dummy spaces
spaces_data = [
    {'name': 'Conference Room A', 'capacity': 20, 'location': 'First Floor'},
    {'name': 'Lecture Hall B',    'capacity': 100,'location': 'Building 3'},
    {'name': 'Meeting Room C',    'capacity': 12, 'location': 'Second Floor'},
    {'name': 'Outdoor Pavilion',  'capacity': 250,'location': 'Garden Area'},
    {'name': 'VIP Lounge',        'capacity': 30, 'location': 'Penthouse'},
]


def generate_placeholder_image(text, size=(800, 600), color=(200, 200, 200)):
    """
    Create a JPEG in-memory image with centered text.
    Returns a Django ContentFile suitable for ImageField.
    """
    img = Image.new('RGB', size, color)
    draw = ImageDraw.Draw(img)
    try:
        font = ImageFont.load_default()
        w, h = draw.textsize(text, font=font)
        pos = ((size[0] - w) // 2, (size[1] - h) // 2)
        draw.text(pos, text, fill=(0, 0, 0), font=font)
    except Exception:
        pass
    buffer = BytesIO()
    img.save(buffer, format='JPEG')
    buffer.seek(0)
    return ContentFile(buffer.read(), name=f"{text.replace(' ', '_')}.jpg")


def main():
    for data in spaces_data:
        space = Space.objects.create(
            name=data['name'],
            capacity=data['capacity'],
            location=data['location'],
            is_booked=False,
        )

        # Attach three placeholder images
        for idx in range(1, 4):
            img_cf = generate_placeholder_image(f"{data['name']} #{idx}")
            setattr(space, f'image{idx}', img_cf)

        space.save()
        print(f"⚙️ Created: {space}")


if __name__ == '__main__':
    main()
