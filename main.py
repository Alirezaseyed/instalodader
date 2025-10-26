import instaloader
import requests
from datetime import datetime

def get_profile_info(profile_name):
    """استخراج اطلاعات کلی پروفایل"""
    L = instaloader.Instaloader(sleep=True, max_connection_attempts=3)
    
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        print(f"\nاطلاعات پروفایل: {profile_name}")
        print(f"نام کاربری: {profile.username}")
        print(f"نام کامل: {profile.full_name}")
        print(f"تعداد فالوورها: {profile.followers}")
        print(f"تعداد فالووینگ‌ها: {profile.followees}")
        print(f"تعداد پست‌ها: {profile.mediacount}")
        print(f"بیوگرافی: {profile.biography[:100] + '...' if profile.biography else 'بدون بیوگرافی'}")
        print(f"لینک پروفایل: https://www.instagram.com/{profile.username}/")
        
        # ذخیره اطلاعات در فایل
        with open(f"{profile_name}_profile_info.txt", 'w', encoding='utf-8') as f:
            f.write(f"نام کاربری: {profile.username}\n")
            f.write(f"نام کامل: {profile.full_name}\n")
            f.write(f"تعداد فالوورها: {profile.followers}\n")
            f.write(f"تعداد فالووینگ‌ها: {profile.followees}\n")
            f.write(f"تعداد پست‌ها: {profile.mediacount}\n")
            f.write(f"بیوگرافی: {profile.biography}\n")
            f.write(f"لینک پروفایل: https://www.instagram.com/{profile.username}/\n")
        print(f"اطلاعات در فایل {profile_name}_profile_info.txt ذخیره شد.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"پروفایل {profile_name} وجود ندارد.")
    except instaloader.exceptions.LoginRequiredException:
        print(f"برای دسترسی به پروفایل {profile_name} نیاز به لاگین دارید (احتمالاً پروفایل خصوصی است).")
    except Exception as e:
        print(f"خطا در استخراج اطلاعات: {e}")

def get_reels_links(profile_name):
    """استخراج لینک‌های ریل‌ها (پست‌های ویدیویی)"""
    L = instaloader.Instaloader(sleep=True, max_connection_attempts=3)
    
    try:
        profile = instaloader.Profile.from_username(L.context, profile_name)
        print(f"\nاستخراج لینک ریل‌ها برای پروفایل: {profile_name}")
        
        reels_links = []
        for post in profile.get_posts():
            if post.is_video:  # فقط پست‌های ویدیویی (ریل‌ها)
                link = f"https://www.instagram.com/p/{post.shortcode}/"
                reels_links.append({
                    'link': link,
                    'date': post.date.strftime('%Y-%m-%d %H:%M:%S'),
                    'likes': post.likes,
                    'views': post.video_view_count,
                    'caption': post.caption[:50] + '...' if post.caption else 'بدون کپشن'
                })
        
        if not reels_links:
            print("هیچ ریل/ویدیویی در این پروفایل یافت نشد.")
            return
        
        # نمایش و ذخیره لینک‌ها
        with open(f"{profile_name}_reels_links.txt", 'w', encoding='utf-8') as f:
            for reel in reels_links:
                print(f"\nریل: {reel['link']}")
                print(f"تاریخ: {reel['date']}")
                print(f"لایک‌ها: {reel['likes']}")
                print(f"ویوها: {reel['views']}")
                print(f"کپشن: {reel['caption']}")
                
                f.write(f"ریل: {reel['link']}\n")
                f.write(f"تاریخ: {reel['date']}\n")
                f.write(f"لایک‌ها: {reel['likes']}\n")
                f.write(f"ویوها: {reel['views']}\n")
                f.write(f"کپشن: {reel['caption']}\n")
                f.write("-" * 50 + "\n")
        
        print(f"لینک‌های ریل در فایل {profile_name}_reels_links.txt ذخیره شد.")
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"پروفایل {profile_name} وجود ندارد.")
    except instaloader.exceptions.LoginRequiredException:
        print(f"برای دسترسی به پروفایل {profile_name} نیاز به لاگین دارید (احتمالاً پروفایل خصوصی است).")
    except Exception as e:
        print(f"خطا در استخراج لینک‌ها: {e}")

def test_reel_link(link):
    """تست دسترسی‌پذیری لینک ریل"""
    try:
        response = requests.get(link, timeout=5)
        if response.status_code == 200:
            print(f"لینک {link} قابل دسترسی است.")
        else:
            print(f"لینک {link} قابل دسترسی نیست (کد وضعیت: {response.status_code}).")
    except requests.exceptions.RequestException as e:
        print(f"خطا در تست لینک {link}: {e}")

def main_menu():
    """منوی اصلی برنامه"""
    while True:
        print("\nمنوی اصلی:")
        print("1. استخراج اطلاعات اکانت")
        print("2. استخراج لینک ریل‌ها")
        print("3. تست لینک ریل")
        print("4. خروج")
        
        choice = input("لطفاً یک گزینه (1-4) انتخاب کنید: ")
        
        if choice == '1':
            profile_name = input("نام کاربری پروفایل را وارد کنید: ")
            get_profile_info(profile_name)
        
        elif choice == '2':
            profile_name = input("نام کاربری پروفایل را وارد کنید: ")
            get_reels_links(profile_name)
        
        elif choice == '3':
            reel_link = input("لینک ریل را وارد کنید (مثال: https://www.instagram.com/p/ABC123/): ")
            test_reel_link(reel_link)
        
        elif choice == '4':
            print("خروج از برنامه...")
            break
        
        else:
            print("گزینه نامعتبر! لطفاً عددی بین 1 تا 4 وارد کنید.")

if __name__ == "__main__":
    # نصب پیش‌نیازها
    try:
        import instaloader
        import requests
    except ImportError:
        print("لطفاً پیش‌نیازها را نصب کنید: pip install instaloader requests")
        exit(1)
    
    # اجرای منوی اصلی
    main_menu()