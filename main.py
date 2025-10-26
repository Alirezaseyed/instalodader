import instaloader
import requests
from datetime import datetime

def get_profile_info(profile_name):
    L = instaloader.Instaloader(sleep=True, max_connection_attempts=3)
    
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        print(f"\nEtelaat profile: {profile_name}")
        print(f"Naam karbari: {profile.username}")
        print(f"Naam kaamel: {profile.full_name}")
        print(f"Tedaad followerha: {profile.followers}")
        print(f"Tedaad followingha: {profile.followees}")
        print(f"Tedaad postha: {profile.mediacount}")
        print(f"Biography: {profile.biography[:100] + '...' if profile.biography else 'Bedoon biography'}")
        print(f"Link profile: https://www.instagram.com/{profile.username}/")
        
        with open(f"{profile_name}_profile_info.txt", 'w', encoding='utf-8') as f:
            f.write(f"Naam karbari: {profile.username}\n")
            f.write(f"Naam kaamel: {profile.full_name}\n")
            f.write(f"Tedaad followerha: {profile.followers}\n")
            f.write(f"Tedaad followingha: {profile.followees}\n")
            f.write(f"Tedaad postha: {profile.mediacount}\n")
            f.write(f"Biography: {profile.biography}\n")
            f.write(f"Link profile: https://www.instagram.com/{profile.username}/\n")
        print(f"Etelaat dar file {profile_name}_profile_info.txt zakhire shod.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"Profile {profile_name} vojood nadarad.")
    except instaloader.exceptions.LoginRequiredException:
        print(f"Baraye dastresi be profile {profile_name} niaz be login darid (ehtemalan profile khosusi ast).")
    except Exception as e:
        print(f"Khatayi dar estekhraj etelaat: {e}")

def get_reel_info(reel_link):
    L = instaloader.Instaloader(sleep=True, max_connection_attempts=3)
    
    try:
        shortcode = reel_link.split('/')[-2] if reel_link.endswith('/') else reel_link.split('/')[-1]
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        
        if not post.is_video:
            print("In link mowred nazar reel ya video nist.")
            return
        
        reel_info = {
            'link': f"https://www.instagram.com/p/{post.shortcode}/",
            'date': post.date.strftime('%Y-%m-%d %H:%M:%S'),
            'likes': post.likes,
            'views': post.video_view_count,
            'caption': post.caption[:50] + '...' if post.caption else 'Bedoon caption',
            'username': post.owner_username
        }
        
        print(f"\nEtelaat reel: {reel_info['link']}")
        print(f"Naam karbari: {reel_info['username']}")
        print(f"Tarikh: {reel_info['date']}")
        print(f"Likeha: {reel_info['likes']}")
        print(f"Viewha: {reel_info['views']}")
        print(f"Caption: {reel_info['caption']}")
        
        with open(f"{reel_info['username']}_reel_{shortcode}.txt", 'w', encoding='utf-8') as f:
            f.write(f"Reel: {reel_info['link']}\n")
            f.write(f"Naam karbari: {reel_info['username']}\n")
            f.write(f"Tarikh: {reel_info['date']}\n")
            f.write(f"Likeha: {reel_info['likes']}\n")
            f.write(f"Viewha: {reel_info['views']}\n")
            f.write(f"Caption: {reel_info['caption']}\n")
        
        print(f"Etelaat dar file {reel_info['username']}_reel_{shortcode}.txt zakhire shod.")
    except instaloader.exceptions.PostNotExistsException:
        print(f"Reel ba in link vojood nadarad.")
    except instaloader.exceptions.LoginRequiredException:
        print(f"Baraye dastresi be in reel niaz be login darid (ehtemalan reel khosusi ast).")
    except Exception as e:
        print(f"Khatayi dar estekhraj etelaat reel: {e}")

def test_reel_link(link):
    try:
        response = requests.get(link, timeout=5)
        if response.status_code == 200:
            print(f"Link {link} ghabel dastresi ast.")
        else:
            print(f"Link {link} ghabel dastresi nist (code vaziat: {response.status_code}).")
    except requests.exceptions.RequestException as e:
        print(f"Khatayi dar test link {link}: {e}")

def main_menu():
    while True:
        print("\nMenu asli:")
        print("1. Estekhraj etelaat account")
        print("2. Estekhraj etelaat reel (az rooye link)")
        print("3. Test link reel")
        print("4. Khorooj")
        
        choice = input("Lotfan yek gozine (1-4) entekhab konid: ")
        
        if choice == '1':
            profile_name = input("Naam karbari profile ra vared konid: ")
            get_profile_info(profile_name)
        
        elif choice == '2':
            reel_link = input("Link reel ra vared konid (masalan: https://www.instagram.com/p/ABC123/): ")
            get_reel_info(reel_link)
        
        elif choice == '3':
            reel_link = input("Link reel ra vared konid (masalan: https://www.instagram.com/p/ABC123/): ")
            test_reel_link(reel_link)
        
        elif choice == '4':
            print("Khorooj az barname...")
            break
        
        else:
            print("Gozine namotabar! Lotfan adadi bein 1 ta 4 vared konid.")

if __name__ == "__main__":
    try:
        import instaloader
        import requests
    except ImportError:
        print("Lotfan pishniazha ra nasb konid: pip install instaloader requests")
        exit(1)
    
    main_menu()