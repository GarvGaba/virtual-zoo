"""
Script to generate PDF report using ReportLab
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Preformatted
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT, TA_CENTER
from reportlab.lib import colors
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import re

def clean_text(text):
    """Remove markdown formatting and clean text"""
    # Remove markdown headers
    text = re.sub(r'^#+\s+(.+)$', r'\1', text, flags=re.MULTILINE)
    # Remove bold/italic
    text = re.sub(r'\*\*(.+?)\*\*', r'\1', text)
    text = re.sub(r'\*(.+?)\*', r'\1', text)
    # Remove code blocks
    text = re.sub(r'```[\s\S]*?```', '', text)
    text = re.sub(r'`(.+?)`', r'\1', text)
    # Remove links
    text = re.sub(r'\[(.+?)\]\(.+?\)', r'\1', text)
    return text.strip()

def read_sections():
    """Read and parse the markdown report"""
    with open('PROJECT_REPORT.md', 'r', encoding='utf-8') as f:
        content = f.read()
    
    sections = []
    current_section = []
    current_title = ""
    
    lines = content.split('\n')
    for line in lines:
        # Detect headers
        if line.startswith('#'):
            if current_title:
                sections.append((current_title, '\n'.join(current_section)))
            current_title = line.strip('# ').strip()
            current_section = []
        else:
            current_section.append(line)
    
    if current_title:
        sections.append((current_title, '\n'.join(current_section)))
    
    return sections

def generate_pdf():
    """Generate PDF report"""
    doc = SimpleDocTemplate(
        "Virtual_Zoo_Project_Report.pdf",
        pagesize=A4,
        rightMargin=72,
        leftMargin=72,
        topMargin=72,
        bottomMargin=18
    )
    
    # Container for the 'Flowable' objects
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#000000'),
        spaceAfter=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    heading1_style = ParagraphStyle(
        'CustomHeading1',
        parent=styles['Heading1'],
        fontSize=14,
        textColor=colors.HexColor('#000000'),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    heading2_style = ParagraphStyle(
        'CustomHeading2',
        parent=styles['Heading2'],
        fontSize=12,
        textColor=colors.HexColor('#000000'),
        spaceAfter=8,
        spaceBefore=10,
        fontName='Helvetica-Bold'
    )
    
    heading3_style = ParagraphStyle(
        'CustomHeading3',
        parent=styles['Heading3'],
        fontSize=11,
        textColor=colors.HexColor('#000000'),
        spaceAfter=6,
        spaceBefore=8,
        fontName='Helvetica-Bold'
    )
    
    normal_style = ParagraphStyle(
        'CustomNormal',
        parent=styles['Normal'],
        fontSize=11,
        textColor=colors.HexColor('#000000'),
        spaceAfter=6,
        alignment=TA_JUSTIFY,
        leading=14
    )
    
    code_style = ParagraphStyle(
        'CodeStyle',
        parent=styles['Code'],
        fontSize=9,
        fontName='Courier',
        leftIndent=20,
        rightIndent=20,
        backColor=colors.HexColor('#f5f5f5'),
        borderColor=colors.HexColor('#cccccc'),
        borderWidth=1,
        borderPadding=5
    )
    
    # Title Page
    story.append(Spacer(1, 2*inch))
    story.append(Paragraph("Virtual Zoo", title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph("Immersive 3D Ecosystem Exploration Platform", 
                        ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=14, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("Project Report", 
                        ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=12, alignment=TA_CENTER)))
    story.append(Spacer(1, 0.2*inch))
    story.append(Paragraph("January 2025", 
                        ParagraphStyle('Subtitle', parent=styles['Normal'], fontSize=11, alignment=TA_CENTER)))
    story.append(PageBreak())
    
    # Table of Contents placeholder
    story.append(Paragraph("Table of Contents", heading1_style))
    story.append(Spacer(1, 0.2*inch))
    
    toc_items = [
        "1. INTRODUCTION",
        "2. GENERAL DESCRIPTION",
        "3. SPECIFIC REQUIREMENTS",
        "4. SCREENSHOTS OF WEBSITE",
        "5. SCREENSHOTS OF CODE",
        "6. SCREENSHOTS OF DATABASE SCHEMA",
        "7. PROJECT STRUCTURE AND DEPLOYMENT"
    ]
    
    for item in toc_items:
        story.append(Paragraph(item, normal_style))
        story.append(Spacer(1, 0.1*inch))
    
    story.append(PageBreak())
    
    # Read and process sections
    sections = read_sections()
    
    for title, content in sections:
        if not title or title.startswith('---'):
            continue
            
        # Add section title
        if title.startswith('##'):
            title = title.replace('##', '').strip()
            story.append(Paragraph(title, heading1_style))
        elif title.startswith('###'):
            title = title.replace('###', '').strip()
            story.append(Paragraph(title, heading2_style))
        else:
            story.append(Paragraph(title, heading1_style))
        
        # Process content
        paragraphs = content.split('\n\n')
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            # Check if it's code
            if para.startswith('```') or para.startswith('    '):
                # Code block
                para = re.sub(r'```\w*\n?', '', para)
                para = para.strip()
                story.append(Preformatted(para, code_style))
            elif para.startswith('- ') or para.startswith('* '):
                # List item
                para = para.replace('- ', '• ', 1).replace('* ', '• ', 1)
                story.append(Paragraph(para, normal_style))
            elif para.startswith('**') or para.startswith('#'):
                # Bold or header
                para = clean_text(para)
                if para.startswith('###'):
                    para = para.replace('###', '').strip()
                    story.append(Paragraph(para, heading3_style))
                elif para.startswith('##'):
                    para = para.replace('##', '').strip()
                    story.append(Paragraph(para, heading2_style))
                else:
                    story.append(Paragraph(para, normal_style))
            else:
                para = clean_text(para)
                if para:
                    story.append(Paragraph(para, normal_style))
            
            story.append(Spacer(1, 0.1*inch))
        
        story.append(Spacer(1, 0.2*inch))
    
    # Build PDF
    doc.build(story)
    print("PDF report generated successfully: Virtual_Zoo_Project_Report.pdf")

if __name__ == '__main__':
    try:
        generate_pdf()
    except Exception as e:
        print(f"Error generating PDF: {e}")
        print("Trying alternative method...")
        # Fallback: create HTML version
        with open('PROJECT_REPORT.md', 'r', encoding='utf-8') as f:
            content = f.read()
        
        html_content = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset="UTF-8">
            <title>Virtual Zoo Project Report</title>
            <style>
                body {{ font-family: Times New Roman, serif; margin: 2cm; }}
                h1 {{ font-size: 18pt; font-weight: bold; }}
                h2 {{ font-size: 14pt; font-weight: bold; }}
                h3 {{ font-size: 12pt; font-weight: bold; }}
                p {{ text-align: justify; line-height: 1.6; }}
                code {{ background: #f5f5f5; padding: 2px 4px; }}
                pre {{ background: #f5f5f5; padding: 10px; border-left: 3px solid #333; }}
            </style>
        </head>
        <body>
            <pre>{content}</pre>
        </body>
        </html>
        """
        
        with open('Virtual_Zoo_Project_Report.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("HTML version created: Virtual_Zoo_Project_Report.html")
        print("You can open this in a browser and print to PDF (Ctrl+P -> Save as PDF)")
