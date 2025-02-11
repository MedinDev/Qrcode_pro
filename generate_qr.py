import os
import qrcode
from PIL import Image

def generate_qr_with_logo(data, logo_path, output_path, qr_size=300, logo_size=60):
    """
    Generates a QR code with a logo in the center.

    :param data: The data to encode in the QR code (e.g., a URL or text).
    :param logo_path: Path to the logo image file.
    :param output_path: Path to save the final QR code image.
    :param qr_size: Size of the QR code image (width and height in pixels).
    :param logo_size: Size of the logo image (width and height in pixels).
    """
    # Generate the QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # High error correction
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    # Create an image from the QR code
    qr_img = qr.make_image(fill_color="black", back_color="white").convert('RGB')

    # Resize the QR code image
    qr_img = qr_img.resize((qr_size, qr_size), Image.LANCZOS)

    # Open the logo image
    logo_path = os.path.abspath(logo_path)  # Convert to absolute path
    logo = Image.open(logo_path)

    # Resize the logo
    logo = logo.resize((logo_size, logo_size), Image.LANCZOS)

    # Calculate the position to paste the logo
    logo_pos = ((qr_img.size[0] - logo.size[0]) // 2, (qr_img.size[1] - logo.size[1]) // 2)

    # Paste the logo onto the QR code
    # Ensure the logo has an alpha channel (transparency) for a clean overlay
    if logo.mode != 'RGBA':
        logo = logo.convert('RGBA')

    qr_img.paste(logo, logo_pos, logo)

    # Save the final image
    qr_img.save(output_path)

    print(f"QR code with logo saved to {output_path}")

# Example usage
data = "https://www.example.com"  # The data you want to encode in the QR code
logo_path = "/Users/mevradhy/PycharmProjects/Qrcode_pro/data/MNClogo.png"  # Path to your logo image
output_path = "qr_with_logo.png"  # Output file path

generate_qr_with_logo(data, logo_path, output_path)