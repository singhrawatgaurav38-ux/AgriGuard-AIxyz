# ==============================================================================
# AgriGuard AI - Automated Empathy Map PDF Generator
# Usage: python generate_empathy_map.py
# Output: Empathy_Map.pdf
# ==============================================================================

from reportlab.lib.pagesizes import letter, landscape
from reportlab.lib import colors
from reportlab.platypus import (
    SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, HRFlowable
)
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle


def build_empathy_map_pdf(filename="Empathy_Map.pdf"):
    # Landscape orientation works best for grid layouts like Empathy Maps
    doc = SimpleDocTemplate(
        filename,
        pagesize=landscape(letter),
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()

    # Custom Color Palette
    PRIMARY = colors.HexColor('#1B4D3E')
    ACCENT = colors.HexColor('#2E7D32')
    BG_LIGHT = colors.HexColor('#F4F7F5')
    TEXT_DARK = colors.HexColor('#222222')

    # Typography Styles
    title_style = ParagraphStyle(
        'DocTitle',
        parent=styles['Heading1'],
        fontName='Helvetica-Bold',
        fontSize=20,
        leading=24,
        textColor=PRIMARY,
        spaceAfter=4
    )

    sub_style = ParagraphStyle(
        'SubTitle',
        parent=styles['Normal'],
        fontName='Helvetica',
        fontSize=10,
        leading=13,
        textColor=colors.HexColor('#555555')
    )

    box_header_style = ParagraphStyle(
        'BoxHeader',
        parent=styles['Heading2'],
        fontName='Helvetica-Bold',
        fontSize=12,
        leading=15,
        textColor=ACCENT,
        spaceAfter=6
    )

    body_style = ParagraphStyle(
        'BodyTextCustom',
        parent=styles['BodyText'],
        fontName='Helvetica',
        fontSize=9,
        leading=12,
        textColor=TEXT_DARK,
        spaceAfter=3
    )

    story = []

    # Title Banner
    story.append(Paragraph("AgriGuard AI — Farmer Empathy Map", title_style))
    story.append(Paragraph("Target Persona: Smallholder Farmer in India (Climate-Vulnerable Regional Agriculture)", sub_style))
    story.append(HRFlowable(width="100%", thickness=1.5, color=PRIMARY, spaceAfter=10))

    # Quadrant Content Definitions
    says_content = [
        Paragraph("<b>🗣️ SAYS</b>", box_header_style),
        Paragraph("• \"Mausam ka koi bharosa nahi hai, kab barish ho jaye.\"", body_style),
        Paragraph("• \"Mujhe kaise pata chalega ki kitni khad (NPK) dalni hai?\"", body_style),
        Paragraph("• \"English apps samajh nahi aate, Hindi ya bolkar batao.\"", body_style),
        Paragraph("• \"Kapas/Chawal ki fasal kaatne ka sahi samay kya hai?\"", body_style),
    ]

    thinks_content = [
        Paragraph("<b>🧠 THINKS</b>", box_header_style),
        Paragraph("• Will climate shifts destroy my yield this season?", body_style),
        Paragraph("• Can I trust AI advice over traditional farming practices?", body_style),
        Paragraph("• Will I be able to recover input costs and repay my loan?", body_style),
        Paragraph("• Is there a simpler way to get hyper-local district advice?", body_style),
    ]

    does_content = [
        Paragraph("<b>🎬 DOES</b>", box_header_style),
        Paragraph("• Relies on local seed sellers and neighbors for advice.", body_style),
        Paragraph("• Manually inspects soil and crop leaf condition.", body_style),
        Paragraph("• Uses basic WhatsApp / Voice assistance on smartphone.", body_style),
        Paragraph("• Visits local extension officers during crop damage.", body_style),
    ]

    feels_content = [
        Paragraph("<b>❤️ FEELS</b>", box_header_style),
        Paragraph("• <b>Anxious:</b> Uncertain weather and fluctuating market prices.", body_style),
        Paragraph("• <b>Overwhelmed:</b> Complex technical agricultural jargon.", body_style),
        Paragraph("• <b>Hopeful:</b> Open to technological tools that boost income.", body_style),
        Paragraph("• <b>Vulnerable:</b> High financial risk on small land holdings.", body_style),
    ]

    pains_content = [
        Paragraph("<b>⚠️ PAINS</b>", box_header_style),
        Paragraph("• Severe yield loss due to sudden droughts/floods.", body_style),
        Paragraph("• Soil degradation from unbalanced fertilizer usage.", body_style),
        Paragraph("• Language barrier in modern digital farming platforms.", body_style),
    ]

    gains_content = [
        Paragraph("<b>🎯 GAINS</b>", box_header_style),
        Paragraph("• Instant 1-minute voice advisories in local regional languages.", body_style),
        Paragraph("• Accurate NPK soil dosage recommendations to save costs.", body_style),
        Paragraph("• Early extreme weather warnings & optimal harvesting dates.", body_style),
    ]

    # Top 2x2 Grid (Says, Thinks, Does, Feels)
    grid_top_data = [
        [says_content, thinks_content],
        [does_content, feels_content]
    ]

    grid_top_table = Table(grid_top_data, colWidths=[386, 386])
    grid_top_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, -1), BG_LIGHT),
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))

    story.append(grid_top_table)
    story.append(Spacer(1, 10))

    # Bottom 1x2 Grid (Pains & Gains)
    grid_bottom_data = [
        [pains_content, gains_content]
    ]

    grid_bottom_table = Table(grid_bottom_data, colWidths=[386, 386])
    grid_bottom_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (0, 0), colors.HexColor('#FFEBEE')),  # Soft Red for Pains
        ('BACKGROUND', (1, 0), (1, 0), colors.HexColor('#E8F5E9')),  # Soft Green for Gains
        ('GRID', (0, 0), (-1, -1), 1, colors.HexColor('#CCCCCC')),
        ('VALIGN', (0, 0), (-1, -1), 'TOP'),
        ('TOPPADDING', (0, 0), (-1, -1), 8),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 8),
        ('LEFTPADDING', (0, 0), (-1, -1), 10),
        ('RIGHTPADDING', (0, 0), (-1, -1), 10),
    ]))

    story.append(grid_bottom_table)

    # Build Document
    doc.build(story)
    print(f"Successfully generated Empathy Map PDF: {filename}")


if __name__ == "__main__":
    build_empathy_map_pdf()