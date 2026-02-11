import qrcode
import os


upi_id = input("Enter your UPI ID: ").strip()
recipient_name = input("Enter Recipient Name: ").strip()
amount = input("Enter Transaction Limit Amount (in ₹): ").strip()
note = input("Enter Transaction Note: ").strip()


if not upi_id or not recipient_name or not amount:
    print("UPI ID, Recipient Name, and Amount cannot be empty.")
    exit()

try:
    float_amount = float(amount)
    if float_amount <= 0:
        raise ValueError
except ValueError:
    print("Invalid amount. Please enter a positive number.")
    exit()


formatted_amount = f"{float_amount:.2f}"


upi_url = (
    f"upi://pay?"
    f"pa={upi_id}&"  # Payee UPI ID
    f"pn={recipient_name.replace(' ', '%20')}&"  # Payee Name
    f"mc=1234&"  # Merchant code (can be dummy)
    f"am={formatted_amount}&"  # Amount
    f"cu=INR&"  # Currency
    f"tn={note.replace(' ', '%20')}"  # Transaction note
)


save_folder = "qr_codes"
os.makedirs(save_folder, exist_ok=True)


apps = {
    "PhonePe": "phonepe_qr.png",
    "Paytm": "paytm_qr.png",
    "GooglePay": "googlepay_qr.png"
}


for app_name, filename in apps.items():
    qr = qrcode.make(upi_url)
    filepath = os.path.join(save_folder, filename)
    qr.save(filepath)
    print(f"{app_name} QR saved at: {filepath}")
    qr.show()
    
    