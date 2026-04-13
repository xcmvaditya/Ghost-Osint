#!/usr/bin/env python3
"""
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     💀  DATA L34K3R - GHOST OSINT TOOL  💀                  ║
║                                                              ║
║     Termux OSINT Tool - By ADIX DEVELOPER                   ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""

import requests
import json
import os
import time
import sys

# ========== COLORS ==========
R = '\033[91m'
G = '\033[92m'
Y = '\033[93m'
B = '\033[94m'
C = '\033[96m'
W = '\033[97m'
Rs = '\033[0m'

def clear():
    os.system('clear')

def banner():
    print(f"""{C}
╔══════════════════════════════════════════════════════════════╗
║                                                              ║
║     {R}💀{C}  DATA L34K3R - GHOST OSINT TOOL  {R}💀{C}                    ║
║                                                              ║
║     {W}Termux OSINT Tool - By ADIX DEVELOPER{R}                  ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Rs}
""")

# ========== API FUNCTIONS ==========

def phone_lookup(number):
    """Phone number lookup"""
    try:
        url = f"https://ph-ng-pi.vercel.app/?number={number}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("success"):
                return data.get("fields", {})
        return None
    except Exception as e:
        return None

def pincode_lookup(pincode):
    """PIN code lookup"""
    try:
        url = f"https://pincode-ng.vercel.app/lookup?pincode={pincode}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("Status") == "Success":
                return data.get("PostOffice", [])
        return None
    except:
        return None

def ff_player_info(uid):
    """Free Fire player info"""
    try:
        url = f"https://ff-info-api-seven.vercel.app/accinfo?uid={uid}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def ff_guild_info(gid, region="IN"):
    """Free Fire guild info"""
    try:
        url = f"https://guild-info-danger.vercel.app/guild?guild_id={gid}&region={region}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def instagram_info(username):
    """Instagram user info"""
    try:
        url = f"https://kallu-insta-info-api.vercel.app/api/insta/{username}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def tiktok_info(username):
    """TikTok user info"""
    try:
        url = f"https://tiktok-api-mafia-ayan.vercel.app/tkinfo?username={username}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            if data.get("status"):
                return data
        return None
    except:
        return None

def youtube_info(channel):
    """YouTube channel info"""
    try:
        url = f"https://kallu-youtube-info-api.vercel.app/api/yt?channel={channel}"
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            return response.json()
        return None
    except:
        return None

def ai_chat(question):
    """AI chat"""
    try:
        url = f"https://text.pollinations.ai/{requests.utils.quote(question)}"
        response = requests.get(url, timeout=15)
        if response.status_code == 200:
            return response.text
        return "Error!"
    except:
        return "Network error!"

# ========== TOOL FUNCTIONS ==========

def tool_phone():
    clear()
    banner()
    print(f"{Y}[📱 PHONE NUMBER LOOKUP]{Rs}\n")
    
    phone = input(f"{G}[?]{W} Enter 10-digit number: {Rs}")
    
    if not phone.isdigit() or len(phone) != 10:
        print(f"{R}[!] Invalid number! Must be 10 digits.{Rs}")
        input(f"\n{Y}Press Enter...{Rs}")
        return
    
    print(f"\n{Y}[*] Searching dark web...{Rs}")
    time.sleep(1)
    
    data = phone_lookup(phone)
    
    if data:
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}📞 Number:{W} {phone}")
        print(f"{Y}🌍 Country:{W} {data.get('Country', 'N/A')}")
        print(f"{Y}📱 SIM:{W} {data.get('SIM card', 'N/A')}")
        print(f"{Y}🔌 Connection:{W} {data.get('Connection', ['N/A'])[0]}")
        print(f"{Y}📍 State:{W} {data.get('Mobile State', 'N/A')}")
        print(f"{Y}🏙️ City:{W} {data.get('Refrence City', 'N/A')}")
        print(f"{Y}👤 Owner:{W} {data.get('Owner Name', '🔒 Hidden')}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        # Save to file
        with open(f"leaked_phone_{phone}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_phone_{phone}.txt{Rs}")
    else:
        print(f"{R}[!] No data found for this number!{Rs}")
        print(f"{Y}[!] Try another number or API may be down.{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_pincode():
    clear()
    banner()
    print(f"{Y}[📍 PIN CODE LOOKUP]{Rs}\n")
    
    pincode = input(f"{G}[?]{W} Enter 6-digit PIN: {Rs}")
    
    if not pincode.isdigit() or len(pincode) != 6:
        print(f"{R}[!] Invalid PIN! Must be 6 digits.{Rs}")
        input(f"\n{Y}Press Enter...{Rs}")
        return
    
    print(f"\n{Y}[*] Searching database...{Rs}")
    time.sleep(1)
    
    data = pincode_lookup(pincode)
    
    if data:
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}📮 PIN Code:{W} {pincode}")
        print(f"{Y}📊 Total Offices:{W} {len(data)}")
        
        for i, office in enumerate(data[:3], 1):
            print(f"\n{Y}🏢 Office #{i}:{Rs}")
            print(f"   📛 Name: {office.get('Name', 'N/A')}")
            print(f"   📍 District: {office.get('District', 'N/A')}")
            print(f"   🗺️ State: {office.get('State', 'N/A')}")
            print(f"   📦 Delivery: {office.get('DeliveryStatus', 'N/A')}")
        
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        with open(f"leaked_pincode_{pincode}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_pincode_{pincode}.txt{Rs}")
    else:
        print(f"{R}[!] No data found for this PIN!{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_ff_player():
    clear()
    banner()
    print(f"{Y}[🎮 FREE FIRE PLAYER LEAK]{Rs}\n")
    
    uid = input(f"{G}[?]{W} Enter Player UID: {Rs}")
    
    if not uid.isdigit():
        print(f"{R}[!] Invalid UID!{Rs}")
        input(f"\n{Y}Press Enter...{Rs}")
        return
    
    print(f"\n{Y}[*] Fetching player data...{Rs}")
    time.sleep(1)
    
    data = ff_player_info(uid)
    
    if data and data.get("basicInfo"):
        basic = data["basicInfo"]
        social = data.get("socialInfo", {})
        clan = data.get("clanBasicInfo", {})
        
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}👤 Name:{W} {basic.get('nickname', 'N/A')}")
        print(f"{Y}🆔 UID:{W} {uid}")
        print(f"{Y}⭐ Level:{W} {basic.get('level', 'N/A')}")
        print(f"{Y}❤️ Likes:{W} {basic.get('liked', 'N/A')}")
        print(f"{Y}📝 Bio:{W} {social.get('socialHighlight', 'No bio')[:50]}")
        print(f"{Y}🏰 Guild:{W} {clan.get('clanName', 'No guild')}")
        print(f"{Y}📅 Created:{W} {basic.get('createAt', 'N/A')}")
        print(f"{Y}🕐 Last Login:{W} {basic.get('lastLoginAt', 'N/A')}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        with open(f"leaked_ff_{uid}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_ff_{uid}.txt{Rs}")
    else:
        print(f"{R}[!] Player not found!{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_ff_guild():
    clear()
    banner()
    print(f"{Y}[🏰 FREE FIRE GUILD LEAK]{Rs}\n")
    
    gid = input(f"{G}[?]{W} Enter Guild ID: {Rs}")
    region = input(f"{G}[?]{W} Region (IN/BD/ID) [IN]: {Rs}").upper() or "IN"
    
    print(f"\n{Y}[*] Fetching guild data...{Rs}")
    time.sleep(1)
    
    data = ff_guild_info(gid, region)
    
    if data and data.get("status") == "success":
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}📛 Name:{W} {data.get('guild_name', 'N/A')}")
        print(f"{Y}🆔 ID:{W} {gid}")
        print(f"{Y}⭐ Level:{W} {data.get('guild_level', 'N/A')}")
        print(f"{Y}👥 Members:{W} {data.get('current_members', 0)}/{data.get('max_members', 0)}")
        print(f"{Y}👑 Leader:{W} {data.get('guild_leader', {}).get('name', 'N/A')}")
        print(f"{Y}📊 Activity:{W} {data.get('total_activity_points', 0):,}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        with open(f"leaked_guild_{gid}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_guild_{gid}.txt{Rs}")
    else:
        print(f"{R}[!] Guild not found!{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_instagram():
    clear()
    banner()
    print(f"{Y}[📸 INSTAGRAM LEAK]{Rs}\n")
    
    username = input(f"{G}[?]{W} Enter Instagram username: {Rs}")
    
    print(f"\n{Y}[*] Fetching Instagram data...{Rs}")
    time.sleep(1)
    
    data = instagram_info(username)
    
    if data and data.get('full_name'):
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}👤 Name:{W} {data.get('full_name', 'N/A')}")
        print(f"{Y}📛 Username:{W} @{username}")
        print(f"{Y}👥 Followers:{W} {data.get('edge_followed_by', {}).get('count', 0):,}")
        print(f"{Y}👣 Following:{W} {data.get('edge_follow', {}).get('count', 0):,}")
        print(f"{Y}📷 Posts:{W} {data.get('edge_owner_to_timeline_media', {}).get('count', 0)}")
        print(f"{Y}🔒 Private:{W} {data.get('is_private', False)}")
        print(f"{Y}✅ Verified:{W} {data.get('is_verified', False)}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        with open(f"leaked_insta_{username}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_insta_{username}.txt{Rs}")
    else:
        print(f"{R}[!] User not found!{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_tiktok():
    clear()
    banner()
    print(f"{Y}[🎵 TIKTOK LEAK]{Rs}\n")
    
    username = input(f"{G}[?]{W} Enter TikTok username: {Rs}")
    
    print(f"\n{Y}[*] Fetching TikTok data...{Rs}")
    time.sleep(1)
    
    data = tiktok_info(username)
    
    if data:
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}👤 Name:{W} {data.get('name', 'N/A')}")
        print(f"{Y}📛 Username:{W} @{username}")
        print(f"{Y}👥 Followers:{W} {data.get('followers', 0):,}")
        print(f"{Y}👣 Following:{W} {data.get('following', 0):,}")
        print(f"{Y}❤️ Likes:{W} {data.get('hearts', 0):,}")
        print(f"{Y}📹 Videos:{W} {data.get('videos', 0)}")
        print(f"{Y}📝 Bio:{W} {data.get('signature', 'No bio')[:50]}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        with open(f"leaked_tiktok_{username}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_tiktok_{username}.txt{Rs}")
    else:
        print(f"{R}[!] User not found!{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_youtube():
    clear()
    banner()
    print(f"{Y}[▶️ YOUTUBE LEAK]{Rs}\n")
    
    channel = input(f"{G}[?]{W} Enter YouTube channel: {Rs}")
    
    print(f"\n{Y}[*] Fetching YouTube data...{Rs}")
    time.sleep(1)
    
    data = youtube_info(channel)
    
    if data and data.get('channel_name'):
        print(f"\n{G}[+] DATA LEAKED!{Rs}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        print(f"{Y}📛 Channel:{W} {data.get('channel_name', 'N/A')}")
        print(f"{Y}👥 Subscribers:{W} {data.get('subscribers', 0):,}")
        print(f"{Y}👁️ Views:{W} {data.get('views', 0):,}")
        print(f"{Y}📹 Videos:{W} {data.get('videos', 0)}")
        print(f"{Y}🌍 Country:{W} {data.get('country', 'N/A')}")
        print(f"{Y}📅 Created:{W} {data.get('created_at', 'N/A')}")
        print(f"{C}════════════════════════════════════════════{Rs}")
        
        with open(f"leaked_youtube_{channel}.txt", "w") as f:
            json.dump(data, f, indent=2)
        print(f"\n{G}[✓] Saved to: leaked_youtube_{channel}.txt{Rs}")
    else:
        print(f"{R}[!] Channel not found!{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

def tool_ai():
    clear()
    banner()
    print(f"{Y}[🤖 AI CHAT - Ask Anything]{Rs}\n")
    print(f"{Y}[!] Type 'exit' to go back{Rs}\n")
    
    while True:
        question = input(f"{G}[?]{W} You: {Rs}")
        
        if question.lower() == 'exit':
            break
        
        if not question.strip():
            continue
        
        print(f"{Y}[*] Thinking...{Rs}")
        answer = ai_chat(question)
        print(f"{C}[🤖 AI]:{W} {answer}{Rs}\n")

def tool_multi():
    clear()
    banner()
    print(f"{Y}[💀 MASS DATA LEAK]{Rs}\n")
    
    target = input(f"{G}[?]{W} Enter target (phone/UID/username): {Rs}")
    
    print(f"\n{Y}[*] Leaking from all databases...{Rs}\n")
    
    results = []
    
    # Phone
    if target.isdigit() and len(target) == 10:
        print(f"{Y}[1/4] Checking phone...{Rs}")
        phone_data = phone_lookup(target)
        if phone_data:
            results.append(f"📱 PHONE: {phone_data.get('Refrence City', 'N/A')}, {phone_data.get('Mobile State', 'N/A')}")
            print(f"{G}✓ Phone data found!{Rs}")
        else:
            print(f"{R}✗ No phone data{Rs}")
    
    # FF
    print(f"{Y}[2/4] Checking Free Fire...{Rs}")
    ff_data = ff_player_info(target)
    if ff_data and ff_data.get("basicInfo"):
        results.append(f"🎮 FF: {ff_data['basicInfo'].get('nickname', 'N/A')} (Level {ff_data['basicInfo'].get('level', 'N/A')})")
        print(f"{G}✓ FF data found!{Rs}")
    else:
        print(f"{R}✗ No FF data{Rs}")
    
    # Instagram
    print(f"{Y}[3/4] Checking Instagram...{Rs}")
    insta_data = instagram_info(target)
    if insta_data and insta_data.get('full_name'):
        results.append(f"📸 IG: {insta_data.get('full_name', 'N/A')} ({insta_data.get('edge_followed_by', {}).get('count', 0)} followers)")
        print(f"{G}✓ Instagram data found!{Rs}")
    else:
        print(f"{R}✗ No Instagram data{Rs}")
    
    # TikTok
    print(f"{Y}[4/4] Checking TikTok...{Rs}")
    tt_data = tiktok_info(target)
    if tt_data:
        results.append(f"🎵 TT: {tt_data.get('name', 'N/A')} ({tt_data.get('followers', 0)} followers)")
        print(f"{G}✓ TikTok data found!{Rs}")
    else:
        print(f"{R}✗ No TikTok data{Rs}")
    
    print(f"\n{C}════════════════════════════════════════════{Rs}")
    
    if results:
        print(f"{G}[+] MASS LEAK COMPLETE!{Rs}")
        print(f"{Y}📊 Found {len(results)} result(s):{Rs}\n")
        for r in results:
            print(f"{W}• {r}{Rs}")
        
        with open(f"mass_leak_{target}.txt", "w") as f:
            f.write("\n".join(results))
        print(f"\n{G}[✓] Saved to: mass_leak_{target}.txt{Rs}")
    else:
        print(f"{R}[!] No information found for '{target}'{Rs}")
    
    input(f"\n{Y}Press Enter...{Rs}")

# ========== MAIN MENU ==========

def main():
    while True:
        clear()
        banner()
        print(f"""
{W}╔══════════════════════════════════════════════════════════════╗
║                      {C}💀 MAIN MENU 💀{W}                                ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║   {G}[1]{W}  📱 Phone Number Leak                               ║
║   {G}[2]{W}  📍 PIN Code Leak                                  ║
║   {G}[3]{W}  🎮 Free Fire Player Leak                          ║
║   {G}[4]{W}  🏰 Free Fire Guild Leak                           ║
║   {G}[5]{W}  📸 Instagram Leak                                 ║
║   {G}[6]{W}  🎵 TikTok Leak                                    ║
║   {G}[7]{W}  ▶️ YouTube Leak                                   ║
║   {G}[8]{W}  🤖 AI Chat                                        ║
║   {G}[9]{W}  💀 Mass Data Leak (All in One)                    ║
║   {G}[0]{W}  🚪 Exit                                           ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝{Rs}
""")
        
        choice = input(f"{G}[?]{W} Select option (0-9): {Rs}")
        
        if choice == "1":
            tool_phone()
        elif choice == "2":
            tool_pincode()
        elif choice == "3":
            tool_ff_player()
        elif choice == "4":
            tool_ff_guild()
        elif choice == "5":
            tool_instagram()
        elif choice == "6":
            tool_tiktok()
        elif choice == "7":
            tool_youtube()
        elif choice == "8":
            tool_ai()
        elif choice == "9":
            tool_multi()
        elif choice == "0":
            print(f"\n{G}[+] Thanks for using DATA L34K3R!{Rs}")
            print(f"{C}Made by ADIX DEVELOPER{Rs}\n")
            break
        else:
            print(f"{R}[!] Invalid option!{Rs}")
            time.sleep(1)

if __name__ == "__main__":
    main()
