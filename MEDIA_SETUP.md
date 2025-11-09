# Media Files Setup Guide

## Images and Videos Integration

The Virtual Zoo application now includes:

### 1. **Ecosystem Images**
- Downloaded from Unsplash (free stock photos)
- High-quality images for each ecosystem
- Automatically downloaded when running `create_demo_data` command

### 2. **Animal Images**
- Real animal photos from Unsplash
- Each animal has a representative image
- Images are downloaded and stored locally

### 3. **Educational Session Videos**
- YouTube video integration
- Real educational content videos
- Embedded video players with full controls

### 4. **3D Hologram Previews**
- Sketchfab 3D model integration
- Interactive 3D model viewers
- Modal popups for immersive viewing
- Support for VR viewing

## How It Works

### Image Download
The `create_demo_data` management command automatically:
1. Downloads images from Unsplash URLs
2. Saves them to the `media/ecosystems/` and `media/animals/` directories
3. Associates them with the respective ecosystem/animal records

### Video Integration
- YouTube and Vimeo URLs are automatically detected
- Video IDs are extracted and embedded
- Responsive video players with 16:9 aspect ratio

### 3D Holograms
- Sketchfab model URLs are detected
- Interactive iframe embeds for 3D viewing
- Modal popups for full-screen viewing
- VR support enabled

## Running the Demo Data Command

```bash
python manage.py create_demo_data
```

This will:
- Create 3 ecosystems with images
- Create 9 animals with images
- Create 3 educational sessions with videos
- Set up 3D hologram previews
- Add quiz questions and comments

## Image Sources

All images are from **Unsplash** (free, high-quality stock photos):
- Ecosystem images: Landscape and nature photography
- Animal images: Wildlife photography
- All images are properly licensed for use

## Video Sources

Educational videos from **YouTube**:
- Real educational content
- Documentaries and nature videos
- Properly embedded with YouTube's embed API

## 3D Model Sources

3D holograms use **Sketchfab**:
- Free 3D model viewer
- Interactive 3D models
- VR support
- Note: Actual model IDs need to be replaced with real Sketchfab model IDs

## Customization

To add your own images:
1. Update the `image_url` in `create_demo_data.py`
2. Or upload directly through the admin panel
3. Images will be automatically processed by Django

To add your own videos:
1. Update the `video_url` in the session creation
2. Supports YouTube and Vimeo URLs
3. Other video platforms can be added by extending the template

To add your own 3D models:
1. Upload to Sketchfab or another 3D hosting service
2. Update the `hologram_preview` URL
3. The template will automatically detect and embed it

## Troubleshooting

If images don't download:
- Check internet connection
- Verify Unsplash URLs are accessible
- Check Django media settings
- Ensure `media/` directory exists and is writable

If videos don't play:
- Verify YouTube/Vimeo URLs are correct
- Check if videos are set to "Public" or "Unlisted"
- Ensure JavaScript is enabled in browser

If 3D models don't load:
- Verify Sketchfab model IDs are correct
- Check if models are set to "Public"
- Ensure iframe embedding is allowed

