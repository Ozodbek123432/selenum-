import subprocess
import re


def wifi_signal_strength():

    """O'z Wi-Fi signall kuchliligini o'lchash"""
    try:
        # Wi-Fi signallarni olish
        result = subprocess.run(['nmcli', '-f', 'SSID,SIGNAL', 'dev', 'wifi'],
                                capture_output=True, text=True)

        print("=== WI-FI SIGNAL KUCHLILIGI ===")
        for line in result.stdout.split('\n')[1:]:
            if line.strip():
                match = re.search(r'(\S+)\s+(\d+)%', line)
                if match:
                    ssid = match.group(1)
                    signal = int(match.group(2))

                    # Signal baholash
                    if signal >= 80:
                        status = "✅ A'lo"
                    elif signal >= 60:
                        status = "✅ Yaxshi"
                    elif signal >= 40:
                        status = "⚠️ O'rtacha"
                    else:
                        status = "❌ Zaif"

                    print(f"📶 {ssid}: {signal}% - {status}")

    except Exception as e:
        print(f"Xatolik: {e}")


wifi_signal_strength()