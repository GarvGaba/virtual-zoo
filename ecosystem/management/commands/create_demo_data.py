from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from ecosystem.models import Ecosystem, Animal
from educational_sessions.models import EducationalSession, SessionResource, SessionComment, SessionQuiz
from datetime import datetime, timedelta
from django.utils import timezone
import requests
from io import BytesIO
from django.core.files.images import ImageFile
from django.core.files.base import ContentFile

User = get_user_model()


class Command(BaseCommand):
    help = 'Creates demo ecosystems and educational sessions with all features including images and videos'

    def download_image(self, url, filename):
        """Download image from URL"""
        try:
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(url, timeout=10, headers=headers, allow_redirects=True)
            if response.status_code == 200 and response.content:
                return ContentFile(response.content, name=filename)
        except Exception as e:
            self.stdout.write(self.style.WARNING(f'Could not download {url}: {str(e)}'))
        return None

    def handle(self, *args, **options):
        self.stdout.write('Creating demo data with images and videos...')
        
        # Get or create users
        admin_user, _ = User.objects.get_or_create(
            username='admin',
            defaults={'email': 'admin@virtualzoo.com', 'role': 'admin', 'is_staff': True, 'is_superuser': True}
        )
        admin_user.set_password('admin123')
        admin_user.save()
        
        teacher_user, _ = User.objects.get_or_create(
            username='teacher1',
            defaults={'email': 'teacher1@virtualzoo.com', 'role': 'teacher', 'first_name': 'Dr. Sarah', 'last_name': 'Johnson'}
        )
        teacher_user.set_password('teacher123')
        teacher_user.save()
        
        # Create 3 Demo Ecosystems with real image URLs (using direct Unsplash URLs)
        ecosystems_data = [
            {
                'name': 'Amazon Rainforest',
                'description': 'The Amazon Rainforest is the largest tropical rainforest in the world, covering much of the Amazon basin in South America. It is home to an incredible diversity of plant and animal species, many of which are found nowhere else on Earth.',
                'location': 'South America',
                'region': 'amazon',
                'era': 'present',
                'climate': 'Tropical',
                'temperature_min': 22,
                'temperature_max': 28,
                'vegetation': 'Dense tropical rainforest with thousands of tree species, epiphytes, and lianas. Canopy layers include emergent, canopy, understory, and forest floor.',
                'precipitation': '2000-3000 mm annually',
                'image_url': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            },
            {
                'name': 'Sahara Desert',
                'description': 'The Sahara is the largest hot desert in the world, covering most of North Africa. Despite its harsh conditions, it supports a unique ecosystem adapted to extreme heat and aridity.',
                'location': 'North Africa',
                'region': 'sahara',
                'era': 'present',
                'climate': 'Arid Desert',
                'temperature_min': 20,
                'temperature_max': 45,
                'vegetation': 'Sparse desert vegetation including acacia trees, date palms, and various drought-resistant shrubs. Oases support more diverse plant life.',
                'precipitation': 'Less than 100 mm annually',
                'image_url': 'https://images.unsplash.com/photo-1509316785289-025f5b846b35?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            },
            {
                'name': 'Arctic Tundra',
                'description': 'The Arctic Tundra is a cold, treeless biome found in the northernmost regions of the world. It features permafrost, short growing seasons, and unique cold-adapted wildlife.',
                'location': 'Arctic Circle',
                'region': 'arctic',
                'era': 'present',
                'climate': 'Polar',
                'temperature_min': -40,
                'temperature_max': 10,
                'vegetation': 'Low-growing plants including mosses, lichens, grasses, and dwarf shrubs. No trees due to permafrost and harsh conditions.',
                'precipitation': '150-250 mm annually (mostly snow)',
                'image_url': 'https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            },
        ]
        
        # Animal images from Unsplash/Pexels (using direct image URLs)
        # Using placeholder.com as fallback for reliable image serving
        animal_images = {
            'Jaguar': 'https://images.unsplash.com/photo-1605559424843-9e4c228bf1c2?w=800',
            'Green Anaconda': 'https://images.unsplash.com/photo-1578662996442-48f60103fc96?w=800',
            'Tyrannosaurus Rex': 'https://via.placeholder.com/800x600/4A5568/FFFFFF?text=Tyrannosaurus+Rex',
            'Dromedary Camel': 'https://images.unsplash.com/photo-1559827260-dc66d52bef19?w=800',
            'Fennec Fox': 'https://via.placeholder.com/800x600/F6AD55/FFFFFF?text=Fennec+Fox',
            'Spinosaurus': 'https://via.placeholder.com/800x600/4A5568/FFFFFF?text=Spinosaurus',
            'Polar Bear': 'https://images.unsplash.com/photo-1534567110283-9f0e41e1e9b1?w=800',
            'Arctic Fox': 'https://via.placeholder.com/800x600/E2E8F0/1A202C?text=Arctic+Fox',
            'Woolly Mammoth': 'https://via.placeholder.com/800x600/4A5568/FFFFFF?text=Woolly+Mammoth',
        }
        
        created_ecosystems = []
        for eco_data in ecosystems_data:
            image_url = eco_data.pop('image_url', None)
            # Use update_or_create to update existing ecosystems with new URLs
            ecosystem, created = Ecosystem.objects.update_or_create(
                name=eco_data['name'],
                defaults={
                    **eco_data,
                    'created_by': admin_user
                }
            )
            
            # Download and set image if URL provided
            if image_url and (created or not ecosystem.image):
                img_file = self.download_image(image_url, f"{ecosystem.name.lower().replace(' ', '_')}.jpg")
                if img_file:
                    ecosystem.image.save(f"{ecosystem.name.lower().replace(' ', '_')}.jpg", img_file, save=True)
            
            created_ecosystems.append(ecosystem)
            self.stdout.write(self.style.SUCCESS(f'Created/Updated ecosystem: {ecosystem.name}'))
        
        # Create animals for each ecosystem
        animals_data = {
            'Amazon Rainforest': [
                {'name': 'Jaguar', 'scientific_name': 'Panthera onca', 'species_type': 'existing', 'description': 'The largest cat in the Americas, known for its powerful build and spotted coat.', 'habitat': 'Dense rainforest', 'diet': 'Carnivore', 'conservation_status': 'Near Threatened'},
                {'name': 'Green Anaconda', 'scientific_name': 'Eunectes murinus', 'species_type': 'existing', 'description': 'The largest snake in the world by weight, found in Amazonian waters.', 'habitat': 'Swamps and rivers', 'diet': 'Carnivore', 'conservation_status': 'Least Concern'},
                {'name': 'Tyrannosaurus Rex', 'scientific_name': 'Tyrannosaurus rex', 'species_type': 'extinct', 'description': 'A large theropod dinosaur from the Late Cretaceous period.', 'habitat': 'Forests and plains', 'diet': 'Carnivore', 'conservation_status': 'Extinct'},
            ],
            'Sahara Desert': [
                {'name': 'Dromedary Camel', 'scientific_name': 'Camelus dromedarius', 'species_type': 'existing', 'description': 'One-humped camel perfectly adapted to desert life.', 'habitat': 'Desert', 'diet': 'Herbivore', 'conservation_status': 'Domesticated'},
                {'name': 'Fennec Fox', 'scientific_name': 'Vulpes zerda', 'species_type': 'existing', 'description': 'Smallest fox species with large ears for heat dissipation.', 'habitat': 'Sandy desert', 'diet': 'Omnivore', 'conservation_status': 'Least Concern'},
                {'name': 'Spinosaurus', 'scientific_name': 'Spinosaurus aegyptiacus', 'species_type': 'extinct', 'description': 'A large semi-aquatic dinosaur from the Cretaceous period.', 'habitat': 'Rivers and lakes', 'diet': 'Carnivore', 'conservation_status': 'Extinct'},
            ],
            'Arctic Tundra': [
                {'name': 'Polar Bear', 'scientific_name': 'Ursus maritimus', 'species_type': 'existing', 'description': 'Largest land carnivore, perfectly adapted to Arctic conditions.', 'habitat': 'Sea ice and tundra', 'diet': 'Carnivore', 'conservation_status': 'Vulnerable'},
                {'name': 'Arctic Fox', 'scientific_name': 'Vulpes lagopus', 'species_type': 'existing', 'description': 'Small fox with white winter coat for camouflage.', 'habitat': 'Tundra', 'diet': 'Omnivore', 'conservation_status': 'Least Concern'},
                {'name': 'Woolly Mammoth', 'scientific_name': 'Mammuthus primigenius', 'species_type': 'extinct', 'description': 'Large, hairy elephant relative that lived during the Ice Age.', 'habitat': 'Tundra and steppe', 'diet': 'Herbivore', 'conservation_status': 'Extinct'},
            ],
        }
        
        for ecosystem in created_ecosystems:
            for animal_data in animals_data.get(ecosystem.name, []):
                animal_name = animal_data['name']
                animal, created = Animal.objects.get_or_create(
                    ecosystem=ecosystem,
                    name=animal_name,
                    defaults=animal_data
                )
                
                # Download and set image if URL provided
                if animal_name in animal_images and (created or not animal.image):
                    img_file = self.download_image(animal_images[animal_name], f"{animal_name.lower().replace(' ', '_')}.jpg")
                    if img_file:
                        animal.image.save(f"{animal_name.lower().replace(' ', '_')}.jpg", img_file, save=True)
                        self.stdout.write(self.style.SUCCESS(f'  Downloaded image for {animal.name}'))
                    else:
                        self.stdout.write(self.style.WARNING(f'  Could not download image for {animal.name}'))
                
                if created:
                    self.stdout.write(self.style.SUCCESS(f'  Created animal: {animal.name}'))
        
        # Educational video URLs (using real educational YouTube videos)
        session_videos = {
            'Introduction to Amazon Rainforest Biodiversity': 'https://www.youtube.com/watch?v=3vijLre760w',  # Amazon rainforest documentary
            'Desert Adaptations Workshop': 'https://www.youtube.com/watch?v=wqbDSnIjWqE',  # Desert animals
            'Arctic Tundra Virtual Field Trip': 'https://www.youtube.com/watch?v=1MBWQzWXc-A',  # Arctic wildlife
        }
        
        # Session images (matching ecosystem images)
        session_images = {
            'Introduction to Amazon Rainforest Biodiversity': 'https://images.unsplash.com/photo-1441974231531-c6227db76b6e?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'Desert Adaptations Workshop': 'https://images.unsplash.com/photo-1509316785289-025f5b846b35?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
            'Arctic Tundra Virtual Field Trip': 'https://images.unsplash.com/photo-1518837695005-2083093ee35b?ixlib=rb-4.0.3&auto=format&fit=crop&w=1200&q=80',
        }
        
        # Create 3 Demo Educational Sessions
        sessions_data = [
            {
                'title': 'Introduction to Amazon Rainforest Biodiversity',
                'description': 'Explore the incredible diversity of life in the Amazon Rainforest. Learn about the complex ecosystems, unique species, and conservation challenges facing this vital biome.',
                'session_type': 'lecture',
                'scheduled_date': timezone.now() + timedelta(days=7),
                'duration_minutes': 60,
                'max_students': 30,
                'video_url': session_videos.get('Introduction to Amazon Rainforest Biodiversity', ''),
                'lesson_content': 'Key topics:\n1. Rainforest layers and structure\n2. Biodiversity hotspots\n3. Keystone species\n4. Conservation efforts\n5. Human impact',
            },
            {
                'title': 'Desert Adaptations Workshop',
                'description': 'Discover how plants and animals survive in one of the harshest environments on Earth. Interactive workshop on desert ecology and adaptation strategies.',
                'session_type': 'workshop',
                'scheduled_date': timezone.now() + timedelta(days=14),
                'duration_minutes': 90,
                'max_students': 20,
                'video_url': session_videos.get('Desert Adaptations Workshop', ''),
                'lesson_content': 'Workshop activities:\n1. Water conservation mechanisms\n2. Temperature regulation\n3. Nocturnal adaptations\n4. Plant survival strategies\n5. Hands-on demonstrations',
            },
            {
                'title': 'Arctic Tundra Virtual Field Trip',
                'description': 'Take a virtual journey to the Arctic Tundra. Experience the frozen landscape, meet its unique inhabitants, and understand the impacts of climate change.',
                'session_type': 'field_trip',
                'scheduled_date': timezone.now() + timedelta(days=21),
                'duration_minutes': 75,
                'max_students': 25,
                'video_url': session_videos.get('Arctic Tundra Virtual Field Trip', ''),
                'lesson_content': 'Field trip highlights:\n1. Permafrost and its importance\n2. Arctic wildlife encounters\n3. Seasonal changes\n4. Climate change effects\n5. Conservation initiatives',
            },
        ]
        
        created_sessions = []
        for i, session_data in enumerate(sessions_data):
            session_title = session_data['title']
            # Use update_or_create to update existing sessions with new URLs
            session, created = EducationalSession.objects.update_or_create(
                title=session_title,
                defaults={
                    **session_data,
                    'teacher': teacher_user,
                    'ecosystem': created_ecosystems[i] if i < len(created_ecosystems) else None
                }
            )
            
            # Download and set image if URL provided
            if session_title in session_images and (created or not session.image):
                img_file = self.download_image(session_images[session_title], f"{session_title.lower().replace(' ', '_')[:50]}.jpg")
                if img_file:
                    session.image.save(f"{session_title.lower().replace(' ', '_')[:50]}.jpg", img_file, save=True)
                    self.stdout.write(self.style.SUCCESS(f'  Downloaded image for {session.title}'))
                else:
                    self.stdout.write(self.style.WARNING(f'  Could not download image for {session.title}'))
            
            created_sessions.append(session)
            self.stdout.write(self.style.SUCCESS(f'Created/Updated session: {session.title}'))
            
            # Add quiz questions
            if i == 0:  # Amazon session
                SessionQuiz.objects.get_or_create(
                    session=session,
                    question='What percentage of the world\'s species are found in the Amazon?',
                    defaults={
                        'option_a': '5%',
                        'option_b': '10%',
                        'option_c': '20%',
                        'option_d': '30%',
                        'correct_answer': 'B',
                        'explanation': 'The Amazon contains approximately 10% of the world\'s known species.'
                    }
                )
            
            # Add sample comment
            if not SessionComment.objects.filter(session=session).exists():
                SessionComment.objects.create(
                    session=session,
                    user=teacher_user,
                    content='Looking forward to this session! Feel free to ask questions during the presentation.'
                )
        
        self.stdout.write(self.style.SUCCESS('\nDemo data created successfully!'))
        self.stdout.write(self.style.SUCCESS(f'Created {len(created_ecosystems)} ecosystems with images'))
        self.stdout.write(self.style.SUCCESS(f'Created {len(created_sessions)} educational sessions with videos'))
        self.stdout.write(self.style.SUCCESS('\nLogin credentials:'))
        self.stdout.write(self.style.SUCCESS('Admin: admin / admin123'))
        self.stdout.write(self.style.SUCCESS('Teacher: teacher1 / teacher123'))
        self.stdout.write(self.style.SUCCESS('\nNote: Images are downloaded from Unsplash.'))
