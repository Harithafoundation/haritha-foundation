from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph,
    Spacer,
    Table,
    TableStyle
)


def create_receipt(donation, filename):

    doc = SimpleDocTemplate(
        filename,
        rightMargin=30,
        leftMargin=30,
        topMargin=30,
        bottomMargin=30
    )

    styles = getSampleStyleSheet()
    story = []

    # -----------------------------
    # HEADER
    # -----------------------------

    title_style = styles["Heading1"]
    title_style.alignment = TA_CENTER
    title_style.textColor = colors.darkgreen

    story.append(
        Paragraph("HARITHA FOUNDATION", title_style)
    )

    story.append(
        Paragraph(
            "Empowering Students Through Education, Skills & Career Opportunities",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Email : harithafoundation@gmail.com",
            styles["Normal"]
        )
    )

    story.append(
        Paragraph(
            "Website : www.harithafoundation.com",
            styles["Normal"]
        )
    )

    story.append(Spacer(1, 0.30 * inch))

    # -----------------------------
    # RECEIPT TITLE
    # -----------------------------

    receipt_table = Table(
        [["DONATION RECEIPT"]],
        colWidths=[520]
    )

    receipt_table.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, -1), colors.darkgreen),

        ("TEXTCOLOR", (0, 0), (-1, -1), colors.white),
        
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("ALIGN", (0, 0), (-1, -1), "CENTER"),

        ("FONTSIZE", (0, 0), (-1, -1), 18),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 10),

        ("TOPPADDING", (0, 0), (-1, -1), 10),

    ]))

    story.append(receipt_table)

    story.append(Spacer(1, 0.25 * inch))

    # -----------------------------
    # RECEIPT DETAILS
    # -----------------------------

    details = [

        ["Receipt No", f"HF-{donation.id:06d}"],

        ["Date", donation.donated_at.strftime("%d-%b-%Y")],

        ["Status", donation.payment_status],

    ]

    table = Table(details, colWidths=[150, 350])

    table.setStyle(TableStyle([

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E8F5E9")),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

    ]))

    story.append(table)

    story.append(Spacer(1, 0.30 * inch))

    # -----------------------------
    # DONOR DETAILS
    # -----------------------------

    story.append(
        Paragraph("<b>DONOR DETAILS</b>", styles["Heading2"])
    )

    donor = [

        ["Name", donation.name],

        ["Email", donation.email],

        ["Phone", donation.phone],

        ["Address", donation.address],

        ["PAN Number", donation.pan_number or "-"],

    ]

    donor_table = Table(donor, colWidths=[150, 350])

    donor_table.setStyle(TableStyle([

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("BACKGROUND", (0, 0), (0, -1), colors.beige),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

    ]))

    story.append(donor_table)

    story.append(Spacer(1, 0.30 * inch))

    # -----------------------------
    # DONATION DETAILS
    # -----------------------------

    story.append(
        Paragraph("<b>DONATION DETAILS</b>", styles["Heading2"])
    )

    donation_table = Table([

        ["Project", donation.project.title],

        ["Donation Amount", f"₹ {donation.amount}"],

        ["Payment ID", donation.payment_id],

        ["Order ID", donation.razorpay_order_id],

    ], colWidths=[150, 350])

    donation_table.setStyle(TableStyle([

        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),

        ("BACKGROUND", (0, 0), (0, -1), colors.HexColor("#E3F2FD")),

        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 8),

    ]))

    story.append(donation_table)

    story.append(Spacer(1, 0.35 * inch))

    # -----------------------------
    # THANK YOU
    # -----------------------------

    thanks = Table([[
        """<b>Thank You!</b><br/><br/>
        Thank you for your generous contribution to
        Haritha Foundation.

        Your support helps us provide education,
        skill development and career opportunities
        to students.

        We sincerely appreciate your kindness."""
    ]], colWidths=[520])

    thanks.setStyle(TableStyle([

        ("BACKGROUND", (0, 0), (-1, -1), colors.HexColor("#E8F5E9")),

        ("BOX", (0, 0), (-1, -1), 1, colors.green),

        ("TOPPADDING", (0, 0), (-1, -1), 15),

        ("BOTTOMPADDING", (0, 0), (-1, -1), 15),

    ]))

    story.append(thanks)

    story.append(Spacer(1, 0.40 * inch))

    # -----------------------------
    # FOOTER
    # -----------------------------

    footer = Paragraph(

        "<b>This is a computer-generated receipt. "
        "No signature is required.</b>",

        styles["Normal"]

    )

    story.append(footer)

    doc.build(story)